#!/usr/bin/env python3

### Import Statements ###

from test import test

### Functions ###


def stock_total(stock_list: list) -> list:
    """LP2

    Ex:
        DAY   1   5   8
        -----------------
        ST0  100 200  _
        ST1   _  50  100
        ST2  200  _  100
        -----------------
        T    300 450 400

    Args:
        stock_list (list): Represents stocks in certain days

    Returns:
        list: Total amount on each day
    """
    if not stock_list:
        return []

    # Set of dates > list based on order
    dates = set()

    for company in stock_list:
        for date, stock in company:
            if date not in dates:
                dates.add(date)

    dates = sorted(dates)

    # List of maps for dates to company lists
    company_maps = []

    for company in stock_list:
        company_map = {}

        for date, stock in company:
            company_map[date] = stock

        company_maps.append(company_map)

    # Do logic based on maps
    result = [0] * len(dates)
    last = dates[0]

    for i in range(len(dates)):
        date = dates[i]
        day_total = 0

        for company_map in company_maps:
            if date in company_map:
                day_total += company_map[date]
            elif i > 0:
                company_map[date] = company_map[last]
                day_total += company_map[date]

        result[i] = day_total
        last = date

    # Return result
    return [(dates[i], result[i]) for i in range(len(dates))]


if __name__ == "__main__":
    stock_list = [
        [("5/1", 100), ("5/5", 200)],
        [("5/5", 50), ("5/8", 100)],
        [("5/1", 200), ("5/8", 100)],
    ]
    expected = [("5/1", 300), ("5/5", 450), ("5/8", 400)]
    test(stock_total(stock_list), expected)
