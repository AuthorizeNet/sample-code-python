import os, sys
import imp

from authorizenet import apicontractsv1
from authorizenet.apicontrollers import *
constants = imp.load_source('modulename', 'constants.py')

def get_customer_profile_ids():
    merchantAuth = apicontractsv1.merchantAuthenticationType()
    merchantAuth.name = constants.apiLoginId
    merchantAuth.transactionKey = constants.transactionKey

    getCustomerProfileIds = apicontractsv1.getCustomerProfileIdsRequest()
    getCustomerProfileIds.merchantAuthentication = merchantAuth

    controller = getCustomerProfileIdsController(getCustomerProfileIds)
    controller.execute()

    response = controller.getresponse()

    if (response.messages.resultCode=="Ok"):
        print("Successfully retrieved customer ids:")
        for identity in response.ids.numericString:
            print(identity)
    else:
        print("response code: %s" % response.messages.resultCode)

    return response

if(os.path.basename(__file__) == os.path.basename(sys.argv[0])):
    get_customer_profile_ids()
