import csv

def compare_csv_files(file1_path, file2_path):
    # Load the contents of the first CSV file into a set
    file1_data = set()
    with open(file1_path, 'r') as file1:
        reader = csv.reader(file1)
        next(reader)  # Skip the header row
        for row in reader:
            transaction_id = row[0]
            file1_data.add(transaction_id)

    # Load the contents of the second CSV file into a set
    file2_data = set()
    with open(file2_path, 'r') as file2:
        reader = csv.reader(file2)
        next(reader)  # Skip the header row
        for row in reader:
            transaction_id = row[0]
            file2_data.add(transaction_id)

    # Find the missing TransactionIDs in each file
    missing_in_file1 = file2_data - file1_data
    missing_in_file2 = file1_data - file2_data

    # Display the missing TransactionIDs
    if missing_in_file1:
        print("Missing TransactionIDs in File1:")
        for transaction_id in missing_in_file1:
            print(transaction_id)
    else:
        print("No missing TransactionIDs in File1.")

    if missing_in_file2:
        print("Missing TransactionIDs in File2:")
        for transaction_id in missing_in_file2:
            print(transaction_id)
    else:
        print("No missing TransactionIDs in File2.")

    # Find the vice versa missing TransactionIDs
    missing_in_both = missing_in_file1.union(missing_in_file2)

    if missing_in_both:
        print("Missing TransactionIDs in both files:")
        for transaction_id in missing_in_both:
            print(transaction_id)
    else:
        print("No missing TransactionIDs in both files.")

# Provide the file paths for comparison
file1_path = 'Files/File1.csv'
file2_path = 'Files/File2.csv'

# Call the function to compare the CSV files
compare_csv_files(file1_path, file2_path)
