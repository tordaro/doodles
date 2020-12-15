import os
import random
import time
import datetime
import pandas as pd
import sqlalchemy as db
from sqlalchemy import Column, Integer, String, Float, DateTime
from sqlalchemy.ext.declarative import declarative_base

engine = db.create_engine("sqlite:///calcula.db", echo=False)
Base = declarative_base()


class Calculations(Base):
    __tablename__ = "calculations"
    id = Column(Integer, primary_key=True)
    problem = Column(String)
    solution = Column(Integer)
    time = Column(Float)
    category = Column(String)
    level = Column(Integer)
    operand = Column(String)
    date = Column(DateTime)
    session = Column(Integer)
    user = Column(String)
    

def categorize(problem):
    parsed = []
    for char in problem:
        if char in '0123456789':
            parsed.append('N')
        else:
            parsed.append(char)
    return ''.join(parsed)


def slice_operators(problem):
    parsed = []
    for char in problem:
        if char in '+-*/':
            parsed.append(char)
    return ''.join(parsed)


def parse(problem):
    category = categorize(problem)
    operators = slice_operators(problem)
    level = category.count('N') - 1
    return category, level, operators


def addition(lb1, up1, lb2, up2):
    d1 = random.randint(lb1, up1)
    d2 = random.randint(lb2, up2)
    solution = d1 + d2
    problem = f"{d1}+{d2}"
    return problem, solution


def game(user, num_problems, func, lb1, up1, lb2, up2):
    mapping = str.maketrans({"+": " + ", "-": " - ", "*": " * ", "/": " / "})
    Base.metadata.create_all(engine)
    Session = db.orm.sessionmaker(bind=engine)
    session = Session()
    last_row = session.query(Calculations).order_by(Calculations.id.desc()).first()
    if last_row:
        session_id = last_row.session + 1
    else:
        session_id = 1
    for i in range(num_problems):
        problem, solution = func(lb1, up1, lb2, up2)
        output_problem = problem.translate(mapping) + " = "
        user_solution = solution + 1
        tic = time.perf_counter()
        is_first_try = True
        while user_solution != solution:
            try:
                if not is_first_try:
                    print("Doh!")
                user_solution = int(input(output_problem))
                is_first_try = False
            except ValueError:
                print("Answer must be an integer")
            # except KeyboardInterrupt:
            #     print("\nYou're not quitting. Fuck you!")

        toc = time.perf_counter()
        tot_time = toc - tic
        category, level, operators = parse(problem)
        date = datetime.datetime.now()
        complete_answer = Calculations(
            problem = problem,
            solution = solution,
            time = tot_time,
            category = category,
            level = level,
            operand = operators,
            date = date,
            session = session_id,
            user = user
        )
        session.add(complete_answer)
    session.commit()


def main():
    os.system("clear")
    print("\n" + f"{'WELCOME TO CALCULA':*^40}" + "\n")
    print("\n" + f"{'Let us take your brain for a spin!':^40}" + "\n")
    print("\nThe problem: N1 + N2 = ?\n")
    lb1 = int(input("Enter lower bound for N1: "))
    ub1 = int(input("Enter upper bound for N1: "))
    lb2 = int(input("Enter lower bound for N2: "))
    ub2 = int(input("Enter upper bound for N2: "))
    iterations = int(input("Enter number of problems you would like: "))
    game("tord", iterations, addition, lb1, ub1, lb2, ub2)


if __name__ == "__main__":
    main()
