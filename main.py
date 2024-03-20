import os
from shutil import rmtree

# Constant representing the typical index of coincidence for English and Portuguese texts.
ENGLISH_COINCIDENCE_INDEX = 0.066
PORTUGUESE_COINCIDENCE_INDEX = 0.074

# Constant representing the most frequent letters in English and Portuguese texts.
ENGLISH_MOST_FREQUENT_LETTERS = ["e", "t"]
PORTUGUESE_MOST_FREQUENT_LETTERS = ["a", "e"]


# Function to check if the text is likely English based on the frequency of the most frequent letters.
def is_text_english(letters_map: dict[str, int]) -> bool:
    """
    Check if the text is likely to be English based on the frequency of the most frequent letters.

    Args:
        letters_map (dict[str, int]): A dictionary with letters as keys and their frequencies as values.

    Returns:
        bool: True if the text is likely to be English, False otherwise.
    """
    # Calculate the relative frequency of the most frequent and second most frequent letters.
    # Compare these frequencies with typical values for English.
    # If the frequencies are close to typical English values, return True.
    # Otherwise, return False.
    total_letters = sum(letters_map.values())
    sorted_letters_map = sorted(
        letters_map.items(), key=lambda x: x[1], reverse=True)
    most_frequent_letter = sorted_letters_map[0][0]
    second_most_frequent_letter = sorted_letters_map[1][0]

    if abs(letters_map[most_frequent_letter] / total_letters - 0.127) < 0.01 and abs(letters_map[second_most_frequent_letter] / total_letters - 0.0905) < 0.01:
        return True


# Function to check if the text is likely Portuguese based on the frequency of the most frequent letters.
def is_text_portuguese(letters_map: dict[str, int]) -> bool:
    """
    Check if the text is likely to be Portuguese based on the frequency of the most frequent letters.

    Args:
        letters_map (dict[str, int]): A dictionary with letters as keys and their frequencies as values.

    Returns:
        bool: True if the text is likely to be Portuguese, False otherwise.
    """
    # Calculate the relative frequency of the most frequent and second most frequent letters.
    # Compare these frequencies with typical values for Portuguese.
    # If the frequencies are close to typical Portuguese values, return True.
    # Otherwise, return False.
    total_letters = sum(letters_map.values())
    sorted_letters_map = sorted(
        letters_map.items(), key=lambda x: x[1], reverse=True)
    most_frequent_letter = sorted_letters_map[0][0]
    second_most_frequent_letter = sorted_letters_map[1][0]

    if abs(letters_map[most_frequent_letter] / total_letters - 0.1463) < 0.03 and abs(letters_map[second_most_frequent_letter] / total_letters - 0.1257) < 0.03:
        return True


# Function to pretty print a list of floats.
def pretty_print_float_array(array: list[float]) -> str:
    """
    Pretty print a list of floats.

    Args:
        array (list[float]): The list of floats.

    Returns:
        str: The pretty printed list of floats.
    """
    # Convert each float in the array to a string with 4 decimal places,
    # then join them with commas and enclose in square brackets.
    return "[" + ", ".join([f"{x:.4f}" for x in array]) + "]"


# Function to generate a dictionary mapping each letter to its frequency in the encrypted text.
def get_letters_map(encrypted_text: str) -> dict[str, int]:
    """
    Generate a dictionary mapping each letter to its frequency in the encrypted text.

    Args:
        encrypted_text (str): The encrypted text.

    Returns:
        dict[str, int]: A dictionary with letters as keys and their frequencies as values.
    """
    # Count the occurrences of each letter in the encrypted text
    # and store them in a dictionary.
    letters_map = {}
    for letter in encrypted_text:
        if letter in letters_map:
            letters_map[letter] += 1
        else:
            letters_map[letter] = 1
    return letters_map


# Function to calculate the index of coincidence of the text.
def calculate_coincidence_index(letters_map: dict[str, int]) -> float:
    """
    Calculate the index of coincidence of the text.

    Args:
        letters_map (dict[str, int]): A dictionary with letters as keys and their frequencies as values.

    Returns:
        float: The index of coincidence.
    """
    # Calculate the index of coincidence based on the frequencies of letters in the text.
    coincidence_index = 0
    total_letters = sum(letters_map.values())
    for letter in letters_map:
        letter_frequency = letters_map[letter]
        coincidence_index += (letter_frequency * (letter_frequency - 1)
                              ) / (total_letters * (total_letters - 1))
    return coincidence_index


# Function to divide the encrypted text into N parts.
def divide_text(encrypted_text: str, number_of_parts: int) -> list[str]:
    """
    Divide the encrypted text into N parts.

    Args:
        encrypted_text (str): The encrypted text.
        number_of_parts (int): The number of parts to divide the text into.

    Returns:
        list[str]: A list containing the divided parts of the text.
    """
    # Divide the text into N parts by taking every Nth character.
    divided_text = []
    for i in range(number_of_parts):
        divided_text.append(encrypted_text[i::number_of_parts])
    return divided_text


