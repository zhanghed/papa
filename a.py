from time import sleep
from threading import Thread
from threading import Event


# define task function
def task(event):
    # execute a task in a loop
    for i in range(100):
        # block for a moment
        sleep(1)
        # check for stop
        if event.is_set():
            # 在此添加退出前要做的工作，如保存文件等
            break
        # report a message
        print('Worker thread running...')
    print('Worker is ended')


# create the event
event = Event()
# create a thread 
thread = Thread(target=task, args=(event,))
# start the new thread
thread.start()
# block for a while
sleep(3)
# stop the worker thread
print('Main stopping thread')
event.set()
# 这里是为了演示，实际开发时，主进程有事件循环，耗时函数不需要调用join()方法
thread.join()
