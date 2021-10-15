import logging
import graypy
import time
my_logger = logging.getLogger('test_logger')
my_logger.setLevel(logging.DEBUG)

handler = graypy.GELFUDPHandler('graylog', 12201)
my_logger.addHandler(handler)
my_adapter = logging.LoggerAdapter(logging.getLogger('test_logger'),
                                   {'username': 'John'})


x = 0
while True:
    print("Hello {} ".format(x), flush=True)
    my_adapter.debug('Hello Graylog.')
    time.sleep(1)
    x += 1
    
print("DONE")
