import click
from flask.cli import with_appcontext


@click.command("init")
@with_appcontext
def init():
    """Create a new admin user"""
    from my_api.extensions import db
    from my_api.models import Project, User

    click.echo("create user")
    # TODO change this for input datas
    user = User(  # nosec
        login="admin",  # nosec
        name="administrator",  # nosec
        email="admin@mail.com",  # nosec
        password="P4s$w0rd",  # nosec
        active=True,  # nosec
    )  # nosec
    db.session.add(user)
    click.echo("created user admin")

    db.session.commit()
