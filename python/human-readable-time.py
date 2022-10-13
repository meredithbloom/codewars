# Human Readable Time
def make_readable(seconds): 
    def single_digit(time):
        if time < 10:
            return('0'+str(time))
        else:
            return(str(time))
    
    hours = seconds//3600
    minutes = (seconds%3600)//60
    secs = seconds-(hours*3600)-(minutes*60)
    print(single_digit(hours)+':'+single_digit(minutes)+':'+single_digit(secs))
    
    

# make_readable(0)
# make_readable(5)
# make_readable(60)
# make_readable(86399)
# make_readable(359999)


