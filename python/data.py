# 指定文件路径
file_path = '/home/b110/code/Stable_Diffusion/xiaoqiu_test_sin.txt'

# 打开文件并写入内容
with open(file_path, 'w') as file:
    for i in range(25001, 25769):  # 从 1 到 27400
        file.write(f"{i}.png\n")  # 写入每一行

print(f"文件已成功写入到 {file_path}")