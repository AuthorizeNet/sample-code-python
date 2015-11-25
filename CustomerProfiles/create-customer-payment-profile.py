from authorizenet import apicontractsv1
from authorizenet.apicontrollers import *

merchantAuth = apicontractsv1.merchantAuthenticationType()
merchantAuth.name = '5KP3u95bQpv'
merchantAuth.transactionKey = '4Ktq966gC55GAX7S'

creditCard = apicontractsv1.creditCardType()
creditCard.cardNumber = "4111111111111111"
creditCard.expirationDate = "2020-12"

payment = apicontractsv1.paymentType()
payment.creditCard = creditCard

profile = apicontractsv1.customerPaymentProfileType()
profile.payment = payment

createCustomerPaymentProfile = apicontractsv1.createCustomerPaymentProfileRequest()
createCustomerPaymentProfile.merchantAuthentication = merchantAuth
createCustomerPaymentProfile.paymentProfile = profile
createCustomerPaymentProfile.customerProfileId = '36731856'

createCustomerPaymentProfileController = createCustomerPaymentProfileController(createCustomerPaymentProfile)
createCustomerPaymentProfileController.execute()

response = createCustomerPaymentProfileController.getresponse()

if (response.messages.resultCode=="Ok"):
	print "Successfully created a customer payment profile with id: %s" % response.customerPaymentProfileId
else:
	print "Failed to create customer payment profile %s" % response.messages.message[0].text
