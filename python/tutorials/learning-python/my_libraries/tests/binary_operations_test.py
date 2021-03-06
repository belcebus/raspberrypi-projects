from ..binary_operations import num_to_binary

def test_binary_0():
   assert num_to_binary(0) == "0"
   assert num_to_binary(1) == "1"
   assert num_to_binary(2) == "10"
   assert num_to_binary(3) == "11"
   assert num_to_binary(4) == "100"
   assert num_to_binary(5) == "101"
   assert num_to_binary(6) == "110"
   assert num_to_binary(-1) == ""
   assert num_to_binary(-2) == ""
