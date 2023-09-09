import secrets  # Import the secrets module for generating secure random elements
import nltk  # Import the Natural Language Toolkit (NLTK) library for working with language data
# Set the path to the NLTK data directory (replace with your actual path)
nltk.data.path.append("/Users/ruby/nltk_data")
# Download specific NLTK resources (WordNet) to the specified directory
nltk.download('wordnet', download_dir="/Users/ruby/nltk_data")


# Import the wordnet module from the NLTK corpus
from nltk.corpus import wordnet
import string  # Import the string module for working with strings

# Function to fetch words based on a specific part of speech (wordnet category)
def fetch_words_by_pos(wordnet_category):
    synsets = []
    if wordnet_category == "noun":
        synsets = wordnet.all_synsets(pos=wordnet.NOUN)
    elif wordnet_category == "verb":
        synsets = wordnet.all_synsets(pos=wordnet.VERB)
    elif wordnet_category == "adj":
        synsets = wordnet.all_synsets(pos=wordnet.ADJ)
    elif wordnet_category == "adv":
        synsets = wordnet.all_synsets(pos=wordnet.ADV)

    # Extract lemma names (words) from synsets and return as a list
    '''
    words = []

    # Outer loop: Iterate over each synset in the synsets list
    for synset in synsets:
        # Inner loop: Iterate over each lemma in the synset
        for lemma in synset.lemmas():
            # Extract the name of the lemma and add it to the words list
            words.append(lemma.name())

    # Return the list of words
    return words
    '''
    words = [lemma.name() for synset in synsets for lemma in synset.lemmas()]
    return words


# Function to choose a base word's part of speech
def choose_base_word_pos():
    parts_of_speech = ["noun", "verb", "adj", "adv"]
    print("Select a part of speech:")
    for idx, pos in enumerate(parts_of_speech, start=1):
        print(f"{idx}. {pos}")

    choice = int(input("Enter the number of your choice: "))
    selected_pos = parts_of_speech[choice - 1].lower()
    print(f"You chose: {selected_pos} as the part of speech for your password's base word.")
    return selected_pos

# Main function to execute the program
def main():
    selected_part = choose_base_word_pos()  # Choose a part of speech
    words = fetch_words_by_pos(selected_part)  # Fetch words based on the chosen part of speech
    base_word = secrets.choice(words)  # Choose a random word from the fetched words
    #password = generate_password(base_word)  # Generate a password using the chosen word
    #print(f"Generated Password: {password}")

# Execute the main function if this script is run directly
if __name__ == "__main__":
    main()









