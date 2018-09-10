# What this project is ?
This is the first project of the Full Stack Web Developer Nanodegree.

The opject of this project : create a reporting tool that prints out reports (in plain text) based on the data in the database. This reporting tool is a Python program using the psycopg2 module to connect to the database.

## How do u run this project ?

### 1. Download and configure: Virtual Machine & Database

**First step:** Download and install [Vagrant](https://www.vagrantup.com/) and [VirtualBox](https://www.virtualbox.org/wiki/Download_Old_Builds_5_1).

**Second step:** Download the VM configuration from files [HERE](https://s3.amazonaws.com/video.udacity-data.com/topher/2018/April/5acfbfa3_fsnd-virtual-machine/fsnd-virtual-machine.zip).

**Third step:** Download DataBase from [This link](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip).

**Fourth step:** Download the python programs (`myTool.py` and `database.py`) from my files the i have sent to you. Then, copy them and the Database file to  the `vagrant/` (one of the folders that you downloaded before in Second step).

**Fifth step:** Open your terminal then run this commands:

```
# Install & Configure VM
# 1.Change the path to vagrant
cd /path/to/vagrant

# Run vagrant up
vagrant up

#  Log into machine
vagrant ssh

# To load the data, cd into the vagrant directory   
cd /vagrant 
# Then use the command
psql -d news -f newsdata.sql

# Close the machine
# Ctrl + D

```
### 2. Running myTool

Open your terminal then run:

```
# Launch the machine
# Change direction to vagrant:
cd /path/to/vagrant

# Then run:
vagrant up
vagrant ssh

# Open shared folder
cd /vagrant 

# Run the program
python myTool.py
```

## Contacts

- [Facebook](https://www.facebook.com/ali.khaled.71465)
- E-mail: engalikhaled@hotmail.com

## References
- [PostgreSQL](https://www.postgresql.org/)
