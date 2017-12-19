#######################################################################################################
##
## FILE: variable_importance_ic.py
##
## CREATED: 31 January 2017 by Brian Williamson
##
## PURPOSE: Calculate the IC for the variable importance parameters, new POI
##
## INPUTS/OUTPUTS: None
##
## UPDATES:
## DDMMYY INIT COMMENTS
## ------ ---- --------
#######################################################################################################
## FUNCTION: variableImportanceIC
## ARGS:   full - model fit to the full data (numpy array)
##      reduced - model fit to the reduced data (numpy array)
##            y - outcome (numpy array)
## standardized - standardized or non-standardized parameter
## RETURNS: influence curve fit to the data
def variableImportanceIC(full = None, reduced = None, y = None, standardized = True):
    import numpy as np
    import pdb
    ## calculate naive estimates
    pdb.set_trace()

    naive_j = np.mean(np.square(full - reduced))
    naive_var = np.mean(np.square(y - np.mean(y)))
    
    ## now calculate ic
    if(standardized):
        ret = (2*np.multiply(y - full, full - reduced) + np.square(full - reduced) - naive_j)/naive_var - (np.square(y - np.mean(y)) - naive_var)*naive_j/(naive_var ** 2)
        
    else:
        ret = (2*np.dot(np.transpose(y - full), full - reduced) + np.square(full - reduced) - naive_j)
    
    return ret