# Function to join the divided text back into a single text.
def join_text(divided_text: list[str], number_of_parts: int) -> str:
    """
    Join the divided text back into a single text.

    Args:
        divided_text (list[str]): A list containing the divided parts of the text.
        number_of_parts (int): The number of parts to divide the text into.

    Returns:
        str: The joined text.
    """
    # Reconstruct the original text by taking characters from each part in order.
    joined_text = ""
    for i in range(len(divided_text[0])):
        for j in range(number_of_parts):
            if i < len(divided_text[j]):
                joined_text += divided_text[j][i]
    return joined_text


# Function to check if all coincidence indexes match the target index.
def coincidence_indexes_match(coincidence_indexes: list[float], target_index: float) -> bool:
    """
    Check if all coincidence indexes match the target index.

    Args:
        coincidence_indexes (list[float]): A list of coincidence indexes.
        target_index (float): The target coincidence index.

    Returns:
        bool: True if all coincidence indexes are close to the target index, False otherwise.
    """
    # Check if all coincidence indexes are within a threshold of the target index.
    for index in coincidence_indexes:
        if abs(index - target_index) > 0.1:
                        return False
    return True


# Function to get the position of a letter in the alphabet.
def position_in_alphabet(letter: str) -> int:
    """
    Get the position of a letter in the alphabet.

    Args:
        letter (str): The letter.

    Returns:
        int: The position of the letter in the alphabet.
    """
    # Calculate the position of a letter in the alphabet based on its Unicode value.
    return ord(letter) - ord("a") + 1


# Function to get the letter at a given position in the alphabet.
def letter_in_alphabet(position: int) -> str:
    """
    Get the letter at a given position in the alphabet.

    Args:
        position (int): The position of the letter in the alphabet.

    Returns:
        str: The letter at the given position in the alphabet.
    """
    # Calculate the letter at a given position in the alphabet based on Unicode values.
    return chr(position + ord("a") - 1)


# Function to calculate the shift needed to go from start_letter to end_letter.
def calculate_shift(start_letter: str, end_letter: str) -> int:
    """
    Calculate the shift needed to go from start_letter to end_letter.

    Args:
        start_letter (str): The start letter.
        end_letter (str): The end letter.

    Returns:
        int: The shift needed to go from start_letter to end_letter.
    """
    # Calculate the shift needed to transform one letter into another, considering the circular nature of the alphabet.
    position_1 = position_in_alphabet(start_letter)
    position_2 = position_in_alphabet(end_letter)
    if position_2 >= position_1:
        return position_2 - position_1 + 1
    return 26 - position_1 + position_2 + 1


# Function to generate all possible combinations of characters by choosing letters from either string.
def string_combinations(str1: str, str2: str) -> list:
    """
    Generate all possible combinations of characters by choosing letters from either string.

    Args:
        str1 (str): The first string.
        str2 (str): The second string.

    Returns:
        list: A list of all possible combinations of characters.
    """
    def generate_combinations(str1: str, str2: str, index: int, current: list):
        if index == len(str1):
            combinations.append(''.join(current))
            return
        generate_combinations(str1, str2, index + 1, current + [str1[index]])
        generate_combinations(str1, str2, index + 1, current + [str2[index]])

    combinations = []
    generate_combinations(str1, str2, 0, [])
    return combinations


