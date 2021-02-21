
def plot_classes(X,y, vars = None, **kwargs):

    """
    Given X and y, where X represents the X values and y the classes, plots outcomes
    with different colors.

    I want to have the option of choosing which variables to plot against each other
    NOTE:
    -----
    - lacks the use of **kwargs *args properly
    - does not have functionality for x, y and title labels
    - does not have legend
    - only 2 dimensional

    """
    if vars:
        pass # here add code for custom variables
    else:
        ncols = int(X.shape[1] ** (1/2))
        nrows = X.shape[1] // ncols

    fig, axes = plt.subplots(nrows = nrows, ncols = ncols, figsize = (nrows * 8, ncols * 8))
    feature_1 = 0
    feature_2 = feature_1 + 1
    for j, column in enumerate(axes):
        for i, row in enumerate(column):
            for y_unique in np.unique(y):
                axes[j,i].plot(
                    X[y == y_unique, feature_1],
                    X[y == y_unique, feature_2],
                    '.'
                )
                axes[j,i].set_xlabel('Feature {}'.format(feature_1))
                axes[j,i].set_ylabel('Feature {}'.format(feature_2))

            feature_2 += 1
            if feature_2 >= X.shape[1]:
                feature_1 += 1
                feature_2 = feature_1 + 1
    plt.legend([*np.unique(y)])
    return fig, axes
