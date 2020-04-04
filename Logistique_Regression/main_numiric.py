# imports
# https://towardsdatascience.com/building-a-logistic-regression-in-python-301d27367c24
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from Model import LogisticRegressionUsingGD
from sklearn.metrics import accuracy_score


def load_data(path, header):
    marks_df = pd.read_csv(path, header=header)
    return marks_df


if __name__ == "__main__":
    # load the data from the file
    data = load_data("data/marks.txt", None)

    # X = feature values, all the columns except the last column
    X = data.iloc[:, :-1]

    # y = target values, last column of the data frame
    y = data.iloc[:, -1]

    # filter out the applicants that got admitted
    admitted = data.loc[y == 1]

    # filter out the applicants that din't get admission
    not_admitted = data.loc[y == 0]

    # plots
    plt.scatter(admitted.iloc[:, 0], admitted.iloc[:, 1], s=10, label='Admitted')
    plt.scatter(not_admitted.iloc[:, 0], not_admitted.iloc[:, 1], s=10,
                label='Not Admitted')

    # preparing the data for building the model

    X = np.c_[np.ones((X.shape[0], 1)), X]
    y = y[:, np.newaxis]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

    theta_zero = np.zeros((X.shape[1], 1))
    # RIDGE : alpha = 0.01 | accuracy = 93.33333333333333
    # FSGM :  accuracy = 93.33333333333333
    #       alpha = 0.5 | epsilon = 0.03
    #       alpha = 0.7 | epsilon = 0.4
    alpha = 0.01
    epsilon = 0.4
    ###################################################################"
    type_penalitty = 'RIDGE'
    # Logistic Regression from scratch using Gradient Descent
    model = LogisticRegressionUsingGD(alpha, epsilon)
    model.fit(X_train, y_train, theta_zero, type_penalitty)
    accuracy = model.accuracy(X_test, y_test.flatten())
    parameters = model.w_
    print("The accuracy of the {} model is {}".format(type_penalitty, accuracy))
    print("The model parameters using Gradient descent")
    print("\n")
    print(parameters)
    ###################################################################"
    type_penalitty = 'FSGM'
    # Logistic Regression from scratch using Gradient Descent
    model = LogisticRegressionUsingGD(alpha, epsilon)
    model.fit(X_train, y_train, theta_zero, type_penalitty)
    accuracy = model.accuracy(X_test, y_test.flatten())
    parameters = model.w_
    print("The accuracy of the {} model is {}".format(type_penalitty, accuracy))
    print("The model parameters using Gradient descent")
    print("\n")
    print(parameters)
    ###################################################################"
    type_penalitty = 'Normal'
    # Logistic Regression from scratch using Gradient Descent
    model = LogisticRegressionUsingGD(alpha, epsilon)
    model.fit(X_train, y_train, theta_zero, type_penalitty)
    accuracy = model.accuracy(X_test, y_test.flatten())
    parameters = model.w_
    print("The accuracy of the {} model is {}".format(type_penalitty, accuracy))
    print("The model parameters using Gradient descent")
    print("\n")
    print(parameters)



    x_values = [np.min(X[:, 1] - 2), np.max(X[:, 2] + 2)]
    y_values = - (parameters[0] + np.dot(parameters[1], x_values)) / parameters[2]

    plt.plot(x_values, y_values, label='Decision Boundary')
    plt.xlabel('Marks in 1st Exam')
    plt.ylabel('Marks in 2nd Exam')
    plt.legend()
    plt.show()

    # Using scikit-learn
    '''
    model = LogisticRegression()
    model.fit(X, y)
    parameters = model.coef_
    predicted_classes = model.predict(X)
    accuracy = accuracy_score(y.flatten(),predicted_classes)
    print('The accuracy score using scikit-learn is {}'.format(accuracy))
    print("The model parameters using scikit learn")
    print(parameters)'''