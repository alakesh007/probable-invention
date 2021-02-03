#!/usr/bin/env python
# coding: utf-8

# In[10]:



import os
from colorama import Fore,Back,Style
dict_topic = {}
dict_name = {}
main_topic_list=[]

for i in range (1,31):
    main_topic_list.append(str(i))

filetopic = open('extempor_topic_list.txt', 'r+')

for topics in filetopic:
    topic = topics.split('#')
    dict_topic[topic[0]] = topic[1]

filetopic.close()

nameroll = open('name_roll.txt', 'r+')

for names in nameroll:
    name = names.split('#')
    dict_name[name[0]] = name[1]

nameroll.close()
while True:
    os.system('color E')
    outputfile = open('output.txt', 'a+')
    print(Fore.YELLOW+"******************************"+Fore.MAGENTA+"Welcome to 120IPRSeconds"+Fore.YELLOW+"*********************************")
    print(Style.RESET_ALL)
    roll = str(input(Fore.CYAN+"Please Enter your Roll no:   ")).strip()
        
    print(Style.RESET_ALL)
    
    if len(roll)==1:
        roll = '0'+roll
        

    while True:
        if roll not in dict_name:
            roll = input(Fore.RED + "Enter a valid Roll no:   ")
            if len(roll)==1:
                roll = '0'+roll
                continue
        else:
            roll_exist = input(Fore.YELLOW+"Is Roll no "+str(roll)+" present? Enter Yes/No ")
            print(Style.RESET_ALL)

            if(roll_exist not in ('y','Y','Yes','yes','yES')):
                roll = input(Fore.RED + "Enter a valid Roll no:   ")
                if len(roll)==1:
                    roll = '0'+roll
                print(Style.RESET_ALL)
                continue
            else:
                break
                print(Style.RESET_ALL)
    
    count = 1
    print(Fore.GREEN+"Welcome {}, please select a topic number between 1 to 30(1 & 30 inclusive)   ".format(dict_name[roll].rstrip()))
    print(Style.RESET_ALL)
        
    topics_existing=[]
    
    topics_file1 = open('topics.txt', 'r+')
    for h in topics_file1:
        topics_existing.append(h.rstrip())
    
    topics_file1.close()
        
    list_diff = list(set(main_topic_list).difference(set(topics_existing)))
    list_diff_int=[]
    
    for j in list_diff:
        list_diff_int.append(int(j))
        
    
    list_diff_sort = sorted(list_diff_int)
    print(Fore.CYAN+"You have below available list of topics to choose from: ")
    print(Style.RESET_ALL)
    print(list_diff_sort)
    
    topic_number = str(input())
        
    while True:
        list_dup_topic = []
        topics_file = open('topics.txt', 'r+')
        for i in topics_file:
            list_dup_topic.append(i.strip())
        topics_file.close()
        
        if not str(topic_number).isdigit():
            topic_number = input(Fore.RED+"Enter a valid topic number between 1 to 30  ")
            print(Style.RESET_ALL)
            continue
            
        elif int(topic_number) not in range(1, 31):
            topic_number = input(Fore.RED+"Enter a valid topic number between 1 to 30  ")
            print(Style.RESET_ALL)
            continue
            
        elif topic_number in list_dup_topic:
            topic_number = input(Fore.RED+"Topic "+dict_topic[str(topic_number)].rstrip()+" already selected,please select a new one  ")
            print(Style.RESET_ALL)
            continue
        else:
            if count < 2:
                print(Fore.CYAN+"Your topic is "+Fore.MAGENTA+ dict_topic[str(topic_number)].rstrip()+Fore.CYAN+",would you like to continue or pass on to a new topic,select any other key to continue or P to select a new topic  ")
                print(Style.RESET_ALL)
                input_new_topic = input()
                if input_new_topic in ('P', 'p'):
                    topic_number = input(Fore.RED+"select a new topic number  ")
                    print(Style.RESET_ALL)
                    count = count + 1
                    continue
                else:
                    break
            else:
                break

    print(Fore.GREEN+"Thanks for selecting topic number "+topic_number+", your topic is: "+Fore.MAGENTA+ dict_topic[str(topic_number)].rstrip()+Fore.GREEN+",think for 30 seconds and then speak for 120 seconds")
    print(Style.RESET_ALL)
    print(Fore.MAGENTA+ "All the very best   ")   
    print(Style.RESET_ALL)
    outputfile.write(str(roll) + " " + dict_name[roll].rstrip() + ":" + dict_topic[str(topic_number)].rstrip())
    outputfile.write('\n')
    outputfile.close()
    topics_file = open('topics.txt', 'a+')
    topics_file.write(str(topic_number))
    topics_file.write('\n')
    topics_file.close()

    exit_status = input(Fore.CYAN+"Would you like to continue?enter No to exit or any other key to continue?   ")
    print(Style.RESET_ALL)

    if exit_status in ('No','NO','no','nO'):
        break
    else:
        continue

os.system('color 7')




# In[ ]:





# In[6]:


topics_file1 = open('topics.txt', 'r+')
for h in topics_file1:
    print(h.rstrip())
topics_file1.close()


# In[ ]:


list11=[]

