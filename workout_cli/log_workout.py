import json

with open('exercise_lib.json', 'r') as read_file:
    exercise_lib = json.load(read_file)
    control_lib = {**exercise_lib}


def define_exercise():
    exercise = {
        'full_name': input('Full name of exercise: '),
        'abbreviation': input('Short name: '),
        'equipment': input('Needed equipment: '),
        'description': input('Enter short description: ')
    }
    return exercise


def unknown_exercise():
    print('\nUknown exercise! The available exercises are: ')
    for exercise in exercise_lib.values():
        print(exercise['full_name'])
    user_wants_new_exercise = input('Make new exercise? (y/n) ')
    if user_wants_new_exercise == 'y':
        exercise = define_exercise()
        exercise_lib[exercise['full_name'].lower()] = exercise
    print()


def main():
    rounds = int(input('Enter number of rounds: '))
    exercise_reps = []
    while True:
        exercise = input('Enter name of exercise: ')
        if exercise == "-1":
            break
        if exercise.lower() not in exercise_lib:
            unknown_exercise()
        reps = int(input('Enter number of reps: '))
        if reps == -1:
            break
        exercise_reps.append((exercise, reps))

    print('Your workout:\n')
    print(f'{rounds} rounds for time of: ')
    for exercise, reps in exercise_reps:
        print(f'\t{reps} {exercise}')

    print('\nSummary: ')
    for exercise, reps in exercise_reps:
        print(f'\t{rounds*reps} {exercise}')
    print()

    if exercise_lib != control_lib:
        with open('exercise_lib.json', 'w') as write_file:
            json.dump(exercise_lib, write_file)


if __name__ == '__main__':
    main()
