from read_file import load_medicines
from operations import display_medicines, handle_sales, handle_restock, get_integer_input

FILENAME = "medicines.txt"

def main():
    print("Initializing MedStore System...")
    medicines = load_medicines(FILENAME)
    
    while True:
        print("\n=====================================")
        print("       MEDSTORE WHOLESALE MENU")
        print("=====================================")
        print("1. View Medicine Inventory")
        print("2. Process Sales Transaction")
        print("3. Process Restock Transaction")
        print("4. Exit")
        print("=====================================")
        
        choice = get_integer_input("Enter your choice (1-4): ")
        
        if choice == 1:
            display_medicines(medicines)
        elif choice == 2:
            handle_sales(medicines)
        elif choice == 3:
            handle_restock(medicines)
        elif choice == 4:
            print("Exiting MedStore System. Goodbye!")
            break
        else:
            print("Error: Invalid choice. Please select 1-4.")

if __name__ == "__main__":
    main()
