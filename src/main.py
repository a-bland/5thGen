import boto3

def main():
    # Gets the service resource
    dynamodb = boto3.resource('dynamodb')

    # Instantiates table resource for existing table
    table = dynamo.Table('users')

    # Testing printing from table
    print = dynamo(table.creation_date_time)
