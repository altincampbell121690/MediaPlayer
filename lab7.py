# lab7: OOP with MediaPlayer and Media classes

from mediaPlayer import MediaPlayer

fileName = "lab7input.txt"


def main():
    playList = MediaPlayer()
    playList.play()
    playList.shuffle()


main()