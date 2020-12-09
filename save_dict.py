# pickle module will make this easier
# pickling could also be used to transfer objects across a network
import pickle

def save_dictionary(myDict, filepath):
    """ Function should save a dictionary to a file """
    # context manager write binary
    with open(filepath, 'wb') as file:
        # pickle save
        pickle.dump(myDict, file)
    
def load_dictionary(filepath):
    """ Function should load a dictionary from a file """
    # context manager read binary
    with open(filepath, 'rb') as file:
        # pickle load
        return pickle.load(file)

d = {1:'a', 2:'b', 3:'c'}
save_dictionary(d, "tmp.pickle")
print(load_dictionary("tmp.pickle"))
