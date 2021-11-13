class Othello:
    def __init__(self, size):
        self.board = [[0] * size for i in range(size)]
        self.size = size

    def print(self):
        print("-"*self.size*3)
        for line in self.board:
            for area in line:
                stone = ' '
                if area == 1:
                    stone = 'o'
                elif area == 2:
                    stone = 'x'
                print('|{}|'.format(stone), end="")
            print("")
            print("-"*self.size*3)

    def put(self, x, y, stone):
        self.board[y][x] = stone

    def is_range(self, v):
        return (v > 0) and (self.size > v)

    def put_default_stone(self):
        ptn = [3, 4]
        for x in ptn:
            for y in ptn:
                self.put(x, y, abs(x - y) + 1)

    def put_ptr_candidates(self, stone):
        ptn = [-1, 0, 1]
        put_candidates = []
        for x in range(self.size):
            for y in range(self.size):
                put_candis = False
                ostone = self.opponent_stone(stone)
                for xv in ptn:
                    for yv in ptn:
                        if xv == yv and xv == 0:
                            continue
                        if not self.board[y][x] == 0:
                            continue
                        cur_x = x + xv
                        cur_y = y + yv
                        oppo_area_ptrs = []
                        while self.is_range(cur_x) and self.is_range(cur_y):
                            if self.board[cur_y][cur_x] == ostone:
                                oppo_area_ptrs.append((cur_x, cur_y))
                            elif self.board[cur_y][cur_x] == stone:
                                if len(oppo_area_ptrs) > 0:
                                    put_candis = True
                                break
                            else:
                                break
                            cur_x += xv
                            cur_y += yv
                        if put_candis:
                            break
                    if put_candis:
                        break
                if put_candis:
                    put_candidates.append((x, y))
        return put_candidates

    def is_finished(self):
        flg = True
        only_stone = self.board[0][0]
        for line in self.board:
            for a in line:
                flg = flg and (a != 0)
                kind_stone = only_stone and a
        return flg and only_stone

    def put_judge(self, x, y, stone):
        self.put(x, y, stone)
        self.judge_ptr((x, y))

    def opponent_stone(self, stone):
        if stone == 1:
            return 2
        elif stone == 2:
            return 1
        else:
            return 0

    def judge_ptr(self, ptr):
        x, y = ptr
        st = self.board[y][x]
        ptn = [-1, 0, 1]
        for i in ptn:
            for j in ptn:
                self.judge_ptr_oneway((x, y), i, j)

    def who_winner(self):
        rst = [0, 0, 0]
        for line in self.board:
            for a in line:
                rst[a] += 1

        winner = 0
        lose = 0
        if rst[1] > rst[2]:
            winner = 1
            lose = 2
        elif rst[1] < rst[2]:
            winner = 2
            lose = 1

        return (winner, rst[winner], rst[lose])

    def count_print(self):
        print("-"*self.size*3)
        for line in self.board:
            acnt, bcnt = [0, 0]
            for area in line:
                stone = ' '
                if area == 1:
                    stone = 'o'
                    acnt += 1
                elif area == 2:
                    stone = 'x'
                    bcnt += 1
                print('|{}|'.format(stone), end="")
            print('    o/x = {}/{}'.format(acnt, bcnt), end="")
            print("")
            print("-"*self.size*3)

    def judge_ptr_oneway(self, ptr, xv, yv):
        x, y = ptr
        cur_x = x + xv
        cur_y = y + yv
        st = self.board[y][x]
        ostone = self.opponent_stone(st)
        def is_range(a): return a > 0 and self.size > a
        put_candidates = []
        while is_range(cur_x) and is_range(cur_y):
            if self.board[cur_y][cur_x] == ostone:
                put_candidates.append((cur_x, cur_y))
            elif self.board[cur_y][cur_x] == st:
                for px, py in put_candidates:
                    self.put(px, py, st)
                return
            else:
                return
            cur_x += xv
            cur_y += yv
