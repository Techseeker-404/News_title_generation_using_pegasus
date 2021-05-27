#!/usr/bin/python3.8
import pandas as pd
import os 

"""
creating dataframe  out of 1000 json formatted data into a 
single csv file.
"""
def create_dataframe():
    frame = pd.DataFrame()
    count = 0
    for files in os.listdir(os.getcwd()):
        #print(files)
        root, exten = os.path.splitext(files)

        if exten == ".json":
            temp_frame = pd.read_json(files, typ='series')
            frame = frame.append(temp_frame, ignore_index=True)


        count += 1

    frame.to_csv("dataset.csv")
    print(count)

    #check file created successfully
    if os.path.isfile("dataset.csv"):
        print("File created")
    else:
        print("File doesn't exist")

if __name__ == "__main__":

    if os.path.isfile("dataset.csv"):
        print("File Exist")
    else: 
        create_dataframe()

