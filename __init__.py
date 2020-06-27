"""
The SAMMpy package consists of a set of Python scripts to perform sensitivity
analysis with considering both parameteric uncertainty and process model 
uncertainty. 

This is the first version of SAMMpy and it is open source and any
assistance is welcomed. Please email us if you want to
contribute.

"""
__name__ = 'sammpy'
__author__ = 'Jing Yang, and Ming Ye'

from SALib.sample import saltelli

class model():
    """
    SAMMpy System Model Class.

    Parameters
    ----------
    name : string, optional
        Name of model. 
    frames : dict, optional
        The system model framework contains the process names and alternative 
        process model options
    env : dict, optional
        The constant variables used in the model simulations
    pars : dict, required
        The random paramters used in the model simulations. Descriptions of 
        parameter names, dists and bounds should be given
    func : function, required
        A pre-defined system model function 
         """

    def __init__(self):
        self.name = None
        self.frames = {}
        self.env = {}
        self.pars = {}
        self.func= None
        
    def sample(self, nobs, seed=933090936):
        """
        Generate the random parameter values using SALib

        Parameters
        ----------
        nobs: int
            Number of sample realizations 
        seed : int, optional
            The random seed

        Returns
        -------
        A NumPy matrix containing the model inputs using Saltelli's sampling
        scheme. The resulting matrix has size of N * D, where D is the 
        number of parameters.  
        """    
        nvars = len(self.pars['names'])
        problem = self.pars.copy()
        problem['num_vars'] = nvars
        values = saltelli.sample(problem, nobs, seed=seed, calc_second_order=False)[::nvars + 2, :]
        
        return values