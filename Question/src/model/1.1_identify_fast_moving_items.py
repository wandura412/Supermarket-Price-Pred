"""
1.1_identify_fast_moving_category
"""
"Finding top 5 fast moving items in each outlet"

def fast_moving_outlet(data):
    filter1 = data[['outlet_code','item_code','sales_qty']]
    df_agg = filter1.groupby(['outlet_code','item_code']).agg({'sales_qty':sum})
    g = df_agg['sales_qty'].groupby('outlet_code', group_keys=False)
    res = g.apply(lambda x: x.sort_values(ascending=False).head(5))
    out1 = res.reset_index()
    out2 = pd.merge(out1,item_df,on='item_code')[['outlet_code','item_code','item_category','sales_qty']]
    return out2.groupby(['outlet_code','item_code','item_category']).agg({'sales_qty':sum})
    
"Finding Which items are the fastest moving from a product category"

def product_weekday(data):
    week1_top5 = weekday_top5(data)
    week1_top5 = week1_top5.reset_index(inplace=False)
    week1_top5_product = week1_top5[week1_top5['item_code']==898]
    fig, ax = plt.subplots(figsize=(15,5))
    sns.barplot(data=week1_top5_product,x='Weekday',y='sales_qty')
    ax.set(xlabel = "Weekday",
           ylabel = "Sales Quantity",
           title = "Variation of Weekday with Sales Quantity")

"Variation of outlet size with outlet code"   
def outlet_size_type(data):
    fig, ax = plt.subplots(figsize=(15,5))
    sns.barplot(data=data,x='outlet_code',y='outlet_area')
    ax.set(xlabel = "Outlet Code",
           ylabel = "Outlet Area",
           title = "Outlet Size variaiton with type ")

"Variation of car park size with outlet size"

def outlet_parking(data):
    fig, ax = plt.subplots(figsize=(15,5))
    sns.lineplot(data=data,y='outlet_parking_lots',x='outlet_area')
    ax.set(ylabel = "Number of parking lots",
           xlabel = "Outlet Area",
           title = "Parking space variation with outlet size ")
