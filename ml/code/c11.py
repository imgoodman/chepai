import pickle
import os

data_folder=os.path.join("D:/python/ml-20m/ml-20m/cifar-10-python","cifar-10-batches-py")

def unpickle(filename):
    fullpath=os.path.join(data_folder,filename)
    with open(fullpath,'rb') as inf:
        return pickle.load(inf, encoding="latin1")


if __name__=="__main__":
    batch1 = unpickle("data_batch_1")
    print(batch1)