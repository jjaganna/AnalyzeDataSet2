import os
import pandas as pd

# input_dir_dvv is the file location for dvv data folder
# input_dir_dv is the file location for dv data folder

# Replace the 'CELL TYPE' with individual folder names Eg : Cell_A, Mixed_Cell_Type_1

# Example: input_dir_dvv = "/home/user/code/AnalyzeDataSet2-master/cell_A/DVV"

input_dir_dvv = ".../AnalyzeDataSet2-master/{CELL TYPE}/DVV"
input_dir_dv = ".../AnalyzeDataSet2-master/{CELL TYPE}//DV"

dvv_files = [f for f in os.listdir(input_dir_dvv)]
dv_files = [f for f in os.listdir(input_dir_dv)]

for dvv_f, dv_f in zip(dvv_files, dv_files):

    dvv_df = pd.read_csv(input_dir_dvv + "/" + dvv_f)
    dv_df = pd.read_csv(input_dir_dv + "/" + dv_f)


    # Here we combine the data of 106999 frequency dvv data with 27999999 dv data
    dvv_df = dvv_df[["real_time_106999","real_data_106999","imag_data_106999"]]
    dv_df = dv_df[["real_data_27999999","imag_data_27999999"]]

    # Scaling the dv data to match the dvv data
    dv_df = dv_df.apply(lambda x: x * 10)

    # Use the combined df data to proceed with analysis. 
    combined_df = pd.concat([dvv_df,dv_df], axis=1, sort=False)
