# async-sync-httpx-request
Demo of async vs sync HTTP requests performance using httpx & asyncio. Synchronous runs 4 API calls sequentially, async runs concurrently with dramatic speedup. Perfect for learning async/await patterns, concurrent programming, and I/O-bound optimization. Includes logging and Scalene profiler integration.

# Async vs Sync HTTP Requests Performance Comparison

This project demonstrates the significant performance difference between synchronous and asynchronous HTTP requests using Python's `httpx` library. It provides a clear, practical example of how async programming can dramatically reduce total execution time when making multiple network requests.

## 🎯 Purpose

To showcase the efficiency gains of asynchronous programming over traditional synchronous approaches when handling multiple I/O-bound tasks, specifically HTTP requests to APIs.

## 📋 Features

- **Synchronous implementation**: Makes sequential API requests, blocking until each completes
- **Asynchronous implementation**: Makes concurrent API requests using asyncio
- **Comprehensive logging**: Detailed logging to track request flow and timing
- **Performance profiling**: Integration with Scalene profiler for performance analysis
- **Real-world simulation**: Proper HTTP headers and error handling structure

## 🚀 Quick Start

### Prerequisites

```bash
pip install httpx asyncio scalene
```

### Profiling

```bash
# Profile the async implementation
scalene run --outfile profile.json async_vs_sync.py
scalene view profile.json
```

### Logs
When you run the code the log file will created.

## 🧠 How It Works

### Synchronous Flow
1. Makes first API request
2. Waits for complete response
3. Makes second API request
4. Repeats for all endpoints
5. Total time = sum of all request times

### Asynchronous Flow
1. Creates all request tasks simultaneously
2. Tasks run concurrently without blocking
3. Gathers results as they complete
4. Total time ≈ slowest single request time

## 🔧 Code Structure

```
├── synchronous()     # Sequential requests
├── asynchronous()    # Concurrent requests with asyncio
├── get_single_api()  # Individual async request handler
└── Logging           # Comprehensive event tracking
```

## 📈 Performance Analysis

The async implementation typically achieves:
- **3-10x speedup** for 4 requests
- **10-100x speedup** for dozens of requests
- Near-linear scaling with concurrency

## 🎓 Learning Outcomes

- Understanding blocking vs non-blocking operations
- Practical asyncio implementation patterns
- HTTP client configuration for async/await
- Performance measurement and profiling
- Concurrent task management

## 🛠️ Customization

### Add More Endpoints
```python
urls = {
    "CustomAPI": "https://yourapi.com/endpoint",
    # Add more...
}
```

### Modify Headers
```python
headers = {
    'User-Agent': 'Your Custom Agent',
    'Authorization': 'Bearer token'
}
```

## 📝 Logging Example

```
INFO [2024-01-01 12:00:01] root - info :: Start synchronous FUNC
INFO [2024-01-01 12:00:02] root - info :: Fetching FirstAPI Ends and Status is <Response [200 OK]>
INFO [2024-01-01 12:00:03] root - info :: Start asyncrounes FUNC
INFO [2024-01-01 12:00:03] root - info :: Task FirstAPI Created!
INFO [2024-01-01 12:00:03] root - info :: Gathering Tasks
INFO [2024-01-01 12:00:04] root - info :: Fetching FirstAPI Ends and Status is <Response [200 OK]>
```

## ⚠️ Important Notes

- **API Endpoints**: Replace example URLs with real endpoints
- **Rate Limiting**: Async may trigger rate limits; implement delays if needed
- **Error Handling**: The code includes `return_exceptions=True` for resilience
- **Profiling**: Scalene provides function-level performance breakdown

## 🤝 Contributing

Suggestions for improvements:
- Add timing decorators
- Implement rate limiting
- Add response comparison validation
- Create visual performance charts
- Add more HTTP methods (POST, PUT, DELETE)

## 📄 License

MIT License - Feel free to use this for learning and demonstrations

## ⭐ Key Takeaway

**Async programming isn't about doing things faster—it's about not waiting unnecessarily.** This example demonstrates how to maximize efficiency during I/O wait times by doing other useful work.

---

*Perfect for: Python developers learning async/await, performance optimization demonstrations, and understanding concurrent programming patterns.*
