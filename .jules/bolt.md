
## 2025-01-31 - Redundant Transformer Inference and Consolidated Memory Scans
**Learning:** Redundant calls to heavy ML models like DistilBERT add significant latency (~14ms per call) even on CPU. Consolidating multiple O(N) passes over the same dataset into a single pass is a key architectural pattern for performance in this codebase.
**Action:** Always check if expensive computation results (like sentiment analysis) can be passed downstream instead of being recomputed. Use consolidated "insight" methods in services to minimize data iterations.
