#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
from colorama import Fore,Back,Style
dict_topic = {}
dict_name = {}

filetopic = open('extempor_topic_list.txt', 'r+')

for topics in filetopic:
    topic = topics.split()
    dict_topic[topic[0]] = topic[1]

filetopic.close()

nameroll = open('name_roll.txt', 'r+')

for names in nameroll:
    name = names.split()
    dict_name[name[0]] = name[1]

nameroll.close()
while True:
    os.system('color E')
    outputfile = open('output.txt', 'a+')
    print(Fore.CYAN+"\033[1m******************************Welcome to 120IPRSeconds*******************************\033[0m")
    roll = str(input(Fore.CYAN+"\033[1mPlease Enter your Roll no:\033[0m")).strip()
    print(Style.RESET_ALL)

    while True:
        if roll not in dict_name:
            roll = input(Fore.RED + "\033[1mEnter a valid roll no\033[0m")
            continue
        else:
            print(Style.RESET_ALL)
            break
    count = 1
    print(Fore.GREEN+"\033[1mWelcome {}, please select a topic number between 1 to 50(1 & 50 inclusive)\033[0m".format(dict_name[roll]))
    print(Style.RESET_ALL)
    topic_number = int(input())
    while True:
        list_dup_topic = []
        topics_file = open('topics.txt', 'r+')
        for i in topics_file:
            list_dup_topic.append(i.strip())
        topics_file.close()

        if topic_number not in range(1, 51):
            topic_number = int(input(Fore.RED+"\033[1mEnter a valid topic number between 1 to 50\033[0m"))
            print(Style.RESET_ALL)
            continue
            
        elif str(topic_number) in list_dup_topic:
            topic_number = int(input(Fore.RED+"\033[1mTopic {} already selected,please select a new one\033[0m".format(dict_topic[str(topic_number)])))
            print(Style.RESET_ALL)
            continue
        else:
            if count < 2:
                print(Fore.CYAN+"\033[1myour topic is {},would you like to continue or pass on to a new topic,select Y to conitue or P to select a new topic\033[0m".format(dict_topic[str(topic_number)]))
                print(Style.RESET_ALL)
                input_new_topic = input()
                if input_new_topic in ('P', 'p'):
                    topic_number = int(input(Fore.RED+"\033[1mselect a new topic number\033[0m"))
                    print(Style.RESET_ALL)
                    count = count + 1
                    continue
                else:
                    break
            else:
                break

    print(Fore.GREEN+"\033[1mThanks for selecting topic number {}, your topic is {} , You have 120 seconds to speak, all the very best\033[0m".format(topic_number, dict_topic[str(topic_number)]))
    print(Style.RESET_ALL)
    outputfile.write(str(roll) + " " + dict_name[roll] + " " + dict_topic[str(topic_number)])
    outputfile.write('\n')
    outputfile.close()
    topics_file = open('topics.txt', 'a+')
    topics_file.write(str(topic_number))
    topics_file.write('\n')
    topics_file.close()

    exit_status = input(Fore.CYAN+"\033[1mWould you like to continue ?,enter No to exit or any other\033[1m key to continue?\033[0m")
    print(Style.RESET_ALL)

    if exit_status in ('no', 'NO', 'No'):
        break
    else:
        continue

os.system('color 7')
