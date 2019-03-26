import os, sys
import imp

from authorizenet import apicontractsv1
from authorizenet.apicontrollers import *
constants = imp.load_source('modulename', 'constants.py')
from decimal import *

def get_transaction_details(transId):
    merchantAuth = apicontractsv1.merchantAuthenticationType()
    merchantAuth.name = constants.apiLoginId
    merchantAuth.transactionKey = constants.transactionKey

    transactionDetailsRequest = apicontractsv1.getTransactionDetailsRequest()
    transactionDetailsRequest.merchantAuthentication = merchantAuth
    transactionDetailsRequest.transId = "40000276420"

    transactionDetailsController = getTransactionDetailsController(transactionDetailsRequest)

    transactionDetailsController.execute()

    transactionDetailsResponse = transactionDetailsController.getresponse()

    if transactionDetailsResponse is not None:
        if transactionDetailsResponse.messages.resultCode == apicontractsv1.messageTypeEnum.Ok:
            print('Successfully got transaction details!')

            print('Transaction Id : %s' % transactionDetailsResponse.transaction.transId)
            print('Transaction Type : %s' % transactionDetailsResponse.transaction.transactionType)
            print('Transaction Status : %s' % transactionDetailsResponse.transaction.transactionStatus)
            print('Auth Amount : %.2f' % transactionDetailsResponse.transaction.authAmount)
            print('Settle Amount : %.2f' % transactionDetailsResponse.transaction.settleAmount)
            if hasattr(transactionDetailsResponse.transaction, 'tax') == True:
                print('Tax : %s' % transactionDetailsResponse.transaction.tax.amount)
            if hasattr(transactionDetailsResponse.transaction, 'profile'):
                print('Customer Profile Id : %s' % transactionDetailsResponse.transaction.profile.customerProfileId)

            if transactionDetailsResponse.messages is not None:
                print('Message Code : %s' % transactionDetailsResponse.messages.message[0]['code'].text)
                print('Message Text : %s' % transactionDetailsResponse.messages.message[0]['text'].text)
        else:
            if transactionDetailsResponse.messages is not None:
                print('Failed to get transaction details.\nCode:%s \nText:%s' % (transactionDetailsResponse.messages.message[0]['code'].text,transactionDetailsResponse.messages.message[0]['text'].text))

    return transactionDetailsResponse

if(os.path.basename(__file__) == os.path.basename(sys.argv[0])):
    get_transaction_details(constants.transactionId)
