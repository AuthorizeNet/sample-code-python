import os, sys
import imp

from authorizenet import apicontractsv1
from authorizenet.apicontrollers import *
constants = imp.load_source('modulename', 'constants.py')

def validate_customer_payment_profile(customerProfileId, customerPaymentProfileId):
    merchantAuth = apicontractsv1.merchantAuthenticationType()
    merchantAuth.name = constants.apiLoginId
    merchantAuth.transactionKey = constants.transactionKey

    validateCustomerPaymentProfile = apicontractsv1.validateCustomerPaymentProfileRequest()
    validateCustomerPaymentProfile.merchantAuthentication = merchantAuth
    validateCustomerPaymentProfile.customerProfileId = customerProfileId
    validateCustomerPaymentProfile.customerPaymentProfileId = customerPaymentProfileId
    validateCustomerPaymentProfile.validationMode = "testMode"

    validateCustomerPaymentProfileCntrlr = validateCustomerPaymentProfileController(validateCustomerPaymentProfile)
    validateCustomerPaymentProfileCntrlr.execute()

    response = validateCustomerPaymentProfileCntrlr.getresponse()

    if (response.messages.resultCode=="Ok"):
        print (response.messages.message[0]['text'].text)
    else:
        print ("ERROR :  Validate Customer Payment Profile: Invalid response")
        print ("response code: %s %s" % {response.messages.message[0]['code'].text, response.messages.message[0]['text'].text})

    return response

if(os.path.basename(__file__) == os.path.basename(sys.argv[0])):
    validate_customer_payment_profile(constants.customerProfileId, constants.customerPaymentProfileId)
