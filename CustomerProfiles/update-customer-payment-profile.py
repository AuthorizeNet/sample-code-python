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

paymentProfile = apicontractsv1.customerPaymentProfileExType()
paymentProfile.billTo = apicontractsv1.customerAddressType()
paymentProfile.billTo.firstName = "John"
paymentProfile.billTo.lastName = "Doe"
paymentProfile.billTo.address = "123 Main St."
paymentProfile.billTo.city = "Bellevue"
paymentProfile.billTo.state = "WA"
paymentProfile.billTo.zip = "98004"
paymentProfile.billTo.country = "USA"
paymentProfile.billTo.phoneNumber = "000-000-000"
paymentProfile.payment = payment
paymentProfile.customerPaymentProfileId = "34823065"

updateCustomerPaymentProfile = apicontractsv1.updateCustomerPaymentProfileRequest()
updateCustomerPaymentProfile.merchantAuthentication = merchantAuth
updateCustomerPaymentProfile.paymentProfile = paymentProfile
updateCustomerPaymentProfile.customerProfileId = "36731856"
updateCustomerPaymentProfile.validationMode = apicontractsv1.validationModeEnum.liveMode

updateCustomerPaymentProfileController = updateCustomerPaymentProfileController(updateCustomerPaymentProfile)
updateCustomerPaymentProfileController.execute()

response = updateCustomerPaymentProfileController.getresponse()

if (response.messages.resultCode=="Ok"):
	print "Successfully updated customer payment profile with id %s" % updateCustomerPaymentProfile.paymentProfile.customerPaymentProfileId
else:
	print response.messages.message[0].text
	print "Failed to update customer with customer payment profile id %s" % updateCustomerPaymentProfile.paymentProfile.customerPaymentProfileId
