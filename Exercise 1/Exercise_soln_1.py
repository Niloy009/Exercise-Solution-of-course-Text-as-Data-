from collections import Counter
import os
import glob



def all_txt_files_found(main_path:str) -> list[str]:
    """Finds all .txt files in a directory.

    Searches the provided main path recursively for files ending in .txt and 
    returns a list of the full file paths.

    Args:
    main_path (str): The main directory path to search in.

    Returns:
    list[str]: A list of paths to .txt files found.
    """
    files = glob.glob(pathname=os.path.join(main_path, '*.txt'))
    return files

def read_four_bytes(filename: str) -> str:
    """Reads the first 4 bytes from a file.

    Opens the file in binary mode, reads 4 bytes from the start, and returns them as a string.

    Args:
    filename (str): The path to the file to read from.

    Returns: 
    str: The first 4 bytes of the file as a string.
    """
    with open(file=filename, mode='rb') as f:
        four_bytes = f.read(4)
    return four_bytes



def detect_encoding(four_bytes:str) -> str:
    """Detects encoding of a file from the first 4 bytes.

        Tries decoding the given 4 byte string with UTF-8 and UTF-16. 
        Returns the encoding if successful, otherwise returns that encoding failed.

        Args:
        four_bytes (str): The first 4 bytes of a file as a string.

        Returns:
        str: The detected encoding, or a message that detection failed.
        
    """

    encoding_check = ['utf-8', 'utf-16']
    decoding = None

    for en in encoding_check:
        try:
            decoding = four_bytes.decode(encoding=en)
            return en
        except UnicodeDecodeError:
            continue
    if decoding:
        return f'The file is encoded with {en}'
    else:
        return 'The file is not encoded with the provided encoding'

def process_lines(text:str) -> list[str]:
    """Processes the given text and returns a list of processed strings.
       preprocessed based on:
       1.Remove punctuation, numbers and special characters
       2.Turn all letters into lower case
       3.Split the text into individual words

    Args:
        text (str): The input text to be processed.

    Returns:
        list[str]: A list of processed strings.
    """

    process_list = []
    processed_str = ''.join(
        char.lower() for char in text if char.isalpha() or char.isspace()
    )
    process_list.extend(iter(processed_str.split(' ')))
    return process_list



if __name__ == '__main__':        
    files = all_txt_files_found(main_path='/media/niloy/Study/TU Dortmund Study/Winter Semester 2023_2024/TADA/Exercise 1')
    content_list = []
    for file in files:
        four_bytes = read_four_bytes(filename=file)
        encoding = detect_encoding(four_bytes=four_bytes)
        with open(file=file, mode='r', encoding=encoding) as f:
            content = f.read()
            split_content = content.split('\n')
            content_list.extend(iter(split_content))

        print('Task 1')
        print(f'File Name:{os.path.basename(file)}')
        print(f'Encoding:{encoding}')
        print(f'Content: {content}')

    print('----------------------------------------------------------------')

    print('Task 2')
    print(f'The one list with all files: {content_list}')
    print(f'The length of the list: {len(content_list)}')

    print('----------------------------------------------------------------')



    print('Task 3')
    word_lists = [process_lines(text=review) for review in content_list]
    print(word_lists)
    
    print('----------------------------------------------------------------')



    print('Task 4')
    all_words  = [word 
                  for word_list in word_lists 
                  for word in word_list]
    word_counter = Counter(all_words)
    
    print(f'Most 5 common words in the corpus: {word_counter.most_common(5)}')
    print('''
          As we see that the most 5 common words are "the, of, a, is, and"
          These are not holding much information as they are stopwords.
          ''')










