import pandas as pd
import os

def pandas():
    # GET PATH
    dataPath = os.path.join(os.getcwd(), "SmallFile.csv")

    # create data_frame
    # index_col=None => index row start 0,1,2... 
    # index_col=n => where n [int] is the column to be index row
    df = pd.read_csv(dataPath, index_col=0) 
    print("--DATA FRAME--")
    print(df)
    print("")

    print("--DATA FRAME INFO--")
    print(df.info())
    print("")

    # extracting subset dataframe
    # df.loc[startrow:endrow, startcolumn:endcolumn, step/skip ]
    # [startIndex:stopIndexButNotInclude] 

    # get spesific column
    print("--DATA COLUMN--")
    print(df["Temp"])
    print("")

    # get spesific row
    print("--DATA ROW [.loc]--")
    print(df.loc["Day 1"])
    print("")

    # position based indexing, when row and column dont have any label
    print("--DATA ROW [.iloc]--")
    print(df.iloc[3:4, :])
    print("")
    
    # pandas series vs dataframe
    print("--PANDAS DATAFRAME [.iloc]--")
    print(df.iloc[4]) # == df.loc["Day 5"]
    print(type(df.iloc[4]))
    print("")
    print("--PANDAS SERIES [.iloc]--") # one column/row selected
    print(df.iloc[[4]])
    print(type(df.iloc[[4]]))
    print("")
    print("df.iloc[[4]] == df.iloc[4]")
    print(df.iloc[[4]] == df.iloc[3])
    print("")

    # calculate using df
    print("--CALCULATE [.mean()]--") # one column/row selected
    print(df["Temp"].mean()) # see dataframe documentation for more calculation
    print(type(df["Temp"].mean()))
    print("")

    # add column to df
    print("--ADD COLUMN TO DF--")
    df["New Column"] = False
    print(df)
    print("")
    print("--MANIPULATE NEW COLUMN IN DF--")
    df.loc[ 1:3, "New Column"] = True
    print(df)
    print("")

    # # change df shape
    # print("--CHANGE DF SHAPE--")
    # print("DF SHAPE : {}".format(df.shape))
    # print(df)
    # print("")
    # tempDF = df.shape
    # df.shape[0] = tempDF[1]
    # df.shape[1] = tempDF[0]
    # print(df.shape)
    # print(df)

    return

# main method
def main():
    pandas()

if __name__ == '__main__':
    main()