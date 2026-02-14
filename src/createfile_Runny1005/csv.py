import csv
from pathlib import Path
from datetime import datetime
import os
path=os.getcwd()
print(path)
path=path.split('/')
print(path)
def tes():
     print(path)
def create_file(topic,field,path):
    for i in range(len(topic)):
            file=topic[i]
            file=path+file.replace('/','-')+'.csv'
            print(file)
            Path(file).parent.mkdir(exist_ok=True,parents=True)
            with open(file,"w",newline='',encoding='utf-8') as f:
                writer=csv.DictWriter(f,fieldnames=field)
                writer.writeheader()
def write_to_file(msg,field,path):
    file=msg.topic
    file=path+file.replace('/','-')+".csv"
    try:
        value=float(msg.payload.decode())
        timestamp=datetime.now().strftime("%Y/%m/%d %H:%M:%S")
        with open(file,'a',newline='',encoding="utf-8") as f:
            writer=csv.DictWriter(f,fieldnames=field)
            writer.writerow({"Data":timestamp,"Timestamp":value})
    except Exception as e:
         print("Error With error code :",e)