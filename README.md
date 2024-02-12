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
    -create application objects which include
        -users - any user of the system, 
        -places - residntial location
        -cities
        -states
        -amenities - provided
        -review - customer review
     - creating objects takes two form
        $creat <object> ie creat User
        or
        #<object>.creat() i.e
        $User.creat()

apart from just creating objects the console appliction support
    >destroy <obname> <objid> - destroy object already created
     - $<object-type>.destroy(<object id>) or destroy <object-type> <object id>
     ie
        $user.destroy("uid134") or $destroy User uid134
    > update - update value of existing object
      - update with <key> <value> or <{dictioanry}>
    > all - this display all objects created based on type or all crated
        $all - all objects created
        $all User - all users creatd
        $User.all() - all users

        can be all , all <type>, <type>.all()

    > show - show specific object
        $show <object type> <object id>
        or
        $<object-type>.show(<object id>)

<author><kiptooharon.hk@gmail.com>
