# Inserting in Dictionary
import pandas as pd

def insert_inDict(fnl_el, fnl_count, fnl_af, fnl_ex, fnl_st, fnl_com):
    dict_final = pd.DataFrame(columns=['Row Labels', 'Count of Date', 'Actuals/Forecast', 'Exhibit', 'Stream', 'Comments'])
    dict_final['Row Labels'] = fnl_el
    dict_final['Count of Date'] = fnl_count
    dict_final['Actuals/Forecast'] = fnl_af
    dict_final['Exhibit'] = fnl_ex
    dict_final['Stream'] = fnl_st
    dict_final['Comments'] = fnl_com

    return dict_final