#!/usr/bin/python3
""" console application module entry of the program """
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
        """does nothing when empty line/ newline characte"""
        pass

    def do_EOF(self, line):
        """ handles end of file -ctrl D - quit"""
        return True

    def do_quit(self, line):
        """ quit the console application """

        return True

    def do_creat(self, line):
        """ create object of provided class """

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
        """print created objects bof class  passes as argument """

        if (len(line) == 0):
            print("** class name missing **")
        else:
            storage.reload()
            objs = storage.all()
            line_tok = line.split(" ")
            if (len(line_tok) != 2):
                print("** instance id missing **")
            else:
                foundclass = False
                foundid = False
                for obj in objs:
                    x = obj.split(".")
                    if (x[0] == line_tok[0]):
                        foundclass = True
                    if (x[1] == line_tok[1]):
                        foundid = True
                    if (foundid is True and foundclass is True):
                        break
                if (foundclass is True and foundid is True):
                    print(objs[".".join(line_tok)])
                elif (foundclass is True and foundid is False):
                    print("** no instance found **")
                elif (foundclass is False):
                    print("** class doesn't exist **")

    def do_destroy(self, line):
        """ delete object created base on its id and class creaed from
            delete from file"""

        x = line.split(" ")
        storage.reload()
        if (len(line) == 0):
            print("** class name missing **")
        else:
            objs = storage.all()
            remove_key = ".".join(x)
            removed_key = False
            if (hasattr(sys.modules[__name__], x[0]) and len(x) == 1):
                print("** instance id missing **")
            elif (hasattr(sys.modules[__name__], x[0]) and len(x) > 1):
                for key, value in objs.items():
                    class_name = key.split('.')
                    if (key == remove_key):
                        removed_key = True
                        del objs[remove_key]
                        storage.objects(objs)
                        storage.save()
                        break
                if (removed_key is False):
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
        else:
            foundclass = False
            for key, value in obj.items():
                x = key.split(".")[0]
                if (x == line):
                    foundclass = True
                    print(value)
            if (foundclass is False):
                print("** class doesn't exist **")

    def do_update(self, line, dic={}):
        """update instance attributes already create"""

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
            else:
                line_tok = line.split(" ")
                if (len(line_tok) == 1):
                    for key in all_objs:
                        foundclass = False
                        if (key.split(".")[0] == line_tok[0]):
                            foundclass = True
                            break
                    if (foundclass):
                        print("** instance id missing **")
                    else:
                        print("** class doesn't exist **")
                elif (len(line_tok) == 2):
                    keyfound = False
                    for key in all_objs:
                        if (key.split(".")[1] == line_tok[1]):
                            keyfound = True
                            break
                    if(keyfound):
                        print("** attribute name missing **")
                    else:
                        print("** no instance found **")
                elif (len(line_tok) == 3):
                    print("** value missing **")
                else:
                    key = line_tok[0] + "." + line_tok[1]
                    attr_dict = all_objs[key].to_dict()
                    attr_dict[line_tok[2]] = line_tok[3]
                    mod_name = sys.modules[__name__]
                    cls = getattr(mod_name, attr_dict["__class__"])
                    obj = cls(**attr_dict)
                    all_objs[key] = obj
                    storage.objects(all_objs)
                    storage.save()

    def __parse_for_cmd(self, line):

        line = re.search(r'[^{]*', line)[0]
        line = line.replace('(', '').replace('"', ' ')\
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

        if (len(line.split(".")) > 1):
            dic = None
            dic_present = re.search(r'\{[^}]*}', line)
            if (dic_present):
                dic = eval(dic_present[0])
                line = self.__parse_for_cmd(line)
            else:
                line = self.__parse_for_cmd(line)

            if hasattr(self, "do_" + line[0]):
                method = getattr(self, "do_" + line[0])
                args = ' '.join(line[1:])
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
        storage.reload()
        obj = storage.all()
        count = 0
        for key in obj:
            if (key.split(".")[0] == line):
                count = count + 1
        print(count)


if __name__ == "__main__":

    HBNBCommand().cmdloop()
