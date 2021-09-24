import os
os.system('rm -rf dork-list.txt')
os.system('touch dork-list.txt')
dorks = open('do.txt','r')
for words in dorks:
    #f = open('dorks.txt','r')
    words = words.strip("news")
    words = words.strip()
    save = open('dork-list.txt','a')
    w = save.write(words+'\n')
    print (words) 
    

