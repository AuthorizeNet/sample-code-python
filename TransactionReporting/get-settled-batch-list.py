"""http://developer.authorize.net/api/reference/index.html#transaction-reporting-get-settled-batch-list"""
import os
import sys
import imp

from datetime import datetime, timedelta
from authorizenet import apicontractsv1
from authorizenet.apicontrollers import getSettledBatchListController
constants = imp.load_source('modulename', 'constants.py')

def get_settled_batch_list():
    """get settled batch list"""
    merchantAuth = apicontractsv1.merchantAuthenticationType()
    merchantAuth.name = constants.apiLoginId
    merchantAuth.transactionKey = constants.transactionKey

    settledBatchListRequest = apicontractsv1.getSettledBatchListRequest()
    settledBatchListRequest.merchantAuthentication = merchantAuth
    settledBatchListRequest.refId = "Sample"
    settledBatchListRequest.includeStatistics = True
    settledBatchListRequest.firstSettlementDate = datetime.now() - timedelta(days=7)
    settledBatchListRequest.lastSettlementDate = datetime.now()

    settledBatchListController = getSettledBatchListController(settledBatchListRequest)
    settledBatchListController.execute()

    response = settledBatchListController.getresponse()

    # Work on the response
    if response is not None:
        if response.messages.resultCode == apicontractsv1.messageTypeEnum.Ok:
            if hasattr(response, 'batchList'):
                print('Successfully retrieved batch list.')
                if response.messages is not None:
                    print('Message Code: %s' % response.messages.message[0]['code'].text)
                    print('Message Text: %s' % response.messages.message[0]['text'].text)
                    print()
                for batchEntry in response.batchList.batch:
                    print('Batch Id: %s' % batchEntry.batchId)
                    print('Settlement Time UTC: %s' % batchEntry.settlementTimeUTC)
                    print('Payment Method: %s' % batchEntry.paymentMethod)
                    if hasattr(batchEntry, 'marketType'):
                        print('Market Type: %s' % batchEntry.marketType)
                    if hasattr(batchEntry, 'product'):
                        print('Product: %s' % batchEntry.product)
                    if hasattr(batchEntry, 'statistics'):
                        if hasattr(batchEntry.statistics, 'statistic'):
                            for statistic in batchEntry.statistics.statistic:
                                if hasattr(statistic, 'accountType'):
                                    print('Account Type: %s' % statistic.accountType)
                                if hasattr(statistic, 'chargeAmount'):
                                    print('  Charge Amount: %.2f' % statistic.chargeAmount)
                                if hasattr(statistic, 'chargeCount'):
                                    print('  Charge Count: %s' % statistic.chargeCount)
                                if hasattr(statistic, 'refundAmount'):
                                    print('  Refund Amount: %.2f' % statistic.refundAmount)
                                if hasattr(statistic, 'refundCount'):
                                    print('  Refund Count: %s' % statistic.refundCount)
                                if hasattr(statistic, 'voidCount'):
                                    print('  Void Count: %s' % statistic.voidCount)
                                if hasattr(statistic, 'declineCount'):
                                    print('  Decline Count: %s' % statistic.declineCount)
                                if hasattr(statistic, 'errorCount'):
                                    print('  Error Count: %s' % statistic.errorCount)
                                if hasattr(statistic, 'returnedItemAmount'):
                                    print('  Returned Item Amount: %.2f' % statistic.returnedItemAmount)
                                if hasattr(statistic, 'returnedItemCount'):
                                    print('  Returned Item Count: %s' % statistic.returnedItemCount)
                                if hasattr(statistic, 'chargebackAmount'):
                                    print('  Chargeback Amount: %.2f' % statistic.chargebackAmount)
                                if hasattr(statistic, 'chargebackCount'):
                                    print('  Chargeback Count: %s' % statistic.chargebackCount)
                                if hasattr(statistic, 'correctionNoticeCount'):
                                    print('  Correction Notice Count: %s' % statistic.correctionNoticeCount)
                                if hasattr(statistic, 'chargeChargeBackAmount'):
                                    print('  Charge Chargeback Amount: %.2f' % statistic.chargeChargeBackAmount)
                                if hasattr(statistic, 'chargeChargeBackCount'):
                                    print('  Charge Chargeback Count: %s' % statistic.chargeChargeBackCount)
                                if hasattr(statistic, 'refundChargeBackAmount'):
                                    print('  Refund Chargeback Amount: %.2f' % statistic.refundChargeBackAmount)
                                if hasattr(statistic, 'refundChargeBackCount'):
                                    print('  Refund Chargeback Count: %s' % statistic.refundChargeBackCount)
                                if hasattr(statistic, 'chargeReturnedItemsAmount'):
                                    print('  Charge Returned Items Amount: %.2f' % statistic.chargeReturnedItemsAmount)
                                if hasattr(statistic, 'chargeReturnedItemsCount'):
                                    print('  Charge Returned Items Count: %s' % statistic.chargeReturnedItemsCount)
                                if hasattr(statistic, 'refundReturnedItemsAmount'):
                                    print('  Refund Returned Items Amount: %.2f' % statistic.refundReturnedItemsAmount)
                                if hasattr(statistic, 'refundReturnedItemsCount'):
                                    print('  Refund Returned Items Count: %s' % statistic.refundReturnedItemsCount)
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
    get_settled_batch_list()
