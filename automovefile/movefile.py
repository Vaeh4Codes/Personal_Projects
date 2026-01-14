from pathlib import Path

move_file = True

def file_verification(file_input):
  if Path(file_input).exists() == False:
    print("File does not exist please try again.")

    return False
  else:
    return True
    
def full_file_path(file_input):
    full_path = Path(file_input).resolve()
    return full_path

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
    while verify_output != True:
      output_path = input("What folder would you like the file to be moved?\n")
    
      verify_output = file_verification(file_path)
    
    print("computing...")
    move_file = False


