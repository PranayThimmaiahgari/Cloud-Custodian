# Cloud-Custodian #

Here is our Cloud-Custodian repository, where we focus on managing cloud environments in a secure, compliant, and cost-effective manner using AWS Lambda functions.

## Overview

Cloud-Custodian is an open-source project that provides a collection of policies and tools for cloud management. The repository contains AWS Lambda function code that can be used to automate various tasks and ensure adherence to best practices.

## Getting Started

To get started with Cloud-Custodian, follow these steps:

1. **Clone the Repository**
    git clone https://github.com/PranayThimmaiahgari/Cloud-Custodian.git cd Cloud-Custodian 

3. **Quick install CloudCustodian**
Custodian is published on pypi as a series of packages with the c7n prefix, its also available as a docker image.

For *Linux and Mac OS*:
 To install Cloud Custodian, run:
```shell
python3 -m venv custodian
source custodian/bin/activate
pip install c7n       # This includes AWS support
```
For *Windows (CMD/PowerShell)*:
 To install Cloud Custodian, run:
```shell
python3 -m venv custodian
.\custodian\Scripts\Activate.ps1     # For Powershell users
.\custodian\Scripts\activate.bat     # Or use this for CMD users
 pip install c7n                      # This includes AWS support
```
