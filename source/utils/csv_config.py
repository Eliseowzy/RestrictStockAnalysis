import pandas as pd


def get_list_by_column(file_name='../data/restrict_stock_detail_20210909.csv', column_name='代码', encoding='gb18030'):
    """Get stock name list from a table.

    Returns:
        list 'code': A stock code list.
    """
    df = pd.read_csv(file_name, encoding=encoding)
    stock_code_list = []
    for stock in df[column_name]:
        stock_code_list.append(stock)
    return stock_code_list
