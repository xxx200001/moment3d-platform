"""Utility functions for training.

For licensing see accompanying LICENSE file.
Copyright (c) 2025 Moment3D Contributors.
"""

from torch.utils.checkpoint import checkpoint


def checkpoint_wrapper(self, fn, *args):
    """Helper function that applies checkpointing.

    If enabled applies grad checkpointing, otherwise just executes the function normally.
    """
    if not hasattr(self, "grad_checkpointing"):
        raise AttributeError(
            "Trying to apply grad checkpointing on a model that does not have a grad_checkpointing "
            "attribute."
        )

    if self.grad_checkpointing:
        return checkpoint(fn, *args, use_reentrant=False)
    else:
        return fn(*args)
