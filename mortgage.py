import pandas as pd


def calc_paybacks(fund, year_interest, period_years, calc_interest_and_fund_func):
    month_interest = year_interest / 12.0
    months_count = period_years * 12
    curr_balance = fund
    paybacks_df = pd.DataFrame(columns=['fund', 'interest', 'total', 'balance'])
    while (curr_balance > 0):
        curr_fund, curr_interest = calc_interest_and_fund_func(fund, month_interest, months_count, curr_balance)
        paybacks_df = paybacks_df.append(
            {
                'fund': curr_fund,
                'interest': curr_interest,
                'total': curr_fund + curr_interest,
                'balance': curr_balance,
            },
            ignore_index=True)
        curr_balance -= curr_fund

    return paybacks_df


def const_fund_calc_interest_and_fund(fund, month_interest, months_count, curr_balance):
    curr_interest = curr_balance * month_interest
    curr_fund = fund / months_count

    return curr_fund, curr_interest


def const_fund(fund, year_interest, period_years):
    return calc_paybacks(fund, year_interest, period_years, const_fund_calc_interest_and_fund)


def shpitzer_calc_interest_and_fund(fund, month_interest, months_count, curr_balance):
    const_payback = fund / ((1 - (1 / ((1 + month_interest) ** months_count))) / month_interest)
    curr_interest = curr_balance * month_interest
    curr_fund = const_payback - curr_interest

    return curr_fund, curr_interest


def shpitzer(fund, year_interest, period_years):
    return calc_paybacks(fund, year_interest, period_years, shpitzer_calc_interest_and_fund)
