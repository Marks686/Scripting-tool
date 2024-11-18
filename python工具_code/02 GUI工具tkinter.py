# tkinter是python标准GUI库, 内置在python安装包中, 无需额外安装
# 应用场景: 解决工具的易用性问题
    # 使用对象是小白
    # 使用流程繁琐

# [基础]GUI工具 tkinter
import tkinter as tk


def add_numbers():
    try:
        x = float(e1.get())
        y = float(e2.get())
        result = x + y
        l3.config(text=result)
    except ValueError:
        l3.config(text="*&^%$^&&*")


# 创建主窗口
window = tk.Tk()

# 给主窗口起个名字
window.title("加法计算器")

# 设置主窗口大小
window.geometry("300x300")

# 主体程序部分, 需要两个输入框分别输入两个加数, 还要有一个按钮来触发加法的动作, 最后要有一个地方显示结果
# tk 支持10+种控件, 主要会用到以下几种:
    # Label 标签控件, 可以显示文本和位图
    # Entry 输入控件
    # Button 按钮控件

# 加数
l1 = tk.Label(window, text="请输入第一个加数: ")
e1 = tk.Entry(window, width=10)
l2 = tk.Label(window, text="请输入第二个加数: ")
e2 = tk.Entry(window, width=10)

# pack() 用于控件摆放, 如果不用这个方法, 只在内存中创建控件, 界面不会显示
l1.pack()
e1.pack()
l2.pack()
e2.pack()

# 按钮
b = tk.Button(window, text="给我加!!!", command=add_numbers)
b.pack()

# 结果
l3 = tk.Label(window, text="结果")
l3.pack()

# 主窗口循环显示
window.mainloop()


# pyinstaller --onefile --windowed xx.py
    # --windowed 对于GUI应用程序, 不显示命令行窗口