import pymupdf 
import argparse
from tqdm import tqdm

digit_words = {"zero": 0, "one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}
number_words = {"hundred": 100, "thousand": 1000, "million": 1000000, "billion": 1000000000, "trillion": 1000000000000}

#Convert a word to float if it is a number
def to_number(word):
    if word.isdigit():  
        # Check if the word is a number
        return float(word)
    if word.lower() in digit_words:
        # Check if the word is a digit word
        return digit_words[word.lower()]
    if "." in word: 
        # Check if the word is a float
        words = word.split(".")
        if len(words) == 2 and words[0].isdigit() and words[1].isdigit():
            return float(word)
    if len(word) > 1 and word[1].isdigit():
        # Check if the word is a number with a prefix (ex. $100)
        return to_number(word[1:])
    return None

#Find the greatest number in a page
def greatest_number_in_page(page_text):
    greatest_number = None
    for i, word in enumerate(page_text.split()):
        number = to_number(word)
        if number is not None:
            #Check if the word is a number
            if greatest_number is None or number > greatest_number:
                greatest_number = number
        elif word.lower() in number_words and i > 0:
            #Check if the word represents a number (ex. "million")
            number = number_words[word.lower()]
            prev_word = page_text.split()[i - 1]
            prev_number = to_number(prev_word)
            if prev_number is not None:
                # Merge the previous number with the number word (ex. "5 hundred" -> 500)
                number *= prev_number
                if greatest_number is None or number > greatest_number:
                    greatest_number = number
    return greatest_number

#Find the greatest number in a PDF
def greatest_number_in_pdf(pdf):
    greatest_number = None
    for page in tqdm(pdf):
        text = page.get_text()
        candidate = greatest_number_in_page(text)
        if candidate is not None:
            if greatest_number is None or candidate > greatest_number:
                greatest_number = candidate
    return greatest_number

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--pdf", type=str, required=True, help="PDF file path")
    args = parser.parse_args()
    pdf = pymupdf.open(args.pdf)
    greatest_number = greatest_number_in_pdf(pdf)
    if greatest_number is None:
        print("No number found")
    else:
        print(f"The greatest number is {float(greatest_number)}")
