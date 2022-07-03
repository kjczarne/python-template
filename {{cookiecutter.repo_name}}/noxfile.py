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

