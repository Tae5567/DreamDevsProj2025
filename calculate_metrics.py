#This file contains functions for calculating the metrics to be reported
"""
Reports:
    - Highest sales volume in a day (max sold products quantity??? and date )
    - Highest sales value in a day( max sales amount and date)
    - Most sold product ID by volume (max product quantity and productId, should retunr only one out od product1 and product2)
    - Highest sales staff ID for each month. (max staffID???) MAX sales value or MAX total products sold by salesstaffID
    - Highest hour of the day by average transaction volume (max hour at avg sales amount???)
"""

#use max function to return highest values vs key object of same data type

def highest_sales_volume(sales_volume):
    return max(sales_volume, key=sales_volume.get)

def highest_sales_value(sales_value):
    return max(sales_value, key=sales_value.get)

def most_products_sold(products_sold):
    return max(products_sold.items(), key=products_sold.get)

def highest_sales_staff_monthly(sales_staff_monthly):
    highest_sales_staff = {}
    for month, sales_staff in sales_staff_monthly.items():
        if sales_staff:
            highest_sales_staff[month] = max(sales_staff, key =sales_staff.get)
    
    return highest_sales_staff

def highest_hour_avg_transactions(avg_trasaction_hourly):
    return max(avg_trasaction_hourly, key= lambda hour: sum(avg_trasaction_hourly[hour])/ len(avg_trasaction_hourly[hour]))