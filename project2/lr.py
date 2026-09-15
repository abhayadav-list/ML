class LogisticRegression:
    def _init__(self,n=1000,y_pred):
        self.







class LinearRegression:
    def __init__(self,n=1000,lr=0.001):
        self.weights=None
        self.bias=None
        self.lr=lr
        self.n=n

    def fit(self,X_train,y_train):
        n_samples,n_features=X_train.shape()
        self.weights = np.zeros(n_features)
        self.bias=0

        for _ in range(n):
            y_pred=np.dot(X_train,self.weights)+self.bias

            dw=(1/n_samples)*np.dot(X_train.T,(y_pred-y_train))
            db=(1/n_samples)*np.sum((y_pred-y_train))

            self.weights=self.weights-lr*dw
            self.bias=self.bias-lr*db

    def pridict(X_Test):
        return (np.dot(X_Test,self.weights)+self.bias)



lin_reg=LinearRegression()
lin_reg.fit(X_train,y_train)
prediction=lin_reg.pridict(X_Test)

def mse(prediction,y_test):
    return np.mean((prediction-y_test)**2)
