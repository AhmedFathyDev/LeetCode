from collections import deque


class Solution:
    """
    @param rooms: m x n 2D grid
    @return: nothing
    """
    def walls_and_gates(self, rooms: list[list[int]]):
        ROWS, COLS = len(rooms), len(rooms[0])

        visit = set()
        que = deque()

        for r in range(ROWS):
            for c in range(COLS):
                if rooms[r][c] == 0:
                    visit.add((r, c))
                    que.append([r, c])

        def add_room(r, c):
            if (r < 0 or r == ROWS or c < 0 or c == COLS or (r, c) in visit or rooms[r][c] == -1):
                return

            visit.add((r, c))
            que.append([r, c])

        distance = 0
        while que:
            for i in range(len(que)):
                r, c = que.popleft()
                rooms[r][c] = distance

                add_room(r + 1, c)
                add_room(r - 1, c)
                add_room(r, c + 1)
                add_room(r, c - 1)

            distance += 1
