import os, sys
import imp

from authorizenet import apicontractsv1
from authorizenet.apicontrollers import *
constants = imp.load_source('modulename', 'constants.py')
from decimal import *

def approve_or_decline_held_transaction(transactionId):
    merchantAuth = apicontractsv1.merchantAuthenticationType()
    merchantAuth.name = constants.apiLoginId
    merchantAuth.transactionKey = constants.transactionKey

    requesttype = apicontractsv1.heldTransactionRequestType()
    requesttype.action = "approve"
    requesttype.refTransId = transactionId

    transactionrequest = apicontractsv1.updateHeldTransactionRequest()
    transactionrequest.merchantAuthentication = merchantAuth
    transactionrequest.heldTransactionRequest = requesttype

    transactionRequestController = updateHeldTransactionController(transactionrequest)
    transactionRequestController.execute()

    response = transactionRequestController.getresponse()

    if response is not None:
        if response.messages.resultCode == "Ok":
            if hasattr(response.transactionResponse, 'messages') == True:
                print ('Successfully updated transaction with Transaction ID: %s' % response.transactionResponse.transId)  
                print ('Transaction Response Code: %s' % response.transactionResponse.responseCode)  
                print ('Message Code: %s' % response.transactionResponse.messages.message[0].code)  
                print ('Description: %s' % response.transactionResponse.messages.message[0].description)  
            else:
                print ('Failed Transaction.')  
                if hasattr(response.transactionResponse, 'errors') == True:
                    print ('Error Code:  %s' % str(response.transactionResponse.errors.error[0].errorCode))  
                    print ('Error message: %s' % response.transactionResponse.errors.error[0].errorText)  
        else:
            print ('Failed Transaction.')  
            if hasattr(response, 'transactionResponse') == True and hasattr(response.transactionResponse, 'errors') == True:
                print ('Error Code: %s' % str(response.transactionResponse.errors.error[0].errorCode))  
                print ('Error message: %s' % response.transactionResponse.errors.error[0].errorText)  
            else:
                print ('Error Code: %s' % response.messages.message[0]['code'].text)  
                print ('Error message: %s' % response.messages.message[0]['text'].text)  
    else:
        print ('Null Response.')  

    return response

if(os.path.basename(__file__) == os.path.basename(sys.argv[0])):
    update_held_transaction(constants.transactionId)