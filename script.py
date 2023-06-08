import torch

data_0 = [3.2, 4.4, -3.2, 0.4]

data_1 = [3.1, 6.4, -8.2, 10.4]

x = torch.tensor([data_0, data_1])

print(x[1][3])
