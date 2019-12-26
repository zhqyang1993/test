##from PIL import Image, ImageDraw, ImageFont  # 引入绘图模块
##import random  # 引入随机函数模块
##from django.http import HttpResponse  # 引入HttpResponse模块，返回响应
##from io import BytesIO  # 在内存中创建
##
##
##def get_random_color():
##    color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
##    return color
##
##
##def verification_code(request):
##    # 1.1 定义变量，宽，高，背景颜色
##    width = 200
##    height = 50
##    background_color = get_random_color()
##    # 1.2 创建画布对象
##    image = Image.new('RGB', (width, height), background_color)
##    # 1.3 创建画笔对象
##    draw = ImageDraw.Draw(image)
##    # 1.4 调用画笔的point()函数绘制噪点
##    for i in range(0, 100):
##        xy = (random.randrange(0, width), random.randrange(0, height))
##        draw.point(xy, fill=get_random_color())
##    # 1.5 调用画笔的line()函数制造线
##    for i in range(0, 10):
##        xy_start = (random.randrange(0, width), random.randrange(0, height))
##        xy_end = (random.randrange(0, width), random.randrange(0, height))
##        draw.line((xy_start, xy_end), fill=get_random_color())
##
##    # 2 用draw.text书写文字
##    rand_python = ''
##    for i in range(4):
##        random_number = str(random.randint(0, 9))
##        random_lower_letter = chr(random.randint(97, 122))
##        random_upper_letter = chr(random.randint(65, 90))
##        rand_python += random.choice([random_number, random_lower_letter, random_upper_letter,])
##        color = get_random_color()
##        text_color = [0, 0, 0]
##        #
##        for j in range(2):
##            if color[j]-background_color[j] <= 30:
##                text_color[j] = 255-color[j]
##            else:
##                text_color[j] = color[j]
##        draw.text((i * (width/4) + 10, 2),
##                  rand_python[i],
##                  tuple(text_color),
##                  font=ImageFont.truetype(r'C:\Windows\Fonts\BRADHITC.TTF', 40),
##                  align='center')
##
##    # 3 释放画笔
##    del draw
##    # 存入session,用于做进一步的验证
##    request.session['verification_code'] = rand_python
##    # 内存文件操作
##    buf = BytesIO()
##    # 将图片保存在内存中，文件类型为png
##    image.save(buf, 'png')
##    # 将内存中的图片数据返回给客户端，MIME类型为图片png
##    return HttpResponse(buf.getvalue(), 'image/png')
##
##from math import sqrt
##
##
##class Triangle(object):
##
##    def __init__(self, a, b, c):
##        self._a = a
##        self._b = b
##        self._c = c
##
##    @staticmethod
##    def is_valid(a, b, c):
##        return a + b > c and b + c > a and a + c > b
##
##    def perimeter(self):
##        return self._a + self._b + self._c
##
##    def area(self):
##        half = self.perimeter() / 2
##        return sqrt(half * (half - self._a) *
##                    (half - self._b) * (half - self._c))
##
##
##def main():
##    a, b, c = 3, 4, 5
##    # 静态方法和类方法都是通过给类发消息来调用的
##    if Triangle.is_valid(a, b, c):
##        t = Triangle(a, b, c)
##        print(t.perimeter())
##        # 也可以通过给类发消息来调用对象方法但是要传入接收消息的对象作为参数
##        # print(Triangle.perimeter(t))
##        print(t.area())
##        # print(Triangle.area(t))
##    else:
##        print('无法构成三角形.')
##
##
##if __name__ == '__main__':
##    main()


