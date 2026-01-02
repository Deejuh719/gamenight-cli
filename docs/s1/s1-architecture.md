   # Sprint 1 Architecture

   ## System Overview

   GameNight follows a **layered architecture** pattern:

```mermaid
flowchart TD
%% ========== Presentation Layer ==========
subgraph "Presentation Layer(Flask)"
  subgraph "API Routes"
    A["game_api.py"
    handle HTTP requests, return JSON]
  end
  subgraph "UI Routes"
    B["game_ui.py"
    render templates, handle form submissions with HTML & Jinja2]
  end
  subgraph "Health Check"
    E["health_check.py"
    check health of the API]
  end
end

%% ========== Business Layer ==========
subgraph "Business Layer"
  A --> C["game_service.py"
  Manage game sessions, enforce rules, no HTTP]
  B --> C
end

%% ========== Domain Layer ==========
subgraph "Domain Layer"
  C -.-> D["game.py
  Game logic (immutable)
  game_session.py
  Active game session (mutable)"]
end
```

## Design Patterns

1. **App Factory:** The `create_app` function in `game_api.py` creates the Flask app instance with the necessary configuration and routes.
2. **Dependency Injection:** The `game_service.py` module uses dependency injection to inject the `game.py` module into the `GameService` class.
3. **Blueprint:** The `game_api.py` and `game_ui.py` modules use blueprints to register routes and views.
4. **Repository:** (Sprint 2) Data persistence abstraction (e.g., repository pattern)

## Technology Stack

Component | Technology | Version
--------- | ---------- | -------
Backend | Flask | 3.0+
Language | Python | 3.11+
Testing | pytest | 8.0+
Coverage | pytest-cov | 4.0+
CI/CD | GitHub Actions | N/A
Templates | Jinja2 | Included