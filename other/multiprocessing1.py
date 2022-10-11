import multiprocessing
import time
import ctypes
def DownloadFile(FileList,size):
    index=0
    while(index<size):
        if FileList != None:
            print(f"{FileList[index]} has been downloaded......")
            time.sleep(1)
            FileList[index] = None
        index=index+1
    print("(inside function) now file list has ")
    print(FileList[:])  #print list 
if __name__ == '__main__':
    #create list
    list = ['file1.zip','file2.zip','file3.zip','file4.zip','file5.zip','file6.zip','file7.zip','file8.zip']
    
    #create array in shared memory in which we can store String for detail 
    #https://docs.python.org/3/library/multiprocessing.html#multiprocessing.Array
    FileList = multiprocessing.Array(ctypes.c_wchar_p,len(list))
    
    #copy list into array 
    for index,FileName in enumerate(list):
        FileList[index] = FileName
        
    print(FileList[:])  #print list 
    p1 = multiprocessing.Process(target=DownloadFile,args=(FileList,len(list),))
    p2 = multiprocessing.Process(target=DownloadFile,args=(FileList,len(list),))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    print("(main module) now file list has ")
    print(FileList[:])  #print list 