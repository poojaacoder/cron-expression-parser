import click

from cron_parser.parse_cron_expression import ParseCronExpression

@click.command()
@click.argument('expression', default= "")
@click.argument('command')
def cli(expression, command):
    try:
        if expression:
            output = ParseCronExpression(expression, command).evaluate()
            click.echo("Cron Expression Parser \n")
            click.echo(output)
        else:
            click.echo("Missing argument : cron expression.")
    except Exception as e:
        print("Exception occured : ",e)


if __name__ == '__main__':
    cli()
