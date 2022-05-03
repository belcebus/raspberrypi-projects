from my_libraries import binary_operations as bo

def test_binary_0():
   assert bo.num_to_binary(0) == "0"
   assert bo.num_to_binary(1) == "1"
   assert bo.num_to_binary(2) == "10"
   assert bo.num_to_binary(3) == "11"
   assert bo.num_to_binary(-1) == ""
   assert bo.num_to_binary(-2) == ""
