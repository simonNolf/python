from playsound import playsound


class Sound_effects:
    """
    This class will play any mp3 file specified, but I can't find a way
    to run it when I run the mainloop ! This is of course a optional functionality for more fun !
    """

    @property
    def welcome(self):
        return playsound("sounds/welcome.mp3")
