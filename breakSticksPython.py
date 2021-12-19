#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Breaking Sticks in Python
@author: zoeblank
29 Nov 2021 (Edited 19 Dec 2021)

Packages used:
    1. random
    2. numpy
    3. matplotlib.pyplot
    4. pandas

A program to anaylze various random breaking points on a 1-unit stick using
uniform and beta distributions.

Compared to a program written in R under the same premise.
"""
#%% Prelim 

"""
Suppose you have a stick with a length of 1 unit.  The stick is broken into 
two pieces with a random breaking point -- we are interested in the 
ratio of the larger piece compared to the smaller piece.
"""

#%% Part 1
"""
Write a program that will simulate the distribution of the larger to the 
smaller piece of the stick when the break point is uniformly distributed. 
Compute the 5-number summary, mean, standard deviation and a histogram.
"""

import random as rd

## generate a random number as breakpoint, calculate ratio
def breakSim1():
    breakpt = rd.uniform(0,1)
    left = breakpt
    right = 1 - breakpt
    ## make sure we're dividing bigger piece / smaller piece
    if (left > right):
        ratio = left / right
    else:
        ratio = right / left
    return ratio

## build a list of 1000 ratios - initialize empty, then fill
break1dist = []
for i in range(1000):
    break1dist.append(breakSim1())
    

## convert mean and std with numpy
import numpy as np
np.mean(break1dist) 
np.std(break1dist)
    
## convert list to dataframe to use .describe()
import pandas as pd
break1_data = pd.Series(break1dist)
break1_data.describe()

## histogram:
import matplotlib.pyplot as plt
plt.hist(break1dist)

#%% Part 2
"""
Write a modified version of your program in Part 1 that allows a user to 
specify the two shape parameters from a Beta distribution; 
the break point is randomly chosen from the corresponding Beta distribution.
"""

## parameters must be input by user
def breakSim2(alpha, beta):
    ## generate break point
    breakpt = rd.betavariate(alpha = alpha, beta = beta)
    left = breakpt
    right = 1 - breakpt
    if (left > right):
        ratio = left / right
    else:
        ratio = right / left
    return ratio

## testing...
breakSim2(4, 4)
breakSim2(4, 4)
breakSim2(4, 4)

## new empty list for observations
break2dist = []
for i in range(1000):
    ## analyzing when parameters both = 4
    break2dist.append(breakSim2(4, 4))

## convert to df for descriptive stats
## (note - mean and std are included in .describe() info)
break2_data = pd.Series(break2dist)
break2_data.describe()

## histogram
plt.hist(break2dist)

## show plots side - by - side
fig = plt.figure()
ax1 = fig.add_subplot(2,2,1)
plt.hist(break1dist, bins=30)
ax2 = fig.add_subplot(2,2,2)
plt.hist(break2dist, bins=30)
fig

"""
How does this distribution compare to that found in Part 1 when both 
shape parameters take on the value 4?

The mean ratio for the part 2 distribution is much smaller than that from part 1.
This makes sense, because with a beta distribution, our break point is more likely
to be close to center than with a uniform distribution.

Further, both the standard deviation and spread from part 2 are much smaller than
those from part 1, again making sense because our beta distribution yields a break
point much more predictable and closer to center. This large standard deviation
makes it difficult to compare our histograms because they are on different x-axes.
"""

#%% Part 3
"""
Consider the situation where the stick is broken into 4 total pieces. 
Write a program that simulates this scenario where each of the break points is 
random based on a corresponding user-specified Beta distribution. 
Calculate the ratio of the largest piece to the smallest pieces in this scenario.
"""

def breakSim3(alpha, beta):
    ## generate initial break point
    breakpt1 = rd.betavariate(alpha = alpha, beta = beta)
    left1 = breakpt1
    right1 = 1 - breakpt1
    
    ## break each side of initial point
    breakptLeft = (rd.betavariate(alpha = alpha, beta = beta)) * left1
    left2a = breakptLeft 
    left2b = left1 - breakptLeft
    
    breakptRight = (rd.betavariate(alpha = alpha, beta = beta)) * right1
    right2a = breakptRight
    right2b = right1 - breakptRight
    
    ## max of all 4 pieces / min of all 4 pieces
    ratio = max(left2a, left2b, right2a, right2b) / min(left2a, left2b, right2a, right2b)
    
    return ratio

## new empty list for storage
break3dist = []
for i in range(1000):
    ## when both parameters = 6
    break3dist.append(breakSim3(6, 6))
    
## convert to df for description
break3_data = pd.Series(break3dist)
break3_data.describe()

## histogram
plt.hist(break3dist, bins = 30)   

## combine all 3 plots into one graphic
fig1 = plt.figure()
ax1 = fig1.add_subplot(2,2,1)
plt.hist(break1dist, bins=30)
ax2 = fig1.add_subplot(2,2,2)
plt.hist(break2dist, bins=30)
ax3 = fig1.add_subplot(2,2,3)
plt.hist(break3dist, bins=30)
fig1

"""
Compare/contrast it with that in Parts 1 and 2 when both shape parameters 
take on the value of 6.

Firstly, we notice that the mean ratio for part 3 is much smaller than part 1,
because we are using a beta distribution. We also note that the ratio for part 3
is slightly larger than part 2, which is to be expected, as we don't generally 
get 4 equal lengths of the stick.

This is reflected in the histograms when comparing parts 2 and 3, because part 3
has fewer ratios closer to 1. This means that part 3 generally had a larger 
difference in lengths between the longest and shortest pieces than part 2, 
which is to be expected.
"""