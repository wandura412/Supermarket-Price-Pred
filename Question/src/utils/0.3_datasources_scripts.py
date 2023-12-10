# Databricks notebook source
print("Module: 0.3 Data Sources Dictionary")

# COMMAND ----------

def get_datasources(conf):
    
    """
    Get datasources required
    """
  
    datasources = {
        "item_df": get_items_info(conf),
        "store_df": get_stores_info(conf),
        "trx_df": get_trx_info(conf)
    }
    
    return datasources