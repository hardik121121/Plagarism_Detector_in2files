from difflib import SequenceMatcher

def read_file(file_path):
    """Reads the content of a file and returns it as a string."""
    try:
        with open(file_path, 'r') as file:
            return file.read()
    except FileNotFoundError:
        print(f"Error: {file_path} not found.")
        return None

def calculate_similarity(data_file1, data_file2):
    """Calculates the similarity ratio between two texts using difflib's SequenceMatcher."""
    matcher = SequenceMatcher(None, data_file1, data_file2)
    return matcher.ratio() * 100

def check_plagiarism(file1, file2):
    """Performs plagiarism check with multiple checks on word and sentence level similarity."""
    # Read the file contents
    data_file1 = read_file(file1)
    data_file2 = read_file(file2)
    
    if data_file1 and data_file2:
        # Overall text similarity (whole document comparison)
        overall_similarity = calculate_similarity(data_file1, data_file2) 
        print(f"Overall Similarity (document level): {overall_similarity:.2f}%")

        # Sentence-level similarity (split into sentences for a finer granularity)
        sentences1 = data_file1.split('. ')
        sentences2 = data_file2.split('. ')

        sentence_matches = 0
        total_sentences = len(sentences1)

        for sentence1 in sentences1:
            for sentence2 in sentences2:
                sentence_similarity = calculate_similarity(sentence1, sentence2)
                if sentence_similarity > 80:  # Consider a match if similarity is above 80%
                    sentence_matches += 1
                    break

        sentence_match_percentage = (sentence_matches / total_sentences) * 100
        print(f"Sentence-Level Similarity: {sentence_match_percentage:.2f}%")

        # Word-level similarity check (splitting words and comparing)
        words1 = set(data_file1.split())
        words2 = set(data_file2.split())
        common_words = words1.intersection(words2)
        word_match_percentage = (len(common_words) / max(len(words1), len(words2))) * 100
        print(f"Word-Level Similarity: {word_match_percentage:.2f}%")

if __name__ == "__main__":
    file1 = 'Demo1.txt'  # Path to the first file
    file2 = 'Demo2.txt'  # Path to the second file
    check_plagiarism(file1, file2)
