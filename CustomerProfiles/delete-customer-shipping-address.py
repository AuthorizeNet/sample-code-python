import os, sys

from authorizenet import apicontractsv1
from authorizenet.apicontrollers import *

def delete_customer_shipping_address(customerProfileId, customerProfileShippingId):

	# Give merchant details
	merchantAuth = apicontractsv1.merchantAuthenticationType()
	merchantAuth.name = '5KP3u95bQpv'
	merchantAuth.transactionKey = '4Ktq966gC55GAX7S'

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
	    print "SUCCESS"
	    print "Message code : %s " % response.messages.message[0].code
	    print "Message text : %s " % response.messages.message[0].text
	else:
	    print "ERROR"
	    print "Message code : %s " % response.messages.message[0].code
	    print "Message text : %s " % response.messages.message[0].text

	return response

if(os.path.basename(__file__) == sys.argv[0].split('/')[-1]):
	delete_customer_shipping_address()
