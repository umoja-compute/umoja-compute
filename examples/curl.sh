curl -X POST "$PUBLIC_URL/v1/completions" \
-H "Content-Type: application/json" \
-d '{
  "model": "gpt-oss:20b",
  "prompt": "Explain Umoja Compute.",
  "max_tokens": 100
}'