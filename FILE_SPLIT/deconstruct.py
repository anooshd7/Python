import sys
import pickle

def split_file(file_path, block_size):
    # Splits the file into blocks
    
    with open(file_path, 'rb') as file:
        data = file.read()

    data = data.replace(b' ', b'')

    # Number of blocks
    num_blocks = len(data) // block_size

    #Padding last block
    '''
    if remaining_bytes > 0:
        n=block_size-remaining_bytes
        padding = ''.join(random.choices(string.ascii_letters, k=block_size-remaining_bytes))
        data += padding.encode()
        file = open("padding.txt", "w")
        file.write(str(n))
        file.close()
    ''' 
    
    # Dictionary to store the unique blocks and their reference numbers
    unique_blocks = {}  

    # Writing the non-duplicate blocks to a file
    with open('non_duplicate_blocks.bin', 'wb') as output_file:
        
        order_arr=[]   # Store sequence of blocks
        
        for i in range(num_blocks + 1):
            block = data[i * block_size: (i + 1) * block_size]
            
            if block:  # Make sure block is not empty
            
                    if block not in unique_blocks:
                        value = len(unique_blocks) + 1                   
                        unique_blocks[block] = value
                        output_file.write(block)
                        
                    # Append the reference numbers to the array
                    order_arr.append(unique_blocks.get(block))
        print(order_arr)
                                       
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
    
with open('metadata.pickle', 'wb') as pickle_file:
        pickle.dump(unique_blocks, pickle_file)
        pickle.dump(order_arr,pickle_file) 
        

