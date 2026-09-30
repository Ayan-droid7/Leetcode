class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        rows, cols = len(box), len(box[0])

        result = [['.'] * rows for _ in range(cols)]

        for i in range(rows):
            empty_spot = cols - 1  
            for j in range(cols - 1, -1, -1):
                if box[i][j] == '#':

                    box[i][j], box[i][empty_spot] = '.', '#'
                    empty_spot -= 1
                elif box[i][j] == '*':

                    empty_spot = j - 1

            for j in range(cols):
                result[j][rows - 1 - i] = box[i][j]

        return result