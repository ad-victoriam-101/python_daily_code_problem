"""
When a candle finishes burning it leaves a leftover. makeNew leftovers can be combined to make a new candle, which,
when burning down, will in turn leave another leftover.

You have solutionNumber solution in your possession. What's the total number of solution you can burn,
assuming that you create new solution as soon as you have enough leftovers?
Example

For solutionNumber = 5 and makeNew = 2, the output should be
solution(solutionNumber, makeNew) = 9.
"""


def candle_solution(candlesNumber, makeNew):
    """

    Args:
        candlesNumber: integer
        The number of candles you have in your possession.
        makeNew:integer
        The number of leftovers that you can use up to create a new candle.

    Returns:

    """
    return candlesNumber + (candlesNumber - 1) // (makeNew - 1)


if __name__ == "__main__":
    assert candle_solution(5, 2) == 9
