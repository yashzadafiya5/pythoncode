from multiprocessing import current_process
import multiprocessing
import time
def getdata(list):
    p=0
    for i in list:
        if list[p]!=None:
            print(f"{i} file is downloaded.....",current_process().name)
            list[p] = None
            time.sleep(1)
        p=p+1
if __name__=="__main__":
    
    manager=multiprocessing.Manager()
    
    list=manager.list(["file1.zip","file2.zip","file3.zip","file4.zip","file5.zip","file6.zip","file7.zip","file8.zip"])
    
    p1=multiprocessing.Process(target=getdata,args=(list,),name='yash')
    p2=multiprocessing.Process(target=getdata,args=(list,),name='bhavdeep')
    
    p1.start()
    p2.start()
    p1.join()
    p2.join()