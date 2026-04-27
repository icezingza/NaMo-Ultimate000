## 2025-01-31 - Redundant Model Inference in Monolithic App
**Learning:** In a monolithic FastAPI app with service-oriented structure, passing raw data (like user messages) between services often leads to redundant expensive operations (like BERT sentiment analysis) if each service is "responsible" for its own analysis. Consolidating these calls at the entry point (controller) and passing the result downstream significantly reduces latency.
**Action:** Always check if a service's input has already been processed by an upstream service or controller before performing expensive computations.

## 2025-01-31 - Response Template Overhead
**Learning:** Re-defining large dictionaries (like response templates) within a method that is called on every request introduces unnecessary allocation overhead.
**Action:** Pre-compute such data structures in the class `__init__` method.
