import os, sys

from authorizenet import apicontractsv1
from authorizenet.apicontrollers import *

def delete_customer_profile(customerProfileId):
	merchantAuth = apicontractsv1.merchantAuthenticationType()
	merchantAuth.name = '5KP3u95bQpv'
	merchantAuth.transactionKey = '4Ktq966gC55GAX7S'

	deleteCustomerProfile = apicontractsv1.deleteCustomerProfileRequest()
	deleteCustomerProfile.merchantAuthentication = merchantAuth
	deleteCustomerProfile.customerProfileId = customerProfileId

	controller = deleteCustomerProfileController(deleteCustomerProfile)
	controller.execute()

	response = controller.getresponse()

	if (response.messages.resultCode=="Ok"):
		print "Successfully deleted customer with customer profile id %s" % deleteCustomerProfile.customerProfileId
	else:
		print response.messages.message[0].text
		print "Failed to delete customer profile with customer profile id %s" % deleteCustomerProfile.customerProfileId

	return response

if(os.path.basename(__file__) == sys.argv[0].split('/')[-1]):
	delete_customer_profile()
