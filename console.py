#!/usr/bin/python3
"""a program that contains the entry point of the command interpreter"""
import cmd


class HBNBCommand(cmd.Cmd):
    """
<<<<<<< HEAD
    provides a prompt for user input, allowing users to execute 
    basic commands and exit the program.
    
    """
=======
        provides a prompt for user input.
        recieves and execute basic commands.
        Exits the program on user temination.
    """

    intro = "Welcome to the HBNB shell. Type help to list commands.\n"
>>>>>>> cb7a27018b1be9175191a6af7a6e6bd1010a3c0d
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """Exit on EOF (Ctrl+D)"""
        return True

    def do_create(self, arg):
        """
            Creates a new instance of BaseModel

            Requires:
                class name to instantiate(BaseModel)

            Usage:
                create BaseModel
        """
        if not arg:
            print("** class name missing **")
        elif arg[0] != "BaseModel":
            print("** class doesn't exist **")
        else:
            new_instance = BaseModel()
            storage.save()
            print(new_instance["id"])

    def do_show(self, arg):
        """
            Prints the string representation of an instance

            Requires:
                class name(BaseModel)
                instance id

            Usage:
                show BaseModel [instance id]
        """
        if not arg:
            print("** class name missing **")
        elif arg[0] != "BaseModel":
            print("** class doesn't exist **")
        elif len(arg) < 2:
            print("** instance id missing **")
        else:
            print("other logic")

    def do_destroy(self, arg):
        """
            Deletes an instance based on the class name and id

            Requires:
                class name(BaseModel)
                instance id

            Usage:
                destroy BaseModel [instance id]
        """
        print(arg)

    def do_all(self, arg):
        """
            Prints all the string representation of an or all instance

            Requires:
               [optional]  class name(BaseModel)

            Usage:
                all : print string representation
                      of all instance
                all BaseModel : print string representation
                                based on the specified class
        """
        print(arg)

    def do_update(self, arg):
        """
            Updates an instance based on the class name and id by
            adding or updating attribute

            Requires:
                class name(BaseModel)
                instance id

            Usage:
                show BaseModel [instance id] [attribute_key] ["value"]

            Constraints:
                Only one attribute can be updated at a time
        """
        print(arg)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
