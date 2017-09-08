import os, sys
import imp

from authorizenet import apicontractsv1
from authorizenet.apicontrollers import *
constants = imp.load_source('modulename', 'constants.py')
from decimal import *

def get_transaction_list():
    merchantAuth = apicontractsv1.merchantAuthenticationType()
    merchantAuth.name = constants.apiLoginId
    merchantAuth.transactionKey = constants.transactionKey

    transactionListRequest = apicontractsv1.getTransactionListRequest()
    transactionListRequest.merchantAuthentication = merchantAuth
    transactionListRequest.batchId = "4551107"

    transactionListController = getTransactionListController(transactionListRequest)

    transactionListController.execute()

    transactionListResponse = transactionListController.getresponse()

    if transactionListResponse is not None:
        if transactionListResponse.messages.resultCode == apicontractsv1.messageTypeEnum.Ok:
            print('Successfully got transaction list!')

            for transaction in transactionListResponse.transactions.transaction:
                print('Transaction Id : %s' % transaction.transId)
                print('Transaction Status : %s' % transaction.transactionStatus)
                print('Amount Type : %s' % transaction.accountType)
                print('Settle Amount : %s' % transaction.settleAmount)
                if hasattr(transaction, 'profile'):
                    print('Customer Profile Id : %s' % transaction.profile.customerProfileId)

            if transactionListResponse.messages is not None:
                print('Message Code : %s' % transactionListResponse.messages.message[0]['code'].text)
                print('Message Text : %s' % transactionListResponse.messages.message[0]['text'].text)
        else:
            if transactionListResponse.messages is not None:
                print('Failed to get transaction list.\nCode:%s \nText:%s' % (transactionListResponse.messages.message[0]['code'].text,transactionListResponse.messages.message[0]['text'].text))

    return transactionListResponse

if(os.path.basename(__file__) == os.path.basename(sys.argv[0])):
    get_transaction_list()
