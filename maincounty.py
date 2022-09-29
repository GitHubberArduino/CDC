# This is a sample Python script.
import json
import pandas as pd

data = {
        'county': [],
        'rate': [],
        'num1': [],
        'num2': [],
        'num3': []
        }

df = pd.DataFrame(data)
year = 2019

def print_df():
    # Use a breakpoint in the code line below to debug your script.
    print(len(df))
    #for d in df.iloc:
    #    print(d)
    df.to_csv('/Users/danielwang/projects/cdc/CrudeCounty2021.csv', index=False)

def parseData(sjson):
    y = json.loads(sjson)
    for r in y["data"]:
        newrecno = len(df.index)
        df.loc[newrecno] = [ r[0], r[1], r[2], r[3], r[4]]

def parseFile():
    # opening file in reading mode
    #lastLine = ""
    with open('/Users/danielwang/projects/cdc/CrudeCounty2021.txt', 'r') as fileobj:
        while (True):
            line = fileobj.readline()
            if not line:
                break;
            if line.startswith("{") :
                parseData(line)
            #lastLine = line


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    parseFile()
    print_df()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/