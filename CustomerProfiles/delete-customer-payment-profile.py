import os, sys
from importlib.machinery import SourceFileLoader

from authorizenet import apicontractsv1
from authorizenet.apicontrollers import *
constants = SourceFileLoader('modulename', 'constants.py').load_module()

def delete_customer_payment_profile(customerProfileId, customerPaymentProfileId):
    merchantAuth = apicontractsv1.merchantAuthenticationType()
    merchantAuth.name = constants.apiLoginId
    merchantAuth.transactionKey = constants.transactionKey

    deleteCustomerPaymentProfile = apicontractsv1.deleteCustomerPaymentProfileRequest()
    deleteCustomerPaymentProfile.merchantAuthentication = merchantAuth
    deleteCustomerPaymentProfile.customerProfileId = customerProfileId
    deleteCustomerPaymentProfile.customerPaymentProfileId = customerPaymentProfileId

    controller = deleteCustomerPaymentProfileController(deleteCustomerPaymentProfile)
    controller.execute()

    response = controller.getresponse()

    if (response.messages.resultCode=="Ok"):
        print("Successfully deleted customer payment profile with customer profile id %s" % deleteCustomerPaymentProfile.customerProfileId)
    else:
        print(response.messages.message[0]['text'].text)
        print("Failed to delete customer paymnet profile with customer profile id %s" % deleteCustomerPaymentProfile.customerProfileId)

    return response

if(os.path.basename(__file__) == os.path.basename(sys.argv[0])):
    delete_customer_payment_profile(constants.customerProfileId, constants.customerPaymentProfileId)
