# little_case--find_average
把data分成10組後取平均數，最後輸出到excel  
  教學:  
    . 有標示###要改的地方###之處為依照個人需求改寫之處  
      eg. 工作表名稱,存放檔案之位置  
      
      
    . 函數解釋  
      read_data : 讀取原始excel檔  
      slice_into_ten_peice : 把每組data切成10等份,且切完後省剩餘的數據丟棄  
      find_average_from_each_peice : 取平均值,並把所有結果儲存  
      output_to_excel : 輸出結果檔案,輸出位置與原始檔存放位置相同        
