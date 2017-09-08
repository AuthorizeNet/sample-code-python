import os, sys
import imp
import random

from authorizenet import apicontractsv1
from authorizenet.apicontrollers import *
constants = imp.load_source('modulename', 'constants.py')
from decimal import *

def get_merchant_details():
    merchantAuth = apicontractsv1.merchantAuthenticationType()
    merchantAuth.name = constants.apiLoginId
    merchantAuth.transactionKey = constants.transactionKey

    getMerchantDetailsRequest = apicontractsv1.getMerchantDetailsRequest()
    getMerchantDetailsRequest.merchantAuthentication = merchantAuth

    controller = getMerchantDetailsController(getMerchantDetailsRequest)
    controller.execute()

    response = controller.getresponse()

    if response is not None:
        if response.messages.resultCode == "Ok":
            print("Merchant Name: ", response.merchantName)
            print("Gateway ID: ", response.gatewayId)
            print("Processors: "),
            for processor in response.processors.processor:
                print(processor.name, "; "),
        else:
            print ("Failed Transaction.")
    else:
        print ("Null Response.")

    return response

if(os.path.basename(__file__) == os.path.basename(sys.argv[0])):
    get_merchant_details()