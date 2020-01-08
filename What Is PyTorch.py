from __future__ import print_function
import torch
import numpy as np

# x = torch.empty(5, 3)
# print(x)

# x = torch.rand(5, 3)
# print(x)

# x = torch.zeros(5, 3, dtype=torch.long)
# print(x)

# x = torch.tensor([5.5, 3])
# print(x)

# x = x.new_ones(5, 3, dtype=torch.double)
# print(x)

# x = torch.randn_like(x, dtype=torch.float)
# print(x)

# print(x.size())

# y = torch.rand(5, 3)

# # print(x + y)

# result = torch.empty(5, 3)

# torch.add(x, y, out=result)
# print(result)

# print(result[:, 1])

#a = result.numpy()

# print(a)

a = np.ones(5)
b = torch.from_numpy(a)
np.add(a, 1, out=a)
print(a)
print(b)

print(torch.cuda.is_available())