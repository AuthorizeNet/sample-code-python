import os, sys
import imp

from authorizenet import apicontractsv1
from authorizenet.apicontrollers import *
constants = imp.load_source('modulename', 'constants.py')

def update_customer_shipping_address(customerProfileId, customerAddressId):
    # Give merchant details
    merchantAuth = apicontractsv1.merchantAuthenticationType()
    merchantAuth.name = constants.apiLoginId
    merchantAuth.transactionKey = constants.transactionKey

    # Give updated address details
    officeAddress = apicontractsv1.customerAddressExType()
    officeAddress.firstName = "Sherlock"
    officeAddress.lastName = "Holmes"
    officeAddress.address = "221B Baker Street"
    officeAddress.city = "London"
    officeAddress.state = "WA"
    officeAddress.zip = "98004"
    officeAddress.country = "UK"
    officeAddress.phoneNumber = "000-000-0000"
    officeAddress.customerAddressId = customerAddressId

    # Create update shipping address request
    updateShippingAddressRequest = apicontractsv1.updateCustomerShippingAddressRequest()
    updateShippingAddressRequest.address = officeAddress
    updateShippingAddressRequest.customerProfileId = customerProfileId
    updateShippingAddressRequest.merchantAuthentication = merchantAuth

    # Make the API call
    updateShippingAddressController = updateCustomerShippingAddressController(updateShippingAddressRequest)
    updateShippingAddressController.execute()
    response = updateShippingAddressController.getresponse()

    if response.messages.resultCode == "Ok":
        print ("SUCCESS")
        print ("Message code : %s " % response.messages.message[0]['code'].text)
        print ("Message text : %s " % response.messages.message[0]['text'].text)
    else:
        print ("ERROR")
        print ("Message code : %s " % response.messages.message[0]['code'].text)
        print ("Message text : %s " % response.messages.message[0]['text'].text)

    return response

if(os.path.basename(__file__) == os.path.basename(sys.argv[0])):
    update_customer_shipping_address(constants.customerProfileId, constants.customerProfileShippingId)
