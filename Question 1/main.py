from load_data import load_dummy_data
import torch
from time import time
if __name__ == "__main__":
    start_time = time()
    load_dummy_data()
    a = torch.load("a.pt")
    print(a)
    end_time = time()
    print(end_time-start_time)