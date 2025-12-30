# GameNight Web Refactor Roadmap

This document outlines a multi-sprint plan to refactor the existing **GameNight CLI** into a **Flask-based web application** with layered architecture, automated tests, and persistent score tracking using SQL.

---

# Sprint 1: Core Architecture & Basic Web UI

## 🎯 Sprint 1 Theme

Establish a **clean architecture** for GameNight by extracting domain logic from the CLI into a **GameService**, creating a **Flask app foundation**, and adding a minimal HTML UI for playing games. The CLI will be treated as a legacy front-end, evolving the project toward a testable, web-ready design.

---

## 1. Role and Background

**Role:** Backend & UI Developer with SQA Focus.

You are responsible for:

- Extracting game logic into a **service layer**.
- Designing **Flask routes** for API and UI.
- Writing **pytest** unit and integration tests.
- Keeping the test suite **CI-friendly** (markers, selective runs).

Patterns reused from previous coursework:

- Domain modeling, service layer, MockTaskService, requests-based API tests.
- Flask app factory, templates, repository pattern for persistence.

---

## 2. Before You Start

- Confirm the **GameNight CLI repo** runs:

```bash
python -m gamenight_cli
```

- Create and activate a **virtual environment** and install base dependencies:

```bash
python -m venv .venv

# Windows PowerShell
.venv\Scripts\Activate.ps1

# bash / zsh
source .venv/bin/activate

pip install flask pytest pytest-cov
```

- Ensure a GitHub Actions workflow exists:

```bash
ls .github/workflows
```

---

## 3. Sprint 1 Objectives

### 3.1 Architecture Goals

- Introduce a **Game domain model** (Game, Player, Round as needed).
- Implement a **GameService** that encapsulates rules and state transitions (no UI code).
- Add a **Flask app factory** (`create_app`) that injects `GameService` and registers blueprints.
- Provide initial:
    - **API routes** (`/api/games/...`) returning JSON.
    - **UI routes** (`/games/...`) rendering basic templates.

### 3.2 Testing Goals

- **Unit tests** for domain models and `GameService`.
- **Integration tests** for API and UI using Flask’s test client and `requests`.
- Start using **MockGameService** to isolate routes.

---

## 4. Sprint 1 Phases

### Phase 1: Planning & Setup

- Create Sprint 1 documentation (Plan, Architecture, Test Plan, Test Cases).
- Use Git to manage documentation:

```bash
git checkout -b s1-gamenight-documentation
edit docs/*
git add docs/
git commit -m "Add GameNight Sprint 1 planning docs"
git push -u origin s1-gamenight-documentation
```

- Create epics and issues (Domain Refactor, Flask Foundation, Basic UI) and manage them with a Kanban board.

---

### Phase 2: Domain Refactor (CLI → GameService)

- Analyze the CLI and extract concepts:
    - Entities: game, player, score, rounds.
    - Core state transitions: new game, add player, play turn, determine winner.
    - Identify where input/print is mixed with rules.

- Implement domain classes (e.g., `Game`, `Player`) and a `GameService` to:
    - Manage games in memory.
    - Provide methods like `create_game`, `add_player`, `apply_move`, `get_game_state`.
    - Return dicts for easy JSON/templating.

- Run domain tests:

```bash
pytest tests/domain -v
pytest tests/domain/test_game_model.py -v
pytest tests/services/test_game_service.py -v
pytest -v
```

---

### Phase 3: Flask App Foundation & Basic API

- Create `create_app` that:
    - Instantiates `GameService`.
    - Attaches it to `app.game_service`.
    - Registers a health blueprint (`/api/health`) and a game API blueprint (`/api/games/...`).

- Create `game_api` blueprint with routes such as:
    - `POST /api/games` – new game.
    - `POST /api/games/<id>/players` – add player.
    - `POST /api/games/<id>/moves` – apply move.
    - `GET /api/games/<id>` – current state.

- Run API tests:

```bash
pytest tests/api -v
pytest tests/api/test_game_api.py -v
```

---

### Phase 4: Minimal Web UI

