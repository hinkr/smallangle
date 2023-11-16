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
    help="Amount of steps between 0 and 2 pi",
    show_default=True,
)
def sin(number):
    """Make a dataframe of chosen values and their sinus between 0 and 2 pi

    Args:
        number (int): Amount of steps between 0 and 2 pi
    """
    x = np.linspace(0, 2 * pi, number)
    df = pd.DataFrame({"x": x, "sin (x)": np.sin(x)})
    print(df)
    return


@main.command()
@click.option(
    "-n",
    "--number",
    default=10,
    help="Amount of steps between 0 and 2 pi",
    show_default=True,
)
def tan(number):
    """Make dataframe of chosen values and their tangent between 0 and 2 pi

    Args:
        number (int): Amount of steps between 0 and 2 pi
    """
    x = np.linspace(0, 2 * pi, number)
    df = pd.DataFrame({"x": x, "tan (x)": np.tan(x)})
    print(df)
    return


@main.command()
@click.argument("epsilon")
def approx(epsilon):
    """Find the upper limit for the small-angle approximation for a chosen accuracy

    Args:
        epsilon (float): accuracy
    """
    angle = 0
    while np.abs(angle - np.sin(angle)) <= float(epsilon):
        angle += 0.001
    print(
        f"For an accuracy of {epsilon},",
        f"the small-angle approximation holds up to x = {round(angle,3)}",
    )
    return


if __name__ == "__main__":
    main()
