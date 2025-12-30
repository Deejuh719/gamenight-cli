# Sprint: Refactor GameNight CLI into Flask Web App

## 🎯 Sprint Theme

In this sprint, you will refactor an existing **CLI-based GameNight application** into a **Flask web application** with layered architecture and multi-layer testing. The goal is to:

- Preserve and clarify **game domain logic** from the CLI.
- Introduce a **GameService** layer suitable for both CLI and Flask.
- Add **HTTP APIs** and **HTML UI** for game play.
- Cover behavior with **pytest (unit/integration)**, **Selenium**, **Playwright**, and **BDD/acceptance-style** testing patterns in a style similar to your Task Tracker sprints.

You will treat the CLI code as a legacy system and evolve it into a testable, web-ready architecture rather than rewriting it from scratch.

---

## 0. Role and Background

**Role:** Backend & UI Developer with SQA Focus

You are responsible for:

- Extracting and refactoring game logic into a **GameService**.
- Designing and implementing **Flask routes** (API and UI).
- Introducing test automation at multiple levels: unit, integration, UI, and acceptance.
- Maintaining a **CI-friendly** test suite with markers and configuration.

You will borrow patterns from:

- **Sprint 3**: domain modeling, TaskService, MockTaskService, requests-based API tests.
- **Sprint 4**: repository pattern, Flask UI, Selenium, Playwright, database and test fixtures.
- **Sprint 5**: external service integration, service injection, mocking, CI-safe markers.

---

## 1. Before You Start

- Confirm the **GameNight CLI repo** is cloned and runs as a CLI from `main` (e.g., `python -m gamenight_cli` or similar).

```bash
# From the repo root, example CLI entry point
python -m gamenight_cli
```

- Create and activate a **virtual environment** and install baseline dependencies:

```bash
# Create venv (if not already created)
python -m venv .venv

# Activate (Windows PowerShell)
.venv\Scripts\Activate.ps1

# Or activate (bash / zsh)
source .venv/bin/activate

# Install base dependencies
pip install flask pytest pytest-cov

# Later you will also install:
pip install selenium webdriver-manager
pip install playwright pytest-playwright
pip install pytest-bdd
```

- Ensure you have a **GitHub Actions** workflow file ready to be updated:

```bash
# Confirm file exists
ls .github/workflows
```

The CLI version is your **baseline behavior**: you will not delete it; instead, you will refactor around it and compare behavior as you go.

---

## 2. Sprint Objectives

### 2.1 Architecture and Refactor Goals

- Introduce a **Game domain model** (classes for Game, Player, Round, etc. as needed).
- Implement a **GameService** that encapsulates game rules and state transitions, independent of any UI.
- Build a **Flask app factory** (`create_app`) that injects services and registers blueprints.
- Provide both:
    - **API routes** (`/api/games/...`) returning JSON.
    - **UI routes** (`/games/...`) rendering templates.

### 2.2 Testing Goals

- **Unit tests** for game models and GameService using pytest and TDD where valuable.
- **Integration tests** for API and UI routes, making real HTTP calls via Flask’s test client and `requests`.
- **UI automation** with Selenium (pytest-based) and Playwright (pytest or pytest-playwright based) to verify key user flows.
- **BDD-style acceptance tests** (pytest-bdd + Playwright) for end-to-end game flows.
- **MockGameService** and test fixtures to ensure isolation, determinism, and CI stability.

### 2.3 CI/CD Goals

- Configure CI to:
    - Run unit and core integration tests on every push.
    - Run Selenium/Playwright tests in headless mode.
    - Exclude or mark slow/external tests where appropriate (e.g., a marker like `external`).

---

## 3. Phase 1 – Planning and Setup

### P1-1: Sprint Documentation

Create a doc set for this sprint (mirroring your previous sprint docs):

- Sprint Plan (scope, stories for GameNight refactor).
- Architecture overview (from CLI to layered Flask).
- Test Plan (layers: unit, integration, UI, BDD).
- Test Cases document including IDs for key flows (e.g., `TC-GN-API-001`, `TC-GN-UI-001`).

Example branch workflow:

