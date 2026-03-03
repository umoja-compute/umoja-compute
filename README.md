# Umoja Compute

![MIT License](https://img.shields.io/badge/license-MIT-green) ![OpenAI
Compatible](https://img.shields.io/badge/OpenAI-Compatible-blue) ![GPU
Powered](https://img.shields.io/badge/GPU-T4%20Powered-orange) ![Open
Source](https://img.shields.io/badge/Open-Source-brightgreen)

------------------------------------------------------------------------

## 🌍 OpenAI-Compatible Infrastructure for Running Open Models Anywhere

**Umoja Compute** is an open-source AI infrastructure platform that
enables developers to run large language models on distributed GPU
compute and expose fully **OpenAI-compatible APIs** --- without paying
expensive cloud inference costs.

It allows you to:

-   Run open models like `gpt-oss:20b`
-   Expose `/v1/chat/completions` endpoints
-   Monitor usage, tokens, and performance
-   Integrate seamlessly with existing OpenAI SDK-based applications

Drop-in replacement. Zero infrastructure barrier.

------------------------------------------------------------------------

# 🚀 Live API Test

## Check Engine Status

``` bash
curl https://5d3c-34-125-193-242.ngrok-free.app/status
```

------------------------------------------------------------------------

## Chat Completion (Windows CMD)

``` bash
curl -X POST "https://5d3c-34-125-193-242.ngrok-free.app/v1/chat/completions" -H "Content-Type: application/json" -d "{\"model\":\"gpt-oss:20b\",\"messages\":[{\"role\":\"user\",\"content\":\"Explain why open AI infrastructure matters.\"}]}"
```

------------------------------------------------------------------------

## Python SDK (OpenAI Compatible)

``` python
from openai import OpenAI

client = OpenAI(
    base_url="https://5d3c-34-125-193-242.ngrok-free.app/v1",
    api_key="none"
)

response = client.chat.completions.create(
    model="gpt-oss:20b",
    messages=[
        {"role": "user", "content": "Explain Umoja Compute in one sentence."}
    ],
)

print(response.choices[0].message.content)
```

------------------------------------------------------------------------

# 🔥 Why Umoja Compute?

AI innovation is often restricted by infrastructure cost, vendor
lock-in, and lack of control.

Umoja Compute removes those barriers by providing:

-   ✅ OpenAI SDK compatibility (`/v1/completions`,
    `/v1/chat/completions`)
-   ✅ Free GPU compute (Google Colab T4)
-   ✅ Persistent model caching (Google Drive)
-   ✅ Public HTTPS endpoints via secure tunneling
-   ✅ Built-in observability (tokens, latency, request metrics)
-   ✅ Agent-ready and workflow-ready integration (n8n, Docker,
    automation systems)

**Build, test, scale --- without infrastructure debt.**

------------------------------------------------------------------------

# 🌍 Why This Matters for Africa

AI infrastructure access is uneven globally.

Many developers, researchers, and startups across Africa face:

-   High cloud GPU costs
-   Limited access to scalable AI infrastructure
-   Dependency on foreign closed platforms

Umoja Compute democratizes AI infrastructure by enabling:

-   Local experimentation with open models
-   Affordable research and hackathon participation
-   Enterprise prototyping without cloud lock-in
-   Ownership and control over AI systems

Infrastructure should not be a privilege.

------------------------------------------------------------------------

# 🏗 Architecture

Client Application\
→ Public HTTPS Endpoint\
→ Flask API\
→ Ollama Runtime\
→ Open Model (`gpt-oss:20b`)\
→ Structured JSON Response

Compute Layer: - Google Colab GPU (T4) - Model cached in Google Drive -
Public routing via ngrok - Token & request observability

------------------------------------------------------------------------

# ⚡ Quick Start

1.  Open notebook\
    `Umoja_Compute_Genesis_v1.ipynb`

2.  Get auth token from https://ngrok.com/

3.  In Colab:

    -   Runtime → Change runtime type → GPU (T4)
    -   Run all cells

4.  Copy your public endpoint

Test:

``` bash
curl -X POST "$PUBLIC_URL/v1/chat/completions" -H "Content-Type: application/json" -d '{
  "model": "gpt-oss:20b",
  "messages": [
    {"role": "user", "content": "Why is open infrastructure important?"}
  ]
}'
```

------------------------------------------------------------------------

# 📊 Observability

Built-in production-style telemetry:

-   Request counting
-   Token tracking
-   Latency monitoring
-   Node health endpoint
-   Multi-node readiness

Designed for benchmarking, hackathons, and early-stage AI infrastructure
validation.

------------------------------------------------------------------------

# 🧠 Ideal For

-   AI startups
-   Research labs
-   University innovation hubs
-   Hackathons
-   Automation builders
-   Agent developers
-   Developers replacing OpenAI endpoints with open models

------------------------------------------------------------------------

# 🛣 Roadmap

-   Streaming support
-   API key authentication
-   Multi-user isolation
-   Docker standalone deployment
-   Kubernetes orchestration
-   Web dashboard for observability
-   Multi-model routing & load balancing

------------------------------------------------------------------------

# 🌟 Vision

Umoja Compute is building the **open infrastructure layer for AI** ---
empowering developers to run, scale, and control their own intelligence
stack without vendor dependency.

Open models deserve open infrastructure.

------------------------------------------------------------------------

# 📜 License

MIT License

------------------------------------------------------------------------

# 🤝 Contributing

We welcome contributors who believe AI infrastructure should be
accessible.

Open an issue. Submit a pull request.\
Let's build the compute layer of the open AI ecosystem.
