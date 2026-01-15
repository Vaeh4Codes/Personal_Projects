from pathlib import Path
import shutil
import os

move_file = True

#This function verifies if the inputed file exists or not
def file_verification(file_input):
  if Path(file_input).exists() == False:
    print("File does not exist please try again.")

    return False
  else:
    return True

#This function converts the inputed file to the full file path  
def full_file_path(file_input):
    full_path = Path(file_input).resolve()
    return full_path

#This function verifies if the inputed output file exists or not
def verify_output(output_path):
  if Path(output_path).exists() == False:
    print("Path does not exist please try again.")


while move_file == True:

  file_path = input(str("What file would you like to move? Please inter in file.extension format.\n"))

  verify_file = file_verification(file_path)

  if verify_file == True:
    full_path = full_file_path(file_path)

    output_path = input("What folder would you like the file to be moved?\n")
    
    verify_output = file_verification(file_path)

    if verify_output != True:
      output_path = input("What folder would you like the file to be moved to?\n")
    
      verify_output = file_verification(file_path)
    else:
      shutil.move(file_path, output_path)
      print(f"{file_path} moved to {output_path}")

      to_continue = input(str("Would you like to move another file?"))

      if to_continue == "yes":
        move_file == True
      else:
        move_file = False

  else:
    verify_file = file_verification(file_path)




