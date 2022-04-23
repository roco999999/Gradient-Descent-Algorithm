# Notebooks importss and Packages

import matplotlib.pyplot as plt
import numpy as np 


#%matplotlib inline

def f(x):
    return (x**2) + x + 1

x_1 = np.linspace(start=-3, stop=3, num = 100)

# PLOTTING 
plt.plot(x_1,f(x_1), color="blue", linewidth = 5)
plt.xlim([-3, 3])
plt.ylim(0, 8)
plt.xlabel("X in değerler",fontsize= 14)
plt.ylabel("f(x)'in değerler",fontsize= 14)
plt.show()

#%%

def df(x):
    return 2*x + 1

plt.figure(figsize=[10, 5])
# First chart : Cost function.
plt.subplot(1, 2, 1)

plt.plot(x_1,f(x_1), color="blue", linewidth = 5)
plt.xlim([-3, 3])
plt.ylim(0, 8)
plt.xlabel("X in değerler",fontsize= 14)
plt.ylabel("f(x)'in değerler",fontsize= 14)
# Second chart : derivative 
plt.subplot(1, 2, 2)
plt.grid()
plt.plot(x_1, df(x_1), color="skyblue", linewidth=5)
plt.xlim(-2, 3)
plt.ylim(-3, 6)

plt.show()


#%%

# GRADIENT DESCENT

new_x = 3
previous_x = 0
presicion = 0.00001
step_multiplier = 0.1

x_list = [new_x]
slope_list = [df(new_x)]

for i in range(500):
    previous_x = new_x
    gradient = df(previous_x)
    new_x = previous_x - step_multiplier * gradient
        
    step_size = abs(new_x - previous_x)
    # print(step_size)
    
    x_list.append(new_x)
    slope_list.append(df(new_x))
    if step_size < presicion:
        print('Loop ran this many times:',i)
        break

print("local minimum occurs at: ", new_x)
print('slope or df(x)', df(new_x))
print('f(x) value cost at this point is: ',f(new_x))

# Superimpose the gradient descent calculations.
plt.figure(figsize=[20, 5])

plt.subplot(1, 3, 1)

plt.plot(x_1,f(x_1), color="blue", linewidth = 2)
plt.xlim(-3, 3)
plt.ylim(0, 8)
plt.grid()
plt.xlabel("X in değerler",fontsize= 16)
plt.ylabel("f(x)'in değerler",fontsize= 16)

values = np.array(x_list)
plt.scatter(x_list, f(values), color= 'black',s = 50, alpha = 0.5)

# Second chart : derivative 
plt.subplot(1, 3, 2)
plt.grid()
plt.xlabel("X")
plt.ylabel("Slope")
plt.xlim(-2, 3)
plt.ylim(-3, 6)

plt.plot(x_1, df(x_1), color="skyblue", linewidth=2)
plt.scatter(x_list, slope_list, color="black", s=50, alpha = 0.5)


plt.show()

# Third chart : derivative (close up) 
plt.title("Gradient Descent Close UP",fontsize = 17)
plt.subplot(1, 3, 3)
plt.grid()
plt.xlabel("X")
plt.ylabel("Slope")
plt.xlim(-0.55, -0.2)
plt.ylim(-0.3, 0.8)

plt.plot(x_1, df(x_1), color="skyblue", linewidth=4, alpha = 0.8)
plt.scatter(x_list, slope_list, color="black", s=100, alpha = 0.5)

plt.show()



#%%

liste = []

def sing(num_bottles):
    #TODO: Add your code to achieve the desired output and pass the challenge. 
    #NOTE: The f String method of String Interpolation does not work. 
    liste = []
    for i in range(num_bottles,0,-1):
        liste.append("'{} bottles of beer on the wall, {} bottles of beer.'".format(i,i))
        liste.append("'Take one down and pass it around, {} bottles of beer on the wall.'".format(i-1))
        liste.append("''")
    
    for i in range(len(liste)):
        print(liste[i])
    
sing(99)









