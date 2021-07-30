import random

scale = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
standard_tuning = ["E", "A", "D", "G", "B", "E"]


def get_fret(string, note):
    displacement = scale.index(string)
    step = scale.index(note)
    return (step + 12 - displacement) % 12


def guess_fret():
    note = random.choice(scale)
    string = random.choice(standard_tuning)
    ans = get_fret(string, note)
    user_ans = -1
    while ans != user_ans:
        user_ans = int(input(f"Enter fret for a {note} on {string}: "))
        if ans == user_ans:
            print("Yay!")
        else:
            print("Wrong answer.")


if __name__ == '__main__':
    guess_fret()
