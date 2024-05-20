# Cloud-Custodian #

Here is our Cloud-Custodian repository, where we focus on managing cloud environments in a secure, compliant, and cost-effective manner using AWS Lambda functions.

## Overview
Cloud-Custodian is an open-source project that provides a collection of policies and tools for cloud management. The repository contains AWS Lambda function code that can be used to automate various tasks and ensure adherence to best practices.

---
# Cloud Custodian Policies

The following are Cloud Custodian policies written in YAML format:

## EC2 Policies

1. **ec2-30days.yml**
2. **ec2-env-tag.yml**
3. **ec2-exp-tag.yml**
4. **ec2-large-instances.yml**
5. **stop-dev-ec2-offhours.yml**
6. **terminate_ec2.yml**
7. **terminate-stopped-ec2.yml**

## S3 Policies

1. **s3_30days.yml**
2. **s3_encrypt.yml**
3. **s3-empty-buckets.yml**

---
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
