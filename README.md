AIRBNB CONSOLE APPLICATION

This is command processor application, it accepts commands, process command and hand the command
to relevant function to handle the command
The console inherits cmd python built in module
To execute via command line
do:
    git clone https://github.com/aruna-hk/AirBnB_clone
    cd to the cloned repo
     execute
        ./console.py
    The console doe the following

    - create objects
        -users
        -places
        -cities
        -states
        -amenitie
        -review
        it can b configured to creat different objects as user wishes by importing classes of objects
        to be created to console file because it uses hasattr(current-module, <attribute_name>) to create objects
        
        creating objects can take two  forms
            $creat <object> ie creat User
            or
            #<object>.creat() i.e  $User.creat()

    console application  also support the following command

    - destroy <obname> <objid> - destroy object already created

      <object-type>.destroy(<object id>) or destroy <object-type> <object id>
      ie

        $user.destroy("uid134") or $destroy User uid134

    - update - update value of existing object
      - update with <key> <value> or <{dictioanry}>
    - all - this display all objects created based on type or all crated
        $all - all objects created
        $all User - all users creatd
        $User.all() - all users

        can be all , all <type>, <type>.all()
    - other commands include count and show

   - example 
    $ git clone https://github.com/aruna-hk/AirBnB_clone.git
    $ cd AirBnB_clone
    $ ./console.py
    (hbnb) creat User
     <some output id of instance created>
    (hbnb) User.creat()
     <some output id of instance created>
    $
    thats just example to create user
    objects created are stored in file name "file.json"
    to hange the output file cd models/engine and edit "file_storage.py" file

    on the parent directory there is a test for the console application
    before test begin file name test_file.json is overwriten with empty json object before tests
    begin so make sure to open test_console.py and change the file to write to in setup() function if u hav file
    named test_file.json to avoid loosing data

<author><kiptooharon.hk@gmail.com>
