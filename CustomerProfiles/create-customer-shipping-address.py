import os, sys
import imp

# Gives error if an address is already present for the given customer Id
from authorizenet import apicontractsv1
from authorizenet.apicontrollers import *
constants = imp.load_source('modulename', 'constants.py')

def create_customer_shipping_address(customerProfileId):
    # Give merchant details
    merchantAuth = apicontractsv1.merchantAuthenticationType()
    merchantAuth.name = constants.apiLoginId
    merchantAuth.transactionKey = constants.transactionKey

    # Give address details
    officeAddress = apicontractsv1.customerAddressType()
    officeAddress.firstName = "John"
    officeAddress.lastName = "Doe"
    officeAddress.address = "123 Main St."
    officeAddress.city = "Bellevue"
    officeAddress.state = "WA"
    officeAddress.zip = "98004"
    officeAddress.country = "USA"
    officeAddress.phoneNumber = "000-000-0000"

    # Create shipping address request
    shippingAddressRequest = apicontractsv1.createCustomerShippingAddressRequest()
    shippingAddressRequest.address = officeAddress
    shippingAddressRequest.customerProfileId = customerProfileId
    shippingAddressRequest.merchantAuthentication = merchantAuth

    # Make an API call
    controller = createCustomerShippingAddressController(shippingAddressRequest)
    controller.execute()
    response = controller.getresponse()

    if response.messages.resultCode == "Ok":
        print("SUCCESS")
        print("Transaction ID : %s " % response.messages.message[0]['text'].text)
        print("Customer address id : %s" % response.customerAddressId)
    else:
        print("ERROR")
        print("Message code : %s " % response.messages.message[0]['code'].text)
        print("Message text : %s " % response.messages.message[0]['text'].text)

    return response

if(os.path.basename(__file__) == os.path.basename(sys.argv[0])):
    create_customer_shipping_address(constants.customerProfileId)