- Create `base.html` and simple views (`game_new.html`, `game_lobby.html`, `game_play.html`).
- Use the template inheritance pattern.
- Create `game_ui` blueprint that:
    - Shows forms for creating games and adding players.
    - Uses Post‑Redirect‑Get and `current_app.game_service`.

- Test UI routes:

```bash
pytest tests/ui/test_game_ui_routes.py -v
python -m app.main
```

---

# Sprint 2: Validation, Persistent Scores (SQL), and Leaderboard

## 🎯 Sprint 2 Theme

Extend the GameNight web app with **server-side validation**, **persistent scores using SQL/SQLAlchemy**, and a **leaderboard displayed on the game selection screen**.

---

## 1. Sprint 2 Objectives

- Add robust **validation** for game setup and moves.
- Introduce a **Score model** and **SQL-backed scoreboard** using SQLAlchemy.
- Display a **leaderboard at game selection** based on persisted data.
- Add tests for Score and leaderboard behavior at model, service, API, and UI levels.

---

## 2. Sprint 2 Phases

### Phase 5: Validation & Server-Side Rules

- Add server-side validation: required player names, valid moves, constraints per game type.
- Render validation errors in templates.

- Test:

```bash
pytest tests/ui/test_game_validation.py -v
python -m app.main
```

---

### Phase 6: SQL-Based Score Persistence

- Introduce a `Score` model with fields like `id`, `player_name`, `wins`, `losses`, `ties`, and `last_played`.
- Create a `ScoreRepository` for CRUD operations and a `ScoreService` for business logic.
- Inject these into `create_app`.

- Test score services with in-memory SQLite:

```bash
pytest tests/scores/test_score_model.py -v
pytest tests/scores/test_score_service.py -v
```

---

### Phase 7: Leaderboard at Game Selection

- Extend the game selection route to show a leaderboard panel for each game type.
- Persist scores at game end using `ScoreService.record_result`.

- Add integration tests:

```bash
pytest tests/integration/test_game_end_scores.py -v
```

---

# Sprint 3: UI Automation, BDD, and Full Regression

## 🎯 Sprint 3 Theme

Add **Selenium** and **Playwright** UI automation and **BDD-style acceptance tests**, then tighten **CI integration** and regression practices for the GameNight web app, including scoreboards.

---

## 1. Sprint 3 Objectives

- UI automation for core game flows using **Selenium** and **Playwright**.
- BDD scenarios for “play game & see updated leaderboard”.
- CI pipeline that runs unit, integration, UI, and selected BDD tests.

---

## 2. Sprint 3 Phases

### Phase 9: Selenium UI Automation

- Install Selenium and WebDriver-manager:

```bash
pip install selenium webdriver-manager
pytest tests/health/test_setup_selenium.py -v -s
```

- Run Selenium tests:

```bash
pytest tests/ui/selenium/test_selenium_gamenight.py -v -s
```

---

### Phase 10: Playwright UI Automation

- Install Playwright and browsers:

```bash
pip install playwright pytest-playwright
playwright install
```

- Run Playwright tests:

```bash
pytest tests/ui/playwright/test_playwright_gamenight.py -v
pytest tests/ui/playwright/test_playwright_gamenight.py -v --headed
```

---

### Phase 11: BDD Acceptance Testing

- Install pytest-bdd:

```bash
pip install pytest-bdd
```

- Add `.feature` files and implement step definitions using Playwright fixtures.

- Run BDD tests:

```bash
pytest tests/acceptance/bdd_game/test_bdd_gamenight.py -v
pytest -m "bdd" -v
```

---

### Phase 12: CI/CD & Regression

- Ensure CI workflow installs all dependencies and runs:
    - Unit + fast integration tests on every push.
    - Selenium and Playwright tests (headless) in selected jobs.
    - BDD tests in a separate job or triggered manually.

- Local regression:

```bash
pytest -v
pytest --cov=app --cov-report=term-missing -v
python -m gamenight_cli
```

---

By organizing the work into three sprints—**core architecture**, **SQL-backed scores & leaderboard**, and **UI automation + BDD**—this roadmap provides a structured approach to refactor and enhance the GameNight application.
