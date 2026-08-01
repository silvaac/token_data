# AGENTS.md

## CI
- Workflow: `.github/workflows/test.yaml` uses `fastai/workflows/nbdev3-ci@master` with Python `3.11`.
- The nbdev3-ci action installs `nbdev>=3.2.1` (currently resolves to 3.3.3) and runs:
  `pip install -e ".[dev]"`, then `nbdev-clean` (checks notebooks are stripped), then
  `nbdev-export` (fails if library/notebooks are out of sync), then `nbdev-test`.
- Deploy: `.github/workflows/deploy.yaml` builds Quarto docs on push to main/master.

## Build / install
- `pip install -e ".[dev]"` — editable install (uses build isolation; fetches latest setuptools).
- The `dev` extra is declared via `setup.py` (`extras_require`), not in `pyproject.toml`.

## nbdev commands (use nbdev 3.3.3 to match CI)
- `nbdev-clean` — strip notebook outputs.
- `nbdev-export` — sync notebooks -> `token_data/*.py` + `_modidx.py` + `pyproject.toml`.
- `nbdev-test` — run notebook tests (requires the project's runtime deps installed).

## Gotchas
- `setup.py` must NOT import `pkg_resources`. setuptools 81+ removed it, and pip's isolated
  build env fetches the latest setuptools, so `from pkg_resources import ...` fails with
  `ModuleNotFoundError: No module named 'pkg_resources'` during editable build.
- nbdev 3.3.3 reads config from `pyproject.toml`'s `[tool.nbdev]` section + `[project]`
  (NOT `settings.ini`). `settings.ini` is legacy and only used by `setup.py` (direct read).
  `get_config().min_python` comes from `pyproject.toml`'s `requires-python`.
- Keep `requires-python` in `pyproject.toml` and `min_python` in `settings.ini` in sync.
  Both must be `>=3.11` (CI runs Python 3.11; 3.14 is unreleased and unsatisfiable on CI).
- `nbdev-export`'s `update_proj` only rewrites the `name` and `requires-python` lines in
  `pyproject.toml` (targeted regex), so manual edits to `[build-system]` survive export.

## Verify a build locally (reproduces the CI build env)
- Use a venv with a recent setuptools (>=81, which lacks `pkg_resources`):
  `pip wheel --no-deps -w /tmp/whl .` should succeed.
