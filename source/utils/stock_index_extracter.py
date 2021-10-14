import pandas as pd
import tushare as ts


def get_stock_change_detail_info(stock_code='301013.SZ', start_date='20210920', end_date='20210929'):
    """Get stock change price detail information.

    Returns:
        pandas.DataFrame 'stock_change_detail_info': A stock price change detail info.
    """
    pd.set_option('display.max_columns', None)
    pro = ts.pro_api()
    stock_change_detail_info = pro.query('daily', ts_code=stock_code, start_date=start_date, end_date=end_date)
    stock_change_detail_info = stock_change_detail_info.sort_values(by='trade_date', ascending=True)
    return stock_change_detail_info


def get_stock_change_ratio(stock_code='301013.SZ', start_date='20210920', end_date='20210929'):
    """Get stock change price ratio.

    Returns:
        pandas.DataFrame 'stock_change_detail_info': A stock price change detail info.
    """
    stock_change_detail_info = get_stock_change_detail_info(stock_code=stock_code, start_date=start_date,
                                                            end_date=end_date)
    size = len(stock_change_detail_info['close'])

    if size != 0:
        stock_change = stock_change_detail_info['close'][0] - stock_change_detail_info['close'][size - 1]
        stock_change_ratio = stock_change / stock_change_detail_info['close'][0]

        return stock_change_ratio


def get_company_latest_basic_eps(stock_code="688662.SH"):
    # 拉取数据
    pro = ts.pro_api('312ec2805a662c9a5d199ac0f8bd6d6c38676e6d011a0432b47728e6')
    latest_basic_eps_info = pro.income(**{
        "ts_code": stock_code,
        "ann_date": "",
        "f_ann_date": "",
        "start_date": 20210401,
        "end_date": 20210901,
        "period": "",
        "report_type": "",
        "comp_type": "",
        "limit": "",
        "offset": ""
    }, fields=[
        "ts_code",
        "basic_eps",
        "ann_date",
        "end_date"
    ])
    latest_basic_eps_info = latest_basic_eps_info.sort_values(by='ann_date', ascending=True)
    basic_eps = latest_basic_eps_info['basic_eps'][0]
    # print(basic_eps)
    return basic_eps
