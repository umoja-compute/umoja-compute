from flask import Flask, request, jsonify
import requests
import time

app = Flask(__name__)

OLLAMA_URL = "http://localhost:11434/api/generate"

# Basic observability storage (in-memory)
request_log = []


def log_request(endpoint, model, start_time):
    latency = time.time() - start_time
    request_log.append({
        "endpoint": endpoint,
        "model": model,
        "latency_seconds": round(latency, 2),
        "timestamp": time.time()
    })


@app.route("/v1/completions", methods=["POST"])
def completions():
    start_time = time.time()
    data = request.json

    model = data.get("model", "gpt-oss:20b")
    prompt = data.get("prompt", "")
    max_tokens = data.get("max_tokens", 200)
    temperature = data.get("temperature", 0.7)

    ollama_payload = {
        "model": model,
        "prompt": prompt,
        "options": {
            "temperature": temperature,
            "num_predict": max_tokens
        },
        "stream": False
    }

    response = requests.post(OLLAMA_URL, json=ollama_payload)
    result = response.json()

    log_request("/v1/completions", model, start_time)

    return jsonify({
        "id": "umoja-completion",
        "object": "text_completion",
        "choices": [
            {
                "text": result.get("response", ""),
                "index": 0,
                "finish_reason": "stop"
            }
        ]
    })


@app.route("/v1/chat/completions", methods=["POST"])
def chat_completions():
    start_time = time.time()
    data = request.json

    model = data.get("model", "gpt-oss:20b")
    messages = data.get("messages", [])

    # Convert chat messages to a single prompt
    prompt = ""
    for msg in messages:
        role = msg.get("role", "user")
        content = msg.get("content", "")
        prompt += f"{role}: {content}\n"
    prompt += "assistant:"

    ollama_payload = {
        "model": model,
        "prompt": prompt,
        "stream": False
    }

    response = requests.post(OLLAMA_URL, json=ollama_payload)
    result = response.json()

    log_request("/v1/chat/completions", model, start_time)

    return jsonify({
        "id": "umoja-chat",
        "object": "chat.completion",
        "choices": [
            {
                "index": 0,
                "message": {
                    "role": "assistant",
                    "content": result.get("response", "")
                },
                "finish_reason": "stop"
            }
        ]
    })


@app.route("/metrics", methods=["GET"])
def metrics():
    return jsonify({
        "total_requests": len(request_log),
        "logs": request_log[-20:]
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)