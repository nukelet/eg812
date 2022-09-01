from itertools import cycle
import numpy as np

def vigenere_table_lookup(key_char, text_char):
    k = key_char.upper()
    t = text_char.upper()
    offset = (ord(t) + ord(k) - 2*ord('A'))%26
    return chr(ord('A') + offset)

def vigenere(key: str, text: str):
    encoded = []
    for k, t in zip(cycle(key), text):
        c = vigenere_table_lookup(k, t)
        encoded.append(c)
        # print(f"{(k,t)} -> {c}")
    return "".join(encoded)

def analyse_vigenere(encoded_text: str, key_len: int):
    arr = np.array(list(encoded_text))
    with open("data/vigenere_statistic.txt", "w") as f:
        for i in range(0, key_len):
            f.write("==================\n")
            f.write(f"OFFSET: {i}\n\n")
            skips = arr[i::key_len]
            unique, counts = np.unique(skips, return_counts=True)
            inds = np.argsort(-counts)
            sorted_chars = unique[inds]
            sorted_counts = counts[inds]
            total_count = 0
            for element, count in zip(sorted_chars, sorted_counts):
                freq = "{:.2f}".format(count*100/len(skips))
                # print(f"{element}: {count}")
                f.write(f"{element}: {freq}%\n")
                total_count += count
            f.write(f"total: {total_count}\n")
    

def main():
    with open("data/clarice.txt", "r") as f:
        # convert to uppercase and then remove spaces/newlines/punctuation/etc
        text_uppercase = f.read().upper()
        text = "".join(filter(str.isalpha, text_uppercase))

    print(len(text))

    key = "carta"
    out = vigenere(key, text)
    analyse_vigenere(out, len(key))
    print(out)
        

if __name__ == "__main__":
    main()