from Google import Create_Service

"""
install Google Python SDK
pip install –upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib
"""

CLIENT_FILE = 'D:\Codes\Python\client-secret.json'
API_NAME = 'youtube'
API_VERSION = 'v3'
SCOPES = ['https://www.googleapis.com/auth/youtube']

service = Create_Service(CLIENT_FILE, API_NAME, API_VERSION, SCOPES)

response = service.subscriptions().list (mine=True, part='id, snippet', maxResults=10) .execute()

items = []
items.extend (response.get('items'))
nextPageToken = response.get('nextPageToken')

while nextPageToken:
    response = service.subscriptions().list(mine=True, part='id,snippet', maxResults=10, pageToken=nextPageToken).execute()
    items.extend(response.get('items'))
    nextPageToken = response.get('nextPageToken')

for indx, item in enumerate(items):
    subscription_id = item['id'] 
    channel_name = item['snippet']['title']
    print('#{0} channel {1} is unsubscribed'.format(indx, channel_name))
    service.subscriptions().delete(id=subscription_id).execute()