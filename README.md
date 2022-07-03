# Python PyPI Package Template

This Cookiecutter is a basic Python Package template that contains:

- `setup.cfg` -> declarative definition of the package and its dependencies
  - `dev` extras -> minimal toolkit for effective high-quality development
    - `pdoc3` -> documentation builder
    - `flake8` -> linter of choice
    - `twine` -> to upload packages
    - `autopep8` -> autoformatter that complements `flake8`
    - `pytest` -> test runner
      - I generally use `unittest`, however `pytest` sometimes comes in handy as a runner with its `marker` feature.
  - `flake8` config -> opinionated config that does not depart from PEP8 too far but adds some sane linter config mods like extending the max line lenght to 100 characters
- `noxfile.py` -> my lint/test/build/deployment automation tool of choice
  - I usually use it both when developing and when running CI jobs for consistency
  - I find `tox` obnoxiously inflexible and the INI-format config file for `tox` is absurd
- `.coveragerc` -> `coverage.py` config
- `.editorconfig` -> so that your editor opens the file formats we care about in a proper manner
- `README.md` template -> no project should be left without at least a basic readme as a piece of documentation
- Source Code directory template -> with a sane layout named after the package itself (not `src`, which I frankly despise) and a tiny command-line application in `main.py`, since I never remember how to put things together in `argparse`.

