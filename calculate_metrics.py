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
def highest_sales_volume(sales_volume_daily):
    return max(sales_volume_daily, key=sales_volume_daily.get)

def highest_sales_value(sales_value_daily):
    return max(sales_value_daily, key=sales_value_daily.get)

def most_products_sold(product_sales):
    return max(product_sales, key=product_sales.get)

def highest_sales_staff_monthly(monthly_sales_staff):
    highest_sales_staff = {}
    for month, sales_staff in monthly_sales_staff.items():
        staff_with_most = max(sales_staff, key=sales_staff.get)
        highest_sales_staff[month] = (staff_with_most, sales_staff[staff_with_most])

    return highest_sales_staff

def highest_hour_avg_transactions(avg_trasaction_hourly):
    return max(avg_trasaction_hourly, key= lambda x: sum(avg_trasaction_hourly[x])/ len(avg_trasaction_hourly[x]))