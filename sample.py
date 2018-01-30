import os


def sample():
    print ("hello world")
    cwddir = os.getcwd()
    print ("the current working directoryis:", cwddir)
    #path = r"C:\Users\GURC4657\Desktop\ppp"
    path = r"\root\Sampletest"
    if os.path.exists(path):
        print("the directory already exists")
    else:
        os.mkdir(path)
        print ("the directory got created")
    os.chdir(path)
    with open("vmtest.txt", 'w') as f:
        f.write("hello world\n Welcome to VM test file")
    print ("file got added")
sample()
