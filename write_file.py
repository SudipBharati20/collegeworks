import datetime
import os

def save_medicines(filename, medicines):
    try:
        with open(filename, 'w') as f:
            for med in medicines:
                line = f"{med['name']}, {med['brand']}, {med['stock']}, {med['rate_tablet']}, {med['rate_strip']}, {med['tablets_per_strip']}\n"
                f.write(line)
    except Exception as e:
        print(f"Error saving inventory: {e}")

def create_sample_file(filename):
    print(f"Creating sample file: {filename}")
    sample_data = [
        "Paracetamol 500mg, Lomus, 1200, 5, 45, 10",
        "Cetirizine 10mg, Quest, 800, 4, 35, 12",
        "Amoxicillin 500mg, Nepal Remedies, 500, 12, 110, 15",
        "Pantoprazole 40mg, Deurali-Janta, 600, 7, 60, 8",
        "ORS Sachet, Time Pharma, 300, 20, 180, 12"
    ]
    with open(filename, 'w') as f:
        for line in sample_data:
            f.write(line + "\n")

def generate_sales_invoice(customer_name, items, total_cost, total_discount):
    date_str = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    file_date = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    
    invoice_dir = "invoice"
    if not os.path.exists(invoice_dir):
        os.makedirs(invoice_dir)
        
    invoice_filename = os.path.join(invoice_dir, f"sale_invoice_{file_date}.txt")
    
    try:
        with open(invoice_filename, 'w') as f:
            f.write("====================================================\n")
            f.write("             MEDSTORE PVT. LTD.\n")
            f.write("               SALES INVOICE\n")
            f.write("====================================================\n")
            f.write(f"Customer Name: {customer_name}\n")
            f.write(f"Date: {date_str}\n")
            f.write("----------------------------------------------------\n")
            f.write(f"{'Medicine':<20} | {'Unit':<6} | {'Qty':<4} | {'Amount'}\n")
            f.write("----------------------------------------------------\n")
            
            for item in items:
                f.write(f"{item['name']:<20} | {item['unit_type']:<6} | {item['quantity']:<4} | Rs. {item['cost']:.2f}\n")
                if item['discount'] > 0:
                    f.write(f"  - Discount (5%): Rs. {item['discount']:.2f}\n")
                    
            f.write("----------------------------------------------------\n")
            f.write(f"Total Discount: Rs. {total_discount:.2f}\n")
            f.write(f"Total Amount Payable: Rs. {total_cost:.2f}\n")
            f.write("====================================================\n")
            f.write("            Thank you for your business!\n")
            f.write("====================================================\n")
        print(f"\nInvoice generated: {invoice_filename}")
    except Exception as e:
        print(f"Error generating invoice: {e}")

def generate_restock_invoice(supplier_name, items, total_cost):
    date_str = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    file_date = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    
    invoice_dir = "invoice"
    if not os.path.exists(invoice_dir):
        os.makedirs(invoice_dir)
        
    invoice_filename = os.path.join(invoice_dir, f"restock_invoice_{file_date}.txt")
    
    try:
        with open(invoice_filename, 'w') as f:
            f.write("====================================================\n")
            f.write("             MEDSTORE PVT. LTD.\n")
            f.write("              RESTOCK INVOICE\n")
            f.write("====================================================\n")
            f.write(f"Supplier Name: {supplier_name}\n")
            f.write(f"Date: {date_str}\n")
            f.write("----------------------------------------------------\n")
            f.write(f"{'Medicine':<20} | {'Qty':<8} | {'Rate':<8} | {'Amount'}\n")
            f.write("----------------------------------------------------\n")
            
            for item in items:
                qty_str = f"{item['quantity']} {item['unit_type'][:3]}"
                f.write(f"{item['name']:<20} | {qty_str:<8} | Rs.{item['rate']:<5.2f} | Rs.{item['cost']:.2f}\n")
                    
            f.write("----------------------------------------------------\n")
            f.write(f"Total Amount: Rs. {total_cost:.2f}\n")
            f.write("====================================================\n")
        print(f"\nInvoice generated: {invoice_filename}")
    except Exception as e:
        print(f"Error generating invoice: {e}")
