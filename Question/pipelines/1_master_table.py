"""
Building the master table
"""
# Merging data to create master table
def merge_data(data1,data2,data3):
    merge1=pd.merge(data1,data2,on='outlet_code')
    merge2=pd.merge(merge1,data3,on='item_code')
    return merge2

master_table=merge_data(trans_df,outlet_df,item_df)

stores =['A','B','C','D','E']
departments = ['Grocery','Beverages','Chilled']

#filtering data according to above criteria

def filter_data(data):
    filter1 = master_table[master_table['outlet_code'].isin(stores)]
    filter2= filter1[filter1['item_department'].isin(departments)]
    filter2['DATE']=pd.to_datetime(filter2['DATE'])
    return filter2