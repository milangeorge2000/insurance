import random
import csv

def generate_dataset():
    companies = []
    name = ["State Farm", "Allstate", "Geico", "Progressive", "USAA"]
    financial_stability = ["A", "B", "C", "D", "E"]
    customer_service = ["Excellent", "Good", "Average", "Poor"]
    availability = ["Nationwide", "Selected states", "Regional"]
   

    for i in range(5000):
        company = {}
        company["Company Name"] = random.choice(name)
        company["Financial stability"] = random.choice(financial_stability)
        # company["Coverage options"] = random.choice(coverage_options)
        company["Claims processing time"] = random.randint(5, 15)
        company["Customer service reputation"] = random.choice(customer_service)
        company["Premium cost"] =str(random.randint(50, 150))
        company["Deductibles"] = str(random.randint(200, 800))
        company["Network of providers"] = random.choice(availability)
        companies.append(company)
    
    return companies

def save_to_csv(companies):
    with open('insurance_companies.csv', 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=["Company Name", "Financial stability", "Claims processing time", "Customer service reputation", "Premium cost", "Deductibles",  "Network of providers"])
        writer.writeheader()
        for company in companies:
            writer.writerow(company)

companies = generate_dataset()
save_to_csv(companies)
