from einops import rearrange

import torch

x = torch.rand(3, 2, 4)

y = rearrange(x, "metagroup group element -> (metagroup group element)")

y = x.view(6,4)

print(x[1][1][2] == y[1][6]) 