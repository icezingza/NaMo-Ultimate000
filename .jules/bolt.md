
## 2025-01-24 - Redundant ML Inference in PersonalizationEngine
**Learning:** Redundant BERT model inference via `emotion_service.analyze_sentiment` was a significant performance bottleneck in the `namo/interact` endpoint. Components should pass around already computed sentiment analysis results (like intensity) whenever possible.
**Action:** Consolidate data flow to ensure heavy operations like ML inference are only performed once per request cycle.
