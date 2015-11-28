from authorizenet import apicontractsv1
from authorizenet.apicontrollers import *

merchantAuth = apicontractsv1.merchantAuthenticationType()
merchantAuth.name = '5KP3u95bQpv'
merchantAuth.transactionKey = '4Ktq966gC55GAX7S'

deleteCustomerPaymentProfile = apicontractsv1.deleteCustomerPaymentProfileRequest()
deleteCustomerPaymentProfile.merchantAuthentication = merchantAuth
deleteCustomerPaymentProfile.customerProfileId = "10000"
deleteCustomerPaymentProfile.customerPaymentProfileId = "20000"

deleteCustomerPaymentProfileController = deleteCustomerPaymentProfileController(deleteCustomerPaymentProfile)
deleteCustomerPaymentProfileController.execute()

response = deleteCustomerPaymentProfileController.getresponse()

if (response.messages.resultCode=="Ok"):
	print "Successfully deleted customer payment profile with customer profile id %s" % deleteCustomerPaymentProfile.customerProfileId
else:
	print response.messages.message[0].text
	print "Failed to delete customer paymnet profile with customer profile id %s" % deleteCustomerPaymentProfile.customerProfileId
