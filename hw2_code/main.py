from torch import nn
import torch
model = nn.Linear(2,1)

input = torch.Tensor([1,2])
output = model(input)
print(output)
for param in model.parameters():
    print(param)