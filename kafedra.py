from students.education import Student
from students.disciplines import Discipline
import argparse



if __name__ == '__main__':
    arg_pars = argparse.ArgumentParser(description='Успеваемость студентов кафедры')
    arg_pars.add_argument('family', metavar='family', type=str, help='фамилия студента')
    arg_pars.add_argument('name', metavar='name', type=str, help='имя студента')
    arg_pars.add_argument('second_name', metavar='second_name', type=str, help='отчество студента')
    arg_pars.add_argument('discipline', metavar='discipline', type=str, help='дисциплина')
    arg_pars.add_argument('rate', metavar='rate', type=int, help='оценка')
    arg_pars.add_argument('test', metavar='test', type=int, help='тестовый балл')

    args = arg_pars.parse_args()

    student = Student(args.family, args.name, args.second_name)
    student.append_to_progress(Discipline(args.discipline, args.rate, args.test))
    student.save_progress()

