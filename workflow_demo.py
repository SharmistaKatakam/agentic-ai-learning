def get_customer_data():
    return ["Customer A", "Customer B", "Customer C"]

def generate_report(customers):
    return f"Report generated for {len(customers)} customers"

customers = get_customer_data()

report = generate_report(customers)

print(report)