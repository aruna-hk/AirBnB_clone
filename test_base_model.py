class test_console(unittest.TestCase):
    """ this class test console """

    def setUp(self):
        self.BaseModel = base_model.BaseModel
        self.User = user.User
        self.Place = place.Place
        self.City = city.City
        self.State = state.State
        self.Amenity = amenity.Amenity
        self.Review = review.Review

    def test_BaseModel_model(self):
        """test BaseModel creation"""
        jstr = ''
        with patch('sys.stdout', new=StringIO()) as f:
            """creating first BaseModel """

            console.HBNBCommand().onecmd("BaseModel.creat()")
        captured_id1 = f.getvalue()
        self.assertTrue(isinstance(captured_id1, str), True)
        self.assertEqual(len(captured_id1), 37) 
        with open("file.json", "r") as file:
            jstr = json.load(file)
        dic = eval(repr(jstr))
        obj_key = "BaseModel." + captured_id1[:-1]
        obj_dict1 = dic[obj_key]
        recreated_obj = self.BaseModel(**obj_dict1)
            #recreatin object with object dictionary
        dict2 = recreated_obj.to_dict()
            #comparing if new object dictionary == existing obj dictionaty
            #should be equl recreated from same dictionaru
        self.assertTrue(dict2 == obj_dict1)

        with patch('sys.stdout', new=StringIO()) as f:
            """creating second BaseModel """

            console.HBNBCommand().onecmd("BaseModel.creat()")
 
        captured_id2 = f.getvalue()
        with open("file.json", "r") as file:
            jstr = json.load(file)
        obj_key2 = "BaseModel." + captured_id2[:-1]
       	obj_dict2 = eval(repr(jstr))
        all_str = str(dic[obj_key]) + '\n' + str(obj_dict2[obj_key2]) + '\n'
        #testing BaseModel.all()
        with patch('sys.stdout', new=StringIO()) as f:
            console.HBNBCommand().onecmd("BaseModel.all()")
        captured_all = f.getvalue()
        self.assertEqual(captured_all, all_str)

        #testing show(<id arg>)
        with patch('sys.stdout', new=StringIO()) as f:
            console.HBNBCommand().onecmd("BaseModel.show(\"{}\")".format(captured_id1[:-1]))
        show_ = f.getvalue()
        self.assertEqual(show_, str(obj_dict1) + '\n')

            #test show invalid id

        
        with patch('sys.stdout', new=StringIO()) as f:
            console.HBNBCommand().onecmd("BaseModel.show(\"invalidid\")")
        output = f.getvalue()
            
        self.assertEqual(output, "** no instance found **\n")

        #test show id not passed
        with patch('sys.stdout', new=StringIO()) as f:
            console.HBNBCommand().onecmd("BaseModel.show()")
        output = f.getvalue()
            
        self.assertEqual(output, "** instance id missing **\n")


        #test_update_BaseModel
        with patch('sys.stdout', new=StringIO()) as f:
            console.HBNBCommand().onecmd("BaseModel.update()")
        
        update_err = f.getvalue()
        self.assertEqual(update_err, "** instance id missing **\n")

        with patch('sys.stdout', new=StringIO()) as f:
            console.HBNBCommand().onecmd("BaseModel.update(\"invalid_id\")")
        
        update_err = f.getvalue()
        self.assertEqual(update_err, "** no instance found **\n") 

        with patch('sys.stdout', new=StringIO()) as f:
            u_key = "\"{}\"".format(obj_key.split('.')[1])
            console.HBNBCommand().onecmd("BaseModel.update({})".format(u_key))
        
        update_err = f.getvalue()
        self.assertEqual(update_err, "** attribute name missing **\n")

        with patch ('sys.stdout', new=StringIO()) as f:
            at_key = "name"
            u_key = "\"{}\"".format(obj_key.split('.')[1])
            console.HBNBCommand().onecmd("BaseModel.update(\"{}\", \"{}\")".format(u_key, at_key))        

        update_err = f.getvalue()
        self.assertEqual(update_err, "** value missing **\n")

        #correct update with key , value
        with patch ('sys.stdout', new=StringIO()) as f:
            at_key = "name"
            value = "kiptoo"
            u_key = "\"{}\"".format(obj_key.split('.')[1])
            console.HBNBCommand().onecmd("BaseModel.update(\"{}\", \"{}\", \"{}\")".format(u_key, at_key, value))        
            obj_dict1[at_key] = value
        with open("file.json", "r") as file:
            jstr = json.load(file)
        all_objects = eval(repr(jstr))
        updated_objects = all_objects[obj_key]
        self.assertEqual(updated_objects, obj_dict1)

        #update with dictionary
        update_with = {"age": 23, "school":"cuk"}
        obj_dict1.update(update_with)

        
        with patch ('sys.stdout', new=StringIO()) as f:
            u_key = "\"{}\"".format(obj_key.split('.')[1])
            console.HBNBCommand().onecmd("BaseModel.update(\"{}\", {})".format(u_key, str(update_with)))        
        
        with open("file.json", "r") as file:
            jstr = json.load(file)
        all_objects = eval(repr(jstr))
        updated_objects = all_objects[obj_key]
        self.assertEqual(updated_objects, obj_dict1)



        with patch ('sys.stdout', new=StringIO()) as f:
            console.HBNBCommand().onecmd("BaseModel.count()")

        count = f.getvalue()
        self.assertEqual(count, "2\n")

        #test destroy obj
            #destroy obj_key
        uid1 = "\"" + obj_key.split('.')[1]
        console.HBNBCommand().onecmd("BaseModel.destroy({})".format(uid1))        
        with patch('sys.stdout', new=StringIO()) as f:
            console.HBNBCommand().onecmd("BaseModel.count()")
        out = f.getvalue()
        self.assertEqual(out, "1\n")
        uid2 = "\"" + obj_key2.split('.')[1]
#        console.HBNBCommand().onecmd("BaseModel.destroy({})".format(uid2))       
 #       with patch('sys.stdout', new=StringIO()) as f:
  #          console.HBNBCommand().onecmd("BaseModel.count()")
   #     out = f.getvalue()
    #    self.assertEqual(out, "0\n")




       

if __name__ == "__main__":
    unittest.main()