##from abc import ABCMeta, abstractmethod
##from random import randint, randrange
##
##
##class Fighter(object, metaclass=ABCMeta):
##    """战斗者"""
##
##    # 通过__slots__魔法限定对象可以绑定的成员变量
##    __slots__ = ('_name', '_hp')
##
##    def __init__(self, name, hp):
##        """初始化方法
##
##        :param name: 名字
##        :param hp: 生命值
##        """
##        self._name = name
##        self._hp = hp
##
##    @property
##    def name(self):
##        return self._name
##
##    @property
##    def hp(self):
##        return self._hp
##
##    @hp.setter
##    def hp(self, hp):
##        self._hp = hp if hp >= 0 else 0
##
##    @property
##    def alive(self):
##        return self._hp > 0
##
##    @abstractmethod
##    def attack(self, other):
##        """攻击
##
##        :param other: 被攻击的对象
##        """
##        pass
##
##
##class Ultraman(Fighter):
##    """奥特曼"""
##
##    __slots__ = ('_name', '_hp', '_mp')
##
##    def __init__(self, name, hp, mp):
##        """初始化方法
##
##        :param name: 名字
##        :param hp: 生命值
##        :param mp: 魔法值
##        """
##        super().__init__(name, hp)
##        self._mp = mp
##
##    def attack(self, other):
##        other.hp -= randint(15, 25)
##
##    def huge_attack(self, other):
##        """究极必杀技(打掉对方至少50点或四分之三的血)
##
##        :param other: 被攻击的对象
##
##        :return: 使用成功返回True否则返回False
##        """
##        if self._mp >= 50:
##            self._mp -= 50
##            injury = other.hp * 3 // 4
##            injury = injury if injury >= 50 else 50
##            other.hp -= injury
##            return True
##        else:
##            self.attack(other)
##            return False
##
##    def magic_attack(self, others):
##        """魔法攻击
##
##        :param others: 被攻击的群体
##
##        :return: 使用魔法成功返回True否则返回False
##        """
##        if self._mp >= 20:
##            self._mp -= 20
##            for temp in others:
##                if temp.alive:
##                    temp.hp -= randint(10, 15)
##            return True
##        else:
##            return False
##
##    def resume(self):
##        """恢复魔法值"""
##        incr_point = randint(1, 10)
##        self._mp += incr_point
##        return incr_point
##
##    def __str__(self):
##        return '~~~%s奥特曼~~~\n' % self._name + \
##            '生命值: %d\n' % self._hp + \
##            '魔法值: %d\n' % self._mp
##
##
##class Monster(Fighter):
##    """小怪兽"""
##
##    __slots__ = ('_name', '_hp')
##
##    def attack(self, other):
##        other.hp -= randint(10, 20)
##
##    def __str__(self):
##        return '~~~%s小怪兽~~~\n' % self._name + \
##            '生命值: %d\n' % self._hp
##
##
##def is_any_alive(monsters):
##    """判断有没有小怪兽是活着的"""
##    for monster in monsters:
##        if monster.alive > 0:
##            return True
##    return False
##
##
##def select_alive_one(monsters):
##    """选中一只活着的小怪兽"""
##    monsters_len = len(monsters)
##    while True:
##        index = randrange(monsters_len)
##        monster = monsters[index]
##        if monster.alive > 0:
##            return monster
##
##
##def display_info(ultraman, monsters):
##    """显示奥特曼和小怪兽的信息"""
##    print(ultraman)
##    for monster in monsters:
##        print(monster, end='')
##
##
##def main():
##    u = Ultraman('骆昊', 1000, 120)
##    m1 = Monster('狄仁杰', 250)
##    m2 = Monster('白元芳', 500)
##    m3 = Monster('王大锤', 750)
##    ms = [m1, m2, m3]
##    fight_round = 1
##    while u.alive and is_any_alive(ms):
##        print('========第%02d回合========' % fight_round)
##        m = select_alive_one(ms)  # 选中一只小怪兽
##        skill = randint(1, 10)   # 通过随机数选择使用哪种技能
##        if skill <= 6:  # 60%的概率使用普通攻击
##            print('%s使用普通攻击打了%s.' % (u.name, m.name))
##            u.attack(m)
##            print('%s的魔法值恢复了%d点.' % (u.name, u.resume()))
##        elif skill <= 9:  # 30%的概率使用魔法攻击(可能因魔法值不足而失败)
##            if u.magic_attack(ms):
##                print('%s使用了魔法攻击.' % u.name)
##            else:
##                print('%s使用魔法失败.' % u.name)
##        else:  # 10%的概率使用究极必杀技(如果魔法值不足则使用普通攻击)
##            if u.huge_attack(m):
##                print('%s使用究极必杀技虐了%s.' % (u.name, m.name))
##            else:
##                print('%s使用普通攻击打了%s.' % (u.name, m.name))
##                print('%s的魔法值恢复了%d点.' % (u.name, u.resume()))
##        if m.alive > 0:  # 如果选中的小怪兽没有死就回击奥特曼
##            print('%s回击了%s.' % (m.name, u.name))
##            m.attack(u)
##        display_info(u, ms)  # 每个回合结束后显示奥特曼和小怪兽的信息
##        fight_round += 1
##    print('\n========战斗结束!========\n')
##    if u.alive > 0:
##        print('%s奥特曼胜利!' % u.name)
##    else:
##        print('小怪兽胜利!')
##
##
##if __name__ == '__main__':
##    main()



