import click
import numpy as np
import pandas as pd
from numpy import pi


@click.group()
def main():
    pass


@main.command()
@click.option(
    "-n",
    "--number",
    default=10,
    help="Amount of steps between 0 and 2pi",
    show_default=True,
)
def sin(number):
    x = np.linspace(0, 2 * pi, number)
    df = pd.DataFrame({"x": x, "sin (x)": np.sin(x)})
    print(df)
    return


@main.command()
@click.option(
    "-n",
    "--number",
    default=10,
    help="Amount of steps between 0 and 2pi",
    show_default=True,
)
def tan(number):
    x = np.linspace(0, 2 * pi, number)
    df = pd.DataFrame({"x": x, "tan (x)": np.tan(x)})
    print(df)
    return


if __name__ == "__main__":
    main()
