import nox


@nox.session
def uml(session: nox.Session):
    session.install(".")
    session.install("pylint")
    session.install("pydot")
    import pydot
    with session.chdir("design"):
        session.run(*"pyreverse {{cookiecutter.package_name}}".split(" "))


@nox.session
def lint(session: nox.Session):
    session.install("flake8")
    session.run("flake8")


@nox.session
def test(session: nox.Session):
    session.install(".")
    session.install("pytest")
    session.run("pytest")


@nox.session
def whl(session: nox.Session):
    session.run(*"python -m setup bdist_wheel".split(" "))


@nox.session
def send(session: nox.Session):
    session.install("twine")
    token = session.env.get("TWINE_TOKEN")
    if not token:
        raise ValueError("PyPi upload token not set!")
    session.run(*"twine upload dist/*.whl -u __token__ -p".split(" "), token)
