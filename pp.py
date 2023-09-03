def main():
    content = []

    print("Simple Content Writing App")
    print("Enter your content. Type 'save' to save and exit.")

    while True:
        line = input("> ")
        
        if line.lower() == 'save':
            save_content(content)
            break
        else:
            content.append(line)

def save_content(content):
    file_name = input("Enter the file name to save your content: ")
    
    try:
        with open(file_name, 'w') as file:
            file.writelines('\n'.join(content))
        print(f"Content saved to {file_name}")
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()
