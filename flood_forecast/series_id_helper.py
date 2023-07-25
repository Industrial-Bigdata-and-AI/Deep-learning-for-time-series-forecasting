import torch
from typing import Dict, List


def handle_csv_id_output(src: Dict[int, torch.Tensor], trg: Dict[int, torch.Tensor], model, criterion, opt,
                         random_sample: bool = False, n_targs: int = 1):
    """A helper function to better handle the output of models with a series_id and compute loss,

    :param src: A dictionary of src sequences (partitioned by series_id)
    :type src: torch.Tensor
    :param trg: A dictionary of target sequences (key as series_id)
    :type trg: torch.Tensor
    :param model: A model that takes both a src and a series_id
    :type model: torch.nn.Module
    """
    total_loss = 0.00
    for (k, v), (k2, v2) in zip(src.items(), trg.items()):
        print("Shape of v below")
        print(v.shape)
        output = model.model(v, k)
        loss = criterion(output, v2[:, :, :n_targs])
        total_loss += loss.item()
        loss.backward()
        opt.step()
    total_loss /= len(src.keys())
    return total_loss


def handle_csv_id_validation(src: Dict[int, torch.Tensor], trg: Dict[int, torch.Tensor], model: torch.nn.Module,
                             criterion: List, random_sample: bool = False, n_targs: int = 1, max_seq_len: int = 100):
    """"""
    losses = [0] * len(criterion)
    for (k, v), (k2, v2) in zip(src.items(), trg.items()):
        output = model(v, k)
        for critt in criterion:
            loss = critt(output, v2[:, :, :n_targs])
            losses[criterion.index(critt)] += loss.item()
    return losses
