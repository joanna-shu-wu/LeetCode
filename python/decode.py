def decode(message_file):
    with open(message_file, 'r') as file:
        lines = file.readlines()

    # Extract numbers from each line and create a pyramid
    pyramid = [list(map(int, line.split()[1:])) for line in lines if line.split()[1].isdigit()]
    max_number = max(pyramid[-1])

    # Ensure that the max_number is not greater than the total number of lines
    max_number = min(max_number, len(lines))

    # Extract words based on the pyramid structure
    decoded_words = []
    for line in pyramid:
        for number in line:
            if number <= max_number:
                decoded_words.append(lines[number - 1].split()[1])

    # Create a space-separated string from the extracted words
    decoded_message = ' '.join(decoded_words)
    
    return decoded_message

message_file = '/Users/shuhsienwu/Documents/GitHub/LeetCode/python/message_file.txt'
decoded_message = decode(message_file)
print(decoded_message)