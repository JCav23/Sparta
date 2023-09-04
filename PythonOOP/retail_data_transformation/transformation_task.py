import csv

def data_cleaning(csv_file_name):
    customer_data = []
    with open(csv_file_name, newline="") as csvfile:
        sales_csv = csv.reader(csvfile, delimiter=",")

        for transaction in sales_csv:
            transaction_data = []
            if transaction[5] == "Electronics":
                transaction_data.append(transaction[1])
                transaction_data.append(transaction[3])
                transaction_data.append(transaction[4])
                transaction_data.append(transaction[5])
                transaction_data.append(transaction[-1])
                customer_data.append(transaction_data)

    return customer_data


print(data_cleaning("retail_sales_dataset.csv"))


def write_clean_data(old_file="retail_sales_dataset.csv", new_file="category_transactions.csv"):
    clean_data = data_cleaning(old_file)
    with open(new_file, "w", newline='') as new_file:
        csv_writer = csv.writer(new_file)
        csv_writer.writerows(clean_data)


write_clean_data()