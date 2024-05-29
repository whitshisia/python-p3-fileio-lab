def write_file(file_name, file_content):
     if not str(file_name).endswith('.txt'):
        file_name = str(file_name) + '.txt'
    
     with open(file_name, 'w') as text_file:
        text_file.write(file_content)

def append_file(file_name, append_content):
     if not str(file_name).endswith('.txt'):
        file_name = str(file_name) + '.txt'
    
     with open(file_name, 'a') as text_file:
        text_file.write(append_content)

def read_file(file_name):
    if not str(file_name).endswith('.txt'):
        file_name = str(file_name) + '.txt'
    
    with open(file_name, 'r') as text_file:
        return text_file.read()
