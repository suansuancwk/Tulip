# -*- coding: utf-8 -*-
import random
import time
import json
from psutil import *
import suoying


class Eternal:
    def __init__(self):
        self.ax0 = 'ð'  # 0
        self.ax1 = 'ð'  # 1
        self.ax2 = 'ð'  # 2
        self.ax3 = 'ð'  # 3
        self.ax4 = 'ð'  # 4
        self.ax5 = 'ð'  # 5
        self.ax6 = 'ð'  # 6
        self.ax7 = 'ð'  # 7
        self.ax8 = 'ð¹'  # 8
        self.ax9 = 'ð·'  # 9
        self.love = 520
        self.like = 1314

    def diann_nc(self):
        # cpu_percent()å¯ä»¥è·åcpuçä½¿ç¨çï¼åæ°intervalæ¯è·åçé´é
        return int(cpu_percent(interval=0.5))

    # cpuè¿è¡xor
    def cpu_xor_jiam(self, sz, cpuzy):
        jg = []
        for i in sz:
            num = int(i)
            jg.append(cpuzy ^ num)
        return jg

    # æ¶é´æ³å¼æ-å å¯
    def xor_time_jiam(self, sz, sjc):
        jg = []
        for i in sz:
            num = int(i)
            jg.append(sjc ^ num)
        return jg

    # å¦å¤ä¸ç§è·åç´¢å¼
    def hqsz1(self):
        str3 = suoying.aqsy.baidu(self='')
        return str3

    def hqsz2(self, zfc):
        str3 = suoying.aqsy.zdy(self='', zfc=zfc)
        return str3

    # å°è¾å¥çå­ç¬¦ä¸²è½¬å«è¿å¶
    def bjz_zh(self, sr):
        ass = []
        bjzsj = []
        for l in sr:
            ass.append(ord(l))
        for m in ass:
            bjzsj.append(oct(m).replace('0o', ''))
        return bjzsj

    # å­ç¬¦ä¸²æ¿æ¢
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
            strjm1.append(strjm + "ð")
            strjm = ''
        sc = ''.join(strjm1)
        return sc

    # ç´¢å¼æ¿æ¢
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

    # å å¯å½æ°
    def jiami(self):
        xz = input('èªå®ä¹å å¯æ¹å¼(1==èç½2==èªå®ä¹)')
        if xz == '1':
            time.sleep(0.5)
            try:
                self.str3 = self.hqsz1()
            except:
                exit('ç½ç»æªè¿æ¥')
        elif xz == '2':
            zfc = input('è¯·è¾å¥èªå®ä¹åå®¹>>>')
            self.str3 = self.hqsz2(zfc=zfc)
        cpuzy1 = self.diann_nc()
        kkk = random.randint(1, 10000)
        cpuzy = kkk * cpuzy1 + self.like
        sjc = int(str(int(time.time()))[-5:])
        print(f"\033[0;31m{'å½åæåº§&None:' + str(self.str3[2])}\033[0m")
        print(f"\033[0;31m{'æåº§ç±æè¿å¿:' + str(self.str3[1])}\033[0m")
        print(f"\033[0;31m{'å½åæ¶é´æ³:' + str(sjc)}\033[0m")
        print(f"\033[0;31m{'cpuç±å¿:' + str(cpuzy)}\033[0m")
        sr = input('è¯·è¾å¥è¦å å¯çæ°æ®:')
        # è¾å¥çå­ç¬¦ä¸²è½¬asciiåè½¬å«è¿å¶ åå¨23489167233ä¸­è·åç´¢å¼ > sx > xor_time > cpu_xor > æ¿æ¢
        syxl = self.jm(self.cpu_xor_jiam(self.xor_time_jiam(self.hqsy(self.bjz_zh(sr)), sjc), cpuzy))
        data = {
            'æ¶é´æ³>>': sjc,
            'ææ>>': sr,
            'æåº§è¿å¿&èªå®ä¹è¯­å¥>>': self.str3[1],
            'cpuç±å¿>>': cpuzy,
            'å¯æ>>': syxl
        }
        with open('sjc.json', 'a', encoding='utf8') as f:
            f.write(json.dumps(data, ensure_ascii=False))
            f.write('\n')
            f.close()
        print(f"\033[0;31m{'å¯æ:'}\033[0m")
        print(syxl)
        return syxl

    def jiam_api(self, xz, sr, zfc):
        if xz == '1':
            time.sleep(0.5)
            try:
                self.str3 = self.hqsz1()
            except:
                exit('ç½ç»æªè¿æ¥')
        elif xz == '2':
            self.str3 = self.hqsz2(zfc=zfc)
        cpuzy1 = self.diann_nc()
        kkk = random.randint(1, 10000)
        cpuzy = kkk * cpuzy1 + self.like
        sjc = int(str(int(time.time()))[-5:])
        print(f"\033[0;31m{'å½åæåº§&None:' + str(self.str3[2])}\033[0m")
        print(f"\033[0;31m{'æåº§ç±æè¿å¿:' + str(self.str3[1])}\033[0m")
        print(f"\033[0;31m{'å½åæ¶é´æ³:' + str(sjc)}\033[0m")
        print(f"\033[0;31m{'cpuç±å¿:' + str(cpuzy)}\033[0m")
        # è¾å¥çå­ç¬¦ä¸²è½¬asciiåè½¬å«è¿å¶ åå¨23489167233ä¸­è·åç´¢å¼ > sx > xor_time > cpu_xor > æ¿æ¢
        syxl = self.jm(
            self.cpu_xor_jiam(self.xor_time_jiam(self.hqsy(self.bjz_zh(sr)), sjc), cpuzy))
        data = {
            'æ¶é´æ³>>': sjc,
            'ææ>>': sr,
            'æåº§è¿å¿&èªå®ä¹è¯­å¥>>': self.str3[1],
            'cpuç±å¿>>': cpuzy,
            'å¯æ>>': syxl
        }
        with open('sjc.json', 'a', encoding='utf8') as f:
            f.write(json.dumps(data, ensure_ascii=False))
            f.write('\n')
            f.close()
        print(f"\033[0;31m{'å¯æ:'}\033[0m")
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

    # æ¨¡å¼1  ï¼ä¸ºèªå¨è·åå å¯çç§é¥ï¼zfcåæ°éä¾¿ï¼åªè¦æå¼å°±è¡ï¼ä¸ä¼åºç¨å°
    # æ¨¡å¼2  ï¼èªå®ä¹ç§é¥ï¼åä¸ºzfcå¯¹åºçåæ°ï¼ä¼åºç¨å°zfcåæ°
