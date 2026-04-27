#!/bin/bash
echo "Running Health Check..."
curl -s -X GET http://localhost:8000/health
echo -e "\n"

echo "Running Main Interaction..."
curl -s -X POST http://localhost:8000/namo/interact \
  -H "Content-Type: application/json" \
  -d '{
    "user_id": "user123",
    "message": "ผมรู้สึกเหงาและเศร้า"
  }'
echo -e "\n"

echo "Running Emotion Analysis..."
curl -s -X POST "http://localhost:8000/namo/analyze-emotion?text=%E0%B8%9C%E0%B8%A1%E0%B8%A3%E0%B8%B9%E0%B9%89%E0%B8%AA%E0%B8%B6%E0%B8%81%E0%B8%94%E0%B8%B5%E0%B9%83%E0%B8%88"
echo -e "\n"

echo "Running Dharma Guidance..."
curl -s -X POST "http://localhost:8000/namo/dharma-guidance?problem=%E0%B8%9C%E0%B8%A1%E0%B8%A3%E0%B8%B9%E0%B9%89%E0%B8%AA%E0%B8%B6%E0%B8%81%E0%B8%40%E0%B8%A3%E0%B9%89%E0%B8%B2&emotion=sadness&intensity=7.5"
echo -e "\n"

echo "Running User Context..."
curl -s -X GET http://localhost:8000/namo/user-context/user123
echo -e "\n"

echo "Running Crisis Detection..."
curl -s -X POST "http://localhost:8000/namo/crisis-check?user_id=user123&message=%E0%B8%9C%E0%B8%A1%E0%B8%AD%E0%B8%A2%E0%B8%B2%E0%B8%81%E0%B8%95%E0%B8%B1%E0%B8%94%E0%B8%AA%E0%B8%B4%E0%B8%99%E0%B9%83%E0%B8%88%E0%B8%AA%E0%B8%B4%E0%B9%89%E0%B8%99%E0%B8%AA%E0%B8%B8%E0%B8%94%E0%B8%8A%E0%B8%B5%E0%B8%A7%E0%B8%B4%E0%B8%95"
echo -e "\n"
