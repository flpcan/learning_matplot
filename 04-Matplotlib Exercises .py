#!/usr/bin/env python
# coding: utf-8

# ___
# 
# <a href='http://www.pieriandata.com'> <img src='../Pierian_Data_Logo.png' /></a>
# ___
# # Matplotlib Exercises 
# Welcome to the exercises for reviewing matplotlib! Take your time with these, Matplotlib can be tricky to understand at first. These are relatively simple plots, but they can be hard if this is your first time with matplotlib, feel free to reference the solutions as you go along.
# 
# Also don't worry if you find the matplotlib syntax frustrating, we actually won't be using it that often throughout the course, we will switch to using seaborn and pandas built-in visualization capabilities. But, those are built-off of matplotlib, which is why it is still important to get exposure to it!
# 
# **NOTE: ALL THE COMMANDS FOR PLOTTING A FIGURE SHOULD ALL GO IN THE SAME CELL. SEPARATING THEM OUT INTO MULTIPLE CELLS MAY CAUSE NOTHING TO SHOW UP.**
# 
# # Exercises
# 
# **We will focus on two commons tasks, plotting a known relationship from an equation and plotting raw data points.**
# 
# Follow the instructions to complete the tasks to recreate the plots using this data:
# 
# ----
# ----
# 
# ### Task One: Creating data from an equation
# 
# It is important to be able to directly translate a real equation into a plot. Your first task actually is pure numpy, then we will explore how to plot it out with Matplotlib. The [world famous equation](https://en.wikipedia.org/wiki/Mass%E2%80%93energy_equivalence) from Einstein:
# 
# $$E=mc^2$$
# 
# 
# Use your knowledge of Numpy to create two arrays: E and m , where **m** is simply 11 evenly spaced values representing 0 grams to 10 grams. E should be the equivalent energy for the mass. You will need to figure out what to provide for **c** for the units m/s, a quick google search will easily give you the answer (we'll use the close approximation in our solutions).
# 
# **NOTE: If this confuses you, then hop over to the solutions video for a guided walkthrough.**

# In[19]:


# CODE HERE
import numpy as np

m = np.linspace(0,10,11)

m


# In[11]:





# In[29]:


# CODE HERE
c = 3*10**8
e = m*c**2

e


# In[15]:





# ### Part Two: Plotting E=mc^2
# 
# Now that we have the arrays E and m, we can plot this to see the relationship between Energy and Mass. 
# 
# **TASK: Import what you need from Matplotlib to plot out graphs:**

# In[30]:


import matplotlib.pyplot as plt


# **TASK: Recreate the plot shown below which maps out E=mc^2 using the arrays we created in the previous task. Note the labels, titles, color, and axis limits. You don't need to match perfectly, but you should attempt to re-create each major component.**

# In[34]:


# CODE HERE
plt.plot(m,e,color="red",lw=5)
plt.xlabel('Mass in Grams')
plt.ylabel('Energy in Joules')
plt.title('E=mc^2')

plt.xlim(0,10)
plt.show()


# In[23]:


# DON'T RUN THE CELL BELOW< THAT WILL ERASE THE PLOT!


# In[24]:





# ### Part Three (BONUS)
# 
# **Can you figure out how to plot this on a logarthimic scale on the y axis? Place a grid along the y axis ticks as well. We didn't show this in the videos, but you should be able to figure this out by referencing Google, StackOverflow, Matplotlib Docs, or even our "Additional Matplotlib Commands" notebook. The plot we show here only required two more lines of code for the changes.**

# In[39]:


# CODE HERE

plt.plot(m,e,color="red",lw=5)
plt.xlabel('Mass in Grams')
plt.ylabel('Energy in Joules')
plt.title('E=mc^2')

plt.xlim(0,10)

plt.yscale("log")
plt.grid(which="both",axis="y")


# In[29]:


# DONT RUN THE CELL BELOW! THAT WILL ERASE THE PLOT!


# In[27]:





