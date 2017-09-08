import os, sys
import imp

from authorizenet import apicontractsv1
from authorizenet.apicontrollers import *
constants = imp.load_source('modulename', 'constants.py')

def delete_customer_shipping_address(customerProfileId, customerProfileShippingId):

    # Give merchant details
    merchantAuth = apicontractsv1.merchantAuthenticationType()
    merchantAuth.name = constants.apiLoginId
    merchantAuth.transactionKey = constants.transactionKey

    # create delete request
    deleteShippingAddress = apicontractsv1.deleteCustomerShippingAddressRequest()
    deleteShippingAddress.merchantAuthentication = merchantAuth
    deleteShippingAddress.customerProfileId = customerProfileId
    deleteShippingAddress.customerAddressId = customerProfileShippingId

    # Make the API call
    deleteShippingAddressController = deleteCustomerShippingAddressController(deleteShippingAddress)
    deleteShippingAddressController.execute()
    response = deleteShippingAddressController.getresponse()

    if response.messages.resultCode == "Ok":
        print("SUCCESS")
        print("Message code : %s " % response.messages.message[0]['code'].text)
        print("Message text : %s " % response.messages.message[0]['text'].text)
    else:
        print("ERROR")
        print("Message code : %s " % response.messages.message[0]['code'].text)
        print("Message text : %s " % response.messages.message[0]['text'].text)

    return response

if(os.path.basename(__file__) == os.path.basename(sys.argv[0])):
    delete_customer_shipping_address(constants.customerProfileId, constants.customerProfileShippingId)
