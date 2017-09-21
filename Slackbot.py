import boto3
import logging
import os
import time
 
logger =logging.getLogger()
logger.setLevel(logging.DEBUG)
    # TODO implement
def dispatch(intent_request):
   
    intent_name=intent_request['currentIntent']['name']
    if intent_name == 'startInstanceIntent':
        return start_ec2(intent_request)
    #raise Exception('Intent with name '+ intent_name + 'not supported')
    elif intent_name == 'stopInstanceIntent':
        return stop_ec2(intent_request)
   
def start_ec2(intent_request):
    card_title='Starting'
    output_session_attributes = {}
    slots=  intent_request['currentIntent']['slots']
    instance_value = intent_request['currentIntent']['slots']['Instance']
    instanceValue = instance_value.lower()
    ec2=boto3.client('ec2', region_name='us-east-1')
    response=ec2.describe_instances()
    insId=[]
    for i in response['Reservations']:
        for j in i["Instances"]:
            for k in j['Tags']:
                if k["Value"]==instanceValue:
                    insId.append(j['InstanceId'])
    ec2.start_instances(InstanceIds=insId)
 
def stop_ec2(intent_request):
    card_title='Starting'
    output_session_attributes = {}
    slots=  intent_request['currentIntent']['slots']
    instance_value = intent_request['currentIntent']['slots']['Instance']
    instanceValue = instance_value.lower()
    ec2=boto3.client('ec2', region_name='us-east-1')
    response=ec2.describe_instances()
    insId=[]
    for i in response['Reservations']:
        for j in i["Instances"]:
            for k in j['Tags']:
                if k["Value"]==instanceValue:
                    insId.append(j['InstanceId'])
    ec2.stop_instances(InstanceIds=insId)
   
def lambda_handler(event, context):
   os.environ['TZ'] = 'America/New_York'
   time.tzset()
   logger.debug('event.bot.name={}'.format(event['bot']['name']))
   return dispatch(event) 