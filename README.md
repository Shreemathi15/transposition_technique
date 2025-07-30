# transposition_technique
Row Transposition and Rail Fence
Rail Fence Cipher
Working Principle:
• Characters are written in a zigzag pattern across two rows.
• The first character goes to the first rail, the second to the second rail, the third again to the
first rail, and so on.
• Ciphertext is formed by reading the characters row by row.
Encryption Steps:
1. Remove spaces and convert text to lowercase.
2. Divide characters between two rails:
• Even-indexed characters → Rail 1
• Odd-indexed characters → Rail 2
3. Concatenate characters from both rails to form the ciphertext.
Decryption Steps:
1. Split the ciphertext into two halves: one for each rail.
2. Interleave characters from both rails to reconstruct the original plaintext.
Example:
Plaintext: `meet at the school house`
Cipher Text: Characters ordered rail-wise.
Decrypted Text: Original text reconstructed by alternating characters from the two rails.
Row Transposition Cipher
Working Principle:
• This technique involves writing the plaintext into a matrix row-wise, based on the length
of a numeric key.
• The columns of the matrix are then rearranged based on the ascending order of digits in
the key.
• The ciphertext is read by traversing the matrix column-wise using the column order
defined by the key.
Encryption Steps:
1. Remove spaces and convert text to lowercase.
2. Create a matrix with rows based on the length of the plaintext and number of columns equal to
the key length.
3. Fill the matrix row-wise.
4. Read columns in the order defined by the sorted key digits to generate the ciphertext.
Decryption Steps:
1. Create an empty matrix of the same size.
2. Fill the matrix column-wise based on the key.
3. Read the matrix row-wise to retrieve the original plaintext.
Example:
Plaintext: `meet at the school house`
Key: `4312567`
Cipher Text: (columns rearranged using the key)
Decrypted Text: Original text restored.
