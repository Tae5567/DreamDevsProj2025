"""
Task: Given a sample data folders of .txt transaction files, write software that:
    - Reads through transaction files in all folders 
    Note line format in transaction file: “4,2025-01-01T16:58:53,[726107:5|553776:5],2114.235”
    
    Reports:
    - Highest sales volume in a day (max sold products quantity??? and date )
    - Highest sales value in a day( max sales amount and date)
    - Most sold product ID by volume (max product quantity and productId, should retunr only one out od product1 and product2)
    - Highest sales staff ID for each month. (max staffID???) MAX sales value or MAX total products sold by salesstaffID
    - Highest hour of the day by average transaction volume (max hour at avg sales amount???)

"""
import os
from process_files import process_files, sales_volume, sales_value, products_sold, sales_staff_monthly, avg_transaction_hour
from calculate_metrics import (
    highest_sales_volume, 
    highest_sales_value,
    most_products_sold, 
    highest_sales_staff_monthly,
    highest_hour_avg_transactions)

#transaction data directory
DATA_DIR = "sample" #renamed to sample-data

def report_metrics(sales_volume_daily, sales_value_daily, product_sales, monthly_sales_staff, avg_transaction_hourly):

    highest_salesVolume_day = highest_sales_volume(sales_volume_daily)
    highest_salesValue_day = highest_sales_value(sales_value_daily)
    highest_products_sold = most_products_sold(product_sales)
    highest_sales_staff = highest_sales_staff_monthly(monthly_sales_staff)
    highest_hour_onAvg = highest_hour_avg_transactions(avg_transaction_hourly)
    #avg_sales_volume = sum(avg_transaction_hour[highest_hour_onAvg]/len(avg_transaction_hour))


    #Print a report of the metrics
    print("Highest sales volume in a day:")
    print(f"{highest_salesVolume_day} ({sales_volume_daily[highest_salesVolume_day]} items)")


if __name__ == "__main__":
    print("\n Monieshop Analytics Report \n")

    #Check if sample data directory actually exists first
    if not os.path.exists(DATA_DIR):
        print("Error! Data directory does not exist!")
        exit(1)
    
    #If directory exists, process transaction files
    process_files(DATA_DIR) #taking DATA_DIR as folder_path

    #Show report
    report_metrics(sales_volume, sales_value, products_sold, sales_staff_monthly, avg_transaction_hour)
