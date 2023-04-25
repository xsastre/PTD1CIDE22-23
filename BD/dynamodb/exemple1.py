import boto3
from boto3.dynamodb.conditions import Key

TABLE_NAME = "basicSongsTable"

# Creating the DynamoDB Client
dynamodb_client = boto3.client('dynamodb', region_name="eu-west-1")

# Creating the DynamoDB Table Resource
dynamodb = boto3.resource('dynamodb', region_name="eu-west-1")
table = dynamodb.Table(TABLE_NAME)

# Use the DynamoDB client get item method to get a single item
response = dynamodb_client.get_item(
    TableName=TABLE_NAME,
    Key={
        'artist': {'S': 'Arturus Ardvarkian'},
        'song': {'S': 'Carrot Eton'}
    }
)
print(response['Item'])

# The client's response looks like this:
# {
#  'artist': {'S': 'Arturus Ardvarkian'},
#  'id': {'S': 'dbea9bd8-fe1f-478a-a98a-5b46d481cf57'},
#  'priceUsdCents': {'S': '161'},
#  'publisher': {'S': 'MUSICMAN INC'},
#  'song': {'S': 'Carrot Eton'}
# }