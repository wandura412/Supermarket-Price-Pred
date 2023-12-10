print("Configuration_script")

# COMMAND ----------

def get_conf():
    
    conf = {
        "paths": {
            "item_info_path" : "..\data\item_info.csv",
            "store_info_path" : "../data/outlet_info.csv",
            "trx_info_path" :  "../data/transactions_info.csv",
        },
        "dates": {
            "start_date": "2022-01-21",
            "end_date": "2022-10-13"
        },
        "required_columns":{
            "store_info": ["stg_outlet_cd", "stg_outlet_area_ft_val", "stg_outlet_parking_lots_num", 
                           "stg_outlet_profile_cat", "stg_outlet_cluster_cat"],
            "item_info": ["stg_item_cd", "stg_item_category_desc_txt", "stg_item_dept_desc_txt"],
            "inscope_departments": ["Grocery", "Chilled", "Beverages", "Household"]
        },
        "params":{
            "no_categories": 5
        },
        "train_test_split": {
            "cutoff": 0.8
        }
    }
    
    return conf