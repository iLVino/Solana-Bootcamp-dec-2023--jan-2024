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
if __name__ == "__main__":
    main()