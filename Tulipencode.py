# -*- coding: utf-8 -*-
import random
import time
import json
from psutil import *
import suoying


class Eternal:
    def __init__(self):
        self.ax0 = '💝'  # 0
        self.ax1 = '💗'  # 1
        self.ax2 = '💘'  # 2
        self.ax3 = '💞'  # 3
        self.ax4 = '💓'  # 4
        self.ax5 = '💌'  # 5
        self.ax6 = '💖'  # 6
        self.ax7 = '💕'  # 7
        self.ax8 = '🌹'  # 8
        self.ax9 = '🌷'  # 9
        self.love = 520
        self.like = 1314

    def diann_nc(self):
        # cpu_percent()可以获取cpu的使用率，参数interval是获取的间隔
        return int(cpu_percent(interval=0.5))

    # cpu进行xor
    def cpu_xor_jiam(self, sz, cpuzy):
        jg = []
        for i in sz:
            num = int(i)
            jg.append(cpuzy ^ num)
        return jg

    # 时间戳异或-加密
    def xor_time_jiam(self, sz, sjc):
        jg = []
        for i in sz:
            num = int(i)
            jg.append(sjc ^ num)
        return jg

    # 另外一种获取索引
    def hqsz1(self):
        str3 = suoying.aqsy.baidu(self='')
        return str3

    def hqsz2(self, zfc):
        str3 = suoying.aqsy.zdy(self='', zfc=zfc)
        return str3

    # 将输入的字符串转八进制
    def bjz_zh(self, sr):
        ass = []
        bjzsj = []
        for l in sr:
            ass.append(ord(l))
        for m in ass:
            bjzsj.append(oct(m).replace('0o', ''))
        return bjzsj

    # 字符串替换
    def jm(self, sy1):
        strjm = ''
        strjm1 = []
        for sri in sy1:
            sri = str(sri)
            for m in sri:
                if m == '0':
                    strjm = strjm + self.ax0
                elif m == '1':
                    strjm = strjm + self.ax1
                elif m == '2':
                    strjm = strjm + self.ax2
                elif m == '3':
                    strjm = strjm + self.ax3
                elif m == '4':
                    strjm = strjm + self.ax4
                elif m == '5':
                    strjm = strjm + self.ax5
                elif m == '6':
                    strjm = strjm + self.ax6
                elif m == '7':
                    strjm = strjm + self.ax7
                elif m == '8':
                    strjm = strjm + self.ax8
                elif m == '9':
                    strjm = strjm + self.ax9
            strjm1.append(strjm + "💑")
            strjm = ''
        sc = ''.join(strjm1)
        return sc

    # 索引替换
    def hqsy(self, bjzsj):
        sy = ''
        sy1 = []
        c = self.str3[0]
        for stm in bjzsj:
            for n in stm:
                sy = sy + str(c.index(n) + 1)
            sy1.append(sy)
            sy = ''
        return sy1

    # 加密函数
    def jiami(self):
        xz = input('自定义加密方式(1==联网2==自定义)')
        if xz == '1':
            time.sleep(0.5)
            try:
                self.str3 = self.hqsz1()
            except:
                exit('网络未连接')
        elif xz == '2':
            zfc = input('请输入自定义内容>>>')
            self.str3 = self.hqsz2(zfc=zfc)
        cpuzy1 = self.diann_nc()
        kkk = random.randint(1, 10000)
        cpuzy = kkk * cpuzy1 + self.like
        sjc = int(str(int(time.time()))[-5:])
        print(f"\033[0;31m{'当前星座&None:' + str(self.str3[2])}\033[0m")
        print(f"\033[0;31m{'星座爱情运势:' + str(self.str3[1])}\033[0m")
        print(f"\033[0;31m{'当前时间戳:' + str(sjc)}\033[0m")
        print(f"\033[0;31m{'cpu爱心:' + str(cpuzy)}\033[0m")
        sr = input('请输入要加密的数据:')
        # 输入的字符串转ascii再转八进制 再在23489167233中获取索引 > sx > xor_time > cpu_xor > 替换
        syxl = self.jm(self.cpu_xor_jiam(self.xor_time_jiam(self.hqsy(self.bjz_zh(sr)), sjc), cpuzy))
        data = {
            '时间戳>>': sjc,
            '明文>>': sr,
            '星座运势&自定义语句>>': self.str3[1],
            'cpu爱心>>': cpuzy,
            '密文>>': syxl
        }
        with open('sjc.json', 'a', encoding='utf8') as f:
            f.write(json.dumps(data, ensure_ascii=False))
            f.write('\n')
            f.close()
        print(f"\033[0;31m{'密文:'}\033[0m")
        print(syxl)
        return syxl

    def jiam_api(self, xz, sr, zfc):
        if xz == '1':
            time.sleep(0.5)
            try:
                self.str3 = self.hqsz1()
            except:
                exit('网络未连接')
        elif xz == '2':
            self.str3 = self.hqsz2(zfc=zfc)
        cpuzy1 = self.diann_nc()
        kkk = random.randint(1, 10000)
        cpuzy = kkk * cpuzy1 + self.like
        sjc = int(str(int(time.time()))[-5:])
        print(f"\033[0;31m{'当前星座&None:' + str(self.str3[2])}\033[0m")
        print(f"\033[0;31m{'星座爱情运势:' + str(self.str3[1])}\033[0m")
        print(f"\033[0;31m{'当前时间戳:' + str(sjc)}\033[0m")
        print(f"\033[0;31m{'cpu爱心:' + str(cpuzy)}\033[0m")
        # 输入的字符串转ascii再转八进制 再在23489167233中获取索引 > sx > xor_time > cpu_xor > 替换
        syxl = self.jm(
            self.cpu_xor_jiam(self.xor_time_jiam(self.hqsy(self.bjz_zh(sr)), sjc), cpuzy))
        data = {
            '时间戳>>': sjc,
            '明文>>': sr,
            '星座运势&自定义语句>>': self.str3[1],
            'cpu爱心>>': cpuzy,
            '密文>>': syxl
        }
        with open('sjc.json', 'a', encoding='utf8') as f:
            f.write(json.dumps(data, ensure_ascii=False))
            f.write('\n')
            f.close()
        print(f"\033[0;31m{'密文:'}\033[0m")
        print(syxl)
        return syxl

    def dy_jia(self):
        m = Eternal()
        m.jiami()

    def api_jia(self, xz, sr, zfc):
        m = Eternal()
        # self,xz,sr,zfc
        c = m.jiam_api(xz=xz, sr=sr, zfc=zfc)
        return c


if __name__ == '__main__':
    app = Eternal()
    t = 'suansuan'
    app.api_jia('1', t, zfc='x')

    # 模式1  ：为自动获取加密的秘钥，zfc参数随便，只要有值就行，不会应用到
    # 模式2  ：自定义秘钥，及为zfc对应的参数，会应用到zfc参数
