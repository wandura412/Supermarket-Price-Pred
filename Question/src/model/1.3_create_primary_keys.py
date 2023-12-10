"""
1.3_create_primary_keys
"""
"Primary Key: Outlet"
def fast_moving_outlet(data):
    filter1 = data[['outlet_code','item_code','sales_qty']]
    df_agg = filter1.groupby(['outlet_code','item_code']).agg({'sales_qty':sum})
    g = df_agg['sales_qty'].groupby('outlet_code', group_keys=False)
    res = g.apply(lambda x: x.sort_values(ascending=False).head(5))
    out1 = res.reset_index()
    out2 = pd.merge(out1,item_df,on='item_code')[['outlet_code','item_code','item_category','sales_qty']]
    return out2.groupby(['outlet_code','item_code','item_category']).agg({'sales_qty':sum})

"Primary Key: Item Category"

def fast_moving_itemcat(data):
    filter1 = data[['item_category','item_code','sales_qty']]
    df_agg = filter1.groupby(['item_category','item_code']).agg({'sales_qty':sum})
    g = df_agg['sales_qty'].groupby('item_category', group_keys=False)
    res = g.apply(lambda x: x.sort_values(ascending=False).head(5))
    return res

itemcat1=pd.merge(weekly_filtered,item_df,on='item_code')[['item_code','item_category','sales_qty']]
fast_moving_itemcat(itemcat1)

"Primary Key: Weekdays"

def weekday_top5(data):
    data['Weekday'] = data['DATE'].dt.day_name()
    filter1 = data[['item_code','sales_qty','Weekday']]
    df_agg = filter1.groupby(['Weekday','item_code']).agg({'sales_qty':sum})
    g = df_agg['sales_qty'].groupby('Weekday', group_keys=False)
    res = g.apply(lambda x: x.sort_values(ascending=False).head(5))
    out1 = res.reset_index()
    out2 = pd.merge(out1,item_df,on='item_code')[['Weekday','item_code','item_category','sales_qty']]
    return out2.groupby(['Weekday','item_code','item_category']).agg({'sales_qty':sum})
