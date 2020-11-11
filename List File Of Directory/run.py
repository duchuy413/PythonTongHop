import os
files = [f for f in os.listdir("C:\UNITY\NativeWebSocket") if os.path.isfile(f)]
for f in files:
    print (f)
    # do something
