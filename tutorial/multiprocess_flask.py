from multiprocessing import Process
from flask import Flask, flash
from time import sleep

app = Flask(__name__)

def testFun():
    print('Starting')
    for cn in range(20):
        print(str(cn) + ' Seconds Later')
        sleep(1)
    return 'FINISH'

@app.route('/kill')
def killproc():
    backProc.terminate()
    return "Killed Porcess "

@app.route('/')
def root():
    global backProc
    backProc = Process(target=testFun, args=())
    backProc.start()
    return "Started a background process"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0',port=8000)
