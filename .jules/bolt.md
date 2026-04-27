
## 2025-05-15 - [Redundant ML Inference & Consolidated Memory Retrieval]
**Learning:** Redundant BERT model inference is a major bottleneck. Passing pre-calculated results (like intensity) between services can save ~30-50ms per request. Consolidating multiple O(N) list iterations into a single pass also significantly reduces overhead in request orchestration.
**Action:** Always check if a request flow calls expensive ML models multiple times with the same input. Consolidate service-level data retrieval into aggregate "insight" methods to minimize passes over memory stores.
