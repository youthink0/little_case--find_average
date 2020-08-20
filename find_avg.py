import pandas as pd
import os
import numpy as np

###要改的地方###
data_address = "C:/Users/a0985/OneDrive/Desktop/"


def read_data() :
    global data_address
    ###要改的地方###
    data_name = data_address + "test" + ".xlsx"
    
    origin_df = pd.DataFrame() #儲存原始檔的dataframe
    
    if os.path.isfile(data_name) : #有此檔案
        ###要改的地方###
        origin_df = pd.read_excel(data_name, sheet_name = '工作表1', header = None) #讀取excel
    else:                          #查無此檔
        print("no data")
        return;
    return origin_df;

def find_average_from_each_peice(each_df, group_size,i) :
    
    get_avg_df = pd.DataFrame(np.random.randn(10, 1), columns=['group' + str(i)])
    for j in range(10): #跑10個loop,算每等份平均
        tmp_df = each_df.loc[group_size*j:group_size*(j+1) - 1]
        get_avg_df['group' + str(i)][j] = tmp_df.mean() 
    
    return get_avg_df;

def slice_into_ten_peice(origin_df) :
    data_group = len(origin_df.columns) #總共有幾組data
    
    get_avg_df = pd.DataFrame()
    for i in range(data_group) : #針對每組data做個別處理
        each_df = origin_df.iloc[:, i]
        each_df = each_df.dropna().reset_index(drop=True) #把有nan的列delete
        group_size = int(len(each_df) / 10)
        #print(each_df,group_size)
        
        #####拿到每等份平均#####
        get_avg_df = find_average_from_each_peice(each_df, group_size,i)
        
        #####結果儲存#####
        if i == 0 :
            result = get_avg_df
        else :
            result['group' + str(i)] = get_avg_df
        #print(result)
    return result;
 
def output_to_excel(result) :
    global data_address
    ###要改的地方###
    output_name = data_address + "胖班代" + ".xlsx"
    result.to_excel(output_name)

if __name__ == "__main__" : 
    
    #####獲取原始資料#####
    origin_df = read_data() 
    #print(origin_df)
    
    #####找到每組的平均值#####
    result = slice_into_ten_peice(origin_df) 
    
    #####輸出結果到excel檔#####
    output_to_excel(result)
    
    print('done')
