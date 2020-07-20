import click

@click.command()
@click.option('--count', default=1, help='number of gretings')
@click.argument('name')
def batman(count, name):
    for _ in range(count):
        click.echo(f'Batman and {name}!')


if __name__ == "__main__":
    batman()
