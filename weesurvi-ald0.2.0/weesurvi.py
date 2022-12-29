import os
import datetime
import tkinter
import tkinter.messagebox

try:
    os.remove("weesurvi-create.py")
except:
    qaz = ''
def error(ert='***',a='t'):
    if a == 't':
        print("<FileError>:\"" + ert + "\"")
    else:
        print("<CodeError>:\"" + ert + "\"")
    print("What is " + ert + "?")
say = ''
print("Weesurvi.[type:ald0.2.0]")
while True:
    ao = input("weesurvi>")
    say += ao + "\n"
    aos = ao.split()
    now = datetime.datetime.now()
    try:
        if '.dll' in aos[1] or '.bat' in aos[1]:
            tkinter.messagebox.showwarning('!!!','You can\'t write or delete .dll or .bat file')
        #create
        elif aos[0] == 'create':
            try:
                with open(aos[1], 'x') as cw:
                    cw.write('')
                with open('weesurvi-log','a') as log:
                    log.write('Admin use ' + ao +' at ' + now.strftime("%Y-%m-%d %H:%M:%S") + ";/n")
            except FileExistsError:
                error(ao)

        elif aos[0] == 'copy':
            try:
                #copy
                with open(aos[1], encoding='utf-8') as cow:
                    a = cow.read()
            except FileNotFoundError:
                error(ao)
            else:
                with open(aos[2], 'w', encoding='utf-8') as coo:
                    coo.write(a)
                with open('weesurvi-log','a') as log:
                    log.write('Admin use ' + ao +' at ' + now.strftime("%Y-%m-%d %H:%M:%S") + ";/n")

        elif aos[0] == 'remove':
            try:
                #remove
                os.remove(aos[1])
                with open('weesurvi-log','a') as log:
                    log.write('Admin use ' + ao +' at ' + now.strftime("%Y-%m-%d %H:%M:%S") + ";/n")
            except FileNotFoundError:
                error(ao)
        elif aos[0] == 'write':
            #write
            with open(aos[1],'w') as wr:
                wr.write(aos[2])
            with open('weesurvi-log','a') as log:
                log.write('Admin use ' + ao +' at ' + now.strftime("%Y-%m-%d %H:%M:%S") + ";/n")
        elif aos[0] == 'read':
            try:
                #read
                with open(aos[1]) as rea:
                    cpp = rea.read()
                    print("read:\n" + cpp)
                with open('weesurvi-log','a') as log:
                    log.write('Admin use ' + ao +' at ' + now.strftime("%Y-%m-%d %H:%M:%S") + ";/n")
            except FileNotFoundError:
                error(ao)
        elif aos[0] == 'break' and aos[1] == 'say':
            #break
            break
        elif aos[0] == 'append':
            try:
                #append
                with open(aos[1],'a') as app:
                    app.write(aos[2])
                with open('weesurvi-log','a') as log:
                    log.write('Admin use ' + ao +' at ' + now.strftime("%Y-%m-%d %H:%M:%S") + ";/n")
            except FileNotFoundError:
                error(ao)
        elif aos[0] == 'save':
            with open('weesurvi-log','a') as log:
                log.write('Admin use ' + ao +' at ' + now.strftime("%Y-%m-%d %H:%M:%S") + ";/n")
            #save
            if aos[1] == 'clean':
                with open(aos[2],'w') as sas:
                    sas.write(say)
                say = ''
            elif aos[1] == 'save':
                with open(aos[2],'w') as sas:
                    sas.write(say)
            else:
                error(ao,'f')
        elif aos[0] == "pi":
            #save
            print(3.14159265)
            with open('weesurvi-log','a') as log:
                log.write('Admin use ' + ao +' at ' + now.strftime("%Y-%m-%d %H:%M:%S") + ";/n")
        elif aos[0] == "abs":
            #abs
            num = aos[1]
            try:
                num = int(num)
                with open('weesurvi-log','a') as log:
                    log.write('Admin use ' + ao +' at ' + now.strftime("%Y-%m-%d %H:%M:%S") + ";/n")
            except ValueError:
                error(ao,'f')
            else:
                print(abs(num))
        elif aos[0] == 'strlen':
            try:
                #len
                with open(aos[1]) as rea:
                    cpp = rea.read()
                with open('weesurvi-log','a') as log:
                    log.write('Admin use ' + ao +' at ' + now.strftime("%Y-%m-%d %H:%M:%S") + ";/n")
            except FileNotFoundError:
                error(ao)
            else:
                print(len(cpp))
        elif aos[0] == 'runpython' and aos[1] == 'hi':
            eval(aos[2])
        elif aos[0] == 'batch_create':
            sos = int(aos[1])
            for i in range(1,sos+1):
                with open(aos[i+1],'w') as fileh:
                    fileh.write('')
                with open('weesurvi-log','a') as log:
                    log.write('Admin use ' + ao +' at ' + now.strftime("%Y-%m-%d %H:%M:%S") + ";/n")
        elif aos[0] == 'batch_remove':
            sos = int(aos[1])
            for i in range(1,sos+1):
                try:
                    os.remove(aos[i+1])
                    with open('weesurvi-log','a') as log:
                        log.write('Admin use ' + ao +' at ' + now.strftime("%Y-%m-%d %H:%M:%S") + ";/n")
                except FileNotFoundError:
                    error(ao)
        elif aos[0] == 'intercept_to':
            try:
                with open(aos[1]) as hello:
                    asdfg = hello.read()
                with open('weesurvi-log','a') as log:
                    log.write('Admin use ' + ao +' at ' + now.strftime("%Y-%m-%d %H:%M:%S") + ";/n")
            except FileNotFoundError:
                error(ao)
            else:
                asdfg = asdfg.replace('\n','qwertyuioplkjhgfdsa')
                xc = asdfg.split('qwertyuioplkjhgfdsa')
                print(xc[aos[2+1]])
        elif aos[0] == "log" and aos[1] == "see":
            with open("weesurvi-log") as seelog:
                print(seelog.read())
        elif aos[0] == "compute":
            eval(aos[1])
        elif aos[0] == "log-clear" and aos[1] == "-?okay":
            with open('weesurvi-log','w') as df:
                df.write('')
        elif aos[0] == "alert":
            tkinter.messagebox.showwarning(aos[1],aos[2])
        elif aos[0] == "echo":
            print(aos[1])
        else:
            error(ao,'f')
            with open('weesurvi-log','a') as log:
                log.write('Admin use error sentence' + ao +' at ' + now.strftime("%Y-%m-%d %H:%M:%S") + ";/n")
    except IndexError:
        error(ao,'f')
        with open('weesurvi-log','a') as log:
            log.write('Admin use error sentence' + ao +' at ' + now.strftime("%Y-%m-%d %H:%M:%S") + ";/n")
    except ValueError:
        error(ao,'f')
        with open('weesurvi-log','a') as log:
            log.write('Admin use error sentence' + ao +' at ' + now.strftime("%Y-%m-%d %H:%M:%S") + ";/n")