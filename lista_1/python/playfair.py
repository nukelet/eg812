import numpy as np

def get_matrix(key: str):
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    flat_matrix = []
    for letter in key:
        if letter not in flat_matrix:
            flat_matrix.append(letter)
    for letter in alphabet:
        if letter not in flat_matrix:
            flat_matrix.append(letter)
    matrix = np.reshape(np.array(flat_matrix), (5,5))
    return matrix

def playfair_decode(msg: str, key: str):
    msg = msg.upper()
    key = key.upper().replace(" ", "")
    matrix = get_matrix(key)
    decoded = []
    print(matrix)
    pairs = list(zip(msg[0::2], msg[1::2]))
    for (a, b) in pairs:
        a_i, a_j = tuple([x[0] for x in np.where(matrix == a)])
        b_i, b_j = tuple([x[0] for x in np.where(matrix == b)])
        # print(f"{a}: {(a_i, a_j)}, {b}: {(b_i, b_j)}")
        if a_i == b_i:
            decoded += [matrix[a_i, a_j-1], matrix[b_i, b_j-1]]
        elif a_j == b_j:
            decoded += [matrix[a_i-1, a_j], matrix[b_i-1, b_j]]
        else:
            decoded += [matrix[a_i, b_j], matrix[b_i, a_j]]

    return "".join(decoded)

def main():
    msg = playfair_decode("CBMOBERNTIBFMEBWDA", "NAOCOMPARTILHE")
    print(msg)

if __name__ == '__main__':
    main()