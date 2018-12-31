#dependencies
import pandas as pd
import numpy as np
import sys
import datetime


def fetch_data(filename):
    """
    This function checks whether the file exists in the directory and returns the content of
    the file as a dataframe.
    """
    
    try:
        data = pd.read_csv(filename)
        return data
    except:
        print("No such file exists! Run read_historical_data to create file for a commodity.")
        print("Also, make sure commodity is either gold or silver")
        return
        

def check_dates(data,start,end):
    """
    This function checks whether the entered dates are in correct format, also it checks
    if the entered dates are well within the range of the dates in the stored data.
    """
    
    try: #checking if data exists
        start_range = data['date'].tolist()[-1]
        end_range = data['date'].tolist()[0]
        
        try:  #checking date format
            datetime.datetime.strptime(start, '%Y-%m-%d')
            datetime.datetime.strptime(end, '%Y-%m-%d')
            
            if start >= start_range and end <= end_range and start < end: #checking range validity
                return start,end
            else:
                print("Input dates are out of range!")
                return
            
        except:
            print("Input dates should have yyyy-mm-dd format!")
            return
        
    except:
        return

        
def calc_mean_var(commodity,start,end):
    """
    This function takes commodity name(i.e gold or silver)and converts it to the csv file name,
    uses start and end dates to find prices within that range, and finally returns mean and variance.
    """
    
    filename = commodity + ".csv"
    data = fetch_data(filename)
    if check_dates(data,start,end) != None :
        start_range = data.index[data['date']==start].tolist()[0]+1
        end_range = data.index[data['date'] == end].tolist()[0]
        temp = (data['price'].iloc[end_range:start_range]).tolist()
        mean = np.mean(np.array(temp))
        var = np.var(np.array(temp))
        return mean,var
    else:
        return None,None

       
            
def print_result():
    commodity = sys.argv[1]
    start = sys.argv[2]
    end = sys.argv[3]
    mean, var = calc_mean_var(commodity,start,end)
    if mean and var:
        print(commodity, mean, var)
    else:
        print()
    


print_result()
