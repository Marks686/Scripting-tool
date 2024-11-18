# [应用]生成指定大小的文件
import tkinter as tk
# 应用场景
    # 头像上传功能, 图片大小边界是1~2M
    # 文件上传功能, 文件大小边界是1~10M

# def generate_file(file_name, size_mb):
#     # 将大小转换为字节
#     size_bytes = size_mb * 1024 * 1024
#     # round() 四舍五入
#     print(size_bytes, round(size_bytes))
#     # 创建一个文件并填充, b"\x00" 表示空字符 Null
#     with open(file_name, "wb") as f:
#         f.write(b"\x00" * round(size_bytes))

# 使用示例
# generate_file("123", 1) # 生成1M大小的文件
# generate_file("123", 0.9) # 生成0.9M大小的文件

# 优化, 可以根据文件类型进行生成
# def generate_file_plus(file_type, file_name, size_mb):
#     # 将大小转换为字节
#     size_bytes = size_mb * 1024 * 1024
#
#     if file_type == "bin":
#         with open(file_name + ".bin", "wb") as f:
#             f.write(b"\x00" * round(size_bytes))
#
#     if file_type == "text":
#         with open(file_name + ".txt", "w") as f:
#             f.write("A" * round(size_bytes))
#
# generate_file_plus("bin", "123", 1)
# generate_file_plus("text", "123", 1)

# 生成 excel 文件需要用到 openpyxl 库
# 生成 图片 文件需要用到 pillow 库, 填充的是像素的 RGB 颜色
# 生成 word 文件需要用到 python-docx 库


def generate_file_plus():
    try:
        file_type = e1.get()
        file_name = e2.get()
        size_mb = float(e3.get())
        # 将大小转换为字节
        size_bytes = size_mb * 1024 * 1024

        if file_type == "bin":
            with open(file_name + ".bin", "wb") as f:
                f.write(b"\x00" * round(size_bytes))

        if file_type == "text":
            with open(file_name + ".txt", "w") as f:
                f.write("A" * round(size_bytes))
    except:
        print("......")


# 创建主窗口
window = tk.Tk()

# 给主窗口起个名字
window.title("生成指定大小的文件")

# 设置窗口大小
window.geometry("300x300")

# 主题程序部分, 需要三个输入框, 分别输入文件类型, 文件名, 文件大小, 还需要一个按钮触发
# 三个输入框
l1 = tk.Label(window, text="请输入文件类型(bin/text): ")
e1 = tk.Entry(window, width=10)
l2 = tk.Label(window, text="请输入要生成的文件名: ")
e2 = tk.Entry(window, width=10)
l3 = tk.Label(window, text="请输入要生成的文件大小(MB): ")
e3 = tk.Entry(window, width=10)

l1.pack()
e1.pack()
l2.pack()
e2.pack()
l3.pack()
e3.pack()
# 按钮
b = tk.Button(window, text="生成", command=generate_file_plus)
b.pack()

# 主窗口循环显示
window.mainloop()

'''
面试题
你写过哪些python的测试小工具, 应用场景, 编写思路是怎样的?[2]
- 我当时设计一个工具, 可以根据我们指定的文件大小生成二进制/文本等类型的文件
- 应用场景是各类文件上传功能的边界验证, 比如
    - 图片上传: 用户头像上传, 物料管理中的图片上传, 轮播图上传等
    - 文件上传: 用户管理中的用户数据导入以及其他需要预设数据的地方, 像部门/角色/菜单管理等
- 编写思路是先确定文件填充的单位是字节, 再根据计算算出指定要填充的空间, 就可以用open()函数来创建文件并
进行循环填充了, 还可以结合 tk 做个GUI程序, 也可以进一步用 pyinstaller 打包成 exe
'''