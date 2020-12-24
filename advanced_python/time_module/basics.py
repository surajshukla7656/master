'''
methods                                        Description

time()                                         return epoch time(in seconds)
sleep(seconds)                                 sleeps for specfied seconds
ctime()                                        return current time(by default) otherwise return date after specifed seconds passed since epoch
localtime()                                    return local time(by default) otherwise return date after specifed seconds passed since epoch (i.e.'time.struct_time(tm_year=2020, tm_mon=11, tm_mday=26, tm_hour=22, tm_min=8, tm_sec=53, tm_wday=3, tm_yday=331, tm_isdst=0)')
                                                - tm_year
                                                - tm_mon
                                                - tm_mday
                                                - tm_hour
                                                - tm_min
                                                - tm_sec
                                                - tm_wday
                                                - tm_yday
                                                - tm_isdst

''
'''

# For Unix system, January 1, 1970, 00:00:00 at UTC is epoch (the point where time begins).
