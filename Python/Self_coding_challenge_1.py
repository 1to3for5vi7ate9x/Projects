# Locked Treasure Chest Solution

def locked_treasure_chest_solution(int_list, secret_word):
    """
    This function takes a list of integers and a secret word to solve the "Locked Treasure Chest" coding challenge.
    It returns a list of integers representing the opened locks.
    
    Args:
    - int_list (list): A list of integers.
    - secret_word (str): The secret word to decode the locks.
    
    Returns:
    - list: A list of integers representing the opened locks.
    """
    
    # Initialize an empty list to store the opened locks
    opened_locks = []
    
    # First Lock: Sum of ASCII values of the characters in the secret word, multiplied by the first integer in the list
    first_lock = sum(ord(char) for char in secret_word) * int_list[0]
    opened_locks.append(first_lock)
    
    # Second Lock: Product of ASCII values of the characters in the secret word, modulo the second integer in the list
    second_lock = 1
    for char in secret_word:
        second_lock *= ord(char)
    second_lock = second_lock % int_list[1]
    opened_locks.append(second_lock)
    
    # Third Lock: Sum of the first integer and the reverse of the second integer, multiplied by the sum of ASCII values of vowels in the secret word
    vowels = "aeiou"
    third_lock = (int_list[0] + int(str(int_list[1])[::-1])) * sum(ord(char) for char in secret_word if char.lower() in vowels)
    opened_locks.append(third_lock)
    
    return opened_locks

# Example usage:
# List of integers: [2, 3, 4], Secret word: "Ankit"
example_int_list = [2, 3, 4]
example_secret_word = "Ankit"
result = locked_treasure_chest_solution(example_int_list, example_secret_word)
print("Opened locks:", result)

