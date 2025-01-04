print("Hello world")
import torch
from torch import Tensor
a = Tensor([0])
print(a.device)
a = a.cuda()
print(a.device)
print(a+1)