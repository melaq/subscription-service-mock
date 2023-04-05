from flask import Flask
from flask import request
from flask_soap import Soap, make_response

app = Flask(__name__)

@app.route('/getSubscriptionList', methods=['POST'])
@Soap('getSubScriptionListReq', 'getSubScriptionListRsp', 'http://www.sdp.com/schema/subscription/v1_0/local')
def get_subscription_list():
    # Extract data from the request
    user_id = request.soap['Body']['getSubScriptionListReq']['userID']['ID']
    action_type = request.soap['Body']['getSubScriptionListReq']['actionType']
    # Add your own logic to retrieve or generate the subscription list
    subscription_list = [
        {
            'productID': '1001',
            'status': '0',
            'effectiveDate': '20080101010101',
            'expireDate': '20090101010101',
            'lastActiveDate': '20080101010101'
        },
        {
            'productID': '1002',
            'status': '0',
            'effectiveDate': '20080101010101',
            'expireDate': '20090101010101',
            'lastActiveDate': '20080101010101'
        }
    ]
    # Create the response
    response = {
        'result': '0',
        'subscriptionList': subscription_list
    }
    return make_response(response)

if __name__ == '__main__':
    app.run(debug=True)
