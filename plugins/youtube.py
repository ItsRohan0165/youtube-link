from googleapiclient.discovery import build

def getVideo(query, API_KEY):
    youtube = build('youtube', 'v3', developerKey=API_KEY)
    search_response = youtube.search().list(q=query, part='id,snippet', maxResults=5).execute()

    videos = []

    for search_result in search_response.get('items', []):
        if search_result['id']['kind'] == 'youtube#video':
            videos.append(search_result['id']['videoId'])

    if len(videos) == 0:
        return None

    return 'https://www.youtube.com/watch?v=' + videos[0]