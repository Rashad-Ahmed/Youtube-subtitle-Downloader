from youtube_transcript_api import YouTubeTranscriptApi
subtitile=YouTubeTranscriptApi.get_transcript('MDR-azB162Y')

#just the subtitiles
with open('D:/Cloud/cloudIntro.txt','w') as f:
    for i in subtitile:
        f.write('%s\n' % i['text'])

#subtitles with details such as duration and start time of each subtitle
'''
with open('D:/Cloud/vid-1.txt','w') as f:
    f.writelines('%s\n' % i for i in subtitile)

#another way
with open('D:/Cloud/vid-1.txt','w') as f:
    for i in subtitile:
        f.write('%s\n' % i)
'''