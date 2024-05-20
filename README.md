# Cloud-Custodian #

Here is our Cloud-Custodian repository, where we focus on managing cloud environments in a secure, compliant, and cost-effective manner using AWS Lambda functions.

## Overview
Cloud-Custodian is an open-source project that provides a collection of policies and tools for cloud management. The repository contains AWS Lambda function code that can be used to automate various tasks and ensure adherence to best practices.

---

# Cloud Custodian Policies

The following are the Cloud Custodian policies written in YAML format:

## EC2 Policies

1. **ec2-30days.yml**:
   - This policy runs every hour, checking for EC2 instances that have been running for more than 30 days, and sends notifications about these instances.

2. **ec2-env-tag.yml**:
   - This policy checks for EC2 instances that are missing the `environment` tag and sends notifications about these instances.

3. **ec2-exp-tag.yml**:
   - This policy checks for EC2 instances that do not have an `ExpirationDate` tag and sends notifications about these instances.

4. **ec2-large-instances.yml**:
   - This policy checks for EC2 instances that are not of type `t2.micro`, `t3.micro`, `t3a.micro`, or `t4g.micro` (i.e., potentially large instances) and sends notifications about these instances.

5. **stop-dev-ec2-offhours.yml**:
   - This policy stops EC2 instances tagged as `dev` during off hours (after 18:00 GMT).

6. **terminate_ec2.yml**:
   - This policy terminates running EC2 instances that have the specific tag `Name` set to `(Instance Name)`.

7. **terminate-stopped-ec2.yml**:
   - This policy terminates EC2 instances that have been stopped for more than 48 hours.

## S3 Policies

1. **s3_30days.yml**:
   - This policy checks for S3 buckets that have been created more than 30 days ago and sends notifications about these buckets.

2. **s3_encrypt.yml**:
   - This policy checks for S3 buckets that do not have an encryption statement, implying they are not encrypted.

3. **s3-empty-buckets.yml**:
   - This policy checks for S3 buckets that have been empty (no objects in them) for more than 48hrs and sends notifications about these buckets.

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
