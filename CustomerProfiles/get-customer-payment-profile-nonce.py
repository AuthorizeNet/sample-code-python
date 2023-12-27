import os, sys
import imp

from authorizenet import apicontractsv1
from authorizenet.apicontrollers import *
from authorizenet.constants import constants
from decimal import *

def get_customer_payment_profile_nonce_details():
    merchantAuth = apicontractsv1.merchantAuthenticationType()
    merchantAuth.name = constants.apiLoginId
    merchantAuth.transactionKey = constants.transactionKey
    refId = "eyJraWQiOiI1YWI2NTIxNDBlZGU3ZWZkMDAwMDAwMDA1NGNlOWRhOCIsImFsZyI6IlJTMjU2In0.eyJqdGkiOiIyMGIyYWU1Ni1hZjk4LTQ5OWMtOTczOS04ZDg1MWQ3YjBkMDIiLCJzY29wZXMiOlsicmVhZCIsIndyaXRlIl0sImlhdCI6MTU0MzM5OTYwOTU0NiwiYXNzb2NpYXRlZF9pZCI6IjM3ODciLCJjbGllbnRfaWQiOiJ4ZVFmcFJSSTVYIiwibWVyY2hhbnRfaWQiOiI2NjgzOTQiLCJhZGRpdGlvbmFsSW5mbyI6IntcImFwaUxvZ2luSWRcIjpcIjI1TDdLVmd3NyAgICAgICAgICAgXCIsXCJyb3V0aW5nSWRcIjpcIiQkMjVMN0tWZ3c3JCRcIn0iLCJleHBpcmVzX2luIjoxNTQzNDI4NDA5NTQ4LCJncmFudF90eXBlIjoiYXV0aG9yaXphdGlvbl9jb2RlIiwic29sdXRpb25faWQiOiJBQUExMDI5MjIifQ.JQL3YovrTOuh3UaBGLxP8RNbzGGeJ1Id309lysnMcRJEYDCpv6999A4n6Yznr6uzePjpEwbiyd2osDoGnrP_wQmpLwGPR3eBb3DIOiAhKuAbc1YdpsNa3rd2qbVHPFO95_x2y6r7yRCvgNiRx01GFOXphZ3gPrSuHd93U-h0OLd6nt2GKQQcZ8IQ7f-44fViNgLEH_FTPETKAaooSK8v4XFa7Fh3rYM-jd5snrK4dnp7L2xcLb3JivKwsVXCtLGkNbjXu6DQFtlbzEyVknv9j7GBJgOTvsE_lBqmQaFIdNrYiOf6bH0xAfelgNy_7db77zvSPfvrH9afb5DB_pTl-Q"

    getCustomerPaymentProfileNonceRequest = apicontractsv1.getCustomerPaymentProfileNonceRequest()
    getCustomerPaymentProfileNonceRequest.merchantAuthentication = merchantAuth
    getCustomerPaymentProfileNonceRequest.connectedAccessToken = refId
    getCustomerPaymentProfileNonceRequest.customerProfileId = "1504802749"
    getCustomerPaymentProfileNonceRequest.customerPaymentProfileId="1504102965"

    controller = getCustomerPaymentProfileNonceController(getCustomerPaymentProfileNonceRequest)
    controller.execute()

    response = controller.getresponse()

    if response is not None:
        if response.messages.resultCode == "Ok":
            print("Success")
            print('Data Descriptor: %s'+ response.opaqueData.dataDescriptor)
            print('Data Value: %s' + response.opaqueData.dataValue)
            print('Expiration Time Stamp: %s' + response.opaqueData.expirationTimeStamp)
        else:
            print("Invalid response")
            print('Code: %s' % (response.messages.message[0]['code'].text))
            print('Text: %s' % (response.messages.message[0]['text'].text))
    else:
        print ("Null Response.")


    return response
if(os.path.basename(__file__) == os.path.basename(sys.argv[0])):
    get_customer_payment_profile_nonce_details()
