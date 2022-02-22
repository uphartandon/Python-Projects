# Health Management system that Lock and Retrieve Data as per users input
client_list= {1:"Harry", 2:"Rohan",3:"Hammad",4:"Nikhil"}
log_list = {1:"Exercise",2:"Diet"}
# print(client_list.items())
# print(client_list.keys())

def gettime():
    import datetime
    return datetime.datetime.now()

try:
    print("Select client name:")
    for key, value in client_list.items():
        print("Press",key,"for",value,"\n",end="")
    client_name = int(input())
    print("Selected Client :", client_list[client_name], "\n",end="")

    print("Press 1 for log")
    print("Press 2 for retrieve")
    op = int(input())

    if op == 1:
        for key, value in log_list.items():
            print("Press", key, "for",value, "\n",end="")
        lock_name = int(input())
        print("Selected Job:", log_list[lock_name])
        f = open(client_list[client_name]+ "_"+log_list[lock_name]+".txt","a")
        k="y"
        while (k != "n"):
            print("Enter",log_list[lock_name], "\n", end="")
            mytext = input()
            f.write("[" + str(gettime()) + "]:"+mytext+"\n")
            k = input("Add more ? y/n")
            continue
        print(log_list[lock_name],"Records Saved Successfully for",client_list[client_name])
        f.close()
    elif op == 2:
        for key, value in log_list.items():
            print("Press", key, "to retrieve", value, "\n", end="")
        lock_name = int(input())
        print(client_list[client_name]+"_" +log_list[lock_name],"Report: ","\n",end="")
        f = open(client_list[client_name]+ "_"+log_list[lock_name]+".txt","rt")
        contents = f.readlines()
        for line in contents:
            print(line,end ="")
        f.close()
    else:
        print("Invalid Input!!!")
except Exception as e:
    print("Provide the correct details")













