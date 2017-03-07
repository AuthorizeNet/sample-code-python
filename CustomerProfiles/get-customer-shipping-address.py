import os, sys
import imp

from authorizenet import apicontractsv1
from authorizenet.apicontrollers import *
constants = imp.load_source('modulename', 'constants.py')

def get_customer_shipping_address(customerProfileId, customerAddressId):
    # Give merchant details
    merchantAuth = apicontractsv1.merchantAuthenticationType()
    merchantAuth.name = constants.apiLoginId
    merchantAuth.transactionKey = constants.transactionKey

    # create get shipping address request
    getShippingAddress = apicontractsv1.getCustomerShippingAddressRequest()
    getShippingAddress.merchantAuthentication = merchantAuth
    getShippingAddress.customerProfileId = customerProfileId
    getShippingAddress.customerAddressId = customerAddressId

    # Make the API call
    getShippingAddressController = getCustomerShippingAddressController(getShippingAddress)
    getShippingAddressController.execute()
    response = getShippingAddressController.getresponse()

    if response.messages.resultCode == "Ok":
        print ("SUCCESS")
        if hasattr(response, 'address') == True:
            print ("The address is")
            print (response.address.firstName +" " + response.address.lastName)
            print (response.address.address)
            print (response.address.city)
            print (response.address.state)
            print (response.address.zip)
            print (response.address.country)
        if not hasattr(response, 'subscriptionIds'):
            print ("no subscriptionIds attr in response")
        else:
            if hasattr(response, 'subscriptionIds') == True:
                if hasattr(response.subscriptionIds, 'subscriptionId') == True:
                    print ("list of subscriptionid:")
                    for subscriptionid in (response.subscriptionIds.subscriptionId):
                        print (subscriptionid)
    else:
        print ("ERROR")
        print ("Message code : %s " % response.messages.message[0]['code'].text)
        print ("Message text : %s " % response.messages.message[0]['text'].text)

    return response

if(os.path.basename(__file__) == os.path.basename(sys.argv[0])):
    get_customer_shipping_address(constants.customerProfileId, constants.customerProfileShippingId)
