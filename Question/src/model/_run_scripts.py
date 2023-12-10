# Databricks notebook source
"""
RUN ALL SUPPORTING NOTEBOOKS FOR MASTER TABLE CREATION
"""

# COMMAND ----------

# MAGIC %run ../utils/_run_scripts

# COMMAND ----------

# MAGIC %run ./1.0_preprocess_datasources

# COMMAND ----------

# MAGIC %run ./1.1_identify_fast_moving_items

# COMMAND ----------

# MAGIC %run ./1.2_get_weekly_sales

# COMMAND ----------

# MAGIC %run ./1.3_create_primary_keys

# COMMAND ----------

# MAGIC %run ./1.4_create_target_variable

# COMMAND ----------

# MAGIC %run ./1.5_sales_related_features

# COMMAND ----------

# MAGIC %run ./1.6_time_related_features

# COMMAND ----------

# MAGIC %run ./1.7_store_related_features

# COMMAND ----------

# MAGIC %run ./1.8_create_master_table

# COMMAND ----------

# MAGIC %run ./1.9_encoding_variables

# COMMAND ----------

# MAGIC %run ./2.0_pipeline_fitting

# COMMAND ----------

# MAGIC %run ./2.1_train_test_split

# COMMAND ----------

# MAGIC %run ./2.2_train_model

# COMMAND ----------

# MAGIC %run ./2.3_transform_model

# COMMAND ----------

# MAGIC %run  ./2.4_calculate_accuracy_metrices

# COMMAND ----------

# MAGIC %run ./2.5_calculate_weekly_mape