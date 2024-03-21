def copy_file(source_file, target_file):
    """
    Copy the contents of the source file to the target file.
    
    Args:
        source_file (str): The path to the source file.
        target_file (str): The path to the target file.
        
    Returns:
        bool: True if the file is successfully copied, False otherwise.
    """
    try:
        with open(source_file, 'r') as source:
            content = source.read()
        
        with open(target_file, 'w') as target:
            target.write(content)
        
        return True
    except Exception as e:
        print(f"An error occurred: {e}")
        return False

# 获取用户输入的源文件和目标文件路径
source_path = input("Enter the path to the source file: ")
target_path = input("Enter the path to the target file: ")

# 调用 copy_file 函数复制文件
success = copy_file(source_path, target_path)

# 根据复制结果输出相应信息
if success:
    print("File copied successfully.")
else:
    print("Failed to copy file.")
