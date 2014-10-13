dictionary={
'adjective':[
    'good',
    'nice',
    'bad',
    'ugly',
    'new',],
'names':[
    'book',
    'computer',
    'bird',
    'tree',
    'table',],
}

import pickle
f = open("s%s%s'%(first_part,w_space,second_part)",'w')
pickle.dump(dictionary, f)
f.close()


f1 = open("%s%s%s'%(first_part,w_space,second_part)",'r')
sd = pickle.load(f1)
f1.close()

import random
first_part=sd['adjective'][random.randint(0,len(sd['adjective'])-1)]
second_part=sd['names'][random.randint(0,len(sd['names'])-1)]
w_space = " "
print '%s%s%s'%(first_part,w_space,second_part)

f3 = open("%s%s%s'%(first_part,w_space,second_part)","w")
f3.writelines('%s%s%s'%(first_part,w_space,second_part))

f3.close()


