def longestest_wrod(file_path):
    longest_word = None 
    try: 
        count = 0 
        with open(file_path, "r") as file_name: 
            for line in file_name.readlines():
                line = line.strip()
                print(line)
                count +=1
                print(count)
                words = line.split(" ")
                if longest_word is None: 
                    longest_word = words[len(words)-1]
                elif len(words[len(words)-1]) > len(longest_word):
                    longest_word = words[len(words)-1]
        print(longest_word)
    except Exception as e: 
        print(e)
longestest_wrod("my_file.txt")