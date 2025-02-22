import os
import glob
import datetime
from collections import defaultdict

SAMPLE_DIR = "sample-data"

# initialise dictionaries to store metrics data values to handle mapping values     
sales_volume =  {}
sales_value = {}
products_sold = {}
sales_staff_monthly = defaultdict(dict)
avg_transaction_hour = defaultdict(list)

def process_transactions(file_path):
    #read transaction files and updates dictionary
    with open(file_path, "r") as file:
        for txt in file:
            line = txt.strip().split(',') # notice that each component/variable of a transaction line is split by a comma
            # A transaction line's components/variiables
            sales_staff_id = int(line[0])
            transaction_date_time = line[1]
            products = line[2].strip("[]").split("|") # notice that products/product quantities is inside [] in the data
            sale_amount = float(line[3])  

        #Track sales 
        total_products = 0
        for product in products: # each product with its corresponding quantity is separated by | before the next produc
            product_id, product_quantity = map(int, product.split(':'))
            total_products += product_quantity
            products_sold[product_id] = products_sold.get(product_id, 0) + product_quantity


        #Get date, month, hour from transaction_date_time
        date = datetime.datetime.fromisoformat(transaction_date_time) #original transaction date in ISO format: YYYY/MM/DD hours and minutes in the data
        transaction_date= date.date()
        transaction_month = transaction_date.strftime("%Y-%m") # get 4 digit year and 2 digit month from date
        transaction_hour = date.hour

        sales_volume[transaction_date] = sales_volume.get(transaction_date, 0) + total_products
        sales_value[transaction_date] = sales_value.get(transaction_date, 0) + sale_amount

        #Track highest sales staff (sales staff that sells the most (makes the most money?))
        if transaction_month not in sales_staff_monthly:
            sales_staff_monthly[transaction_month] = {} 
        sales_staff_monthly[transaction_month][sales_staff_id] = sales_staff_monthly[transaction_month].get(sales_staff_id, 0)+ sale_amount

        #Track transactions made per hour
        if transaction_hour not in avg_transaction_hour:
            avg_transaction_hour[transaction_hour] = []
        avg_transaction_hour[transaction_hour].append(total_products)


def process_files(data_dir):
    #read all transaction files in the particular directory/folder, e,g: test-case-1
    for folder in os.listdir(data_dir):
        folder_path = os.path.join(data_dir, folder)
        if os.path.isdir(folder_path): #ensure folder path is directory
            #get .txt files in the directory
            for file_path in glob.glob(os.path.join(folder_path, "*.txt")):
                process_transactions(file_path) #call function to process transactions
                                       







