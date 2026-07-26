# Testing

Tests live in `game/testcases.rpy` and use Ren'Py's built-in test framework
(`testsuite` / `testcase` statements). Add new tests there — do not create a
second file unless it grows large.

## Running

From the repo root, run the full suite:

```
/home/vadim/Загрузки/renpy-8.5.3-sdkarm/renpy.sh . test
```

Run one testcase by id (ids use `::`, e.g. `smoke::start_to_menu`,
`integrity::routing_labels_exist`):

```
/home/vadim/Загрузки/renpy-8.5.3-sdkarm/renpy.sh . test smoke::start_to_menu
```

Useful flags: `--hide-header`, `--report-detailed`.

## Requirements

- Tests need a **real display** (`DISPLAY=:0`). `SDL_VIDEODRIVER=dummy` hangs.
- Exit code 0 = pass, 1 = fail. CI should fail the build on non-zero.

## Test DSL cheat-sheet

```
testsuite name:          # a group of tests
    setup:               # runs once (set $ _test.timeout = N)
        ...
    before testcase:     # runs before each testcase
        ...
    testcase my_test:    # an individual test
        description "..."
        click "Начать" raw until screen "say"   # click button by text, wait for screen
        advance until screen "choice"           # advance dialogue until a screen appears
        click "Дебют Гроба" raw until screen "document_reader"
        assert screen "document_reader"         # assert a screen is shown
        $ value = renpy.has_label("demo_end")   # run python in store scope
        assert eval "value"                     # assert a python expression
        pause 0.5                               # fixed delay

testsuite global:        # special: wraps every other suite
    before testsuite:
        if not screen "main_menu":
            run MainMenu(confirm=False)
    teardown:
        exit                                 # quit the game after the run
```

### Key statements

| Statement | Purpose |
|---|---|
| `click "text" raw until <cond>` | click a button by text, repeat until condition |
| `advance until <cond>` | advance dialogue until condition (screen / label / text) |
| `assert screen "name"` | assert a screen is currently shown |
| `assert eval "expr"` | assert a python expression (uses store globals) |
| `$ code` | run python in store scope |
| `pause N` | fixed delay in seconds |
| `run Action()` | run a screen action (e.g. `Start()`, `MainMenu(confirm=False)`) |
| `keysym "K_RETURN"` | send a keypress |
| `type "text"` | type a string (for input screens) |

Conditions can use: `screen "name"`, `not screen "name"`, `label "name"`,
`eval "expr"`, `"text" raw`, combined with `and` / `or` / `not`.

## Existing tests

- **`smoke::start_to_menu`** — Start → dialogue → first menu → document reader.
  Covers the core advance → menu → screen flow.
- **`integrity::routing_labels_exist`** — all chapter labels wired in
  `script.rpy` are defined. Catches "label not found" crashes.
- **`integrity::sublabels_exist`** — key event/logic sublabels referenced via
  `call` exist (`ch2_4_rip_mask`, `parry`, `acquire_item`, …).
- **`integrity::items_registry_valid`** — every `ITEMS` entry has the required
  `name`/`img` keys.
- **`integrity::companions_and_masks_defined`** — `companion_chars` and core
  state helpers (`stat_add`, `set_companion`, `break_mask`, `leon_take_wound`)
  are defined in store.

## What to test and gotchas

- When you wire a new chapter label or item, add a check to the `integrity`
  suite — these catch "label not found" crashes deterministically.
- **Fast-skip stalls at menus.** `skip fast until label X` does NOT auto-pick
  choices in this Ren'Py version. Drive menus explicitly with
  `advance until screen "choice"` then `click "choice text" raw`.
- **`until label X` needs the label callback.** The smoke suite registers
  `renpy.test.testexecution.add_reached_label` in its `setup`; if you use
  `until label` in a new suite, register it too.
- **Assertions on store state**: `$` assigns into the store, then
  `assert eval "expr"` checks it. Reference globals directly
  (`callable(stat_add)`, `ITEMS`, `renpy.has_label(...)`).
- **Test isolation**: the `MainMenu(confirm=False)` action does not reliably
  reset from deep in a call stack. Keep each `smoke` testcase a single
  continuous flow (Start → … → final assertion) rather than relying on a
  `before testcase` reset between separate game-entry tests.
