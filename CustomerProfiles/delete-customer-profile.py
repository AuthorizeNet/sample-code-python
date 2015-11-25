from authorizenet import apicontractsv1
from authorizenet.apicontrollers import *

merchantAuth = apicontractsv1.merchantAuthenticationType()
merchantAuth.name = '5KP3u95bQpv'
merchantAuth.transactionKey = '4Ktq966gC55GAX7S'

deleteCustomerProfile = apicontractsv1.deleteCustomerProfileRequest()
deleteCustomerProfile.merchantAuthentication = merchantAuth
deleteCustomerProfile.customerProfileId = "36152115"

deleteCustomerProfileController = deleteCustomerProfileController(deleteCustomerProfile)
deleteCustomerProfileController.execute()

response = deleteCustomerProfileController.getresponse()

if (response.messages.resultCode=="Ok"):
	print "Successfully deleted customer with customer profile id %s" % deleteCustomerProfile.customerProfileId
else:
	print response.messages.message[0].text
	print "Failed to delete customer profile with customer profile id %s" % deleteCustomerProfile.customerProfileId
