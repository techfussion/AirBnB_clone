#!/usr/bin/python3
"""a program that contains the entry point of the command interpreter"""
import cmd

class HBNBCommand(cmd.Cmd):
    """
    provides a prompt for user input, allowing users to execute 
    basic commands and exit the program.
    
    """
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """Exit on EOF (Ctrl+D)"""
        return True

if __name__ == '__main__':
    HBNBCommand().cmdloop()
