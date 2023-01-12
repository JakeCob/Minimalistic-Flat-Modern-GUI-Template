# Count of date

def count_date(dict_data):
    """_This function counts the date of each individual eid_
    Args:
        dict_data (_dictionary object_): _dictionary of the input data_
    """
    
    eid_list = dict_data['EID']
    date_list = dict_data['Date']
    af_list = dict_data['Actuals/Forecast']
    ex_list = dict_data['Contract (FT,ID,ITPMO)']
    st_list = dict_data['Stream']
    com_list = dict_data['PMO comments']
    
    fnl_el = [] # Final eid list
    fnl_dl = [] # Final date list
    fnl_count = [] # Final count of dates list
    fnl_af = [] # Final array of Actual and Forecast
    fnl_ex = [] # Final array of Exhibit
    fnl_st = [] # Final array of Stream
    fnl_com = [] # Final array of Comments
    
    curr_in = 0 # Current index
    
    
    """
        Getting the unique eids and their dates
    """
    for eid in eid_list:
        if eid not in fnl_el:
            fnl_el.append(eid)
            fnl_dl.append([date_list[curr_in]])
            fnl_af.append(af_list[curr_in])
            fnl_ex.append(ex_list[curr_in])
            fnl_st.append(st_list[curr_in])
            fnl_com.append(com_list[curr_in])
            
        else:
            temp_index = fnl_el.index(eid)
            if date_list[curr_in] not in fnl_dl[temp_index]:
                fnl_dl[temp_index].append(date_list[curr_in])
                
        curr_in += 1
    
    
    """
        Getting the count of dates for each eid
    """    
    for dl_list in fnl_dl:
        fnl_count.append(len(dl_list))
        
    
    return fnl_el, fnl_dl, fnl_count, fnl_af, fnl_ex, fnl_st, fnl_com
# end of function
