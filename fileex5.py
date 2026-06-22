file_path="my_file.txt" 
content_to_write="Hello,Python!\nThis is a new line." 
content_to_overwrite="This is a new content."
content_to_append="\nThis is the appended content."
with open(file_path,'a') as file:
    file.write(content_to_append)
    print(f"Content appended to '{file_path}'\n,content")
    content=file.read()
    print(f"Content read from '{file_path}'\n",content)