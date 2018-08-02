"""
graphics.py is responsible for initiating all graphics of the game
"""
#-----------------------------------------------------------------------------#
from Tkinter import *
import tkSimpleDialog
import rules

def main():

    # window dimensions
    cw, ch = 500, 700

    """
    initiates all aspects of game play, including displaying all graphics,
    monitoring events (time based ticks and keyboard commands), and contains
    end game interface information
    """
    def start_game():

        # initialize canvas
        C = Canvas(W, width=cw, height=ch)
        C.pack()

        frog = PhotoImage(file='img/frog.gif')
        redcar = PhotoImage(file='img/redcar.gif')
        purplecar = PhotoImage(file='img/purplecar.gif')
        bluecar = PhotoImage(file='img/bluecar.gif')
        greencar = PhotoImage(file='img/greencar.gif')
        yellowcar = PhotoImage(file='img/yellowcar.gif')
        background = PhotoImage(file='img/background.gif')

        """
        draws the game board and background
        """

        def draw(board):

            global player_score
            global num_ticks

            # clear previous drawings
            C.delete('all')

            # draw the background
            C.create_image(cw/2, ch/2, image=background)

            # find each spot in board
            for row in range(len(board)):
                for column in range(len(board[0])):
                    spot = board[row][column]
                    # draws the cars
                    if spot == 'c':
                        if column == 0:
                            C.create_image(cw/5 * column + cw/10,
                                ch/10 * row + ch/20, image= redcar)
                        elif column == 1:
                            C.create_image(cw/5 * column + cw/10,
                                ch/10 * row + ch/20, image= purplecar)
                        elif column == 2:
                            C.create_image(cw/5 * column + cw/10,
                                ch/10 * row + ch/20, image= bluecar)
                        elif column == 3:
                            C.create_image(cw/5 * column + cw/10,
                                ch/10 * row + ch/20, image= greencar)
                        else:
                            C.create_image(cw/5 * column + cw/10,
                                ch/10 * row + ch/20, image= yellowcar)
                    # draws the frog
                    elif spot == 'f':
                        C.create_image(cw/5 * column + cw/10,  \
                                       ch/10 * row + ch/20, image=frog)

            # updates player score
            if num_ticks <= 100:
                player_score = num_ticks
                multiplier = '1X'
            elif num_ticks <= 200:
                player_score = 100 + (num_ticks-100)*2
                multiplier = '2X'
            elif num_ticks <= 300:
                player_score = 300 + (num_ticks-200)*3
                multiplier = '3X'
            elif num_ticks <= 400:
                player_score = 600 + (num_ticks-300)*4
                multiplier = '4X'
            elif num_ticks <= 550:
                player_score = 1000 + (num_ticks-400)*5
                multiplier = '5X'
            elif num_ticks <= 700:
                player_score = 1750 + (num_ticks-550)*6
                multiplier = '6X'
            elif num_ticks <= 850:
                player_score = 2650 + (num_ticks-700)*7
                multiplier = '7X'
            elif num_ticks <= 1050:
                player_score = 3700 + (num_ticks-850)*8
                multiplier = '8X'
            elif num_ticks <= 1300:
                player_score = 5300 + (num_ticks-1050)*9
                multiplier = '9X'
            else:
                player_score = 7550 + (num_ticks-1300)*10
                multiplier = '10X'

            # draw current score
            C.create_text(cw/2, 20, text=str(player_score), fill='yellow',
                font=('futura', 24))

            # draw multiplier
            C.create_text(30, 20, text=multiplier, fill='yellow',
                font=('futura', 24))

        """
        moves frog after being called
        """
        def key(event):
            global board

            # right arrow pressed
            if repr(event.char) == "u'\uf703'":
                if rules.check_right(board):
                    board = rules.move_right(board)
                    draw(board)
                else:
                    end_game()
            # left arrow pressed
            elif repr(event.char) == "u'\uf702'":
                if rules.check_left(board):
                    board = rules.move_left(board)
                    draw(board)
                else:
                    end_game()
            # up arrow pressed
            elif repr(event.char) == "u'\uf700'":
                if rules.check_up(board):
                    board = rules.move_up(board)
                    draw(board)
                else:
                    end_game()
            # down arrow pressed
            elif repr(event.char) == "u'\uf701'":
                if rules.check_down(board):
                    board = rules.move_down(board)
                    draw(board)
                else:
                    end_game()

        """
        broadcasts a tick event on intervals based on the number of ticks, and
        keeps track of the number of ticks
        """
        def ticker():
            global num_ticks
            global playing
            if playing:
                W.event_generate('<<tick>>')
                num_ticks += 1
                if num_ticks < 100:
                    W.after(130, ticker)
                elif num_ticks < 250:
                    W.after(120, ticker)
                elif num_ticks < 400:
                    W.after(110, ticker)
                elif num_ticks < 650:
                    W.after(100, ticker)
                elif num_ticks < 900:
                    W.after(90, ticker)
                elif num_ticks < 1200:
                    W.after(80, ticker)
                else:
                    W.after(70, ticker)

        """
        checks and updates the board along with graphics after being called
        """
        def update(event):
            global board
            global num_ticks
            if rules.check(board):
                board = rules.update(board, num_ticks)
                draw(board)
            else:
                end_game()

        """
        prompts user for their initials
        """
        def score_prompt():
            root = Tk()
            root.withdraw()

            # prompt for and receive initials
            initials = tkSimpleDialog.askstring('Initials',
                'Provide Your Initials to Save Your Score!')

            if initials != None:
                # keep prompting until exactly 3 letters are given
                while len(initials) != 3 or not initials.isalpha():
                    initials = tkSimpleDialog.askstring('Initials', \
                        'Initials Must Contain Exactly Three Letters')
                    # window is closed after trying an incorrect input
                    if initials == None:
                        break
            root.destroy()
            if initials != None:
                initials = initials.upper()
            return initials

        """
        writes new scores into scores.txt
        """
        def write_scores(scores):
            scores = rules.sort_scores(scores)
            writer = open('scores.txt', 'w')
            for initial, score in scores:
                writer.write(initial + " " + str(score) + "\n")
            writer.close()

        """
        ends the game and calculates user's scores; if individuals' score is in
        the top 5, it prompts for user's initials and adds the score into
        scores.txt
        """
        def end_game():

            global playing
            playing = False
            global player_score

            """
            closes window and opens end game window
            """
            W.destroy()
            global E
            E = Tk()
            E.title('Frogger50')

            # window characteristics
            screen_w = E.winfo_screenwidth()
            screen_h = E.winfo_screenheight()
            window_x = screen_w/2 - cw/2
            window_y = screen_h/2 - ch/2
            E.geometry('{}x{}+{}+{}'.format(cw,ch,window_x,window_y))
            E.resizable(width=FALSE, height=FALSE)

            # end screen info
            es_title = Label(master = E, text = 'Game Over',
                             font = ('Impact', 80))
            es_score = Label(master = E, text = 'Score: {}'.format(player_score),
                             font = ('Futura', 48))
            restart = Button(master = E, text = 'Main Menu', command = erst,
                             font = ('Impact', 52))
            es_title.pack()
            es_score.pack(ipady=0.2*ch)
            restart.pack(ipady=0.1*ch)

            # generate scores list from scores.txt
            lookup = open('scores.txt', 'r')
            scores = []
            num_lines = 0
            for line in lookup:
                num_lines += 1
                text = line.rstrip('\n')
                initial, score = text.split(' ')[0], int(text.split(' ')[1])
                scores.append((initial, score))
            lookup.close()

            # update scores.txt if necessary
            if num_lines < 5:
                initials = score_prompt()
                if initials == None:
                    return
                scores.append((initials, player_score))
                write_scores(scores)

            elif num_lines == 5:
                # new score is greater than lowest
                if scores[4][1] < player_score:
                    initials = score_prompt()
                    if initials == None:
                        return
                    del scores[4]
                    scores.append((initials, player_score))
                    write_scores(scores)

        """
        initalizes all game functions and values
        """
        global player_score
        player_score = 0
        global playing
        playing = True
        global num_ticks
        num_ticks = 0
        global board
        board = rules.new()
        draw(board)
        ticker()

        # keyboard listener
        if playing:
            C.focus_set()
            C.bind('<Key>', key)

        # updates board after each tick
        W.bind('<<tick>>', update)

    """
    initializes the window, main menu, and high score page
    """

    W = Tk()

    W.title('Frogger50')

    # window characteristics
    screen_w = W.winfo_screenwidth()
    screen_h = W.winfo_screenheight()
    window_x = screen_w/2 - cw/2
    window_y = screen_h/2 - ch/2

    # define window dimensions, and opening location
    W.geometry('{}x{}+{}+{}'.format(cw,ch,window_x,window_y))

    # do not allow resizing of window
    W.resizable(width=FALSE, height=FALSE)

    # command to play game
    def ply():
        title.pack_forget()
        author.pack_forget()
        high_scores.pack_forget()
        play.pack_forget()
        start_game()

    # command to high score screen
    def scr():
        title.pack_forget()
        author.pack_forget()
        high_scores.pack_forget()
        play.pack_forget()
        hs_title.pack()
        ordered_scores.pack(ipady=0.1*ch)
        menu.pack(ipady=0.1*ch)

    # command for restarting window from main menu
    def rst():
        W.destroy()
        main()

    # command for leaving end screen and restarting window
    def erst():
        global E
        E.destroy()
        main()

    # remember main menu information
    play = Button(master = W, text = 'Play!', command = ply,
                  font = ('Futura', 52))

    high_scores = Button(master = W, text = 'High Scores', command = scr,
                         font = ('Futura', 52))

    title = Label(master = W, text = 'Frogger50',
                  font = ('Impact', 100, 'bold'))

    author = Label(master = W, text = 'Creator: Collin Price',
                   font = ('Impact', 24))

    # lookup top scores from scores.txt, and save as string
    lookup = open('scores.txt', 'r')
    line_number = 0
    text = ''
    for line in lookup:
        line_number += 1
        text = text + '{}. '.format(str(line_number)) + line

    # remember high score menu info
    hs_title = Label(master = W, text = 'High Scores',
                     font = ('Impact', 80, 'bold'))
    ordered_scores = Label(master = W,
                           text = '{}'.format(text),
                           font = ('Impact', 48))
    menu = Button(master = W, text = 'Main Menu', command = rst,
                  font = ('Futura', 52, 'bold'))

    # displays main menu
    title.pack()
    play.pack(ipady=0.1*ch)
    high_scores.pack(ipady=0.2*ch)
    author.pack(ipady=0.5*ch)

    # open window
    W.mainloop()

if __name__ == "__main__":
    main()

