#!/usr/bin/python3
""" console application module entry of the program """
import cmd
from models.base_model import BaseModel
from models import storage
from models.state import State
from models.user import User
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

class HBNBCommand(cmd.Cmd):
    """ class cmd processor, inherit cmd module """

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
        elif (line == "BaseModel"):
            newobj = BaseModel()
            print(newobj.id)
            storage.save()
        elif (line == "User"):
            newuser = User()
            print(newuser.id)
            storage.save()
        elif (line == "State"):
            newstate = State()
            print(newstate.id)
            storage.save()
        elif (line == "City"):
            newcity = City()
            print(newcity.id)
            storage.save()
        elif (line == "Place"):
            newplace = Place()
            print(newplace.id)
            storage.save()
        elif (line == "Amenity"):
            newA = Amenity()
            print(newA.id)
            storage.save()
        elif (line == "Review"):
            newRev = Review()
            print(newRev.id)
            storage.save()
        else:
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

               
    def do_update(self, line):
        """update instance attributes already create"""
        #load values from file
        #join args with . 
        #compare keys with joined args
        #if === seach deeper, to 
        storage.reload()#rload created objects
        if (len(line) == 0):
            print("** class name missing **")
        else:
            line_tok = line.split(" ")
            all_objs = storage.all()#load all objects
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

    def default(self, line):
        parts = line.split(".")
        if (len(parts) > 1):
            parts.reverse()
            parts[0] = parts[0][:-2]
            method = "do_" + parts[0]
            if hasattr(self, method):
                methodn = getattr(self, method)
                lis2 = parts[1:]
                methodn(" ".join(lis2))
            else:
                print("*** Unknown syntax: {}".format(line))
        else:
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
