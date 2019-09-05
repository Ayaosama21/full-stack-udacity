# Log Analysis Project

Description:

using psycopg2 module to connect the database, our task is to create a tool to report (text file) based on the daya in the database


#### Requiers:

* install VM(virtual machine)
* install vagrant
* run vagrant up in our terminal
* run vagrant ssh in our terminal


#### Setup Project:

  1.Install vagrant and VM
  2.Download or Clone full-stack-udacity
  3. Download the [data](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip) from here.
  4.unzip the file after downloading it. the file is called newsdata.sql.
  5.copy the newsdata.sql file and content of this current repositery.
  [Here](https://github.com/Ayaosama21/full-stack-udacity).
  

#### Lanuching the Virtual Machine:

  1.Launch the Vagrant VM by using command:
  
      $ vagrant up
      
  2. log into using command:
  
    $ vagrant ssh
      
  3. change directory into /vagrant then using ls.
  
  
#### Setting the Database:

  1. use the command to load data:
  
    $ cd vagrant
    $ psql -d news -f newsdata.sql
  
  2. to connect the database use this command :
  
    $ psql -d news
    
  3. you can create article view.
  
  
#### Running our code:

    1.to run log.py using :
        
        $python3 log.py
