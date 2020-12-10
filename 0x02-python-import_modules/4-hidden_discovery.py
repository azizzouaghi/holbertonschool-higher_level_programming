#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
file_name = dir(hidden_4)
for i in range(0, len(file_name)):
    if (file_name[i][0] != '_'):
        print(file_name[i])
