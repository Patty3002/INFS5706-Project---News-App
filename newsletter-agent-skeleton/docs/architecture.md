# Initial architecture

```text
React/Vite frontend
        |
        | HTTP/JSON API
        v
FastAPI backend
        |
        +-- preference data
        +-- news provider
        +-- AI summary provider
        +-- newsletter renderer
        +-- email provider
        +-- scheduler
```

The frontend should not call third-party news, AI, or email services directly. Those credentials and integrations should remain in the backend.

The initial boundary between frontend and backend should be JSON over HTTP. This keeps the frontend replaceable and makes it possible to test the backend independently.
