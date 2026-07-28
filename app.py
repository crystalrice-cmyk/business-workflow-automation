from datetime import datetime
import csv
import os


DATA_FILE = "requests.csv"


def determine_priority(business_impact):
    if business_impact.lower() == "high":
        return "HIGH"
    elif business_impact.lower() == "medium":
        return "MEDIUM"
    else:
        return "LOW"


def assign_team(request_type):
    request_type = request_type.lower()

    if "system" in request_type or "software" in request_type:
        return "IT Systems"
    elif "payroll" in request_type or "hr" in request_type:
        return "Human Resources"
    elif "equipment" in request_type or "maintenance" in request_type:
        return "Facilities"
    else:
        return "Business Operations"


def get_next_request_id():
    if not os.path.exists(DATA_FILE):
        return "REQ-1001"

    with open(DATA_FILE, "r", newline="") as file:
        reader = csv.reader(file)
        rows = list(reader)

    request_count = max(len(rows) - 1, 0)
    next_number = 1001 + request_count

    return f"REQ-{next_number}"


def save_request(request):
    file_exists = os.path.exists(DATA_FILE)

    with open(DATA_FILE, "a", newline="") as file:
        writer = csv.DictWriter(
            file,
            fieldnames=[
                "Request_ID",
                "Requester",
                "Department",
                "Request_Type",
                "Description",
                "Business_Impact",
                "Priority",
                "Assigned_Team",
                "Status",
                "Date_Created"
            ]
        )

        if not file_exists:
            writer.writeheader()

        writer.writerow(request)


def create_request():
    requester = input("Requester name: ")
    department = input("Department: ")
    request_type = input("Request type: ")
    description = input("Request description: ")
    business_impact = input("Business impact (Low/Medium/High): ")

    request = {
        "Request_ID": get_next_request_id(),
        "Requester": requester,
        "Department": department,
        "Request_Type": request_type,
        "Description": description,
        "Business_Impact": business_impact,
        "Priority": determine_priority(business_impact),
        "Assigned_Team": assign_team(request_type),
        "Status": "NEW",
        "Date_Created": datetime.now().strftime("%m/%d/%Y")
    }

    save_request(request)

    print("\n--- Request Created ---")
    print(f"Request ID: {request['Request_ID']}")
    print(f"Requester: {request['Requester']}")
    print(f"Department: {request['Department']}")
    print(f"Request Type: {request['Request_Type']}")
    print(f"Description: {request['Description']}")
    print(f"Business Impact: {request['Business_Impact']}")
    print(f"Priority: {request['Priority']}")
    print(f"Assigned Team: {request['Assigned_Team']}")
    print(f"Status: {request['Status']}")
    print(f"Date Created: {request['Date_Created']}")


create_request()
