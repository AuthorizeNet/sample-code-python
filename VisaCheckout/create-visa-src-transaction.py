import os, sys
import imp

from authorizenet import apicontractsv1
from authorizenet.apicontrollers import *
constants = imp.load_source('modulename', 'constants.py')
from decimal import *

def create_visa_src_transaction():

    merchantAuth = apicontractsv1.merchantAuthenticationType()
    merchantAuth.name = constants.apiLoginId
    merchantAuth.transactionKey = constants.transactionKey
    # Populate the payment data
    opaqueData = apicontractsv1.opaqueDataType()
    opaqueData.dataDescriptor = "COMMON.VCO.ONLINE.PAYMENT"
    opaqueData.dataValue = "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"
    opaqueData.dataKey = "ZW6TOD05lWOtUYVunXhYmXRBA6d7UTVezRCwUYLrK/xHPK5LDuZe5Rk/sT223vO0NdD7iQXMPqnQrCS1myW+CFceOKiUuoA0zKJ6TZ84q/+msPG66DDdzDxeKKdE5Qjt"
    paymentType = apicontractsv1.paymentType()
    paymentType.opaqueData = opaqueData
    # Create the payment transaction request
    transactionRequest = apicontractsv1.transactionRequestType()
    transactionRequest.transactionType = apicontractsv1.transactionTypeEnum.authCaptureTransaction
    transactionRequest.callId = "1238408836021304101"
    transactionRequest.amount = Decimal('14.00')
    transactionRequest.payment = paymentType
    # Make the API Request
    request = apicontractsv1.createTransactionRequest()
    request.merchantAuthentication = merchantAuth
    request.transactionRequest = transactionRequest
    # Execute the API request
    controller = createTransactionController(request)
    controller.execute()
    # Get the response
    response = controller.getresponse()

    if response is not None:
        if response.messages.resultCode == "Ok":
            if hasattr(response.transactionResponse, 'messages') == True:
                print ('Successfully created transaction with Transaction ID: %s' % response.transactionResponse.transId)  
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
    create_visa_src_transaction()
