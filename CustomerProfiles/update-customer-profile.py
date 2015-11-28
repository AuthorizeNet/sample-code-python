from authorizenet import apicontractsv1
from authorizenet.apicontrollers import *

merchantAuth = apicontractsv1.merchantAuthenticationType()
merchantAuth.name = '5KP3u95bQpv'
merchantAuth.transactionKey = '4Ktq966gC55GAX7S'

updateCustomerProfile = apicontractsv1.updateCustomerProfileRequest()
updateCustomerProfile.merchantAuthentication = merchantAuth
updateCustomerProfile.profile = apicontractsv1.customerProfileExType()

updateCustomerProfile.profile.customerProfileId = "36152115"
updateCustomerProfile.profile.merchantCustomerId = "mycustomer"
updateCustomerProfile.profile.description = "john doe"
updateCustomerProfile.profile.email = "email@email.com"

updateCustomerProfileController = updateCustomerProfileController(updateCustomerProfile)
updateCustomerProfileController.execute()

response = updateCustomerProfileController.getresponse()

if (response.messages.resultCode=="Ok"):
	print "Successfully updated customer with customer profile id %s" % updateCustomerProfile.profile.customerProfileId
else:
	print response.messages.message[0].text
	print "Failed to update customer profile with customer profile id %s" % updateCustomerProfile.profile.customerProfileId
