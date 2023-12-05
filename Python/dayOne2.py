import re
from word2number import w2n

def extract_first_and_last(line):
    # Use regular expression to find all numeric values and digits in the line
    numbers = re.findall(r'\b(?:zero|one|two|three|four|five|six|seven|eight|nine|[0-9])+\b', line)

    # Check if there are any numeric values in the line
    if numbers:
        # Find the first and last numeric values or digits
        first_element = numbers[0]
        last_element = numbers[-1]

        # Extract only the leading numeric part from the elements
        first_element_numeric = re.search(r'(?:zero|one|two|three|four|five|six|seven|eight|nine|[0-9])+', first_element).group()
        last_element_numeric = re.search(r'(?:zero|one|two|three|four|five|six|seven|eight|nine|[0-9])+', last_element).group()

        # Convert the numeric parts to integers
        first_value = w2n.word_to_num(first_element_numeric) if first_element.isalpha() else int(re.search(r'[0-9]+', first_element_numeric).group())
        last_value = w2n.word_to_num(last_element_numeric) if last_element.isalpha() else int(re.search(r'[0-9]+', last_element_numeric).group())

        return first_value, last_value

    return None, None

def main():
    # Open the input file for reading
    with open('input.txt', 'r') as file:
        # Initialize a variable to store the sum of first and last values
        total_sum = 0

        # Read each line and process it
        for line in file:
            line = line.strip()  # Remove leading and trailing whitespaces
            first_value, last_value = extract_first_and_last(line)

            # Check if both first and last values are found
            if first_value is not None and last_value is not None:
                # Combine the values and add to the total sum
                combined_value = first_value + last_value
                total_sum += combined_value

                # Print the results for each line
                print(f"Line: {line}, First: {first_value}, Last: {last_value}, Combined: {combined_value}")

        # Print the total sum of combined values
        print("Total Sum:", total_sum)

if __name__ == "__main__":
    main()
