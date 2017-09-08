import os, sys
import imp

from authorizenet import apicontractsv1
from authorizenet.apicontrollers import *
constants = imp.load_source('modulename', 'constants.py')

def get_customer_payment_profile(customerProfileId, customerPaymentProfileId):

    merchantAuth = apicontractsv1.merchantAuthenticationType()
    merchantAuth.name = constants.apiLoginId
    merchantAuth.transactionKey = constants.transactionKey

    getCustomerPaymentProfile = apicontractsv1.getCustomerPaymentProfileRequest()
    getCustomerPaymentProfile.merchantAuthentication = merchantAuth
    getCustomerPaymentProfile.customerProfileId = customerProfileId
    getCustomerPaymentProfile.customerPaymentProfileId = customerPaymentProfileId

    controller = getCustomerPaymentProfileController(getCustomerPaymentProfile)
    controller.execute()

    response = controller.getresponse()

    if (response.messages.resultCode=="Ok"):
        print("Successfully retrieved a payment profile with profile id %s and customer id %s" % (getCustomerPaymentProfile.customerProfileId, getCustomerPaymentProfile.customerProfileId))
        if hasattr(response, 'paymentProfile') == True:
            if hasattr(response.paymentProfile, 'subscriptionIds') == True:
                if hasattr(response.paymentProfile.subscriptionIds, 'subscriptionId') == True:
                    print("list of subscriptionid:")
                    for subscriptionid in response.paymentProfile.subscriptionIds.subscriptionId:
                        print(subscriptionid)
    else:
        print("response code: %s" % response.messages.resultCode)
        print("Failed to get payment profile information with id %s" % getCustomerPaymentProfile.customerPaymentProfileId)

    return response

if(os.path.basename(__file__) == os.path.basename(sys.argv[0])):
    get_customer_payment_profile(constants.customerProfileId, constants.customerPaymentProfileId)
