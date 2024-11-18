# [基础]打包神器 pyinstaller
# 应用场景: 把python程序打包成exe文件

def add_numbers(x, y):
    return x + y


try:
    x = float(input("请输入第一个加数: "))
    y = float(input("请输入第二个加数: "))
    result = add_numbers(x, y)
    print("和是: {}".format(result))
except ValueError:
    print("输入错误")

# 打开 cmd 或 pycharm里的终端(推荐用终端, 后续打包需要进入脚本所在目录)
# 运行 pip install pyinstaller, 安装 pyinstaller
# 执行 pyinstaller --onefile xx.py, 在 dist 文件夹里即可得到对应的exe可执行程序
    # --onefile 创建单个打包的可执行文件