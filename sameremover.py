def remove_duplicate_mobile_numbers(input_file, output_file):
    try:
        with open(input_file, 'r') as f:
            numbers = f.read().splitlines()

        # Remove duplicates while preserving order
        seen = set()
        unique_numbers = []
        for number in numbers:
            cleaned = number.strip()
            if cleaned and cleaned not in seen:
                seen.add(cleaned)
                unique_numbers.append(cleaned)

        # Write unique numbers to output file
        with open(output_file, 'w') as f:
            for number in unique_numbers:
                number = '92' + number[1:]
                print(f"Processing number: {number}")
                f.write(number +","+'\n')

        print(f"Duplicates removed. Output saved to: {output_file}")

    except Exception as e:
        print("Error:", e)

# Example usage
remove_duplicate_mobile_numbers('number.txt', 'unique_mobile_numbers.txt')
input("goodbye")
