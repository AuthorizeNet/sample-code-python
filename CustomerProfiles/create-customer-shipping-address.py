# Gives error if an address is already present for the given customer Id
from authorizenet import apicontractsv1
from authorizenet.apicontrollers import *

# Give merchant details
merchantAuth = apicontractsv1.merchantAuthenticationType()
merchantAuth.name = '5KP3u95bQpv'
merchantAuth.transactionKey = '4Ktq966gC55GAX7S'

# Give address details
officeAddress = apicontractsv1.customerAddressType();
officeAddress.firstName = "John"
officeAddress.lastName = "Doe"
officeAddress.address = "123 Main St."
officeAddress.city = "Bellevue"
officeAddress.state = "WA"
officeAddress.zip = "98004"
officeAddress.country = "USA"
officeAddress.phoneNumber = "000-000-0000"

# Create shipping address request
shippingAddressRequest = apicontractsv1.createCustomerShippingAddressRequest();
shippingAddressRequest.address = officeAddress
shippingAddressRequest.customerProfileId = "36152165"
shippingAddressRequest.merchantAuthentication = merchantAuth

# Make an API call
createCustomerShippingAddressController= createCustomerShippingAddressController(shippingAddressRequest)
createCustomerShippingAddressController.execute()
response = createCustomerShippingAddressController.getresponse();

if response.messages.resultCode == "Ok":
    print "SUCCESS"
    print "Transaction ID : %s " % response.messages.message[0].text
    print "Customer address id : %s" % response.customerAddressId
else:
    print "ERROR"
    print "Message code : %s " % response.messages.message[0].code
    print "Message text : %s " % response.messages.message[0].text
