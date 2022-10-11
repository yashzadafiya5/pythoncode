import multiprocessing
from multiprocessing import current_process
import urllib.request
import time
import random as rd
def DownloadFile(list):
    for url in reversed(list):
        try:
            file_name =  str(rd.randint(100000,999999)) + ".zip"
            urllib.request.urlretrieve(url, file_name)
            # time.sleep(1)
            list.pop()
            print(f"{file_name} downloaded is download by ",current_process().name)
        except urllib.error.HTTPError:
            print("File not found")
        except IndexError:
            return     
if __name__=='__main__':
    #create manager object 
    manager = multiprocessing.Manager()

    #create shared list 
    list = manager.list([
    'https://drive.google.com/uc?export=download&id=1IQNB5lNU7i2M_R0chJCk64XlvTh8QmKZ',
    'https://drive.google.com/uc?export=download&id=1IQwK_8YM6RlV7r5RFejPQXSgTIj9-mOx',
    'https://drive.google.com/uc?export=download&id=1o9DtaYEb1N-C_L7kqCAgfE0D5RaEwbZH',
    'https://file-examples-com.github.io/uploads/2017/02/zip_10MB.zip',
    'https://file-examples-com.github.io/uploads/2017/02/zip_9MB.zip',
])

    #create process class object 
    p2 = multiprocessing.Process(target=DownloadFile,args=(list,),name='Param')
    p1 = multiprocessing.Process(target=DownloadFile,args=(list,),name='Yash')
    start_time = time.time();
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    end_time = time.time();
    difference = end_time - start_time
    print("Time taken",difference)