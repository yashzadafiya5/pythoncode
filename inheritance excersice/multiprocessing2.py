import multiprocessing
import time
import ctypes
def DownloadFile(FileList,size):
    index=0
    while index<size:
        
        if FileList[index] !=None:
            #print(f"{FileList[index]} has been downloaded......")
            time.sleep(1)
            FileList[index]= None
            
            print("(inside function) now file list has ")
            print(FileList[:])  #print list
            index=index+1

        else:
            index=index+1
                    
                
if __name__ == '__main__':
    #create list
    list = ['file1.zip','file2.zip','file3.zip','file4.zip','file5.zip','file6.zip','file7.zip','file8.zip']
    size=len(list) 
    #create array in shared memory in which we can store String for detail 
    #https://docs.python.org/3/library/multiprocessing.html#multiprocessing.Array
    FileList = multiprocessing.Array(ctypes.c_wchar_p,size)
    #copy list into array 
    for index,FileName in enumerate(list): 
        FileList[index] = FileName
      
    print(FileList[:])  #print list 
    p1 = multiprocessing.Process(target=DownloadFile,args=(FileList,size))
    p2 = multiprocessing.Process(target=DownloadFile,args=(FileList,size))
    p1.start()
    p1.join()
    p2.start()
    p2.join()
    print("(main module) now file list has ") 
    print(FileList[:])  #print list 