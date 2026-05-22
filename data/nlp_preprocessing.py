import torch
import torch.nn as nn
from torchtyping import TensorType

# torch.tensor(python_list) returns a Python list as a tensor
class Solution:
    def get_dataset(self, positive: List[str], negative: List[str]) -> TensorType[float]:
        
        words_col = set()

        for sentence in positive+negative:
            for word in sentence.split():
                words_col.add(word)
        words_col = sorted(list(words_col))
        
        words_dic = {}

        for i, word in enumerate(words_col):
            words_dic[word] = i+1
        tensors = []
        for sentence in positive+negative:
            curr_list=[]
            for word in sentence.split():
                curr_list.append(words_dic[word])
            tensors.append(torch.tensor(curr_list))
        print(tensors)
        return nn.utils.rnn.pad_sequence(tensors, batch_first = True)

