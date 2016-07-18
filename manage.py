import argparse
from textwrap import dedent


def list_func(args):
    import os
    keyboard_module_list = os.listdir('heconvert/keyboard')
    keyboard_module_list.remove('__init__.py')
    print(keyboard_module_list)


def create(args):
    import os
    keyboard_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'heconvert', 'keyboard')
    os.chdir(keyboard_dir)
    os.mkdir(args.name)
    os.chdir(os.path.join(keyboard_dir, args.name))
    open('__init__.py', 'a')
    with open('core.py', 'a') as f:
        f.write(dedent("""\
        # Write your converting algorithm and classes here
        def h2e(string):
            # convert hangul to english
            pass


        def e2h(string):
            # convert english to hangul
            pass
        """))
    with open('interface.py', 'a') as f:
        fmt = dedent("""\
        # AUTO-GENERATED FILE. DO NOT MODIFY
        from heconvert.keyboard.{module}.core import e2h, h2e
        from heconvert.misc.util import Namespace

        KEYBOARD = Namespace(e2h=e2h, h2e=h2e)
        """.format(module=args.name))
        f.write(fmt)
    with open('mapping.py', 'a') as f:
        f.write(dedent("""\
        # Write your character-keyboard mapping here
        """))
    print('new keyboard module "{}" has been created'.format(args.name))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='heconvert management script')
    subparser = parser.add_subparsers(help='sub-command help')
    if 'list_parser':
        list_parser = subparser.add_parser('list', help='list all of registered keyboard layout')
        list_parser.set_defaults(func=list_func)
    if 'create_parser':
        create_parser = subparser.add_parser('create', help='create an new keyboard module in the "keyboard" directory')
        create_parser.add_argument('name', type=str, help='new keyboard layout name')
        create_parser.set_defaults(func=create)

    arguments = parser.parse_args()
    if not hasattr(arguments, 'func'):
        parser.print_help()
    else:
        arguments.func(arguments)
