def dp_minDistance(word1, word2):
        # edit distance (dynamic programming solution)

        # form table
        m = len(word1)
        n = len(word2)
        table = [[0] * (n+1) for _ in range(m+1)]
        """
        initialize table by filling each cell with 0.
        [0] * (n+1) creates a row based on n+1 (horizontally)
        for _ in range(m+1) repeats row creation m+1 times, filling up the columns (vertically)
        """

        # base cases
        for i in range(m+1):
            table[i][0] = i
        for j in range(n+1):
            table[0][j] = j

        # fill table
        for i in range(1, m+1):
            for j in range(1, n+1):
                if word1[i-1] == word2[j-1]:
                    table[i][j] = table[i-1][j-1]
                else:
                    table[i][j] = 1 + min(table[i-1][j], table[i][j-1], table[i-1][j-1])
        
        return table[-1][-1]

if __name__ == "__main__":
    w1 = "intention"
    w2 = "execution"
    print(dp_minDistance(w1, w2))