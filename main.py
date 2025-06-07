import torch

words = torch.tensor([[1,2,3],[4,5,6],[7,8,9],[10,11,12],[11,22,33],[44,55,66],[12,33,12]])

idx = torch.tensor([[0,4],[1,2]])

word = torch.gather(words,dim=0,index=idx)

print(word)
print(word.shape)


