import sys
import pickle

def split_file(file_path, block_size):
    # Splits the file into blocks
    
    with open(file_path, 'rb') as file:
        data = file.read()

    data = data.replace(b' ', b'')

    blocks = [data[i * block_size: (i + 1) * block_size] for i in range(len(data) // block_size + 1)]

    # Remove empty blocks
    blocks = [block for block in blocks if block]

    unique_blocks = {}
    order_arr = []

    # Writing the non-duplicate blocks to a file
    with open('non_duplicate_blocks.bin', 'wb') as output_file:
        for block in blocks:
            if block not in unique_blocks:
                prev_key = len(unique_blocks) + 1
                unique_blocks[block] = prev_key
            order_arr.append(unique_blocks[block])
            output_file.write(block)
                                       
    # Minimum disk space 
    minimum_disk_space = len(unique_blocks) * block_size

    return minimum_disk_space, unique_blocks, order_arr


file_path = sys.argv[1]
block_size = int(sys.argv[2])
minimum_space, unique_blocks, order_arr = split_file(file_path, block_size)
print(f"File split into blocks and non-duplicate blocks stored in 'non_duplicate_blocks.bin'.")
print(f"Minimum disk space required: {minimum_space} bytes.")

for block, value in unique_blocks.items():
    print(f"Block: {block}  Value: {value}")
    
with open('metadata2.pickle', 'wb') as pickle_file:
        pickle.dump(unique_blocks, pickle_file)
        pickle.dump(order_arr,pickle_file) 
        

