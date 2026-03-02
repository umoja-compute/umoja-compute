# Architecture

Umoja Compute runs open models using distributed compute.

Flow:

Client
→ Public Endpoint (ngrok)
→ Flask API
→ Ollama Runtime
→ Model (gpt-oss:20b)
→ Response

Compute:
- Google Colab GPU (T4)
- Model cached in Google Drive