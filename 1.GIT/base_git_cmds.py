#!/usr/bin/python3
import argparse
import subprocess
import os

DIR_PATH = str(os.getcwd())

def check_git_status(path_check):
    os.chdir(path_check)
    result = subprocess.run(['git', 'status'], stdout=subprocess.DEVNULL)
    return result.returncode


def clone(args):
    try:
        while os.path.exists(args.dest):
            print('Такая директория уже существует. Создать клон не получиться. ')
            args.dest = input("Укажите другой путь...\n")
            print(f'Директория {args.dest}')
        else:
            print(f'Директория {args.dest}')
            result = subprocess.run(['git', 'clone', f'{args.src}', f'{args.dest}'], encoding='utf-8',
                                    stdout=subprocess.PIPE)
    except:
        name = args.src[args.src.rfind('/') + 1:-4]
        print(name)
        while name in os.listdir('.'):
            print('Такая директория уже существует. Создать клон не получиться.')
            name = input("Укажите другой путь...\n")
            print(f'Директория {name}')
        else:
            print(f'Все норм, клонируем репозиторий в директорию {name}')
            result = subprocess.run(['git', 'clone', f'{args.src}'], encoding='utf-8', stdout=subprocess.PIPE)
            print(result.stdout)
            print(result.returncode)

            result = subprocess.run(['cd', '/home/eugen/git-test/111/Md-SA2-24-23'], encoding='utf-8', stdout=subprocess.PIPE)
            print(result.stdout)
            print(result.returncode)



def create_branch(args):
    if check_git_status(args.dest) != 0:
        print(f'Указанная директория не содерижит репозиторий. Не могу создать новую ветку.')
    else:
        branch_list = subprocess.run(['git', 'branch'], encoding='utf-8', stdout=subprocess.PIPE).stdout.split()
        if args.branch in branch_list:
            print(f"Ветка с именем {args.branch} уже существует.")
        else:
            result = subprocess.run(['git', 'checkout', '-b', f'{args.branch}'], stdout=subprocess.DEVNULL)
            # print(result.stdout)
            print(f'Вы в новой ветке {args.branch}')


def create_commit(args):
    print(f'{args.msg}')
    result = subprocess.run(['git', 'add', '--all'])
    print(result.stdout)
    result = subprocess.run(['git', 'commit', '-m', f'{args.msg}'])
    print(result.stdout)

def make_push(args):
    print(f'{args.msg}')
    result = subprocess.run(['git', 'branch', '--show-current'], encoding='utf-8', stdout=subprocess.PIPE)
    print(f'Мы находимся в ветке {result.stdout}')
    result = subprocess.run(['git', 'push'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    print(f'Код выполнения задачи {result.returncode}')


parser = argparse.ArgumentParser()
subparsers = parser.add_subparsers(title='subcommands',
                                   description='valid subcommands',
                                   help='description')

# -----------Команда клонирования репозитария в указанную директорию------
clone_parser = subparsers.add_parser('clone', help='create new db')
clone_parser.add_argument(metavar='db-filename', dest='src',
                          default='DFLT_DB_NAME', help='source')
clone_parser.add_argument('--destination', '-d', dest='dest', #default=DIR_PATH,
                          help='destination', )
clone_parser.set_defaults(func=clone)

# -----------Создание новой ветки и переключение на неё-------------------
create_branch_parser = subparsers.add_parser('create_branch', help='Create new branch & go into. Enter name of branch')
create_branch_parser.add_argument(metavar='branch_name', dest='branch',
                                  help='branch')
create_branch_parser.add_argument('--destination', '-d', dest='dest', default=DIR_PATH,
                                  help='destination', )
create_branch_parser.set_defaults(func=create_branch)

# -----------Добавление файлов в индекс и создание коммита-----------------
create_commit_parser = subparsers.add_parser('create_commit', help='Create new branch & go into. Enter name of branch')
create_commit_parser.add_argument('--message', '-m', dest='msg', default='new_commit',
                                  help='Enter message.', )
create_commit_parser.set_defaults(func=create_commit)

# -----------Отправка ветки на удаленный репозиторий-----------------------
make_push_parser = subparsers.add_parser('make_push', help='Create new branch & go into. Enter name of branch')
make_push_parser.set_defaults(func=make_push)

if __name__ == '__main__':
    args = parser.parse_args()
    if not vars(args):
        parser.print_usage()
    else:
        args.func(args)
