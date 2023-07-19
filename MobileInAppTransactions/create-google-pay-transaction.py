import os, sys
import imp

from authorizenet import apicontractsv1
from authorizenet.apicontrollers import *
constants = imp.load_source('modulename', 'constants.py')
from decimal import *

def create_google_pay_transaction():

    merchantAuth = apicontractsv1.merchantAuthenticationType()
    merchantAuth.name = constants.apiLoginId
    merchantAuth.transactionKey = constants.transactionKey

    opaqueData = apicontractsv1.opaqueDataType()
    opaqueData.dataDescriptor = "COMMON.GOOGLE.INAPP.PAYMENT"
    opaqueData.dataValue = "1234567890ABCDEF1111AAAA2222BBBB3333CCCC4444DDDD5555EEEE6666FFFF7777888899990000"

    paymentType = apicontractsv1.paymentType()
    paymentType.opaqueData = opaqueData

    lineItem = apicontractsv1.lineItemType()
    lineItem.itemId = "1"
    lineItem.name = "vase"
    lineItem.description = "Cannes logo"
    lineItem.quantity = 18
    lineItem.unitPrice = 45.00

    lineItemsArray = apicontractsv1.ArrayOfLineItem()
    print(lineItemsArray)
    # lineItemArray.lineItem

    # transactionrequest = apicontractsv1.transactionRequestType()
    # transactionrequest.transactionType = apicontractsv1.transactionTypeEnum.authCaptureTransaction
    # transactionrequest.amount = Decimal('151')
    # transactionrequest.payment = paymentType

    # request = apicontractsv1.createTransactionRequest()
    # request.merchantAuthentication = merchantAuth
    # request.refId = "Sample"
    # request.transactionRequest = transactionrequest

    # controller = createTransactionController(request)
    # controller.execute()

    # response = controller.getresponse()

    # if response is not None:
    #     if response.messages.resultCode == "Ok":
    #         if hasattr(response.transactionResponse, 'messages') == True:
    #             print ('Successfully created transaction with Transaction ID: %s' % response.transactionResponse.transId)
    #             print ('Transaction Response Code: %s' % response.transactionResponse.responseCode)
    #             print ('Message Code: %s' % response.transactionResponse.messages.message[0].code)
    #             print ('Description: %s' % response.transactionResponse.messages.message[0].description)
    #             print ('AUTH Code : %s' % response.authCode)
    #         else:
    #             print ('Failed Transaction.')
    #             if hasattr(response.transactionResponse, 'errors') == True:
    #                 print ('Error Code:  %s' % str(response.transactionResponse.errors.error[0].errorCode))
    #                 print ('Error message: %s' % response.transactionResponse.errors.error[0].errorText)
    #     else:
    #         print ('Failed Transaction.')
    #         if hasattr(response, 'transactionResponse') == True and hasattr(response.transactionResponse, 'errors') == True:
    #             print ('Error Code: %s' % str(response.transactionResponse.errors.error[0].errorCode))
    #             print ('Error message: %s' % response.transactionResponse.errors.error[0].errorText)
    #         else:
    #             print ('Error Code: %s' % response.messages.message[0]['code'].text)
    #             print ('Error message: %s' % response.messages.message[0]['text'].text)
    # else:
    #     print ('Null Response.')

    # return response

if(os.path.basename(__file__) == os.path.basename(sys.argv[0])):
    create_google_pay_transaction()
