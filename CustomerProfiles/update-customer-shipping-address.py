import os, sys

from authorizenet import apicontractsv1
from authorizenet.apicontrollers import *

def update_customer_shipping_address(customerProfileId, customerAddressId):
	# Give merchant details
	merchantAuth = apicontractsv1.merchantAuthenticationType()
	merchantAuth.name = '5KP3u95bQpv'
	merchantAuth.transactionKey = '4Ktq966gC55GAX7S'

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
	    print "SUCCESS"
	    print "Message code : %s " % response.messages.message[0].code
	    print "Message text : %s " % response.messages.message[0].text
	else:
	    print "ERROR"
	    print "Message code : %s " % response.messages.message[0].code
	    print "Message text : %s " % response.messages.message[0].text

	return response

if(os.path.basename(__file__) == sys.argv[0].split('/')[-1]):
	update_customer_shipping_address()