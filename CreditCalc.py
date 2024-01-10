import math
import click

@click.command()
@click.option("--type", required=True, help="The type must be either 'diff' or 'annuity'")
@click.option("--principal", type=float, help="Enter a positive principal number")
@click.option("--periods", type=int, help="Enter a positive periods number")
@click.option("--interest", type=float, help="Enter a positive interest number")
@click.option("--payment", type=float, help="Enter a positive payment number", required=False)
def command_line(type, principal, periods, interest, payment):
    if (principal is not None and principal <= 0) or \
       (periods is not None and periods <= 0) or \
       (interest is not None and interest <= 0) or \
       (payment is not None and payment <= 0):
        click.echo("Incorrect parameters.")
        return

    if type == "diff" and payment is not None:
        click.echo("Incorrect parameters.")
        return

    if type == "diff":
        if principal is not None and periods is not None and interest is not None:
            i = float((interest / 100) / (12 * (100 / 100)))
            total = 0
            for month in range(1, periods + 1):
                payment = math.ceil((principal / periods) + i * (principal - ((principal * (month - 1)) / periods)))
                total += payment
                click.echo(f"Month {month}: payment is {payment}")
            overpayment = round(total - principal)
            click.echo(f"\nOverpayment = {overpayment}")
        else:
            click.echo("Incorrect parameters")
    elif type == "annuity":
        if principal is not None and periods is not None and interest is not None and payment is None:
            i = float((interest / 100) / (12 * (100 / 100)))
            payment = math.ceil(principal * (i * (1 + i)**periods) / ((1 + i)**periods - 1))
            click.echo(f"Your annuity payment = {payment}!")
            total = payment * periods
            overpayment = round(total - principal)
            click.echo(f"Overpayment = {overpayment}")

        elif payment is not None and periods is not None and interest is not None and principal is None:
            i = float((interest / 100) / (12 * (100 / 100)))
            principal = math.floor(payment / ((i * (1 + i) ** periods) / ((1 + i) ** periods - 1)))
            click.echo(f"Your loan principal = {principal}!")
            total = payment * periods
            overpayment = round(total - principal)
            click.echo(f"Overpayment = {overpayment}")

        elif payment is not None and periods is None and interest is not None and principal is not None:
            i = float((interest / 100) / (12 * (100 / 100)))
            n = math.ceil(math.log(payment / (payment - i * principal), 1 + i))
            years = n // 12
            months = n % 12
            if years < 1:
                click.echo(f"It will take {months} months to repay this loan!")
            elif months == 0:
                click.echo(f"It will take {years} years to repay this loan!")
            else:
                click.echo(f"It will take {years} years and {months} months to repay this loan!")

            total = payment * n
            overpayment = round(total - principal)
            click.echo(f"Overpayment = {overpayment}")

        else:
            click.echo("Incorrect parameters.")

    else:
        click.echo("Unknown type was provided")


if __name__ == "__main__":
    command_line()
