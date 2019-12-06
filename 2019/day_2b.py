def get_chunks(l, n):
    for i in range(0, len(l), n):
        yield l[i:i+n]

def run(input):
	chunk_size = 4
	for noun in range(0, 99):
		for verb in range(0, 99):
			data = input[:]
			data[1] = noun
			data[2] = verb			
			chunks = list( get_chunks(data, chunk_size) )

			for chunk in chunks:
				opcode = chunk[0]

			 	if opcode == 1 or opcode == 2:
			 		value_1 = data[chunk[1]]
			 		value_2 = data[chunk[2]]
			 		storage_index = chunk[3]

			 		if opcode == 1:
			 			data[storage_index] = value_1 + value_2
			 		else:
			 			data[storage_index] = value_1 * value_2
			 	elif opcode == 99 and data[0] == 19690720:
		 			return 100 * noun + verb


input = [1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,13,1,19,1,19,9,23,1,5,23,27,1,27,9,31,1,6,31,35,2,35,9,39,1,39,6,43,2,9,43,47,1,47,6,51,2,51,9,55,1,5,55,59,2,59,6,63,1,9,63,67,1,67,10,71,1,71,13,75,2,13,75,79,1,6,79,83,2,9,83,87,1,87,6,91,2,10,91,95,2,13,95,99,1,9,99,103,1,5,103,107,2,9,107,111,1,111,5,115,1,115,5,119,1,10,119,123,1,13,123,127,1,2,127,131,1,131,13,0,99,2,14,0,0]
input[1] = 12
input[2] = 2

print run(input)