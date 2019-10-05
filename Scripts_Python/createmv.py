#!/usr/bin/env python

import boto3

ec2 = boto3.resource('ec2')

# cria instancia de maquina na aws
instance = ec2.create_instances(
    ImageId='ami-07d0cf3af28718ef8',
    MinCount=1,
    MaxCount=1,
    InstanceType='t2.micro')

print(instance[0].id)
