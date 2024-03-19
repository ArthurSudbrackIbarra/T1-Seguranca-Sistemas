# Constant representing the typical index of coincidence for English and Portuguese texts.
ENGLISH_COINCIDENCE_INDEX = 0.066
PORTUGUESE_COINCIDENCE_INDEX = 0.074


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
        if abs(index - target_index) > 0.01:
            return False
    return True


# Main function.
def main():
    # Reading the encrypted text file.
    file_path = "encrypted/cipher10.txt"
    file_reader = open(file_path, "r")
    encrypted_text = file_reader.read()
    file_reader.close()

    # Try different key lengths from 1 to 15.
    key_length = 0
    sub_texts = []
    for i in range(1, 16):
        new_texts = divide_text(encrypted_text, i)
        coincidence_indexes = []
        # Calculate the index of coincidence for each divided text.
        for text in new_texts:
            letters_map = get_letters_map(text)
            coincidence_index = calculate_coincidence_index(letters_map)
            coincidence_indexes.append(coincidence_index)

        # Check if the coincidence index is close to the English coincidence index.
        # If so, the length of the key is likely found.
        if coincidence_indexes_match(coincidence_indexes, PORTUGUESE_COINCIDENCE_INDEX):
            key_length = i
            sub_texts = new_texts
            print(
                f"For Key Length = {i}, Coincidence Indexes = {coincidence_indexes} It's a match! The key length is likely {i}.\n")
            break
        print(
            f"For Key Length = {i}, Coincidence Indexes = {coincidence_indexes} Hmmm... not quite it. Let's try another key length.\n")

    # Now that we have the key length, we can try to decrypt the text using the Vigenere cipher.


# Entry point of the program.
if __name__ == "__main__":
    main()
