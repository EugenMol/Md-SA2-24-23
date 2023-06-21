#!/usr/bin/python3
import argparse
import shutil
import subprocess
import os

DIR_PATH = str(os.getcwd())


def create(args):
    shutil.copy(args.src, args.dest)


def check_git_status(path_check):
    os.chdir(path_check)
    result = subprocess.run(['git', 'status'])
    print(f'Результат выполнения комнады: {result.returncode}')
    return result.returncode


def clone(args):
    print(args.dest)
    result = subprocess.run(['git', 'clone', f'{args.src}', f'{args.dest}'])
    print(result.stdout)


def create_branch(args):
    if check_git_status(args.dest) != 0:
        print(f'Здесь нет репозитория. Не могу создать новую ветку.')
    else:
        result = subprocess.run(['git', 'checkout', '-b', f'{args.branch}'])
        print(result.stdout)
        print(f'Вы в новой ветке {args.branch}')


def create_commit(args):
    print(f'{args.msg}')
    result = subprocess.run(['git', 'add', '--all'])
    print(result.stdout)
    result = subprocess.run(['git', 'commit', '-m', f'{args.msg}'])
    print(result.stdout)

# def make_push(args):
#     print(f'{args.msg}')
#     result = subprocess.run(['git', 'add', '--all'])
#     print(result.stdout)
#     result = subprocess.run(['git', 'commit', '-m', f'{args.msg}'])
#     print(result.stdout)


parser = argparse.ArgumentParser()
subparsers = parser.add_subparsers(title='subcommands',
                                   description='valid subcommands',
                                   help='description')

# -----------Команда клонирования репозитария в указанную директорию------
clone_parser = subparsers.add_parser('clone', help='create new db')
clone_parser.add_argument(metavar='db-filename', dest='src',
                          default='DFLT_DB_NAME', help='source')
clone_parser.add_argument('--destination', '-d', dest='dest', default=DIR_PATH,
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

if __name__ == '__main__':
    args = parser.parse_args()
    if not vars(args):
        parser.print_usage()
    else:
        args.func(args)
