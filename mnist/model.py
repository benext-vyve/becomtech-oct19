import pickle 
from sklearn.externals import joblib

class Model:
    def __init__(self):
        try:
            self.model = joblib.load("mnist_digits_clf.pkl")
        except:
            raise(TypeError)

    def predict(self, image):
        if image.shape[1] == 784:
            return self.model.predict(image)
        else:
            raise(ValueError)
    
