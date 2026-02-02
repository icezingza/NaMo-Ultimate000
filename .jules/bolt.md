
## 2025-01-30 - Redundant BERT inference in interaction flow
**Learning:** Redundant BERT model inference via `emotion_service.analyze_sentiment` was a significant performance bottleneck in the main interaction loop. Components were re-calculating sentiment analysis results that were already available in the calling context.
**Action:** Pass pre-calculated sentiment data (like intensity) between components instead of re-running model inference. Pre-compute static response templates in class constructors to avoid redundant dictionary creation.