##import tkinter
##import tkinter.messagebox
##
##
##def main():
##    flag = True
##
##    # 修改标签上的文字
##    def change_label_text():
##        nonlocal flag
##        flag = not flag
##        color, msg = ('red', 'Hello, world!')\
##            if flag else ('blue', 'Goodbye, world!')
##        label.config(text=msg, fg=color)
##
##    # 确认退出
##    def confirm_to_quit():
##        if tkinter.messagebox.askokcancel('温馨提示', '确定要退出吗?'):
##            top.destroy()
##
##    # 创建顶层窗口
##    top = tkinter.Tk()
##    # 设置窗口大小
##    top.geometry('240x160')
##    # 设置窗口标题
##    top.title('example')
##    # 创建标签对象并添加到顶层窗口
##    label = tkinter.Label(top, text='Hello, world!', font='Arial -32', fg='red')
##    label.pack(expand=1)
##    # 创建一个装按钮的容器
##    panel = tkinter.Frame(top)
##    # 创建按钮对象 指定添加到哪个容器中 通过command参数绑定事件回调函数
##    button1 = tkinter.Button(panel, text='修改', command=change_label_text)
##    button1.pack(side='left')
##    button2 = tkinter.Button(panel, text='退出', command=confirm_to_quit)
##    button2.pack(side='right')
##    panel.pack(side='bottom')
##    # 开启主事件循环
##    tkinter.mainloop()
##
##
##if __name__ == '__main__':
##    main()



