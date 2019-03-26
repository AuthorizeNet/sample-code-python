import os, sys
import imp

from authorizenet import apicontractsv1
from authorizenet.apicontrollers import *
constants = imp.load_source('modulename', 'constants.py')
from decimal import *

def get_customer_profile_transaction_list(customerProfileId):
    merchantAuth = apicontractsv1.merchantAuthenticationType()
    merchantAuth.name = constants.apiLoginId
    merchantAuth.transactionKey = constants.transactionKey

    transactionListForCustomerRequest = apicontractsv1.getTransactionListForCustomerRequest()
    transactionListForCustomerRequest.merchantAuthentication = merchantAuth
    transactionListForCustomerRequest.customerProfileId = customerProfileId

    transactionListForCustomerController = getTransactionListForCustomerController(transactionListForCustomerRequest)

    transactionListForCustomerController.execute()

    transactionListForCustomerResponse = transactionListForCustomerController.getresponse()

    if transactionListForCustomerResponse is not None:
        if transactionListForCustomerResponse.messages.resultCode == apicontractsv1.messageTypeEnum.Ok:
            print('Successfully got transaction list!')

            for transaction in transactionListForCustomerResponse.transactions.transaction:
                print('Transaction Id : %s' % transaction.transId)
                print('Transaction Status : %s' % transaction.transactionStatus)
                print('Amount Type : %s' % transaction.accountType)
                print('Settle Amount : %.2f' % transaction.settleAmount)

            if transactionListForCustomerResponse.messages is not None:
                print('Message Code : %s' % transactionListForCustomerResponse.messages.message[0]['code'].text)
                print('Message Text : %s' % transactionListForCustomerResponse.messages.message[0]['text'].text)
        else:
            if transactionListForCustomerResponse.messages is not None:
                print('Failed to get transaction list.\nCode:%s \nText:%s' % (transactionListForCustomerResponse.messages.message[0]['code'].text,transactionListForCustomerResponse.messages.message[0]['text'].text))

    return transactionListForCustomerResponse

if(os.path.basename(__file__) == os.path.basename(sys.argv[0])):
    get_customer_profile_transaction_list('36152127')
