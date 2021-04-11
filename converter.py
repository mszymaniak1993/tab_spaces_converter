import argparse
import os
from shutil import copyfile
import random

class Converter:

    def __init__(self, command):
        self.command = command
    
    # -f 
    def conversion_type(self, length_of_spaces):
        choice = self.command.spaces_tabs
        if (choice is not None): #if value -f is writed
            choice = self.command.spaces_tabs.lower()
            if (choice == "tabs"):
                Converter.start_convert(choice, length_of_spaces)
            elif (choice == "spaces"):
                Converter.start_convert(choice)
        else: #if value -f is not writed
            number = random.randint(1, 10)
            if number % 2 == 0:
                Converter.start_convert(choice = "tabs", length_of_spaces = number)
            else:
                Converter.start_convert(choice = "spaces")
    
    # -r
    def need_backup(self):
        if (self.command.backup is not None):
            Converter.make_copy()

    # -t
    def number_of_spaces(self):
        if (self.command.tab_length is not None): #if value -t is writed
            if (self.command.tab_length > 0 and self.command.tab_length != 4):
                return self.command.tab_length
        return 4 #if value -t is not writed

    @classmethod
    def make_copy(cls):
        backup_folder = "Backup files"
        if (not os.path.isdir(backup_folder)): #if we don't have backup directory
            os.mkdir(backup_folder) #create directory
        for filename in os.listdir(): #list fo files in directory 
            if filename.endswith(".txt"): #check that file endswith.txt
                name_file = filename[:filename.find('.')] #get file name
                backup_file = "{}\\{}_backup.txt".format(backup_folder, name_file) #create file
                number_of_copy = 1 #counter for copy file
                new_backup_file = "{}_({}).txt".format(backup_file[:backup_file.find('.')], number_of_copy)
                if (os.path.isfile(backup_file)): #check if file exists
                    if filename.endswith(".txt"): #find txt files
                        for i in os.listdir("{}".format(backup_folder)): #list of files in backup directory
                            new_backup_file = "{}_({}).txt".format(backup_file[:backup_file.find('.')], number_of_copy) #create backup copy file
                            if (not os.path.exists(new_backup_file)): #check if new_backup_file exsist
                                new_backup_file = "{}_({}).txt".format(backup_file[:backup_file.find('.')], number_of_copy)
                                copyfile(filename, new_backup_file) #create copy
                            number_of_copy += 1 #counter for number of copies in directory
                else:
                    copyfile(filename, backup_file) #create copy

    @classmethod
    def start_convert(cls, choice, length_of_spaces=4):
        edited_lines = 0
        for filename in os.listdir():
            if filename.endswith('.txt'):
                with open(filename, 'r') as reader:
                    lines = reader.readlines()
                    with open(filename, 'w') as writer:
                        for line in lines:
                            if (choice == "spaces"): #if value -f is spaces or random chosen
                                if(line[0] == " "):
                                    line=line.replace(" ", "\t", 1)
                                    edited_lines +=1
                            if (choice == "tabs"): #if value -f is spaces or random chosen
                                if(line[0] == "\t"):
                                    line=line.replace("\t", " "*length_of_spaces, 1)
                                    edited_lines +=1
                            writer.write(line) #add edited (or not) line to file
                print("W pliku {} edytowano {} linijek".format(filename, edited_lines))
            edited_lines = 0

def run(args):
    z = Converter(args)
    z.need_backup()
    lenght_of_spaces = z.number_of_spaces()
    z.conversion_type(lenght_of_spaces)

def main():
    parser=argparse.ArgumentParser(description="Converter tab to spaces and spaces to tabs")
    parser.add_argument("-f", help="Sing to convert. Available spaces or tabs", dest='spaces_tabs', type=str)
    parser.add_argument("-r", help="If writen program will make backup file", dest='backup', type=str)
    parser.add_argument("-t", help="How many spaces have tab, default=4", dest="tab_length", type=int, required=False)
    parser.set_defaults(func=run)
    args = parser.parse_args()
    args.func(args)

if __name__  == "__main__":
    main()
