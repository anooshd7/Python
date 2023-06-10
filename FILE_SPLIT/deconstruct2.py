""" 
Input : <file> block_size

1. Read file contents
2. Iterate through contents based on block size
3. Find number of non-duplicate blocks
4. Output = number of non-duplicate blocks x block_size 

Load chunks of data, not whole file at once
Append the block size, block contents, etc. to another file as you read the contents of the og file
Use dictionaries
Use padding for last block, and remove padding in reconstruct

Bonus: Program tells you what block size is best/msot efficient

"""

# with open('order_array.pickle','wb') as pickle_file2:
#         pickle.dump(order_arr,pickle_file2)

# # Order Array    
    # with open(input_file2, 'rb') as pickle_file2:
    #     order_arr = pickle.load(pickle_file2)



def split_file(file_path, block_size):
    with open(file_path, 'rb') as file:
        data = file.read()

    data = data.replace(b' ', b'')

    # Generate the blocks using list comprehension
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

minspace,unique,arr = split_file('test.bin',3) 
print(arr)




