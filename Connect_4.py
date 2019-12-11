import tkinter as tk
import tkinter.messagebox


class Connect_4:
    def __init__(self):
        # Counts how many coins have been placed
        self.counter = 0

        # Creates 2d array simulating connect 4 board
        self.c4_board = [['', '', '', '', '', '', ''],
                         ['', '', '', '', '', '', ''],
                         ['', '', '', '', '', '', ''],
                         ['', '', '', '', '', '', ''],
                         ['', '', '', '', '', '', ''],
                         ['', '', '', '', '', '', '']]

        self.main_window = tk.Tk()
        self.main_window.title('Connect Four')

        # Where the buttons will go
        self.top_frame = tk.Frame()
        self.bottom_frame = tk.Frame()
        self.canvas_frame = tk.Frame()

        self.reset_button = tk.Button(self.top_frame, text='Reset', bd=3, command=lambda: self.reset())
        self.reset_button.pack(pady=10)

        self.button1 = tk.Button(self.top_frame, text='', width=2, height=1, bd=3,
                                 command=lambda: self.add_coin(row=0, col=0))
        self.button2 = tk.Button(self.top_frame, text='', width=2, height=1, bd=3,
                                 command=lambda: self.add_coin(row=0, col=1))
        self.button3 = tk.Button(self.top_frame, text='', width=2, height=1, bd=3,
                                 command=lambda: self.add_coin(row=0, col=2))
        self.button4 = tk.Button(self.top_frame, text='', width=2, height=1, bd=3,
                                 command=lambda: self.add_coin(row=0, col=3))
        self.button5 = tk.Button(self.top_frame, text='', width=2, height=1, bd=3,
                                 command=lambda: self.add_coin(row=0, col=4))
        self.button6 = tk.Button(self.top_frame, text='', width=2, height=1, bd=3,
                                 command=lambda: self.add_coin(row=0, col=5))
        self.button7 = tk.Button(self.top_frame, text='', width=2, height=1, bd=3,
                                 command=lambda: self.add_coin(row=0, col=6))
        self.button1.pack(side='left', padx=37, pady=15)
        self.button2.pack(side='left', padx=37, pady=15)
        self.button3.pack(side='left', padx=37, pady=15)
        self.button4.pack(side='left', padx=37, pady=15)
        self.button5.pack(side='left', padx=37, pady=15)
        self.button6.pack(side='left', padx=37, pady=15)
        self.button7.pack(side='left', padx=37, pady=15)

        # Creates canvas used to simulate connect 4 board
        self.board = tk.Canvas(self.canvas_frame, width=700, height=600)
        self.draw_board()
        self.board.pack()

        self.top_frame.pack()
        self.bottom_frame.pack()
        self.canvas_frame.pack()
        tk.mainloop()

    def draw_board(self):
        self.board.create_rectangle(0, 0, 700, 600, fill="#0000FF")
        for i in range(10, 700, 100):
            for k in range(10, 600, 100):
                self.board.create_oval(i, k, i + 80, k + 80, width=4, fill='#FFFFFF')

    def draw_button(self, x_cord=0, y_cord=0, color=''):
        self.board.create_oval(x_cord + 10, y_cord + 10, x_cord + 90, y_cord + 90, fill=color, width=4)

    def reset(self):
        self.board.create_rectangle(0, 0, 700, 600, fill="#0000FF")

        for i in range(10, 700, 100):
            for k in range(10, 600, 100):
                self.board.create_oval(i, k, i + 80, k + 80, width=4, fill='#FFFFFF')

        for row in range(6):
            for col in range(7):
                self.c4_board[row][col] = ''

        self.counter = 0

    def add_coin(self, row=0, col=0):
        if self.c4_board[5 - row][col] == 'R' or self.c4_board[5 - row][col] == 'Y':
            try:
                self.add_coin(row=row+1, col=col)
            except IndexError:
                pass
        else:
            if self.counter % 2 == 0:
                self.draw_button(x_cord=col * 100, y_cord=500 - (row * 100), color='#ff0000')
                self.c4_board[5 - row][col] = 'R'
                self.counter += 1
            else:
                self.draw_button(x_cord=col * 100, y_cord=500 - (row * 100), color='#FFFF00')
                self.c4_board[5 - row][col] = 'Y'
                self.counter += 1
        self.find_winner()

    def find_winner(self):
        try:
            # Searches for horizontal Wins
            for row in range(6):
                for col in range(4):
                    if self.c4_board[row][0 + col] == "R" and self.c4_board[row][1 + col] == "R" \
                            and self.c4_board[row][2 + col] == "R" and self.c4_board[row][3 + col] == "R":
                        self.announce_winner('Red')
            for row in range(6):
                for col in range(4):
                    if self.c4_board[row][0 + col] == "Y" and self.c4_board[row][1 + col] == "Y" \
                            and self.c4_board[row][2 + col] == "Y" and self.c4_board[row][3 + col] == "Y":
                        self.announce_winner('Yellow')

            # Searches for verticle Wins
            for row in range(3):
                for col in range(7):
                    if self.c4_board[0 + row][col] == "R" and self.c4_board[1 + row][col] == "R" \
                            and self.c4_board[2 + row][col] == "R" and self.c4_board[3 + row][col] == "R":
                        self.announce_winner('Red')
            for row in range(3):
                for col in range(7):
                    if self.c4_board[0 + row][col] == "Y" and self.c4_board[1 + row][col] == "Y" \
                            and self.c4_board[2 + row][col] == "Y" and self.c4_board[3 + row][col] == "Y":
                        self.announce_winner('Yellow')

            # Searches for diagnal wins maybe
            for row in range(3):
                for col in range(3, 7):
                    if self.c4_board[row][col] == "Y" and self.c4_board[row + 1][col - 1] == "Y" \
                            and self.c4_board[row + 2][col - 2] == "Y" and self.c4_board[row + 3][col - 3] == "Y":
                        self.announce_winner('Yellow')
            for row in range(3):
                for col in range(3, 7):
                    if self.c4_board[row][col] == "R" and self.c4_board[row + 1][col - 1] == "R" \
                            and self.c4_board[row + 2][col - 2] == "R" and self.c4_board[row + 3][col - 3] == "R":
                        self.announce_winner('Red')
            for row in range(3):
                for col in range(4):
                    if self.c4_board[row][col] == "Y" and self.c4_board[row + 1][col + 1] == "Y" \
                            and self.c4_board[row + 2][col + 2] == "Y" and self.c4_board[row + 3][col + 3] == "Y":
                        self.announce_winner('Yellow')
            for row in range(3):
                for col in range(4):
                    if self.c4_board[row][col] == "R" and self.c4_board[row + 1][col + 1] == "R" \
                            and self.c4_board[row + 2][col + 2] == "R" and self.c4_board[row + 3][col + 3] == "R":
                        self.announce_winner('Red')
        except IndexError:
            pass

    def announce_winner(self, winner):
        tk.messagebox.showinfo('Winner', winner + ' WINS!!!')
        self.reset()


connect_4_GUI = Connect_4()
