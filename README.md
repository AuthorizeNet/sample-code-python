# Python Sample Code for the Authorize.Net SDK
[![Travis CI Status](https://travis-ci.org/AuthorizeNet/sample-code-python.svg?branch=master)](https://travis-ci.org/AuthorizeNet/sample-code-python)

This repository contains working code samples which demonstrate Python integration with the [Authorize.Net Python SDK](https://github.com/AuthorizeNet/sdk-python).  

The samples are organized into categories and common usage examples, just like our [API Reference Guide](http://developer.authorize.net/api/reference). Our API Reference Guide is an interactive reference for the Authorize.Net API. It explains the request and response parameters for each API method and has embedded code windows to allow you to send actual requests right within the API Reference Guide.


## Using the Sample Code

The samples are all completely independent and self-contained. You can analyze them to get an understanding of how a particular method works, or you can use the snippets as a starting point for your own project.

You can also run each sample directly from the command line.

## Running the Samples From the Command Line
* Clone this repository:
```
    $ git clone https://github.com/AuthorizeNet/sample-code-python.git
```
* Install the [Authorize.Net Python SDK](https://www.github.com/AuthorizeNet/sdk-python):
```
    $ pip install authorizenet
```  
* Run the individual samples by name. For example:
```
    $ python PaymentTransactions/[CodeSampleName]
```
e.g.
```
    $ python PaymentTransactions/charge-credit-card.py
```
