from googleapiclient.discovery import build
import os

try:
    api_key=os.environ.get('youtube_api_key')
    id=input("Enter Channel Id: ")
    #create an api specific service object
    youtube=build('youtube','v3',developerKey=api_key)
    request=youtube.channels().list(part='statistics',id=id)
    response=request.execute()
    info=response['items'][0]['statistics']
    subscriberCount=info['subscriberCount']
    videoCount=info['videoCount']
    viewCount=info['viewCount']
    print(f"Total video: {videoCount}")
    print(f"Total subscriber: {subscriberCount}")
    print(f"Total views: {viewCount}")
except Exception as e:
    print("Your Request can not be successed")