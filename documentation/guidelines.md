# GameNight Web Refactor Roadmap

This roadmap is structured into **three sprints**, similar to your Task Tracker labs. It includes example code snippets, step-by-step phases, and clear stopping points to ensure you do not get ahead of yourself.

---

# Sprint 1: Core Architecture & Basic Web UI

## 🎯 Sprint 1 Theme

In this sprint, you will:

- Extract core **game rules** from the existing `gamenight-cli` into a **GameService**.
- Build a minimal **Flask app** using an **app factory** pattern.
- Implement basic **API** and **HTML UI** for creating and viewing a game.
- Add **pytest** unit and integration tests following patterns from Task Tracker labs.

You will **not** use SQL, Selenium, Playwright, or BDD yet. Focus on clean separation of concerns and small, testable pieces.

---

## 0. Role and Background

**Role:** Backend & UI Developer with SQA focus.

You are responsible for:

- Moving logic out of the CLI (I/O) layer.
- Encapsulating rules in domain and service classes.
- Wiring those services into Flask routes.
- Writing tests that confirm each layer works correctly.

This mirrors:

- Sprint 3: `Task` + `TaskService` + Mock services and requests tests.
- Sprint 4: `create_app`, route blueprints, and template-based UI.

---

## 1. Before You Start

### P0-1: Run the Existing CLI

From the `gamenight-cli` repo root:

```bash
python -m gamenight_cli
```

Observe:

- What options the main menu offers.
- How a game starts and ends.
- What data is tracked (players, scores, rounds).

Write down **key concepts** (e.g., “players”, “rounds”, “current turn”, “winner”).

### P0-2: Environment Setup

Create and activate a virtual environment:

```bash
python -m venv .venv
```

For Windows PowerShell:

```bash
.venv\Scripts\Activate.ps1
```

For bash/zsh:

```bash
source .venv/bin/activate
```

Install base dependencies:

```bash
pip install flask pytest pytest-cov
```

Check if a CI workflow exists:

```bash
ls .github/workflows
```

---

## 2. Sprint 1 Objectives

By the end of Sprint 1:

- You have a `Game` domain class and a `GameService` with in-memory storage.
- You have `create_app()` that wires `GameService` into Flask.
- You can:
    - `POST /api/games` to create a game.
    - `GET /api/games/<id>` to inspect game state.
- You have a minimal UI to:
    - Create a game via form.
    - View game state in a template.
- You have pytest tests covering domain, service, and basic routes.

---

## 3. Phase 1 – Planning & Setup (Sprint 1)

### P1-1: Sprint 1 Documentation Branch

Create a documentation branch:

```bash
git checkout -b s1-gamenight-docs
```

Create documentation files:

```bash
mkdir docs
touch docs/s1_plan.md docs/s1_architecture.md docs/s1_tests.md
git add docs/
git commit -m "Add GameNight Sprint 1 documentation"
git push -u origin s1-gamenight-docs
```

In `docs/s1_plan.md`, clearly state:

- “No database in Sprint 1.”
- “No browser automation in Sprint 1.”
- “Focus on GameService, basic APIs, and basic templates.”

---

## 4. Phase 2 – Domain Refactor (CLI → GameService)

### P2-1: Identify Domain Logic in CLI

Open your CLI entry module and locate:

- Menu/input functions (`input()`, `print()`).
- Logic that checks if a move is valid or game is over.
- Computations for who wins and how scores are tracked.

Mark these with comments like:

```python
# TODO: Move this rule into GameService
```

The goal is to mirror Task Tracker’s move from controllers into `TaskService`.

### P2-2: Create `Game` Domain Model

Create `app/models/game.py`:

```python
from dataclasses import dataclass, field
from typing import List, Optional, Dict, Any

@dataclass
class Game:
        id: int
        game_type: str
        players: List[str] = field(default_factory=list)
        state: Dict[str, Any] = field(default_factory=dict)
        winner: Optional[str] = None

        def to_dict(self) -> Dict[str, Any]:
                """Serialize Game to a JSON-friendly dict."""
                return {
                        "id": self.id,
                        "game_type": self.game_type,
                        "players": self.players,
                        "state": self.state,
                        "winner": self.winner,
                }
```

Write tests for the `Game` model in `tests/domain/test_game_model.py`:

```python
from app.models.game import Game

def test_game_to_dict_includes_basic_fields():
        game = Game(id=1, game_type="trivia", players=["Alice"], state={"round": 1})
        result = game.to_dict()
        assert result["id"] == 1
        assert result["game_type"] == "trivia"
        assert result["players"] == ["Alice"]
        assert result["state"]["round"] == 1
        assert result["winner"] is None
```

Run the tests:

```bash
pytest tests/domain/test_game_model.py -v
```

### P2-3: Implement `GameService` (In-Memory)

Create `app/services/game_service.py`:

```python
from typing import Dict, Any, List
from app.models.game import Game

class GameService:
        """In-memory game manager."""

        def __init__(self) -> None:
                self._games: Dict[int, Game] = {}
                self._next_id: int = 1

        def create_game(self, game_type: str, players: List[str]) -> Dict[str, Any]:
                game = Game(
                        id=self._next_id,
                        game_type=game_type,
                        players=list(players),
                        state={"round": 1, "status": "in_progress"},
                )
                self._games[self._next_id] = game
                self._next_id += 1
                return game.to_dict()

        def get_game_state(self, game_id: int) -> Dict[str, Any]:
                game = self._games.get(game_id)
                if not game:
                        raise KeyError(f"Game {game_id} not found")
                return game.to_dict()
```

Write tests for `GameService` in `tests/services/test_game_service.py`:

```python
from app.services.game_service import GameService

def test_create_game_returns_dict_with_id_and_players():
        service = GameService()
        result = service.create_game("trivia", ["Alice", "Bob"])
        assert result["id"] == 1
        assert result["players"] == ["Alice", "Bob"]
        assert result["state"]["status"] == "in_progress"

def test_get_game_state_returns_same_data():
        service = GameService()
        created = service.create_game("trivia", ["Alice"])
        state = service.get_game_state(created["id"])
        assert state["id"] == created["id"]
        assert state["players"] == ["Alice"]
```

Run the tests:

```bash
pytest tests/services/test_game_service.py -v
```

---

The document continues with detailed steps for building the Flask app, implementing routes, creating templates, and adding tests. Each phase builds incrementally, ensuring clarity and focus on test-driven development principles.
