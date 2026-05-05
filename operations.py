from write_file import save_medicines, generate_sales_invoice, generate_restock_invoice

FILENAME = "medicines.txt"

def display_medicines(medicines):
    if not medicines:
        print("No medicines found in inventory.")
        return
    print("\n=====================================================================================================")
    print("                              MEDSTORE PVT. LTD. - MEDICINE INVENTORY")
    print("=====================================================================================================")
    print(f"{'No.':<4} | {'Medicine Name':<20} | {'Brand':<15} | {'Stock (Tabs)':<12} | {'Rate/Tab':<10} | {'Rate/Strip':<12} | {'Tabs/Strip':<10}")
    print("-" * 101)
    for i, med in enumerate(medicines):
        print(f"{i+1:<4} | {med['name']:<20} | {med['brand']:<15} | {med['stock']:<12} | {med['rate_tablet']:<10.2f} | {med['rate_strip']:<12.2f} | {med['tablets_per_strip']:<10}")
    print("=====================================================================================================")
    print(f"Total medicines listed: {len(medicines)}\n")

def get_integer_input(prompt):
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print("Error: Please enter a valid integer.")

def get_float_input(prompt):
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("Error: Please enter a valid number.")

def handle_sales(medicines):
    print("\n--- Sales Transaction ---")
    customer_name = input("Enter customer name: ").strip()
    if not customer_name:
        print("Customer name cannot be empty. Transaction cancelled.")
        return

    purchased_items = []
    total_cost = 0.0
    total_discount = 0.0

    while True:
        display_medicines(medicines)
        med_index = get_integer_input("Select Medicine No. to buy (or 0 to finish): ") - 1
        
        if med_index == -1:
            break
            
        if med_index < 0 or med_index >= len(medicines):
            print("Error: Invalid medicine selection.")
            continue
            
        med = medicines[med_index]
        
        print("Unit Type: 1. Tablet  2. Strip")
        unit_choice = get_integer_input("Select Unit Type (1 or 2): ")
        if unit_choice not in [1, 2]:
            print("Error: Invalid unit selection.")
            continue
            
        unit_type = "tablet" if unit_choice == 1 else "strip"
        quantity = get_integer_input(f"Enter quantity of {unit_type}s to buy: ")
        
        if quantity <= 0:
            print("Error: Quantity must be greater than 0.")
            continue
            
        tabs_needed = quantity if unit_type == "tablet" else quantity * med['tablets_per_strip']
        
        if tabs_needed > med['stock']:
            print(f"Error: Not enough stock! Available stock: {med['stock']} tablets.")
            continue

        cost = 0.0
        discount = 0.0
        
        if unit_type == "tablet":
            cost = quantity * med['rate_tablet']
        else:
            cost = quantity * med['rate_strip']
            if quantity >= 2:
                discount = cost * 0.05
                
        final_cost = cost - discount
        med['stock'] -= tabs_needed
        
        purchased_items.append({
            'name': med['name'],
            'brand': med['brand'],
            'unit_type': unit_type,
            'quantity': quantity,
            'cost': cost,
            'discount': discount,
            'final_cost': final_cost
        })
        
        total_cost += final_cost
        total_discount += discount
        print(f"Added {quantity} {unit_type}(s) of {med['name']} to cart.")
        
        more = input("Buy more items? (y/n): ").strip().lower()
        if more != 'y':
            break

    if purchased_items:
        save_medicines(FILENAME, medicines)
        generate_sales_invoice(customer_name, purchased_items, total_cost, total_discount)
        print("Sales transaction completed.")
    else:
        print("No items purchased.")

def handle_restock(medicines):
    print("\n--- Restock Transaction ---")
    supplier_name = input("Enter supplier name: ").strip()
    if not supplier_name:
        print("Supplier name cannot be empty. Transaction cancelled.")
        return

    restocked_items = []
    total_cost = 0.0

    while True:
        display_medicines(medicines)
        med_index = get_integer_input("Select Medicine No. to restock (or 0 to finish): ") - 1
        
        if med_index == -1:
            break
            
        if med_index < 0 or med_index >= len(medicines):
            print("Error: Invalid medicine selection.")
            continue
            
        med = medicines[med_index]
        
        print("Unit Type: 1. Tablet  2. Strip")
        unit_choice = get_integer_input("Select Unit Type (1 or 2): ")
        if unit_choice not in [1, 2]:
            print("Error: Invalid unit selection.")
            continue
            
        unit_type = "tablet" if unit_choice == 1 else "strip"
        quantity = get_integer_input(f"Enter quantity of {unit_type}s to restock: ")
        
        if quantity <= 0:
            print("Error: Quantity must be greater than 0.")
            continue
            
        rate = get_float_input(f"Enter purchase rate per {unit_type}: ")
        
        cost = quantity * rate
        total_cost += cost
        
        tabs_added = quantity if unit_type == "tablet" else quantity * med['tablets_per_strip']
        
        med['stock'] += tabs_added
        
        restocked_items.append({
            'name': med['name'],
            'brand': med['brand'],
            'unit_type': unit_type,
            'quantity': quantity,
            'rate': rate,
            'cost': cost
        })
        
        print(f"Added {quantity} {unit_type}(s) of {med['name']} to restock list.")
        
        more = input("Restock more items? (y/n): ").strip().lower()
        if more != 'y':
            break

    if restocked_items:
        save_medicines(FILENAME, medicines)
        generate_restock_invoice(supplier_name, restocked_items, total_cost)
        print("Restock transaction completed.")
    else:
        print("No items restocked.")
