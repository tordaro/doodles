

def main():
    rounds = int(input('Enter number of rounds: '))
    exercise_reps = []
    while True:
        exercise = input('Enter name of exercise: ')
        reps = int(input('Enter number of reps: '))
        exercise_reps.append((exercise, reps))
        is_done = input('Done? (y/n) ')
        if is_done == 'y':
            break

    print('Your workout: ')
    print(f'\t{rounds} rounds for time of: ')
    for exercise, reps in exercise_reps:
        print(f'\t\t{reps} of {exercise}')

    print('Summary: ')
    for exercise, reps in exercise_reps:
        print(f'\t{rounds*reps} reps of {exercise}')


if __name__ == '__main__':
    main()
