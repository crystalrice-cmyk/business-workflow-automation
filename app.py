# Business Workflow Automation System
# Main application


def create_request():
    """Collect information for a new business request."""

    requester = input("Requester name: ")
    department = input("Department: ")
    request_type = input("Request type: ")
    description = input("Request description: ")
    business_impact = input("Business impact (Low/Medium/High): ")

    print("\n--- Request Created ---")
    print(f"Requester: {requester}")
    print(f"Department: {department}")
    print(f"Request Type: {request_type}")
    print(f"Description: {description}")
    print(f"Business Impact: {business_impact}")


create_request()
