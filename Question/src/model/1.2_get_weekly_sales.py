"""
1.2_get_weekly_sales
"""
"Getting differences in sales data to make data stationary"

def get_diff(data):
    data['sales_diff'] = data['sales_qty'].diff()
    data = data.dropna()
    
    data.to_csv('../data/stationary_df.csv')
    return data

"Getting Weekly Data"

def weekly_data(data):
    data1 = data[['item_code','outlet_code','DATE','sales_qty']]
    data1['DATE'] =data1['DATE'] - pd.to_timedelta(7, unit='d')
    #calculate max of values, grouped by week
    return data1.groupby([pd.Grouper(key='DATE',freq='W'),'outlet_code','item_code'])['sales_qty'].sum().reset_index()