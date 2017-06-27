#import multiprocessing
#print multiprocessing.cpu_count()
bind = "0.0.0.0:9007"
workers = 8 #multiprocessing.cpu_count() * 2 + 1
timeout = 300