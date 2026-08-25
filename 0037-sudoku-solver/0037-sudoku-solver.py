class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for r in range(9):
            for c in range(9):

                if board[r][c] != '.':
                    num = board[r][c]
                    box = (r // 3) * 3 + (c // 3)

                    rows[r].add(num)
                    cols[c].add(num)
                    boxes[box].add(num)

        def solve():

            for r in range(9):
                for c in range(9):

                    if board[r][c] == '.':

                        box = (r // 3) * 3 + (c // 3)

                        for num in "123456789":

                            if (num not in rows[r] and
                                num not in cols[c] and
                                num not in boxes[box]):

                                board[r][c] = num
                                rows[r].add(num)
                                cols[c].add(num)
                                boxes[box].add(num)

                                if solve():
                                    return True

                                # BACKTRACK
                                board[r][c] = '.'
                                rows[r].remove(num)
                                cols[c].remove(num)
                                boxes[box].remove(num)

                        return False

            return True

        solve()


    #     self.solve(board)
    # def solve(self,board):
    #     for r in range(9):
    #         for c in range(9):
    #             if board[r][c]=='.':
    #                 for num in range(1,10):
    #                     num_char=str(num)

    #                     if self.isValid(board,r,c,num_char):
    #                         board[r][c]=num_char
    #                         if self.solve(board):
    #                             return True
    #                         else:
    #                             board[r][c]='.'
    #                 return False
    #     return True
    # def isValid(self,board,row,col,num_char):
    #     box_row_start=(row//3)*3
    #     box_col_start=(col//3)*3
        
    #     for i in range(9):
    #         if board[row][i]==num_char:
    #             return False
    #         if board[i][col]==num_char:
    #             return False
    #         box_row=(box_row_start)+i//3
    #         box_col=(box_col_start)+i%3
    #         if board[box_row][box_col]==num_char:
    #             return False
    #     return True


        