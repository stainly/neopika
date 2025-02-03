# Guidelines for Contributing

NeoPika welcomes contributions in all forms. These may be bugs, feature requests, documentation, or examples. Please feel free to:

1. Submit an issue
2. Open a pull request
3. Help with outstanding issues and pull requests 

## Open an issue

If you find a bug or have a feature request, please [open an issue](https://github.com/stainly/neopika/issues) on GitHub. Please just check that the issue doesn't already exist before opening a new one.

## Local development steps

### Create a forked branch of the repo

Do this once but keep it up to date:

1. [Fork the kayak/NeoPika repo on GitHub](https://github.com/stainly/neopika/fork)
2. Clone forked repo and set upstream:

```bash
git clone git@github.com:<your-username>/neopika.git
cd neopika
git remote add upstream git@github.com:stainly/neopika.git
```

### Setup local development environment

1. Setup up python virtual environment

   Create and activate the environment using `uv`:

   ```bash
   uv sync --all-groups
   ```

2. Run the tests

   The unit tests are run with `unittest` via `tox`. To run the tests locally:

   ```bash
   uv run --dev tox
   ```

   These tests will also run on GitHub Actions when you open a pull request.

3. Build the docs locally

   Our docs are built with MkDocs. To build the docs locally:

   ```bash
   uv run --docs mkdocs build
   ```

   To serve the docs locally with hot-reloading:

   ```bash
   uv run --docs mkdocs serve
   ```

## Pull Request checklist

Please check that your pull request meets the following criteria:

- Unit tests pass
- pre-commit hooks pass
- Docstring and examples and checking for correct render in the docs

## Documentation

Documentation is built with MkDocs and hosted on [Read the Docs](https://neopika.readthedocs.io/en/latest/). The latest builds are displayed on their site [here](https://readthedocs.org/projects/neopika/builds/).

The code documentation is to be written in the docstrings of the code itself or in the various `.md` files in project root or the `docs/` directory.

The docstrings should follow the [Google style](https://google.github.io/styleguide/pyguide.html#38-comments-and-docstrings) format.