```bash
git checkout -b s-gamenight-documentation

# Edit docs/*
git status
git add docs/
git commit -m "Add GameNight sprint planning docs"
git push -u origin s-gamenight-documentation
```

### P1-2: Issue Tracking and Board

Set up epics and issues and a Kanban board in GitHub’s UI (Backlog → Ready → In Progress → In Review → Done).

---

## 4. Phase 2 – Domain Refactor from CLI to GameService (TDD-leaning)

### P2-1: Analyze Existing CLI and Extract Domain Concepts

Run the existing CLI to understand flows:

```bash
python -m gamenight_cli
```

Identify entities (game, player, score, etc.) and which functions mix I/O with rules.

### P2-2: Design and Implement Domain Model and GameService

After writing or updating unit tests for domain classes and `GameService`:

```bash
# Run only domain-related tests
pytest tests/domain -v

# Run specific modules if helpful
pytest tests/domain/test_game_model.py -v
pytest tests/services/test_game_service.py -v

# Or run the entire suite
pytest -v
```

Use TDD where adding new domain behavior is valuable: write failing tests, add minimal implementations, then re-run tests.

Purpose: ensure game logic stands alone, independent of CLI or Flask.

---

## 5. Phase 3 – Flask App Foundation and API Routes

### P3-1: App Factory and Dependency Injection

Once you create `create_app` and app-factory tests:

```bash
# Run app factory tests
pytest tests/test_app_factory.py -v
```

Sanity-check the Flask app manually:

```bash
python -m app.main
```

Then open `http://localhost:5000/api/health` in a browser or with curl.

### P3-2: Game API Blueprint

After implementing the game API routes and tests:

```bash
# Run only API tests
pytest tests/api -v

# Or run a specific API test file
pytest tests/api/test_game_api.py -v
```

Each route should delegate to `current_app.game_service` and return JSON, similar to the Task Tracker API routes.

### P3-3: E2E API Tests via `requests`

For end-to-end tests that call the live server:

Terminal 1 – start server:

```bash
python -m app.main
```

In a second terminal:

Terminal 2 – run requests-based tests:

```bash
pytest tests/api_requests/test_game_api_requests.py -v
```

Manual curl checks:

```bash
curl http://localhost:5000/api/health

curl -X POST http://localhost:5000/api/games \
-H "Content-Type: application/json" \
-d '{"config": {"rounds": 3}}'
```

This mirrors the Sprint 3 pattern using `requests` for API workflow testing.

---

## 6. Phase 4 – Web UI Templates and Routes

### P4-1: Base Template and Game Views

After wiring `base.html` and game templates:

```bash
# Run UI integration tests for routes and templates
pytest tests/ui/test_game_ui_routes.py -v
```

Manually test in a browser:

```bash
python -m app.main
```

Then visit `http://localhost:5000/games/new` or `http://localhost:5000/games/<id>`, similar to how Task Tracker UI was validated.

### P4-2: UI Routes (Blueprint)

Whenever you modify UI routes:

```bash
pytest tests/ui/test_game_ui_routes.py -v
```

Ensure routes use `current_app.game_service` and follow Post‑Redirect‑Get like your Task form routes.

---

## 7. Phase 5 – Validation and Server-Side Rules

### P5-1: Input Validation and Error Handling

To verify validation tests:

```bash
pytest tests/ui/test_game_validation.py -v
```

Manual validation:

```bash
python -m app.main
```

Submit forms with invalid input and confirm error messages and no corrupted state, mirroring Task Tracker server-side validation practices.

---

## 8. Phase 6 – Selenium UI Automation (pytest)

### P6-1: Selenium Setup and Health Check

Install Selenium and WebDriver-manager:

```bash
pip install selenium webdriver-manager
```

Run a Selenium setup/health test:

```bash
pytest tests/health/test_setup_selenium.py -v -s
```

This follows the Sprint 4 Selenium health-check pattern.

### P6-2: Selenium Tests for Core Game Flow

Ensure the Flask server is running:

Terminal 1:

```bash
python -m app.main
```

Then run Selenium tests:

