# Databricks notebook source
print("Module: 0.2 Common data source utility functions")

# COMMAND ----------

def get_stores_info(conf):
    
    """
    Returns store information
    
    Parameters:
      conf (dict): Contains configurations
    
    Returns:
      pyspark dataframe: store_info
    """
        
    stores_info = read_csv(conf["paths"]["store_info_path"])
    
    stores_info = (
        stores_info
          .select(conf["required_columns"]["store_info"])
    )
    
    return stores_info

# COMMAND ----------

def get_items_info(conf):
    
    """
    Returns item information
    
    Parameters:
      conf (dict): Contains configurations
    
    Returns:
      pyspark dataframe: item_info
    """
    
    item_info = read_csv(conf["paths"]["item_info_path"])
    
    item_info = (
        item_info
          .select(conf["required_columns"]["item_info"])
    )
    
    return item_info

# COMMAND ----------

def get_trx_info(conf):
    
    """
    Returns transcation information
    
    Parameters:
      conf (dict): Contains configurations
    
    Returns:
      pyspark dataframe: trx_info
    """
    
    trx_info = read_csv(conf["paths"]["trx_info_path"])
    
    return trx_info