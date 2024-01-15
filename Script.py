import linecache

payloadfile = open("test.txt", "r")
totalline=0
url = input()
maliciouspayload=0


#for count line in a file
while True:
        content=payloadfile.readline()
        if not content:
                break
        totalline=totalline+1

#Check url payload on test.txt
for line in range(totalline):
        payload=linecache.getline('test.txt', line).replace('\n',"")
        if payload in url:
            maliciouspayload=maliciouspayload+1

#url malicious
if maliciouspayload >= 2:
        print ("Url is Malicious")

#url safe
else:
        print ("Url is Safe")

payloadfile.close()