```bash
# Visual mode (if tests honor a LEARNINGMODE flag)
pytest tests/ui/selenium/test_selenium_gamenight.py -v -s

# Headless mode for CI
pytest tests/ui/selenium/test_selenium_gamenight.py -v -s
```

Selectors should be stable (IDs/ARIA attributes) as recommended in your UI labs.

---

## 9. Phase 7 – Playwright UI Automation (pytest / pytest-playwright)

### P7-1: Playwright Configuration

Install Playwright and browsers:

```bash
pip install playwright pytest-playwright
playwright install
```

Smoke-test the setup:

```bash
pytest tests/ui/playwright/test_playwright_smoke.py -v
```

### P7-2: Playwright Tests for Game Flows

If your tests require a running server:

Terminal 1:

```bash
python -m app.main
```

Then execute Playwright tests:

```bash
# Headless (default, if configured)
pytest tests/ui/playwright/test_playwright_gamenight.py -v

# Headed/visual mode
pytest tests/ui/playwright/test_playwright_gamenight.py -v --headed
```

This mirrors how Sprint 4 used Playwright for fast UI automation.

---

## 10. Phase 8 – BDD Acceptance Testing (pytest-bdd + Playwright)

### P8-1: BDD Setup

Install pytest-bdd:

```bash
pip install pytest-bdd
```

After adding `.feature` files and step definitions, run your BDD tests:

```bash
pytest tests/acceptance/bdd_game/test_bdd_gamenight.py -v
```

Or, if you mark them:

```bash
pytest -m "bdd" -v
```

Sprint 4 used this pattern to keep BDD tests separate and manageable.

### P8-2: Step Definitions Using Playwright

Step definitions will typically reuse the same Playwright fixtures; run them with:

```bash
pytest tests/acceptance/bdd_game/test_bdd_gamenight.py -v
```

These tests serve as acceptance coverage for key GameNight flows.

---

## 11. Phase 9 – Test Isolation, Reset Helpers, and CI-Oriented Configuration

### P9-1: Game State Reset and Fixtures

After adding reset endpoints (e.g., `POST /api/games/reset`) and fixtures:

```bash
# Run tests that rely on reset behavior
pytest tests/test_reset_helpers.py -v
```

Manual reset test:

```bash
python -m app.main
```

Then, in another terminal:

```bash
curl -X POST http://localhost:5000/api/games/reset
```

This follows the same pattern as your Task Tracker reset fixtures and endpoints.

### P9-2: pytest Configuration

After editing `pytest.ini` to configure markers, ignore patterns, and warnings, validate with:

```bash
pytest -v
```

You should see the expected suite layout and ignored paths, similar to previous sprint configurations.

---

## 12. Phase 10 – CI/CD Integration

### P10-1: CI Job Structure

Locally, approximate CI’s behavior before pushing:

```bash
# Fast unit + integration (no external, no UI, no BDD)
pytest -m "not external and not ui and not bdd" -v

# UI tests
pytest tests/ui -v

# BDD tests
pytest -m "bdd" -v
```

Then push your changes to trigger CI:

```bash
git status
git add .
git commit -m "Implement GameNight Flask refactor + tests"
git push
```

Your CI workflow can mirror Sprint 4 and 5 patterns for server startup, health checks, and marker-based test selection.

---

## 13. Phase 11 – Regression, Evidence, and Documentation

### P11-1: Regression Checklist

Run the full suite:

```bash
pytest -v
```

With coverage:

```bash
pytest --cov=app --cov-report=term-missing -v
```

Confirm CLI still functions:

```bash
python -m gamenight_cli
```

This ensures both legacy and new paths remain correct, similar to how older Task Tracker sprints were kept green during refactors.

### P11-2: Evidence and README Updates

Update docs and commit:

```bash
git add README.md docs/ images/
git commit -m "Update docs and add GameNight screenshots"
git push
```

Document architecture, how to run the CLI and Flask app, and how to run each test layer, following the documentation style used in previous labs.

---

By following this sprint structure, you move the GameNight CLI from a single-interface script to a **multi-layer, test-driven web application** with modern QA practices: service layers, dependency injection, unit and integration tests, UI automation, BDD acceptance tests, and a CI pipeline designed for reliability and speed.