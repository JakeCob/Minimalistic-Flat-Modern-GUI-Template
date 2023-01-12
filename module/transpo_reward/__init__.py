# Transpo Reward
"""
    This module computes the reward for the Transpo Team
"""

def compute_reward(rto_days):    
    if rto_days <= 5:
        award = 'No Award'
        rp_points = 0
        rp_php = 0
        
    elif rto_days >= 6 and rto_days <= 8:
        award = 'Applaud'
        rp_points = 640
        rp_php = 1888
        
    elif rto_days >= 9  and rto_days <= 11:
        award = 'Applaud + Kudos'
        rp_points = 960
        rp_php = 2832
        
    elif rto_days >= 12  and rto_days <= 14:
        award = 'Cheer'
        rp_points = 1280
        rp_php = 3776
        
    elif rto_days >= 15  and rto_days <= 17:
        award = 'Cheer + Kudos'
        rp_points = 1600
        rp_php = 4720
        
    elif rto_days >= 18  and rto_days <= 20:
        award = 'Celebrate'
        rp_points = 1920
        rp_php = 5664
        
    elif rto_days == 21:
        award = 'Celebrate + Kudos'
        rp_points = 2240
        rp_php = 6608
       
    else:
        award = 'No Award'
        rp_points = 0
        rp_php = 0
        
    return award, rp_points, rp_php
# end of function
