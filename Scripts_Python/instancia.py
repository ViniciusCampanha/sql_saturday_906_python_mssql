#!/usr/bin/env python

import boto3
import botocore
import sys
import random
import time

# Replace following parameters with your IP and credentials

rds = boto3.client('rds')
try:
    response = rds.create_db_instance(
    DBInstanceIdentifier='pythondbmssql',
    MasterUsername='dbadmin',
    MasterUserPassword='abcdefg123456789',
    DBInstanceClass='db.m5.large',
    Engine='sqlserver-se',
    AllocatedStorage=20,
    BackupRetentionPeriod=3,
    LicenseModel='license-included'
    )
    print(response)
except Exception as error:
    print (error)