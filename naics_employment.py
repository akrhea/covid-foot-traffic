import numpy as np
import pandas as pd

def naics_employment(week,zipp,naics,feature_output):
    '''
    Inputs: 
        week - int or string
        zip - int
        naics - scalar
        feature_output - the dataframe from external_features.csv, or a Dataframe that contains that data

    Return:
        naics_columns: 1x5 dataframe with the establishment count by 2,3,4,5, and 6-digit naics codes as columns
        '''
    naics_2 = 'num_biz_'+str(naics)[:2]+'----'
    naics_3 = 'num_biz_'+str(naics)[:3]
    naics_4 = 'num_biz_'+str(naics)[:4]
    naics_5 = 'num_biz_'+str(naics)[:5]
    naics_6 = 'num_biz_'+str(naics)[:6]
    naics_columns = feature_output[(feature_output['week']==week)&(feature_output['ZIP']==int(zipp))] \
    [[naics_2,naics_3,naics_4,naics_5,naics_6]]
    naics_columns.rename(columns={naics_2: "naics_2_num_biz",
                                  naics_3: "naics_3_num_biz",
                                  naics_4: "naics_4_num_biz",
                                  naics_5: "naics_5_num_biz",
                                  naics_6: "naics_6_num_biz"},
                                  inplace=True)
    return naics_columns