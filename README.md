# Python Project Template
# ai_dev

This is the core AI Python development environment.

## Features

- Conda-based environment with reproducible `environment.yml`
- Fast, deterministic installs using [`uv`](https://github.com/astral-sh/uv)
- Linting and formatting with `ruff`
- Git hygiene enforced via `pre-commit`

## Setup

```bash
# Create env
conda env create -f environment.yml
conda activate ai_dev

# Install Python packages (fast)
uv pip install -r requirements.txt

# Enable pre-commit hooks
pre-commit install
