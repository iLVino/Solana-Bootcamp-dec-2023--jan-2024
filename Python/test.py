import re
from word2number import w2n

def extract_first_and_last(line):
    # Find all numeric values, whether they are written as words or digits
    numbers = re.findall(r'(zero|one|two|three|four|five|six|seven|eight|nine|\d)', line)

    if numbers:
        first_element = numbers[0]
        last_element = numbers[-1]

        # Take only the first digit for the first numeric value
        first_numeric_value = w2n.word_to_num(first_element) if first_element.isalpha() else int(re.search(r'[0-9]+', first_element).group())
        first_numeric_value_str = str(first_numeric_value)

        # Take only the last digit for the last numeric value
        last_numeric_value = w2n.word_to_num(last_element) if last_element.isalpha() else int(re.search(r'[0-9]+', last_element).group())
        last_numeric_value_str = str(last_numeric_value)

        concatenated_digits = int(first_numeric_value_str + last_numeric_value_str)

        return concatenated_digits, first_numeric_value, last_numeric_value

    return None, None


def main():
    with open("input.txt", 'r') as file:

        total_sum = 0       

        for line in file:
            concatenated_digits, first_numeric_value, last_numeric_value = extract_first_and_last(line)
             
            total_sum += concatenated_digits
             
            print(f"Line: {line}, First: {first_numeric_value}, Last: {last_numeric_value}, Concatenated: {concatenated_digits}")

        print("Total Sum:", total_sum)

if __name__ == "__main__":
    main()
 