"""
Created on Thu Jun 25 21:52:56 2020

@author: Jing
"""

import numpy as np
import matplotlib.pyplot as plt

def plot(model, Ret):
    '''
    Plots mean against variance of the output difference

    '''

    '''
    Create bar chart of difference-based sensitivity results

    Parameters
    ----------
    model: object, defined in sammpy
    Ret: dict, of sensitivity results

    '''
    plt.figure(figsize=(5, 5))
    x = np.arange(len(model.frames['names']))

    plt.scatter(Ret['mean'], Ret['variance'])
    for i in range(len(model.frames['names'])):
        plt.text(Ret['mean'][i], Ret['variance'][i], model.frames['names'][i],
                 fontsize=14)
    plt.xlabel('Mean', fontsize=14)
    plt.ylabel('Variance', fontsize=14)
    
    plt.show()
    return 



