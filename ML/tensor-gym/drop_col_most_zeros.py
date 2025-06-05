import torch

def drop_column(A: torch.tensor) -> torch.tensor:
    """
    Drops the column of A containing the most 0 values.

    Parameters:
        tensor: A 2D tensor.
    Returns:
        tensor: The input tensor with the column containing the most 0 values removed.
    """

    result = None
    ### your code here ###
    num_cols = A.shape[1]
    mask = torch.arange(num_cols)

    zero_check = A == 0
    zero_count_col = zero_check.sum(dim=0)
    max_zero_col = zero_count_col.argmax()
    mask = mask != max_zero_col
    
    result = A[:, mask]
    return result

if __name__ == '__main__':
    A = torch.tensor([[0, 1, 2], [0, 0, 1]])
    print(A)
    ans = drop_column(A)
    print(ans)
