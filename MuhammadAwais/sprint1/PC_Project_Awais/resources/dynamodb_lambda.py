import json
from DBTable import dynamoDBTable
import constants


def lambda_handler(events, context):
    db = dynamoDBTable();
    Message = events['Records'][0]['Sns']['Message']
    Message = json.loads(Message)
    
    parsed_message =  Message['AlarmName']
    createdDate = Message['StateChangeTime']
    db.dynamo_data(constants.TABLE_NAME, parsed_message, createdDate)