# ---
# ---
# 
# ## Task Two: Creating plots from data points
# 
# In finance, the yield curve is a curve showing several yields to maturity or interest rates across different contract lengths (2 month, 2 year, 20 year, etc. ...) for a similar debt contract. The curve shows the relation between the (level of the) interest rate (or cost of borrowing) and the time to maturity, known as the "term", of the debt for a given borrower in a given currency.
# 
# The U.S. dollar interest rates paid on U.S. Treasury securities for various maturities are closely watched by many traders, and are commonly plotted on a graph such as the one on the right, which is informally called "the yield curve".
# 
# **For this exercise, we will give you the data for the yield curves at two separate points in time. Then we will ask you to create some plots from this data.**
# 
# ## Part One: Yield Curve Data
# 
# **We've obtained some yeild curve data for you from the [US Treasury Dept.](https://www.treasury.gov/resource-center/data-chart-center/interest-rates/pages/textview.aspx?data=yield). The data shows the interest paid for a US Treasury bond for a certain contract length. The labels list shows the corresponding contract length per index position.**
# 
# **TASK: Run the cell below to create the lists for plotting.**

# In[40]:


labels = ['1 Mo','3 Mo','6 Mo','1 Yr','2 Yr','3 Yr','5 Yr','7 Yr','10 Yr','20 Yr','30 Yr']

july16_2007 =[4.75,4.98,5.08,5.01,4.89,4.89,4.95,4.99,5.05,5.21,5.14]
july16_2020 = [0.12,0.11,0.13,0.14,0.16,0.17,0.28,0.46,0.62,1.09,1.31]


# **TASK: Figure out how to plot both curves on the same Figure. Add a legend to show which curve corresponds to a certain year.**

# In[43]:


# CODE HERE
fig = plt.figure()

axes = fig.add_axes([0,0,1,1])

axes.plot(labels,july16_2007, label= "july16_2007")
axes.plot(labels,july16_2020, label= "july16_2020")

axes.legend()


# In[38]:


# DONT RUN THE CELL BELOW! IT WILL ERASE THE PLOT!


# In[36]:





# **TASK: The legend in the plot above looks a little strange in the middle of the curves. While it is not blocking anything, it would be nicer if it were *outside* the plot. Figure out how to move the legend outside the main Figure plot.**

# In[44]:


# CODE HERE
fig = plt.figure()

axes = fig.add_axes([0,0,1,1])

axes.plot(labels,july16_2007, label= "july16_2007")
axes.plot(labels,july16_2020, label= "july16_2020")

axes.legend(loc=(1.04,0.5))


# In[45]:


# DONT RUN THE CELL BELOW! IT WILL ERASE THE PLOT!


# In[47]:





# **TASK: While the plot above clearly shows how rates fell from 2007 to 2020, putting these on the same plot makes it difficult to discern the rate differences within the same year. Use .suplots() to create the plot figure below, which shows each year's yield curve.**

# In[47]:


# CODE HERE

fig,axes = plt.subplots(nrows=2,ncols=1, figsize =(12,8))

axes[0].plot(labels,july16_2007,)
axes[1].plot(labels,july16_2020,)

axes[0].set_title("july16_2007")
axes[1].set_title("july16_2020")


# In[51]:


# DONT RUN THE CELL BELOW! IT WILL ERASE THE PLOT!


# In[52]:





# **BONUS CHALLENGE TASK: Try to recreate the plot below that uses twin axes. While this plot may actually be more confusing than helpful, its a good exercise in Matplotlib control.**

# In[48]:


# CODE HERE
fig, ax1 = plt.subplots()

ax1.plot(labels,july16_2007, lw=2, color="blue")
ax1.set_ylabel("july16_2007", fontsize=18, color="blue")
for label in ax1.get_yticklabels():
    label.set_color("blue")
    
ax2 = ax1.twinx()
ax2.plot(labels,july16_2020, lw=2, color="red")
ax2.set_ylabel("july16_2020", fontsize=18, color="red")
for label in ax2.get_yticklabels():
    label.set_color("red")


# In[63]:


# DONT RUN THE CELL BELOW! IT ERASES THE PLOT!


# In[73]:





# -----
