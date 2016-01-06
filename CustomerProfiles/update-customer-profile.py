import os, sys

from authorizenet import apicontractsv1
from authorizenet.apicontrollers import *

def update_customer_profile(customerProfileId):
	merchantAuth = apicontractsv1.merchantAuthenticationType()
	merchantAuth.name = '5KP3u95bQpv'
	merchantAuth.transactionKey = '4Ktq966gC55GAX7S'

	updateCustomerProfile = apicontractsv1.updateCustomerProfileRequest()
	updateCustomerProfile.merchantAuthentication = merchantAuth
	updateCustomerProfile.profile = apicontractsv1.customerProfileExType()

	updateCustomerProfile.profile.customerProfileId = customerProfileId
	updateCustomerProfile.profile.merchantCustomerId = "mycustomer"
	updateCustomerProfile.profile.description = "john doe"
	updateCustomerProfile.profile.email = "email@email.com"

	controller = updateCustomerProfileController(updateCustomerProfile)
	controller.execute()

	response = controller.getresponse()

	if (response.messages.resultCode=="Ok"):
		print "Successfully updated customer with customer profile id %s" % updateCustomerProfile.profile.customerProfileId
	else:
		print response.messages.message[0].text
		print "Failed to update customer profile with customer profile id %s" % updateCustomerProfile.profile.customerProfileId

	return response

if(os.path.basename(__file__) == sys.argv[0].split('/')[-1]):
	update_customer_profile()