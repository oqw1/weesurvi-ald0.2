import time
import os

HandleFile = input("Enter the file you want to run (ending with .wrf):")
ls = ''
print("The file is being read")
with open(HandleFile + '.wrf') as re:
    Text = re.read()
print("Lexical analysis is in progress.")
text = Text.split('\n')

print('Start execution.')
i = 0
while(i > -1):
    ls = text[i].split(' ')
    if ls[0] == 'create':
        try:
            with open(ls[1],'w') as cr:
                cr.write(' ')
        except FileExistsError:
            print('Create error in line' + str(i))
            break
        else:
            ls.clear()
            i = i + 1
            try:
                ls = text[i]
            except IndexError:
                print("[Finished]")
                break
    elif ls[0] == 'write':
        with open(ls[1],'w',encoding='utf-8') as wr:
            wr.write(ls[2])
        ls.clear()
        i = i + 1
        try:
            ls = text[i]
        except IndexError:
            print("[Finished]")
            break
    elif ls[0] == 'remove':
        try:
            os.remove(ls[1])
        except FileNotFoundError:
            print('Remove error in line' + str(i))
            break
        else:
            ls.clear()
            i = i + 1
            try:
                ls = text[i]
            except IndexError:
                print("[Finished]")
                break
    elif ls[0] == 'copy':
            try:
                #copy
                with open(ls[1], encoding='utf-8') as cow:
                    a = cow.read()
            except FileNotFoundError:
                print('Copy error in line' + str(i))
                break
            else:
                with open(ls[2], 'w', encoding='utf-8') as coo:
                    coo.write(a)
            ls.clear()
            i = i + 1
            try:
                ls = text[i]
            except IndexError:
                print("[Finished]")
                break
    elif ls[0] == 'read':
        try:
            #read
            with open(ls[1]) as rea:
                cpp = rea.read()
                print("read:\n" + cpp + '\n')
        except FileNotFoundError:
            print('Read error in line' + str(i))
            break
        else:
            ls.clear()
            i = i + 1
            try:
                ls = text[i]
            except IndexError:
                print("[Finished]")
                break
    elif ls[0] == 'append':
        try:
            #append
            with open(ls[1],'a') as app:
                app.write(ls[2])
        except FileNotFoundError:
                print('Append error in line' + str(i))
                break
        else:
            ls.clear()
            i = i + 1
            try:
                ls = text[i]
            except IndexError:
                print("[Finished]")
                break
    elif ls[0] == 'echo':
        print(ls[1])
        ls.clear()
        i = i + 1
        try:
            ls = text[i]
        except IndexError:
            print("[Finished]")
            break