# import os
# import pickle


# def reconstruct_file(input_file, output_file, block_size):
#     # Read the unique_blocks dictionary from the pickle file
#     with open(input_file, 'rb') as pickle_file:
#         unique_blocks = pickle.load(pickle_file)

#     # Create a list of all unique blocks based on their counts
#     blocks_list = []
#     for block, count in unique_blocks.items():
#         blocks_list.extend([block] * count)

#     # Concatenate all blocks to reconstruct the original data
#     data = b''.join(blocks_list)

#     # Remove any padding from the last block, if present
#     remaining_bytes = len(data) % block_size
#     if remaining_bytes > 0:
#         data = data[:-remaining_bytes]

#     # Write the reconstructed file
#     with open(output_file, 'wb') as file:
#         file.write(data)


# # Example usage
# input_file = 'unique_blocks.pickle'
# output_file = 'reconstructed_file.bin'
# block_size = 3
# reconstruct_file(input_file, output_file, block_size)
# print(f"File reconstructed from non-duplicate blocks. Saved as: {output_file}")


import os
import pickle


def reconstruct_file(input_file, output_file):
    # Read the unique blocks from the input file
    with open(input_file, 'rb') as file:
        unique_blocks = file.read()

    # Write the reconstructed file
    with open(output_file, 'wb') as file:
        file.write(unique_blocks)
    
    with open('padding.txt', 'r') as file:
        n = file.read()
        a=int(n)
    # Remove any padding from the last block, if present
    print(type(unique_blocks))
    print(type(a))
    if a > 0:
        unique_blocks = unique_blocks[:-a]
      
   

# Example usage
input_file = 'non_duplicate_blocks.bin'
output_file = 'reconstructed_file.bin'
reconstruct_file(input_file, output_file)
print(f"File reconstructed from non-duplicate blocks. Saved as: {output_file}")
