"""http://developer.authorize.net/api/reference/index.html#transaction-reporting-get-unsettled-transaction-list"""
import os
import sys
import imp

from authorizenet import apicontractsv1
from authorizenet.apicontrollers import getUnsettledTransactionListController
constants = imp.load_source('modulename', 'constants.py')

def get_unsettled_transaction_list():
    """get unsettled transaction list"""
    merchantAuth = apicontractsv1.merchantAuthenticationType()
    merchantAuth.name = constants.apiLoginId
    merchantAuth.transactionKey = constants.transactionKey

    # set sorting parameters
    sorting = apicontractsv1.TransactionListSorting()
    sorting.orderBy = apicontractsv1.TransactionListOrderFieldEnum.id
    sorting.orderDescending = True

    # set paging and offset parameters
    paging = apicontractsv1.Paging()
    # Paging limit can be up to 1000 for this request
    paging.limit = 20
    paging.offset = 1

    request = apicontractsv1.getUnsettledTransactionListRequest()
    request.merchantAuthentication = merchantAuth
    request.refId = "Sample"
    request.sorting = sorting
    request.paging = paging

    unsettledTransactionListController = getUnsettledTransactionListController(request)
    unsettledTransactionListController.execute()

    # Work on the response
    response = unsettledTransactionListController.getresponse()

    if response is not None:
        if response.messages.resultCode == apicontractsv1.messageTypeEnum.Ok:
            if hasattr(response, 'transactions'):
                print('Successfully retrieved transaction list.')
                if response.messages is not None:
                    print('Message Code: %s' % response.messages.message[0]['code'].text)
                    print('Message Text: %s' % response.messages.message[0]['text'].text)
                    print('Total Number In Results: %s' % response.totalNumInResultSet)
                    print()
                for transaction in response.transactions.transaction:
                    print('Transaction Id: %s' % transaction.transId)
                    print('Transaction Status: %s' % transaction.transactionStatus)
                    if hasattr(transaction, 'accountType'):
                        print('Account Type: %s' % transaction.accountType)
                    print('Settle Amount: %.2f' % transaction.settleAmount)
                    if hasattr(transaction, 'profile'):
                        print('Customer Profile ID: %s' % transaction.profile.customerProfileId)
                    print()
            else:
                if response.messages is not None:
                    print('Failed to get transaction list.')
                    print('Code: %s' % (response.messages.message[0]['code'].text))
                    print('Text: %s' % (response.messages.message[0]['text'].text))
        else:
            if response.messages is not None:
                print('Failed to get transaction list.')
                print('Code: %s' % (response.messages.message[0]['code'].text))
                print('Text: %s' % (response.messages.message[0]['text'].text))
    else:
        print('Error. No response received.')

    return response

if(os.path.basename(__file__) == os.path.basename(sys.argv[0])):
    get_unsettled_transaction_list()