# Main function.
def main():
    file_path = "encrypted/" + input("Enter the name of the encrypted text file (inside the 'encrypted' folder): ")

    print("=" * 70 + " FIRST STEP [KEY LENGTH] " + "=" * 70)

    # Reading the encrypted text file.
    if not file_path.endswith(".txt"):
        file_path += ".txt"
    file_reader = open(file_path, "r")
    encrypted_text = file_reader.read()
    file_reader.close()

    # Try different key lengths from 1 to 20.
    key_length = 0
    sub_texts = []
    language = "UNKNOWN"
    for i in range(1, 21):
        sub_texts = divide_text(encrypted_text, i)
        coincidence_indexes = []
        is_english_results, is_portuguese_results = [], []

        # Calculate the index of coincidence for each divided text.
        for text in sub_texts:
            letters_map = get_letters_map(text)
            coincidence_indexes.append(
                calculate_coincidence_index(letters_map))
            is_english_results.append(is_text_english(letters_map))
            is_portuguese_results.append(is_text_portuguese(letters_map))

        # Check if all coincidence indexes match the typical index of coincidence for English or Portuguese texts.
        # Also check if the two most frequent letters in each sub-text are close to the most frequent letters in English or Portuguese texts.
        # If so, the length of the key is likely found.
        if coincidence_indexes_match(coincidence_indexes, ENGLISH_COINCIDENCE_INDEX) and all(is_english_results):
            key_length = i
            language = "ENGLISH"
            print(
                f"=> For Key Length = {i}, Coincidence Indexes = {pretty_print_float_array(coincidence_indexes)} [MATCHED]")
            print(f"=> The key length is likely {key_length}")
            print(f"=> The text was likely written in English")
            break
        elif coincidence_indexes_match(coincidence_indexes, PORTUGUESE_COINCIDENCE_INDEX) and all(is_portuguese_results):
            key_length = i
            language = "PORTUGUESE"
            print(
                f"=> For Key Length = {i}, Coincidence Indexes = {pretty_print_float_array(coincidence_indexes)} [MATCHED]")
            print(f"\n=> The key length is likely {key_length}")
            print(f"=> The text was likely written in Portuguese")
            break
        print(
            f"=> For Key Length = {i}, Coincidence Indexes = {pretty_print_float_array(coincidence_indexes)} [NO MATCH]")

    print("=" * 70 + " SECOND STEP [KEY PASSWORD] " + "=" * 68)

    # Iterate over each sub-text and find the most frequent letter to decrypt the text.
    password_by_shifting_all_by_most_frequent_letter = ""
    password_by_shifting_all_by_second_most_frequent_letter = ""
    for i, text in enumerate(sub_texts):
        letters_map = get_letters_map(text)
        text_most_frequent_letter = max(letters_map, key=letters_map.get)
        language_most_frequent_letters = ENGLISH_MOST_FREQUENT_LETTERS if language == "ENGLISH" else PORTUGUESE_MOST_FREQUENT_LETTERS
        if i == 0:
            print(f"=> Considering the language's most frequent letters {language_most_frequent_letters} for performing the shifts")
        shift_1 = calculate_shift(
            language_most_frequent_letters[0], text_most_frequent_letter)
        shift_2 = calculate_shift(
            language_most_frequent_letters[1], text_most_frequent_letter)
        key_1_letter = letter_in_alphabet(shift_1)
        key_2_letter = letter_in_alphabet(shift_2)
        password_by_shifting_all_by_most_frequent_letter += key_1_letter
        password_by_shifting_all_by_second_most_frequent_letter += key_2_letter
        print(
            f"=> For Sub-Text {i + 1}, Most Frequent Letter = {text_most_frequent_letter}, Shift = {shift_1} or {shift_2}")

    # Generate all possible key passwords by combining the letters obtained from the shifts.
    possible_passwords = string_combinations(
        password_by_shifting_all_by_most_frequent_letter, password_by_shifting_all_by_second_most_frequent_letter)
    # Put first and last combinations in positions 0 and 1 respectively.
    # This is because they are the most likely to be the correct key password.
    if len(possible_passwords) > 2:
        aux = possible_passwords[1]
        possible_passwords[1] = possible_passwords[-1]
        possible_passwords[-1] = aux
    print(f"\n=> We are assuming that the most frequent letter in each sub-text is either the first or the second most frequent letter in the {str.lower(language)} language")
    print(f"==> Assuming that the most frequent letter in all sub-texts is mapped to '{language_most_frequent_letters[0]}', the key password would be: '{password_by_shifting_all_by_most_frequent_letter}'")
    print(f"==> Assuming that the second most frequent letter in all sub-texts is mapped to '{language_most_frequent_letters[1]}', the key password would be: '{password_by_shifting_all_by_second_most_frequent_letter}'")
    print(f"==> By permutating these two key passwords, we get a total of {len(possible_passwords)} possible key passwords")
    print(f"\n==> The possible key passwords are: {possible_passwords}")

    # Decrypt the text using the possible key passwords.
    # Save each decrypted text to a file.
    print("=" * 70 + " THIRD STEP [DECRYPTED TEXT] " + "=" * 68)
    if os.path.exists("decrypted"):
        rmtree("decrypted")
    os.makedirs("decrypted")
    for password in possible_passwords:
        decrypted_text = ""
        for i, letter in enumerate(encrypted_text):
            shift = calculate_shift(password[i % key_length], letter)
            decrypted_text += letter_in_alphabet(shift)
        save_path = f"decrypted/{password}.txt"
        file_writer = open(save_path, "w")
        file_writer.write(decrypted_text)
        file_writer.close()
        print(f"=> Decrypted text using key password '{password}' saved to '{save_path}'")
    print("=> All possible decrypted texts saved to the 'decrypted' folder")
    print("=" * 70 + " END " + "=" * 92)

# Entry point of the program.
if __name__ == "__main__":
    main()
