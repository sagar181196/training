N =input()
x=[]
for y in range(int(N)):
    aa = raw_input()
    action = aa.split(' ')
    print(action)
    # if action[0] == "print":
    #     print(x)
    # elif action[0]=="pop":
    #     x.pop()
    # elif action[0]=="sort":
    #     x.sort()
    # elif action[0]=="reverse":
    #     x.sort(reverse=True)  
    # elif action[0] == 'append':
    #     x.append(int(action[1]))
weight_pound = input("weight pound : ")
weight_kg = int(weight_pound)*0.45

print('your weight in kg {}'.format(weight_kg))


   
    