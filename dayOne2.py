import re
from word2number import w2n

def process_line(line):
    
    numbers = re.findall(r'\b(?:zero|one|two|three|four|five|six|seven|eight|nine)\b', line)

    first_element = numbers[0]

    if first_element.isalpha():
         # It's a word representing a numeric value
        numeric_value = w2n.word_to_num(first_element)
        print(f"The first element '{first_element}' is a word representing the numeric value {numeric_value}.")
    elif first_element.isdigit():
    # It's a numeric digit
        numeric_value = int(first_element)
        print(f"The first element '{first_element}' is a numeric digit with the value {numeric_value}.")
    else:
    # It's neither a word nor a numeric digit
        print(f"The first element '{first_element}' is neither a word nor a numeric digit.")



def process_line(line):
    first_digit = next(char for char in line if char.isdigit())
    last_digit = next(char for char in reversed(line) if char.isdigit())

    two_digit_number = int(first_digit + last_digit)
    
    return two_digit_number

def main():

    with open('input.txt', 'r') as file:
            total_sum = 0

            for line in file:
             line = line.strip() 
             result = process_line(line)

             total_sum += result

            print("Total sum", total_sum)
            #print("numeric values", extract_numbers)
if __name__ == "__main__":
    main()

