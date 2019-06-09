import click
from gui import Gui


@click.group()
def cli():
    pass


@cli.command()
def gui():
    app = Gui()
    app.mainloop()


if __name__ == '__main__':
    cli()