##from enum import Enum, unique
##from math import sqrt
##from random import randint
##
##import pygame
##
##
##@unique
##class Color(Enum):
##    """颜色"""
##
##    RED = (255, 0, 0)
##    GREEN = (0, 255, 0)
##    BLUE = (0, 0, 255)
##    BLACK = (0, 0, 0)
##    WHITE = (255, 255, 255)
##    GRAY = (242, 242, 242)
##
##    @staticmethod
##    def random_color():
##        """获得随机颜色"""
##        r = randint(0, 255)
##        g = randint(0, 255)
##        b = randint(0, 255)
##        return (r, g, b)
##
##
##class Ball(object):
##    """球"""
##
##    def __init__(self, x, y, radius, sx, sy, color=Color.RED):
##        """初始化方法"""
##        self.x = x
##        self.y = y
##        self.radius = radius
##        self.sx = sx
##        self.sy = sy
##        self.color = color
##        self.alive = True
##
##    def move(self, screen):
##        """移动"""
##        self.x += self.sx
##        self.y += self.sy
##        if self.x - self.radius <= 0 or \
##                self.x + self.radius >= screen.get_width():
##            self.sx = -self.sx
##        if self.y - self.radius <= 0 or \
##                self.y + self.radius >= screen.get_height():
##            self.sy = -self.sy
##
##    def eat(self, other):
##        """吃其他球"""
##        if self.alive and other.alive and self != other:
##            dx, dy = self.x - other.x, self.y - other.y
##            distance = sqrt(dx ** 2 + dy ** 2)
##            if distance < self.radius + other.radius \
##                    and self.radius > other.radius:
##                other.alive = False
##                self.radius = self.radius + int(other.radius * 0.146)
##
##    def draw(self, screen):
##        """在窗口上绘制球"""
##        pygame.draw.circle(screen, self.color,
##                           (self.x, self.y), self.radius, 0)
##
##
##def main():
##    # 定义用来装所有球的容器
##    balls = []
##    # 初始化导入的pygame中的模块
##    pygame.init()
##    # 初始化用于显示的窗口并设置窗口尺寸
##    screen = pygame.display.set_mode((800, 600))
##    # 设置当前窗口的标题
##    pygame.display.set_caption('大球吃小球')
##    running = True
##    # 开启一个事件循环处理发生的事件
##    while running:
##        # 从消息队列中获取事件并对事件进行处理
##        for event in pygame.event.get():
##            if event.type == pygame.QUIT:
##                running = False
##                
##            # 处理鼠标事件的代码
##            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
##                # 获得点击鼠标的位置
##                x, y = event.pos
##                radius = randint(10, 100)
##                sx, sy = randint(-10, 10), randint(-10, 10)
##                color = Color.random_color()
##                # 在点击鼠标的位置创建一个球(大小、速度和颜色随机)
##                ball = Ball(x, y, radius, sx, sy, color)
##                # 将球添加到列表容器中
##                balls.append(ball)
##        screen.fill((255, 255, 255))
##        # 取出容器中的球 如果没被吃掉就绘制 被吃掉了就移除
##        for ball in balls:
##            if ball.alive:
##                ball.draw(screen)
##            else:
##                balls.remove(ball)
##        pygame.display.flip()
##        # 每隔50毫秒就改变球的位置再刷新窗口
##        pygame.time.delay(50)
##        for ball in balls:
##            ball.move(screen)
##            # 检查球有没有吃到其他的球
##            for other in balls:
##                ball.eat(other)
##
##
##if __name__ == '__main__':
##    main()




##def main():
##    f = None
##    try:
##        f = open("qwe.txt", "r", encoding="utf-8")
##        print(f.read())
##    except FileNotFoundError:
##        print("无法打开指定的文件!")
##    except LookupError:
##        print("指定了未知的编码!")
##    except UnicodeDecodeError:
##        print("读取文件时解码错误!")
##    finally:
##        if f:
##            f.close()
##
##
##if __name__ == "__main__":
##    main()



##import json
##
##
##def main():
##    mydict = {
##        'name': '骆昊',
##        'age': 38,
##        'qq': 957658,
##        'friends': ['王大锤', '白元芳'],
##        'cars': [
##            {'brand': 'BYD', 'max_speed': 180},
##            {'brand': 'Audi', 'max_speed': 280},
##            {'brand': 'Benz', 'max_speed': 320}
##        ]
##    }
##    try:
##        with open('data.json', 'w', encoding='utf-8') as fs:
##            json.dump(mydict, fs, ensure_ascii=False)
##    except IOError as e:
##        print(e)
##    print('保存数据完成!')
##
##
##if __name__ == '__main__':
##    main()



from time import sleep
from threading import Thread, Lock


