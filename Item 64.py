import os, shutil, time, sched
pastafonte = "C:/Users/renato/Desktop/Origin Folder"
pastadestino = "C:/Users/renato/Desktop/Destination Folder"
lastday = time.time() - 24*60*60
s = sched.scheduler(time.time, time.sleep)


def do_something(sc):
    for file in os.listdir(pastafonte):
        filepath = os.path.join(pastafonte, file)
        if os.path.getmtime(filepath) >= lastday:
            print file
            fonte = os.path.join(pastafonte, file)
            dest = os.path.join(pastadestino, file)
            shutil.move(fonte, dest)
    s.enter(60*60*24, 1, do_something, (sc,))
s.enter(60*60*24, 1, do_something, (s,))
s.run()
