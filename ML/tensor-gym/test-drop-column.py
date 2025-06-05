import unittest
import torch
from drop_col_most_zeros import drop_column  # Replace 'your_module' with the module containing your function

class TestDropColumn(unittest.TestCase):
    """Test cases for the drop_column function.
    
    The drop_column function removes the column with the most zeros from a tensor.
    These tests assume that there will always be one column with strictly more zeros 
    than any other column (no ties) or there will be no zeros at all.
    """
    
    def test_basic_functionality(self):
        """Test that the function correctly drops the column with the most zeros."""
        # Column 1 has the most zeros (3)
        tensor = torch.tensor([[1, 0, 3], 
                              [4, 0, 6], 
                              [7, 0, 9]])
        expected = torch.tensor([[1, 3], 
                                [4, 6], 
                                [7, 9]])
        result = drop_column(tensor)
        self.assertTrue(torch.equal(result, expected))
    
    def test_clear_max_zeros(self):
        """Test where one column clearly has more zeros than the others."""
        # Column 1 has 3 zeros, more than any other column
        tensor = torch.tensor([[1, 0, 3], 
                              [4, 0, 6], 
                              [7, 0, 9]])
        expected = torch.tensor([[1, 3], 
                                [4, 6], 
                                [7, 9]])
        result = drop_column(tensor)
        self.assertTrue(torch.equal(result, expected))
    
    def test_uneven_zeros(self):
        """Test with an all-zero tensor but with uneven column sizes."""
        # Create a tensor where all elements are zeros, but columns have different sizes
        tensor = torch.zeros((3, 4))
        # Add a non-zero value to the last column to ensure it's not the one with most zeros
        tensor[0, 3] = 1
        
        # We expect the result to have the first 3 columns dropped (since one has max zeros)
        # and only the last column (which has one non-zero value) to remain
        expected = torch.tensor([[1], [0], [0]])
        
        result = drop_column(tensor)
        
        # Shape should be (3, 3) - one column dropped
        self.assertEqual(result.shape, (3, 3))
    
    
    def test_non_2d_tensor(self):
        """Test with a non-2D tensor - should raise an error."""
        tensor = torch.tensor([1, 2, 3])
        with self.assertRaises(ValueError):
            drop_column(tensor)
    
    def test_float_values(self):
        """Test with a tensor containing float values (including exact zeros)."""
        tensor = torch.tensor([[1.1, 0.0, 3.3], 
                              [4.4, 0.0, 6.6], 
                              [0.0, 7.7, 9.9]])
        # Column 1 has the most zeros (2)
        expected = torch.tensor([[1.1, 3.3], 
                                [4.4, 6.6], 
                                [0.0, 9.9]])
        result = drop_column(tensor)
        self.assertTrue(torch.equal(result, expected))
    
    def test_different_dtypes(self):
        """Test with tensors of different dtypes."""
        tensor = torch.tensor([[1, 0, 3], 
                              [0, 5, 0], 
                              [7, 0, 9]], dtype=torch.int64)
        result = drop_column(tensor)
        self.assertEqual(result.dtype, tensor.dtype)
        
        tensor = torch.tensor([[1.0, 0.0, 3.0], 
                              [0.0, 5.0, 0.0], 
                              [7.0, 0.0, 9.0]], dtype=torch.float32)
        result = drop_column(tensor)
        self.assertEqual(result.dtype, tensor.dtype)
    
    def test_large_tensor(self):
        """Test with a larger tensor with a clear column to drop."""
        n, m = 100, 50
        tensor = torch.ones((n, m))
        
        # Make one column have more zeros than any other
        zero_col = m // 2
        # Make 60% of values in this column zero
        zero_indices = torch.randperm(n)[:int(n * 0.6)]
        tensor[zero_indices, zero_col] = 0
        
        # Make other columns have fewer zeros
        for col in range(m):
            if col != zero_col:
                # Make at most 30% of values zero in other columns
                num_zeros = torch.randint(0, int(n * 0.3), (1,)).item()
                if num_zeros > 0:
                    indices = torch.randperm(n)[:num_zeros]
                    tensor[indices, col] = 0
        
        result = drop_column(tensor)
        
        # Verify one column was dropped
        self.assertEqual(result.shape, (n, m-1))
        
        # Verify the column with most zeros was dropped by checking
        # that the percentage of zeros in the result is less than in the input
        input_zero_pct = torch.sum(tensor == 0).item() / tensor.numel()
        result_zero_pct = torch.sum(result == 0).item() / result.numel()
        
        self.assertLess(result_zero_pct, input_zero_pct)
        
    def test_device_preservation(self):
        """Test that the function preserves the device of the input tensor."""
        if torch.cuda.is_available():
            tensor = torch.tensor([[1, 0, 3], 
                                  [4, 0, 6], 
                                  [7, 0, 9]]).cuda()
            result = drop_column(tensor)
            self.assertEqual(result.device, tensor.device)

if __name__ == '__main__':
    unittest.main()
