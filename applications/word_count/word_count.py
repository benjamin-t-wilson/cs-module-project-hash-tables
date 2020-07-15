ignored_chars = (":", ";", ",", ".", "-", "+", "=", "/", "\\", "|", "[", "]", "{", "}", "(", ")", "*", "^", "&", "\"")

def word_count(s):
    # Your code here
    for char in ignored_chars:
        s = s.replace(char, "")
    s = s.lower().split()
    word_dict = {}
    if len(s) == 1 and s[0] == "":
        return {}
    for word in s:
        if word not in word_dict:
            word_dict[word] = 1
        else:
            word_dict[word] += 1
    return word_dict



if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))