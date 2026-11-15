def mask_card_number(number):
    """
    Hides all but the last four digits of a card number.
    Assumes number is a non-empty string.
    """
    if not isinstance(number, str):
        return None
    digits = number.replace(' ', '').replace('-', '')
    if len(digits) < 4 or not digits.isdigit():
        return None
    return '*' * 12 + digits[-4:]

def parse_transaction(line):
    """
    Parses 'date,category,amount' into a (category, amount) tuple.
    Assumes all three fields are present and amount is a whole number.
    """
    if not isinstance(line, str):
        return None
    parts = line.split(',')
    if len(parts) != 3:
        return None
    try:
        amount = int(parts[2])
    except ValueError:
        return None
    return parts[1].strip().lower(), amount

def parse_statement_total(text):
    """
    Reads the amount from a line such as 'Total: 12,500'.
    Assumes the line has a colon followed by a number.
    """
    if not isinstance(text, str):
        return None
    parts = text.split(':')
    if len(parts) != 2:
        return None
    try:
        return int(parts[1].replace(',', ''))
    except ValueError:
        return None

def main():
    print("==== Running mask_card_number ====")
    value = input("Enter a card number (e.g. 4111 1111 1111 1234): ")
    print("Masked card number:", mask_card_number(value))

    print("\n==== Running parse_transaction ====")
    value = input("Enter a transaction as DATE,CATEGORY,AMOUNT (e.g. 2026-11-05,dining,1550): ")
    print("Category and amount:", parse_transaction(value))

    print("\n==== Running parse_statement_total ====")
    value = input("Enter the statement total line (e.g. Total: 12,500): ")
    print("Statement total:", parse_statement_total(value))

if __name__ == "__main__":
    main()
