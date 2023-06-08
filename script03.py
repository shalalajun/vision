from einops import rearrange

import torch

x = torch.randn(2,4)

y = rearrange(x, "group element -> element group")

print(x[1][2] == y[2][1])



