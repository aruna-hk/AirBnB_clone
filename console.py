#!/usr/bin/python3
""" console application module entry of the program
    accept commands, process the commands ad pass the hand over
    command to command handler """

import cmd
from models.base_model import BaseModel
from models import storage
import re
from models.state import State
from models.user import User
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
import sys


class HBNBCommand(cmd.Cmd):
    """ class cmd processor, inherit cmd module """

    prompt = "(hbnb) "

    def emptyline(self):
        """does nothing when empty line
            does nothing when newline character is entered"""

        pass

    def do_EOF(self, line):
        """ handles end of file -ctrl D - quit"""

        return True

    def do_quit(self, line):
        """ quit the console application """

        return True

    def do_creat(self, line):
        """ create object of provided class """

        storage.reload()
        if (len(line) == 0):
            print("** class name missing **")
        else:
            try:
                x = getattr(sys.modules[__name__], line)
                newobj = x()
                print(newobj.id)
                storage.save()
            except AttributeError as e:
                print("** class doesn't exist **")

    def do_show(self, line):
        """print created objects of class  passes as argument """

        if (len(line) == 0):
            print("** class name missing **")
        elif (hasattr(sys.modules[__name__], line.split(' ')[0])):
            storage.reload()
            objs = storage.all()
            line_tok = line.split(' ')
            if (len(line_tok) != 2):
                print("** instance id missing **")
            else:
                found = False
                kk = '.'.join(line_tok)
                for obj in objs:
                    if (obj == kk):
                        found = True
                if (found):
                    print(objs[".".join(line_tok)])
                else:
                    print("** no instance found **")
        else:
            print("** class doesn't exist **")

    def do_destroy(self, line):
        """ delete object created base on its id and class creaed from
            delete from file"""

        storage.reload()
        x = line.split(" ")
        if (len(line) == 0):
            print("** class name missing **")
        else:
            objs = storage.all()
            remove_key = ".".join(x)
            if (hasattr(sys.modules[__name__], x[0]) and len(x) == 1):
                print("** instance id missing **")
            elif (hasattr(sys.modules[__name__], x[0]) and len(x) > 1):
                try:
                    del objs[remove_key]
                    storage.objects(objs)
                    storage.save()
                except KeyError as e:
                    print("** no instance found **")
            else:
                print("** class doesn't exist **")

    def do_all(self, line):
        """ print all instance of objects from provided class"""

        storage.reload()
        obj = storage.all()
        if (len(line) == 0):
            for key, value in obj.items():
                print(value)
        elif (hasattr(sys.modules[__name__], line.split(' ')[0])):
            for key, value in obj.items():
                x = key.split(".")[0]
                if (x == line.split(' ')[0]):
                    print(value)
        else:
            print("** class doesn't exist **")

    def do_update(self, line, dic={}):
        """update instance attributes already createD"""

        storage.reload()
        all_objs = storage.all()
        if (len(dic) != 0):
            try:
                obj_id = '.'.join(line.split(' '))
                obj = all_objs[obj_id].to_dict()
                obj.update(dic)
                new_obj = getattr(sys.modules[__name__], obj["__class__"])
                all_objs[obj_id] = new_obj(**obj)
                storage.objects(all_objs)
                storage.save()
            except Exception as e:
                print("** no instance found **")
            storage.save()
        else:
            if (len(line) == 0):
                print("** class name missing **")
            elif (hasattr(sys.modules[__name__], line.split(' ')[0])):
                line_tok = line.split(" ")
                if (len(line_tok) == 1):
                    print("** instance id missing **")
                elif (len(line_tok) == 2):
                    print("** attribute name missing **")
                elif (len(line_tok) == 3):
                    print("** value missing **")
                else:
                    value = ' '.join(line_tok[3:])
                    key = line_tok[0] + "." + line_tok[1]
                    attr_dict = all_objs[key].to_dict()
                    attr_dict[line_tok[2]] = value.replace('"', '')
                    mod_name = sys.modules[__name__]
                    cls = getattr(mod_name, attr_dict["__class__"])
                    obj = cls(**attr_dict)
                    all_objs[key] = obj
                    storage.objects(all_objs)
                    obj.save()
            else:
                print("**class doesn't exist ***")

    def __parse_for_cmd(self, line):
        """ helper function to format string to be passed to
            command processors"""

        line = re.search(r'[^{]*', line)[0]
        line = line.replace('(', '').replace('"', ' ').replace('\'', ' ')\
            .replace(',', ' ').replace('.', ' ').replace(')', '')
        line = line.split(' ')
        line[0], line[1] = line[1], line[0]

        lines = []
        for i in range(len(line)):
            if (len(line[i]) > 0):
                lines.append(line[i].replace(' ', ''))
        del line
        return lines

    def default(self, line):
        """hijack deault processing of lines such to handle
            <class>.<comman>()
         """
        if (len(line.split(".")) > 1):
            dic = None
            dic_present = re.search(r'\{[^}]*}', line)
            if (dic_present):
                dic = eval(dic_present[0])
                lin = self.__parse_for_cmd(line)
            else:
                lin = self.__parse_for_cmd(line)

            if hasattr(self, "do_" + lin[0]):
                method = getattr(self, "do_" + lin[0])
                args = ' '.join(lin[1:])
                if (dic):
                    method(args, dic)
                else:
                    method(args)
            else:
                print("*** Unknown syntax: {}".format(line))
        else:
            pass
            super().default(line)

    def do_count(self, line):
        """count created objects all obj is no arguments
            or count specific class objects """

        storage.reload()
        obj = storage.all()
        if (len(line) == 0):
            print(len(obj))
        elif (hasattr(sys.modules[__name__], line.split(' ')[0])):
            count = 0
            for key in obj:
                if (key.split(".")[0] == line):
                    count = count + 1
            print(count)
        else:
            print("** class doesn't exist **")


if __name__ == "__main__":
    """ execute console if not imported """

    HBNBCommand().cmdloop()
