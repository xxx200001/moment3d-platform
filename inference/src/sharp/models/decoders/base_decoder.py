"""Contains the base class for decoders.

For licensing see accompanying LICENSE file.
Copyright (c) 2025 Moment3D Contributors.
"""

import abc
from typing import List

import torch
from torch import nn


class BaseDecoder(nn.Module, abc.ABC):
    """Base decoder class."""

    dim_out: int

    @abc.abstractmethod
    def forward(self, encodings: List[torch.Tensor]) -> torch.Tensor:
        """Decode (multi-resolution) encodings."""
