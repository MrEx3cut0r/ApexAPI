import click

@click.group()
def cli():
    pass

@cli.command()
def new(project_name: str):
    pass

@cli.command()
@click.option("--host", default="localhost")
@click.option("--port", default=8080)
@click.option("--reload", default=True)
def run(
    host: str,
    port: int,
    reload: bool
):
    pass

@cli.command()
@click.option("--message", default="localhost")
@click.option("--auto", default=False)
@click.option("--upgrade", default=False)
@click.option("--downgrade", default=False)
def migrate():
    pass

@cli.command()
def generate():
    pass

@cli.command()
def test():
    pass

@cli.command()
def docs():
    pass

@cli.command()
def deploy():
    pass

@cli.command()
def config():
    pass

@cli.command()
def shell():
    pass
