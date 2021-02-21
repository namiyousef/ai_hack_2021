def plotting(x, activation = None, normalization = None, plot = True, **kwargs):
    """
    Function to plot distributions for x depending on the type of normalization (transformation)
    and activation applied.

    Dependencies:
    -------------

    import matplotlib.pyplot as plt
    import seaborn as sns
    import pandas as pd

    Parameters:
    -----------
    x : pd.DataFrame
        dataframe of the data whose boxplot is to be plotted

    activation : func
        callable function that applies a transformation to x

    normalization : sklearn.preprocessing item
        a scaler from sklearn (can be MinMax, Robust, etc)

    plot : bool
        can be set to false to prevent plots (i.e when optimising)

    **kwargs
        kwargs for the activation functions
    """
    x_cols = x.columns
    x = x.copy()
    x = np.asarray(x)

    if activation:
        x = activation(x, **kwargs)
        activation = activation.__name__.upper()
    else:
        activation = 'NONE'


    if normalization:
        x = normalization().fit_transform(x)
        normalization = normalization.__name__.upper()
    else:
        normalization = 'NONE'

    if plot:
        fig, ax = plt.subplots(nrows = 1, ncols = 2, figsize = (16,8))
        fig.suptitle(('The distribution of the data with {} normalization for an activation'
                      ' function of {}'.format(normalization ,activation)), fontsize=16)

        for i in range(x.shape[1]):
            ax[0].hist(x[:,i], alpha = 0.2)
        ax[0].legend(x_cols)
        ax[1] = sns.boxplot(data = x)
        plt.xticks(rotation=15)
        plt.show()

    return pd.DataFrame(data = x, columns = x_cols), kurtosis(x), skew(x)

