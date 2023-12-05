from multiprocessing import cpu_count

# Socket Path

bind = 'unix:/home/gis1000/project2b/rrams2api.sock'



# Worker Options

workers = cpu_count() + 1
worker_class = 'uvicorn.workers.UvicornWorker'



# Logging Options

loglevel = 'debug'
accesslog = '/home/gis1000/project2b/log1x_access.log'
errorlog =  '/home/gis1000/project2b/log1x_error.log'