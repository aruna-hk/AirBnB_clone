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
        #load arguments
        #split key with .
        #check if first token == line printif
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
        #split line wit rspect to "space"
        #join line with . === key
        #load objects from a file
        #compare keys with key if equal remove from dict
        #save to file
        x = line.split(" ")
        storage.reload()
        if (len(line) == 0):
            print("** class name missing **")
        else:
            x = line.split(" ")
            objs = storage.all()#objects reloaded
            if (len(x) == 1):
                cls = False
                for key in objs:
                    if (key.split(".")[0] == x[0]):
                        cls = True
                if cls:
                    print("** instance id missing **")
                else:
                    print("** class doesn't exist **")
                del objs
            elif (len(x) >= 2):
                for key in objs:#search for x , key to remove
                    keypair = key.split(".")
                    clsflag = False
                    idflag = False

                    if (keypair[0] == x[0]):
                        clsflag = True
                    if (keypair[1] == x[1]):
                        idflag = True
                    if (clsflag is True and idflag is True):
                        break

                if (idflag is True and clsflag is True):
                    val = objs.pop(".".join(x))
                    del val
                    storage.objects = objs
                    storage.save()
                elif (idflag is False and clsflag is True):
                    print("** no instance found **")
                elif (clsflag is False):
                    print("** class doesn't exist **")


    def do_all(self, line):
        """ print all instance of objects from provided class"""

        #load objects
        #split key with .
        #compare split with line is == print value
        storage.reload()#reload objects
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
        #load values from file
        #join args with . 
        #compare keys with joined args
        #if === seach deeper, to 
        storage.reload()#rload created objects
        all_objs = storage.all()#load all objects
        if (len(dic) != 0):
            obj_id = '.'.join(line.split(' '))
            try:
                all_objs[obj_id].update(dic)
            except KeyError as e:
                pass
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
                    all_objs[line_tok[0] + "." + line_tok[1]][line_tok[2]] = line_tok[3]
                    storage.objects = all_objs
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
