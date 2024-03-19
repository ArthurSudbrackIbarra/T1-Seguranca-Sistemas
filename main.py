# Constant representing the typical index of coincidence for English and Portuguese texts.
ENGLISH_COINCIDENCE_INDEX = 0.066
PORTUGUESE_COINCIDENCE_INDEX = 0.074

# Constant representing the most frequent letter in English and Portuguese texts.
ENGLISH_MOST_FREQUENT_LETTER = "e"
PORTUGUESE_MOST_FREQUENT_LETTER = "a"


# Function to check if the text is likely english based on the frequency of the most frequent letters.
def is_text_english(letters_map: dict[str, int]) -> bool:
    """
    Check if the text is likely to be English based on the frequency of the most frequent letter.

    Args:
        letters_map (dict[str, int]): A dictionary with letters as keys and their frequencies as values.

    Returns:
        bool: True if the text is likely to be English, False otherwise.
    """
    total_letters = sum(letters_map.values())
    sorted_letters_map = sorted(letters_map.items(), key=lambda x: x[1], reverse=True)
    most_frequent_letter = sorted_letters_map[0][0]
    second_most_frequent_letter = sorted_letters_map[1][0]

    # English E letter is the most frequent letter and it has 12.7% frequency.
    # English T letter is the second most frequent letter and it has 9.05% frequency.
    # Check if the most frequent letter is close to the English E letter.
    # Check if the second most frequent letter is close to the English T letter.
    # If so, the text is likely to be English.
    if abs(letters_map[most_frequent_letter] / total_letters - 0.127) < 0.01 and abs(letters_map[second_most_frequent_letter] / total_letters - 0.0905) < 0.01:
        return True


# Function to check if the text is likely portuguese based on the frequency of the most frequent letters.
def is_text_portuguese(letters_map: dict[str, int]) -> bool:
    """
    Check if the text is likely to be Portuguese based on the frequency of the most frequent letter.

    Args:
        letters_map (dict[str, int]): A dictionary with letters as keys and their frequencies as values.

    Returns:
        bool: True if the text is likely to be Portuguese, False otherwise.
    """
    total_letters = sum(letters_map.values())
    sorted_letters_map = sorted(letters_map.items(), key=lambda x: x[1], reverse=True)
    most_frequent_letter = sorted_letters_map[0][0]
    second_most_frequent_letter = sorted_letters_map[1][0]

    print(abs(letters_map[most_frequent_letter] / total_letters - 0.1463))

    # Portuguese A letter is the most frequent letter and it has 14.63% frequency.
    # Portuguese E letter is the second most frequent letter and it has 12.57% frequency.
    # Check if the most frequent letter is close to the Portuguese A letter.
    # Check if the second most frequent letter is close to the Portuguese E letter.
    # If so, the text is likely to be Portuguese.
    if abs(letters_map[most_frequent_letter] / total_letters - 0.1463) < 0.01 and abs(letters_map[second_most_frequent_letter] / total_letters - 0.1257) < 0.01:
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
    return "[" + ", ".join([f"{x:.3f}" for x in array]) + "]"


# Function to generate a dictionary mapping each letter to its frequency in the encrypted text.
def get_letters_map(encrypted_text: str) -> dict[str, int]:
    """
    Generate a dictionary mapping each letter to its frequency in the encrypted text.

    Args:
        encrypted_text (str): The encrypted text.

    Returns:
        dict[str, int]: A dictionary with letters as keys and their frequencies as values.
    """
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
    position_1 = position_in_alphabet(start_letter)
    position_2 = position_in_alphabet(end_letter)
    if position_2 >= position_1:
        return position_2 - position_1 + 1
    return 26 - position_1 + position_2 + 1
    

# Main function.
def main():
    print("=" * 70 + " FIRST STEP [KEY LENGTH] " + "=" * 70)
    # Reading the encrypted text file.
    file_path = "encrypted/cipher30.txt"
    file_reader = open(file_path, "r")
    encrypted_text = file_reader.read()
    file_reader.close()

    # Try different key lengths from 1 to 20.
    key_length = 0
    sub_texts = []
    language = ""
    for i in range(1, 21):
        sub_texts = divide_text(encrypted_text, i)
        coincidence_indexes = []
        is_english = False
        is_portuguese = False

        # Calculate the index of coincidence for each divided text.
        for text in sub_texts:
            letters_map = get_letters_map(text)  
            coincidence_index = calculate_coincidence_index(letters_map)
            coincidence_indexes.append(coincidence_index)

            # ! This is totally wrong, only the last sub-text is being checked.
            is_english = is_text_english(letters_map)
            is_portuguese = is_text_portuguese(letters_map)

        # Check if the coincidence index is close to the detected language coincidence index.
        # If so, the length of the key is likely found.
        if coincidence_indexes_match(coincidence_indexes, ENGLISH_COINCIDENCE_INDEX) and is_english:
            key_length = i
            language = "ENGLISH"
            print(
                f"=> For Key Length = {i}, Coincidence Indexes = {pretty_print_float_array(coincidence_indexes)} [MATCHED]")
            print (f"=> The key length is most likely '{key_length}'")
            print(f"=> The text is likely to be written in 'English'")
            break
        elif coincidence_indexes_match(coincidence_indexes, PORTUGUESE_COINCIDENCE_INDEX) and is_portuguese:
            key_length = i
            language = "PORTUGUESE"
            print(
                f"=> For Key Length = {i}, Coincidence Indexes = {pretty_print_float_array(coincidence_indexes)} [MATCHED]")
            print (f"=> The key length is most likely '{key_length}'")
            print(f"=> The text is likely to be written in 'Portuguese'")
            break
        print(
            f"=> For Key Length = {i}, Coincidence Indexes = {pretty_print_float_array(coincidence_indexes)} [NO MATCH]")

    print("=" * 70 + " SECOND STEP [KEY PASSWORD] " + "=" * 68)

    # Iterate over each sub-text and find the most frequent letter to decrypt the text.
    key_password = ""
    decrypted_texts = []
    for i, text in enumerate(sub_texts):
        letters_map = get_letters_map(text)
        most_frequent_letter = max(letters_map, key=letters_map.get)
        language_most_frequent_letter = ENGLISH_MOST_FREQUENT_LETTER if language == "ENGLISH" else PORTUGUESE_MOST_FREQUENT_LETTER
        shift = calculate_shift(language_most_frequent_letter, most_frequent_letter)
        key_letter = letter_in_alphabet(shift)
        key_password += key_letter
        print(f"=> For Sub-Text {i + 1}, Most Frequent Letter = {most_frequent_letter}, Shift = {shift}")

        # Decrypt the sub-text using the key letter.
        decrypted_text = ""
        for letter in text:
            correct_letter_position = calculate_shift(key_letter, letter)
            decrypted_text += letter_in_alphabet(correct_letter_position)
        decrypted_texts.append(decrypted_text)
    print(f"=> The key password is '{key_password}'")

    # Join the decrypted sub-texts into a single text.
    decrypted_text = join_text(decrypted_texts, key_length)
    
    # Save the decrypted text to a file.
    file_writer = open("decrypted.txt", "w")
    file_writer.write(decrypted_text)
    file_writer.close()
    print("=" * 166)
    print(f"=> The decrypted text has been saved to 'decrypted.txt'")


# Entry point of the program.
if __name__ == "__main__":
    main()
