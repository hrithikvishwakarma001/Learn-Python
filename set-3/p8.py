# File I/O: Write a Python program that reads a file, counts the number of words, and writes the count to a new file.
# Input: A text file named "input.txt" with the content "Hello world"
# Output: A text file named "output.txt" with the content "Number of words: 2"

def count_words(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
        words = content.split()
        return len(words)

def write_word_count(file_path, count):
    with open(file_path, 'w') as file:
        file.write(f"Number of words: {count}")


input_file = "input.txt"
output_file = "output.txt"

word_count = count_words(input_file)
write_word_count(output_file, word_count)

print(f"Number of words in the input file: {word_count}")
print(f"Word count has been written to {output_file}")
