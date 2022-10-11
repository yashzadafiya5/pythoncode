from pytube import YouTube

def Download(video_url,path=None):
    
    url=YouTube(video_url)
    if path==None:
        path='C:\\new_python\\yash'
    url.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').asc().first().download(path)
    print('vido is successfully download')
    
url=input('enter a valid url :=')
path=input(' enter a valid path :=')
Download(url,path)



