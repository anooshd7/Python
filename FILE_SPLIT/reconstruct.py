import pickle

def reconstruct_file(input_file, output_file):
    
    # Accessing Dictionary and Order Array
    with open(input_file, 'rb') as pickle_file:
        unique_blocks = pickle.load(pickle_file)
        order_arr=pickle.load(pickle_file)
      
    # Reconstructing original file
    output=[]    
    for i in range(len(order_arr)):
        for key,value in unique_blocks.items():
            if value == order_arr[i]:
                output.extend([key])
                
    data = b''.join(output)
                
    '''
    # Removing padding
    with open('padding.txt', 'r') as file:
        n = file.read()
        a=int(n)
    if a > 0:
        data = data[:-a]
    '''

    # Write to output file
    with open(output_file, 'wb') as file:
        file.write(data)


input_file = 'metadata.pickle'
output_file = 'reconstructed_file.bin'
reconstruct_file(input_file, output_file)
print(f"File reconstructed and saved as: {output_file}")
