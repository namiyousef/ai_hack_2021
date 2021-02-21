# neural model (really just made for fun)

from tensorflow.keras import Input, Model
from tensorflow.keras.layers import BatchNormalization, Dense
from tensorflow.keras.optimizers import Adam
from sklearn.model_selection import KFold
from time import time
import numpy as np
import matplotlib.pyplot as plt

def nn(X, y):
    print(X.shape)

    # add automation to this
    def uncompiled_model(X):
        inputs = Input(shape=(X.shape[1],), name='Data')
        x = Dense(16, activation='relu')(inputs)
        x = BatchNormalization()(x)
        x = Dense(8, activation='relu')(x)
        x = BatchNormalization()(x)
        x = Dense(16, activation='relu')(x)
        x = BatchNormalization()(x)
        outputs = Dense(1, activation='relu')(x)

        model = Model(inputs=inputs, outputs=outputs)
        return model

    def compile_model(X):
        model = uncompiled_model(X)
        model.compile(
            optimizer=Adam(learning_rate=0.001),  # RMSprop has potential for improvement but needs high epochs
            loss="mse",  # binary_crossentropy #hinge not bad?
            metrics=["accuracy",
                     ],
        )
        return model

    return compile_model(X)


def cross_validate(X,y,K = 5, **kwargs):
    """
    function to cross validate a neural network model

    Dependencies:
    -------------

    from sklearn.model_selection import KFold
    import numpy as np

    Parameters:
    -----------

    X : np.array OR pd.DataFrame
        the X data

    y : np.array OR pd.DataFrame OR pd.Series
        the target variable

    K : int
        number of folds, defualts to 5 (80-20 data split)

    **kwargs:
        kwargs for model.fit keras


    Return:
    -------

    scores : list[*float]
        list containing evaluation scores for the model

    histories : not sure of exact outout
    """
    scores = []
    histories = []
    for train, test in KFold(n_splits=K, shuffle=True).split(X,y):
        model = nn(X, y)
        start = time()
        histories.append(model.fit(X[train], y[train],
                                   validation_data = (X[test],y[test]),
                                   **kwargs).history)
        print(time() - start)
        scores.append(model.evaluate(X[test], y[test], verbose = 0))
    print("average loss: ", np.asarray(scores)[:,0].mean())
    print("average accuracy: ", np.asarray(scores)[:,1].mean()) # make sure that accuracy is the first metric in compile
    print(model.summary())
    return scores, histories

def plot_histories(histories, metrics = ['loss', 'accuracy', 'val_accuracy','val_loss']):
    """
    function to plot the histories of a neural network model

    histories :

    metrics : [str, str, str, str]
        metrics to plot

    Returns:
    --------
    None
    """
    fig, axes = plt.subplots(nrows = (len(metrics) - 1) // 2 + 1, ncols = 2, figsize = (16,16))
    axes = axes.reshape((len(metrics) - 1) // 2 + 1, 2)
    for i,metric in enumerate(metrics):
        for history in histories:
            axes[(i+2)//2 - 1, 1 - (i+1)%2].plot(history[metric])
            axes[(i+2)//2 - 1, 1 - (i+1)%2].legend([i for i in range(len(histories))])


            #axes[(i+2)//2 - 1, 1 - (i+1)%2].axhline(y=max(history[metric]))
            axes[(i+2)//2 - 1, 1 - (i+1)%2].set_xticks(
                np.arange(max(history[metric]))
            )