##class Account(object):
##
##    def __init__(self):
##        self._balance = 0
##        self._lock = Lock()
##
##    def deposit(self, money):
##        # 先获取锁才能执行后续的代码
##        self._lock.acquire()
##        try:
##            new_balance = self._balance + money
##            sleep(0.01)
##            self._balance = new_balance
##        finally:
##            # 在finally中执行释放锁的操作保证正常异常锁都能释放
##            self._lock.release()
##
##    @property
##    def balance(self):
##        return self._balance
##
##
##class AddMoneyThread(Thread):
##
##    def __init__(self, account, money):
##        super().__init__()
##        self._account = account
##        self._money = money
##
##    def run(self):
##        self._account.deposit(self._money)
##
##
##def main():
##    account = Account()
##    threads = []
##    for _ in range(100):
##        t = AddMoneyThread(account, 1)
##        threads.append(t)
##        t.start()
##    for t in threads:
##        t.join()
##    print('账户余额为: ￥%d元' % account.balance)
##
##
##if __name__ == '__main__':
##    main()





##from socket import socket, SOCK_STREAM, AF_INET
##from base64 import b64encode
##from json import dumps
##from threading import Thread
##
##
##def main():
##    
##    # 自定义线程类
##    class FileTransferHandler(Thread):
##
##        def __init__(self, cclient):
##            super().__init__()
##            self.cclient = cclient
##
##        def run(self):
##            my_dict = {}
##            my_dict['filename'] = '11.png'
##            # JSON是纯文本不能携带二进制数据
##            # 所以图片的二进制数据要处理成base64编码
##            my_dict['filedata'] = data
##            # 通过dumps函数将字典处理成JSON字符串
##            json_str = dumps(my_dict)
##            # 发送JSON字符串
##            self.cclient.send(json_str.encode('utf-8'))
##            self.cclient.close()
##
##    # 1.创建套接字对象并指定使用哪种传输服务
##    server = socket()
##    # 2.绑定IP地址和端口(区分不同的服务)
##    server.bind(('10.18.1.89', 5566))
##    # 3.开启监听 - 监听客户端连接到服务器
##    server.listen(512)
##    print('服务器启动开始监听...')
##    with open('11.png', 'rb') as f:
##        # 将二进制数据处理成base64再解码成字符串
##        data = b64encode(f.read()).decode('utf-8')
##    while True:
##        client, addr = server.accept()
##        # 启动一个线程来处理客户端的请求
##        FileTransferHandler(client).start()
##
##
##if __name__ == '__main__':
##    main()
##








from smtplib import SMTP
from email.header import Header
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart

import urllib


def main():
    # 创建一个带附件的邮件消息对象
    message = MIMEMultipart()
    
    # 创建文本内容
    text_content = MIMEText('附件中有本月数据请查收', 'plain', 'utf-8')
    message['Subject'] = Header('本月数据', 'utf-8')
    # 将文本内容添加到邮件消息对象中
    message.attach(text_content)

    # 读取文件并将文件作为附件添加到邮件消息对象中
    with open('新建文本文档.txt', 'rb') as f:
        txt = MIMEText(f.read(), 'base64', 'utf-8')
        txt['Content-Type'] = 'text/plain'
        txt['Content-Disposition'] = 'attachment; filename=hello.txt'
        message.attach(txt)
    # 读取文件并将文件作为附件添加到邮件消息对象中
    with open('abc.xlsx', 'rb') as f:
        xls = MIMEText(f.read(), 'base64', 'utf-8')
        xls['Content-Type'] = 'application/vnd.ms-excel'
        xls['Content-Disposition'] = 'attachment; filename=month-data.xlsx'
        message.attach(xls)
    
    # 创建SMTP对象
    smtper = SMTP('smtp.163.com')
    # 开启安全连接
    # smtper.starttls()
    sender = '18202762824@163.com'
    receivers = ['1058167890@qq.com']
    # 登录到SMTP服务器
    # 请注意此处不是使用密码而是邮件客户端授权码进行登录
    # 对此有疑问的读者可以联系自己使用的邮件服务器客服
    smtper.login(sender, 'kcy13433243579')
    # 发送邮件
    smtper.sendmail(sender, receivers, message.as_string())
    # 与邮件服务器断开连接
    smtper.quit()
    print('发送完成!')


if __name__ == '__main__':
    main()
