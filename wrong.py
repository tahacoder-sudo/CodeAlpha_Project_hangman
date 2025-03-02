databases = {}
menu = """
    Welcome to the Database Management System :)
    Please select an option:
    1. Create a new database
    2. Open an existing database
    3. Exit
"""

# main menu
while True:
    print(menu)

    choice = input("Enter your choice: ")

    if choice == "1":
        # 1) Creating
        database_name = input("Enter the name of the new database: ")
        if database_name in databases:
            print("A database with this name already exists. Please try a different name.")
        else:
            metadata = []
            while True:
                field_name = input("Enter field name (or press 'x' to finish): ")
                if field_name.lower() == 'x':
                    break
                field_length = input("Enter length for this field (integer): ")
                if field_length.isdigit():
                    metadata.append({'field name': field_name, 'field length': int(field_length)})
                else:
                    print("Please enter a valid integer for length.")
            databases[database_name] = {'metadata': metadata, 'records': []}
            print(f"Database '{database_name}' created successfully.")

    elif choice == "2":
        # 2) Opening existing database
        database_name = input("Enter the name of the database to open: ")
        if database_name in databases:
            print(f"Database '{database_name}' opened successfully.")
            while True:
                print("""
                Database Options:
                1. Add a record
                2. Edit a record
                3. Delete a record
                4. View all records
                5. Return to the main menu
                """)

                db_choice = input("Enter your choice: ")

                if db_choice == "1":
                    # Adding
                    new_record = {}
                    for field in databases[database_name]['metadata']:
                        field_name = field['field name']
                        field_value = input(f"Enter value for '{field_name}' (or 'x' to exit): ")
                        if field_value.lower() == 'x':
                            break
                        new_record[field_name] = field_value
                    databases[database_name]['records'].append(new_record)
                    print("Record added successfully.")

                elif db_choice == "2":
                    # Editing
                    records = databases[database_name]['records']
                    if not records:
                        print("No records to edit.")
                    else:
                        for i, record in enumerate(records):
                            print(f"{i + 1}. {record}")
                        record_index = input("Enter the record number to edit (or 'x' to cancel): ")
                        if record_index.isdigit():
                            record_index = int(record_index) - 1
                            if 0 <= record_index < len(records):
                                record = records[record_index]
                                for field in databases[database_name]['metadata']:
                                    field_name = field['field name']
                                    current_value = record[field_name]
                                    new_value = input(
                                        f"Current '{field_name}': {current_value}. Enter new value (or press Enter to keep): ")
                                    if new_value:
                                        record[field_name] = new_value
                                print("Record updated successfully.")
                            else:
                                print("Invalid record number.")
                        elif record_index.lower() != 'x':
                            print("Invalid input. Please enter a valid record number.")

                elif db_choice == "3":
                    # Deleting
                    records = databases[database_name]['records']
                    if not records:
                        print("No records to delete.")
                    else:
                        for i, record in enumerate(records):
                            print(f"{i + 1}. {record}")
                        record_index = input("Enter the record number to delete (or 'x' to cancel): ")
                        if record_index.isdigit():
                            record_index = int(record_index) - 1
                            if 0 <= record_index < len(records):
                                records.pop(record_index)
                                print("Record deleted successfully.")
                            else:
                                print("Invalid record number.")
                        elif record_index.lower() != 'x':
                            print("Invalid input. Please enter a valid record number.









