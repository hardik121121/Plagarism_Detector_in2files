# 🚨 Plagiarism Detector 🚨

A simple yet powerful Python-based plagiarism detection tool that compares two text files and calculates the similarity percentage between them. 🔍 The tool uses the **difflib** library to analyze content and identify plagiarism based on sequence matching.

## 🛠 Features

- **Overall Similarity**: Detects the overall similarity between two text files and returns a percentage. 📊
- **Sentence-Level Similarity**: Compares individual sentences and highlights overlapping content. 📝
- **Word-Level Similarity**: Analyzes individual words to calculate how much they match across the two documents. 🔤

## 📥 Installation

1. Clone the repository to your local machine:
   ```bash
   git clone https://github.com/your-username/plagiarism-detector.git
   cd plagiarism-detector
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## ⚡ Usage

1. Ensure you have two text files (`Demo1.txt` and `Demo2.txt`) in the same directory as the script.

2. Run the plagiarism detection script:
   ```bash
   python plagiarism_detector.py
   ```

3. The script will display the similarity percentage between the two files:
   
   **Example Output**:
   ```
   🚨 Plagiarised Content is: 8.68%
   📝 Sentence-Level Similarity: 42.11%
   🔤 Word-Level Similarity: 23.33%
   ```

## 🧠 How It Works

This plagiarism detection tool uses the **SequenceMatcher** class from the `difflib` library to compare the contents of two text files. The `ratio()` method returns a similarity score between 0 and 1, which is then converted into a percentage to display how much overlap exists between the documents.

### 📊 Steps:
1. **Overall Similarity**: Compares the entire content of both files. 
2. **Sentence-Level Similarity**: Breaks the text into individual sentences and compares them for overlap.
3. **Word-Level Similarity**: Tokenizes the text into individual words and compares the word sequences.

## ⚙️ Requirements

- Python 3.x
- Required libraries: `difflib`, `nltk` (for sentence and word tokenization)
  
To install the necessary libraries, run:
```bash
pip install nltk
```

## 📜 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

## 🤝 Contributing

We welcome contributions! Feel free to fork the repository, make improvements, and submit a pull request. Let’s make plagiarism detection even better! 💻

## 🙏 Acknowledgments

- Thanks to the `difflib` library for the similarity comparison algorithm. 
- A shoutout to **NLTK** for helping with tokenizing sentences and words. 🧑‍💻
