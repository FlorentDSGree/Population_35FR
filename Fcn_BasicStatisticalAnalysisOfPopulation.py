
# coding: utf-8

# In[ ]:


from __future__ import division
from math import cos, asin, sqrt


# In[ ]:


# This function create a list that contains the number in log base 10 order
# Inputs:
# - start: first value of the list, must be a positive integer
# - stop: last value of the list, must be a positive integer

# function to create log bin for plot
def CreateLogBin(start,stop):
    # Initialisation
    stopTemp  = stop
    z         = start
    increment = 0
    flag      = 0
    bins      = list()

    # While loop to calculate the number of for loop to run next
    while flag == 0:
        increment = increment + 1
        stopTemp = stopTemp/10
        # If loop to check whether stopTemp = start
        if stopTemp == start:
            flag = 1
    # For loop to create the log bin
    for y in range(0,increment):
        for x in range(1,10):
            bins.append(x*z)
        z = z*10
    # Add the last value
    bins.append(int((x+1)*z/10))
    return bins


# In[ ]:


# This function define the lower and higher boundary for the analysis using log base 10
# Inputs:
# - Value: either the min or max value of the population
# - MinMaxParameters: either 'Min' (when min population specified) or 'Max' (when max population specified)

def DefineMinMaxLog(Value,MinMaxParameters):

    i = Value
    k = 0
    while i > 1:
        k = k + 1
        i = i/10
    if MinMaxParameters == 'Min':
        ValueBorder = 10**(k-1) # Should be; ValueBorder = 10**(k-1); but when define as function it must be modified to make it working
    elif MinMaxParameters == 'Max': 
        ValueBorder = 10**k
    return ValueBorder


# In[ ]:


# This function remove the hist value where the value is 0 at the begining and at the end of the list
# The purpose is to reduce the x axis in the plot to make it easier to read

def RemoveLastFirstValuesWhenZero(hist,bin_edges):
    #Get index until last value not 0
    for LastNotZero in range(0,len(hist)):
        if hist[len(hist)-1-LastNotZero] > 0:
            break
    #Get index of first not 0 value
    for FirstNotZero in range(0,len(hist)):
        if hist[FirstNotZero] > 0:
            break
    #Update hist and bin_edges
    hist = hist[FirstNotZero:-LastNotZero]
    bin_edges = bin_edges[FirstNotZero:-LastNotZero]
    return hist,bin_edges


# In[ ]:


# This function calculate the euclidean distance between 2 coordinates (latitude/longitude)

def DistanceCoordToKm(lat1, lon1, lat2, lon2):
    p = 0.017453292519943295     #Pi/180
    a = 0.5 - cos((lat2 - lat1) * p)/2 + cos(lat1 * p) * cos(lat2 * p) * (1 - cos((lon2 - lon1) * p)) / 2
    return 12742 * asin(sqrt(a)) #2*R*asin...

