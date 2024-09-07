# app.py

from flask import Flask, request, jsonify
from models import ProductEnquiryForms_4, CustomerDetails_4, session

"""
Main Flask application with API routes for managing records in the database.
"""

app = Flask(__name__)


# Route to insert records into both tables
@app.route('/post_records', methods=['POST'])
def post_records():
    """
    Inserts records into the 'productenquiryforms_4' and 'customerdetails_4' tables.

    Request:
    POST /post_records
    JSON Body:
    {
        "customername": "John Doe",
        "gender": "Male",
        "age": 30,
        "occupation": "Engineer",
        "mobileno": 9876543210,
        "email": "johndoe@example.com",
        "vechiclemodel": "Model X",
        "state": "California",
        "district": "District A",
        "city": "San Francisco",
        "existingvehicle": "None",
        "dealerstate": "California",
        "dealertown": "Town A",
        "dealer": "Dealer ABC",
        "briefaboutenquiry": "Interested in purchasing a new car",
        "expecteddateofpurchase": "2024-12-01",
        "intendedusage": "Personal",
        "senttodealer": false,
        "dealercode": "ABC123",
        "leadid": "LEAD12345",
        "comments": "Looking for more details",
        "createddate": "2024-09-07",
        "ispurchased": false,

        "customer_leadid": "LEAD12345",
        "customer_city": "San Francisco",
        "customer_dealer": "Dealer ABC",
        "customer_dealercode": "ABC123",
        "customer_senttodealer": false
    }
    """
    data = request.get_json()
    try:
        # Insert into ProductEnquiryForms_4
        product_record = ProductEnquiryForms_4(
            CustomerName=data['customername'],
            Gender=data['gender'],
            Age=data['age'],
            Occupation=data['occupation'],
            MobileNo=data['mobileno'],
            Email=data['email'],
            VehicleModel=data['vechiclemodel'],
            State=data['state'],
            District=data['district'],
            City=data['city'],
            ExistingVehicle=data['existingvehicle'],
            DealerState=data['dealerstate'],
            DealerTown=data['dealertown'],
            Dealer=data['dealer'],
            BriefAboutEnquiry=data['briefaboutenquiry'],
            ExpectedDateOfPurchase=data['expecteddateofpurchase'],
            IntendedUsage=data['intendedusage'],
            SentToDealer=data['senttodealer'],
            DealerCode=data['dealercode'],
            LeadId=data['leadid'],
            Comments=data['comments'],
            CreatedDate=data['createddate'],
            IsPurchased=data['ispurchased']
        )
        session.add(product_record)

        # Insert into CustomerDetails_4
        customer_record = CustomerDetails_4(
            LeadId=data['customer_leadid'],
            CustomerName=data['customername'],
            MobileNo=data['mobileno'],
            City=data['customer_city'],
            Dealer=data['customer_dealer'],
            DealerCode=data['customer_dealercode'],
            SentToDealer=data['customer_senttodealer']
        )
        session.add(customer_record)

        session.commit()
        return jsonify({"message": "Records added successfully!"}), 201
    except Exception as e:
        session.rollback()
        return jsonify({"error": str(e)}), 500


# Route to fetch all records
@app.route('/get_records', methods=['GET'])
def get_records():
    """
    Retrieves all records from 'productenquiryforms_4' and 'customerdetails_4' tables.
    """
    try:
        product_records = session.query(ProductEnquiryForms_4).all()
        customer_records = session.query(CustomerDetails_4).all()

        # Remove '_sa_instance_state' before returning the records
        product_list = [{k: v for k, v in record.__dict__.items() if k != '_sa_instance_state'} for record in
                        product_records]
        customer_list = [{k: v for k, v in record.__dict__.items() if k != '_sa_instance_state'} for record in
                         customer_records]

        return jsonify({
            "ProductEnquiryForms_4": product_list,
            "CustomerDetails_4": customer_list
        }), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


# Run the application
if __name__ == '__main__':
    app.run(debug=True)
