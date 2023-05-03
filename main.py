import time
import os.path
import tkinter
from tkinter import *
from PIL import Image, ImageTk
import random

k5 = 'K5'

k2 = 'K2'

k3 = 'K3'

k14 = 'K14'

m16 = 'M16'

m60 = 'M60'

SWR = 'M60-REVOLVER'

eq = ['K5']

lista = []

list1 = []

stg = []

inp = input("1.전쟁속으로, 2.게임 종료, 3.제작자들 : ")

sleep = 200

c = 0 #UI

n = 0  #조건 반복문 함수

t = 0 #

hp = 100

hydro = 0 #수분

hungry = 0 #배고픔

MRE = 3 #전투식량
handfood = 5 #수제음식
polf = 0 #정크푸드

water = 20 #물 갯수

rad = 0 #방사능 수치

Ammo = 60

Gold = 90000

Silver = 1000

Weapon = []

#저장된 변수 불러오기
#j = 0
#if os.path.isfile("value_file.txt"):
  #f = open("value_file.txt", 'r')
  #lines = f.readlines()
  #for line in lines:
    #j = j + 1
    #if j == 2:
      #eq = line
  #j = 0

if inp == "1":
  if os.path.isfile("save_file.txt"):
    f = open("save_file.txt", 'r')
    lines = f.readlines()
    for line in lines:
      if line != "인트로" and line == "save data":
        f = open("save_file.txt", 'a')
        f.write("\n인트로")
        f.close()
        print("게임 시작")
        time.sleep(3)

        print("2014년..")
        time.sleep(2)
        print("핵전쟁의 화마가 온 세계를 뒤 엎었다.")
        time.sleep(2)
        print("지하철은 순식간에 만원이 되었고,")
        time.sleep(2)
        print("대부분의 대피소는 더이상 사람이 들어 갈 수 없을정도로 포화 되었다.")
        time.sleep(2)
        print("그리고 대부분의 사람이 핵공격에 목숨을 잃었다.")
        time.sleep(2)
        print("이제 대피소 이외의 지역은 전부 방사능으로 폐허가 되었으며,")
        time.sleep(2)
        print("그 누구도 방사능 지역에 갈 수 없었다.")
        time.sleep(2)
        print("하지만 점차 방사능 지수는 내려가고,")
        time.sleep(2)
        print("사람들은 방독면과 두꺼운 옷을 입고 지상으로 올라왔다.")
        time.sleep(2)
        print("지상의 상황은 최악이였다.")
        time.sleep(2)
        print("각종 괴물들과 생명체들이 우리들을 위협했다.")
        time.sleep(2)
        print("그래서 따로 전문직으로 등장한 직업이 추종자, 스토커다.")
        time.sleep(2)
        print("이들은 여러명의 인간을 압살할 수 있는 괴물들을 아무렇지도 않게 죽이고,")
        time.sleep(2)
        print("각종 물품들을 모아 대피소를 발전시켰다.")
        time.sleep(2)
        print("그런 사람들이 있어서 우리 지하철에 있던 대피소 인원들은 하루 하루 삶을 연명하고 있었고...")
        time.sleep(4)
        print("난 거기에 있었다.")
        time.sleep(8)
        sp = input("당신의 대피소 이름을 입력하세요:  ")
        print("당신의 대피소 이름이", sp, "입니까?")
        ye = input("1.네,2.아니오")

        if ye == ("1"):
          print("대피소를 불러오는 중...")
        elif ye == ("2"):
          sp = input("당신의 대피소 이름을 입력하세요:  ")
          print("당신의 쉘터 이름이", sp, "입니까?")
          ye = input("1.네,2.아니오")
      elif line != "인트로":
        f = open("save_file.txt", 'w')
        f.write("save data")
if inp == "2":
  n = n + 1


while n == 0:
  if inp == "1": #샤워실
    shel = input("""1.샤워실, 2.식사, 3.취침, 4.창고, 5.상점 ,6.지도, 7.의료, 8.퀘스트 """)

    if shel == "1":
      print("방사능 수치", rad)
      cure = input("방사능을 씻으시겠습니까? 1.네, 2.아니오")
      if cure == "1":
        rad = rad - 50
        if rad <= 0:
          rad = 0
      elif cure == "2":
        shel

    if shel == "2": #식사
      print("식사를 하시겠습니까?")
      print("포만감: ", hungry, "수분: ", hydro)
      eat = input("1.MRE+물250ml, 2.수제 비상식량+물125ml, 3.오염된 식량+물75ml, 4.먹지않는다.")
      if eat == "1" and MRE <= 0:
        print("먹을 것이 부족합니다.")
        print("포만감: ", hungry, "수분: ", hydro)
      elif eat == "1":
        hungry = hungry + 100
        hydro = hydro + 100
        MRE = MRE - 1
        water = water - 0.25
        if hungry >= 300:
          hungry = 300
        if hydro >= 300:
          hydro = 300
        print("식사중...")
        time.sleep(1)
        print("식사중..")
        time.sleep(1)
        print("식사중...")
        time.sleep(1)
        print("식사 완료")
        time.sleep(1)
        print("포만감: ", hungry, "수분: ", hydro)
      elif eat == "2" and handfood <= 0:
        print("먹을 것이 부족합니다.")
        print("포만감: ", hungry, "수분: ", hydro)
      elif eat == "2":
        hungry = hungry + 50
        hydro = hydro + 50
        handfood = handfood - 1
        water = water - 0.125
        if hungry >= 300:
          hungry = 300
        if hydro >= 300:
          hydro = 300
        print("식사중...")
        time.sleep(1)
        print("식사중..")
        time.sleep(1)
        print("식사중...")
        time.sleep(1)
        print("식사 완료")
        time.sleep(1)
        print("포만감: ", hungry, "수분: ", hydro)
      elif eat == "3" and polf <= 0:
        print("먹을 것이 부족합니다.")
        print("포만감: ", hungry, "수분: ", hydro)
      elif eat == "3":
        hungry = hungry + 25
        hydro = hydro + 25
        hp = hp - 2
        polf = polf - 1
        water = water - 0.125
        if hungry >= 300:
          hungry = 300
        if hydro >= 300:
          hydro = 300
        print("식사중...")
        time.sleep(1)
        print("식사중..")
        time.sleep(1)
        print("식사중...")
        time.sleep(1)
        print("식사 완료")
        time.sleep(1)
        print("포만감: ", hungry, "수분: ", hydro, "HP", hp)
      elif eat == "4":
        shel

    if shel == "3": #취침
      print("행동력: ", sleep)
      zzz = input("취침하시겠습니까? 1.네, 2.아니오")
      if zzz == "1":
        sleep = sleep + 100
        if sleep >= 200:
          sleep = 200
        print("취침중...")
        time.sleep(1)
        print("취침중..")
        time.sleep(1)
        print("취침중...")
        time.sleep(1)
        print("취침 완료")
        time.sleep(1)
        print("행동력: ", sleep)
      elif zzz == "2":
        shel

    if shel == "4": #무기고
      print(Weapon)
      eqi = input("K5, K2, K3, K14, M16, M60, SW_M60")
      if eqi in Weapon:
        eq.append(Weapon)
        eq.clear()
        eq.append(eqi)
      else:
        print(eqi + "을/를 소지하고 있지 않습니다.")

      print("장착된 무기: ", eq)
      print("탄약: ", Ammo, "발")
      print("아이템: ", "볼트:", (stg.count('볼트')), "전선:", (stg.count('전선')))
      print("고철 조각:", (stg.count('고철 조각')), "공구상자:", (stg.count('공구상자')))
      print("붕대:", (stg.count('bandage')), "모르핀:", (stg.count('morphine')))
      print("구급상자:", (stg.count('mk')), "간이붕대:", (stg.count('간이붕대')))

    if shel == "5":
      print("골드 소지량: ", Gold, "실버 소지량: ", Silver)
      print("강수원: 어서오시게나 총포, 탄약, 수제 비상식량, MRE 뭐든지 있다네.")
      print("뭘 살겐가?")
      sm = input("1.무기, 2.탄약 30발 구매, 3.식량, 4.물 구매, 5.의료 물품, 6.돌아간다.")
      if sm == "1":
        print("1.K2=1000GOLD, 2.K5 = 200GOLD, 3.K3 = 1750GOLD, 4.K14 = 4000 GOLD")
        print("5.M16 = 900 GOLD, 6.M60 = 2900GOLD, 7.M60-REVOLVER = 400GOLD")
        Gs = input("1.K2, 2.K5, 3.K3, 4.K14, 5.M16, 6.M60, 7.M60-REVOLVER, 8.돌아간다." )
        if Gs == "1" and Gold < 1000:
          print("골드가 부족합니다.")
          print("골드 소지량: ", Gold, "실버 소지량: ", Silver)
          shel
        elif Gs == "1":
          Gold = Gold - 1000
          Weapon.append('K2')
          print("K2 소총을 구매하였습니다.")
          print("골드 소지량: ", Gold, "실버 소지량: ", Silver)
          shel
        if Gs == "2" and Gold < 200:
          print("골드가 부족합니다.")
          print("골드 소지량: ", Gold, "실버 소지량: ", Silver)
          shel
        elif Gs == "2":
          Gold = Gold - 200
          Weapon.append('K5')
          print("K5 권총을 구매하였습니다.")
          print("골드 소지량: ", Gold, "실버 소지량: ", Silver)
          shel
        if Gs == "3" and Gold < 1750:
          print("골드가 부족합니다.")
          print("골드 소지량: ", Gold, "실버 소지량: ", Silver)
          shel
        elif Gs == "3":
          Gold = Gold - 1750
          Weapon.append('K3')
          print("K3 경기관총을 구매하였습니다.")
          print("골드 소지량: ", Gold, "실버 소지량: ", Silver)
          shel
        if Gs == "4" and Gold < 4000:
          print("골드가 부족합니다.")
          print("골드 소지량: ", Gold, "실버 소지량: ", Silver)
          shel
        elif Gs == "4":
          Gold = Gold - 4000
          Weapon.append('K14')
          print("K14 저격총을 구매하였습니다.")
          print("골드 소지량: ", Gold, "실버 소지량: ", Silver)
          shel
        if Gs == "5" and Gold < 900:
          print("골드가 부족합니다.")
          print("골드 소지량: ", Gold, "실버 소지량: ", Silver)
          shel
        elif Gs == "5":
          Gold = Gold - 900
          Weapon.append('M16')
          print("M16 소총을 구매하였습니다.")
          print("골드 소지량: ", Gold, "실버 소지량: ", Silver)
          shel
        if Gs == "6" and Gold < 900:
          print("골드가 부족합니다.")
          print("골드 소지량: ", Gold, "실버 소지량: ", Silver)
          shel
        elif Gs == "6":
          Gold = Gold - 2900
          Weapon.append('M60')
          print("M60 경기관총을 구매하였습니다.")
          print("골드 소지량: ", Gold, "실버 소지량: ", Silver)
          shel
        if Gs == "7" and Gold < 400:
          print("골드가 부족합니다.")
          print("골드 소지량: ", Gold, "실버 소지량: ", Silver)
          shel
        elif Gs == "7":
          Gold = Gold - 400
          Weapon.append('M60-REVOLVER')
          print("M60-REVOLVER 권총을 구매하였습니다.")
          print("골드 소지량: ", Gold, "실버 소지량: ", Silver)
          shel
        if Gs == "8":
          shel

      if sm == "2":
        Ammo = Ammo + 30
        Silver = Silver - 50
        print("탄약을 구매했습니다. +30발")
        print("현재 탄약 소지량", Ammo, "발")
      elif sm == "2" and Silver < 50:
        print("실버가 부족합니다.")
        print("골드 소지량: ", Gold, "실버 소지량: ", Silver)

      if sm == "3":
        print("MRE(30S), 수제 비상식량(12S), 오염된 식량(2S)")
        Fs = input("1.MRE, 2.수제 비상식량, 3.오염된 식량, 4.돌아간다.")
        if Fs == "1":
          Silver = Silver - 30
          MRE = MRE + 3
          print("MRE를 구매했습니다.")
          print("MRE 소지량", MRE)
        elif Fs == "2":
          Silver = Silver - 12
          handfood = handfood + 1
          print("수제 비상식량을 구매했습니다.")
          print("수제 비상식량 소지량: ", handfood)
        elif Fs == "3":
          Silver = Silver - 4
          polf = polf + 2
          print("오염된 식량을 구매했습니다.")
          print("오염된 식량 소지량", polf)
        elif Fs == "4":
          shel

      if sm == "4":
        Ws = input("1. 1리터=5Gold, 2. 5리터=24Gold, 3. 10리터=49Gold, 4. 20리터=98Gold, 5. 돌아간다.")
        if Ws == "1":
          Gold = Gold - 5
          water = water + 1
          print("물 1리터를 구매하였습니다.")
          print("골드 소지량: ", Gold, "실버 소지량: ", Silver)
        elif Ws == "1" and Gold < 5:
          print("골드가 부족합니다.")
          print("골드 소지량: ", Gold, "실버 소지량: ", Silver)
        if Ws == "2":
          Gold = Gold - 24
          water = water + 5
          print("물 5리터를 구매하였습니다.")
          print("골드 소지량: ", Gold, "실버 소지량: ", Silver)
        elif Ws == "2" and Gold < 24:
          print("골드가 부족합니다.")
          print("골드 소지량: ", Gold, "실버 소지량: ", Silver)
        if Ws == "3":
          Gold = Gold - 49
          water = water + 10
          print("물 10리터를 구매하였습니다.")
          print("골드 소지량: ", Gold, "실버 소지량: ", Silver)
        elif Ws == "3" and Gold < 49:
          print("골드가 부족합니다.")
          print("골드 소지량: ", Gold, "실버 소지량: ", Silver)
        if Ws == "4":
          Gold = Gold - 98
          water = water + 20
          print("물 20리터를 구매하였습니다")
          print("골드 소지량: ", Gold, "실버 소지량: ", Silver)
        elif Ws == "4" and Gold < 98:
          print("골드가 부족합니다.")
          print("골드 소지량: ", Gold, "실버 소지량: ", Silver)
        if Ws == "5":
          shel
      if sm == "5":
        ms = input("1.붕대, 2.구급상자, 3.모르핀, 4.간이 붕대, 5.돌아간다.")
        if ms == "1":
          bandage=input("1. 1개=5Gold, 2. 5개=20Gold, 3. 10개=40Gold")
          if bandage == "1":
            Gold = Gold-5
            stg.append ('bandage')
            print("붕대 1개를 구매하였습니다.")
            print("골드 소지량: ", Gold, "실버 소지량: ", Silver)
            shel
          elif bandage == "1" and Gold <5:
            print("골드가 부족합니다.")
            print("골드 소지량: ", Gold, "실버 소지량: ", Silver)
            shel
          if bandage == "2":
            Gold = Gold-20
            for i in range(1, 5):
              stg.append ('bandage')
            print("붕대 5개를 구매하였습니다.")
            print("골드 소지량: ", Gold, "실버 소지량: ", Silver)
            shel
          elif bandage == "2" and Gold <20:
            print("골드가 부족합니다.")
            print("골드 소지량: ", Gold, "실버 소지량: ", Silver)
            shel
          if bandage == "3":
            Gold = Gold-40
            for i in range(1, 10):
              stg.append ('bandage')
            print("붕대 10개를 구매하였습니다.")
            print("골드 소지량: ", Gold, "실버 소지량: ", Silver)
            shel
          elif bandage == "3" and Gold <40:
            print("골드가 부족합니다.")
            print("골드 소지량: ", Gold, "실버 소지량: ", Silver)
            shel
          if bandage == "4":
            shel
        if ms == "2":
          mk=input("1. 1개=10Gold, 2. 5개=40Gold, 3. 10개=80Gold, 4. 돌아간다.")
          if mk == "1":
            Gold = Gold-10
            stg.append ('mk')
            print("구급상자 1개를 구매하였습니다.")
            print("골드 소지량: ", Gold, "실버 소지량: ", Silver)
            shel
          elif mk == "1" and Gold <10:
            print("골드가 부족합니다.")
            print("골드 소지량: ", Gold, "실버 소지량: ", Silver)
            shel
          if mk == "2":
            Gold = Gold-40
            for i in range(1, 5):
              stg.append ('mk')
            print("구급상자 5개를 구매하였습니다.")
            print("골드 소지량: ", Gold, "실버 소지량: ", Silver)
            shel
          elif mk == "2" and Gold <40:
            print("골드가 부족합니다.")
            print("골드 소지량: ", Gold, "실버 소지량: ", Silver)
            shel
          if mk == "3":
            Gold = Gold-80
            for i in range(1, 10):
              stg.append ('mk')
            print("구급상자 10개를 구매하였습니다.")
            print("골드 소지량: ", Gold, "실버 소지량: ", Silver)
            shel
          elif mk == "3" and Gold <80:
            print("골드가 부족합니다.")
            print("골드 소지량: ", Gold, "실버 소지량: ", Silver)
            shel
          if mk == "4":
            shel
        if ms == "3":
          morphine=input("(1.)1개=20Gold, (2.)5개=80Gold, (3.)10개=160Gold")
          if morphine == "1":
            Gold = Gold-20
            stg.append ('morphine')
            print("모르핀 1개를 구매하였습니다.")
            print("골드 소지량: ", Gold, "실버 소지량: ", Silver)
            shel
          elif morphine == "1" and Gold <20:
            print("골드가 부족합니다.")
            print("골드 소지량: ", Gold, "실버 소지량: ", Silver)
            shel
          if morphine == "2":
            Gold = Gold-80
            for i in range(1, 5):
              stg.append ('morphine')
            print("모르핀 5개를 구매하였습니다.")
            print("골드 소지량: ", Gold, "실버 소지량: ", Silver)
            shel
          elif morphine == "2" and Gold <80:
            print("골드가 부족합니다.")
            print("골드 소지량: ", Gold, "실버 소지량: ", Silver)
            shel
          if morphine == "3":
            Gold = Gold-160
            for i in range(1, 10):
              stg.append ('morphine')
            print("모르핀 10개를 구매하였습니다.")
            print("골드 소지량: ", Gold, "실버 소지량: ", Silver)
            shel
          elif morphine == "3" and Gold <160:
            print("골드가 부족합니다.")
            print("골드 소지량: ", Gold, "실버 소지량: ", Silver)
            shel
        if ms == "4":
          hb=input("(1.)1개=4Gold, (2.)5개=16Gold, (3.)10개=32Gold")
          if hb == "1":
            Gold = Gold-4
            stg.append ('간이붕대')
            print("간이붕대 1개를 구매하였습니다.")
            print("골드 소지량: ", Gold, "실버 소지량: ", Silver)
            shel
          elif hb == "1" and Gold <4:
            print("골드가 부족합니다.")
            print("골드 소지량: ", Gold, "실버 소지량: ", Silver)
            shel
          if hb == "2":
            Gold = Gold-16
            for i in range(1, 5):
              stg.append ('간이붕대')
            print("간이붕대 5개를 구매하였습니다.")
            print("골드 소지량: ", Gold, "실버 소지량: ", Silver)
            shel
          elif hb == "2" and Gold <16:
            print("골드가 부족합니다.")
            print("골드 소지량: ", Gold, "실버 소지량: ", Silver)
            shel
          if hb == "3":
            Gold = Gold-32
            for i in range(1, 10):
              stg.append ('간이붕대')
            print("간이붕대 10개를 구매하였습니다.")
            print("골드 소지량: ", Gold, "실버 소지량: ", Silver)
            shel
          elif hb == "3" and Gold <32:
            print("골드가 부족합니다.")
            print("골드 소지량: ", Gold, "실버 소지량: ", Silver)
            shel
    if shel == "6": #지도
      c=0
      t=0

      fm = input("1.E-마트, 2.서울숲, 3.교도소, 4.공사장, 5.전자상가 ")
      if fm == "1":
        sleep = sleep - 35
        print("E-마트로 이동합니다...")
        time.sleep(1)
        print("이동중...")
        time.sleep(1)
        print("이동중..")
        time.sleep(1)
        print("이동중...")
        print("도착했습니다.")
        while c == 0:
          mv = input("1.조사한다., 2.쉘터로 돌아간다. ")
          if mv == "2":
            shel
            c = c + 1
          if mv == "1":
            for i in range(1, 20):
              list1.append("어두운 그림자 속에서 소형 크리쳐가 모습을 드러냅니다!!")
            for i in range(1, 15):
              list1.append("기괴한 웃음 소리를 내며 부랑자가 모습을 드러냅니다!!")
            for i in range(1, 10):
              list1.append("먹이의 냄새를 맡고 중형 크리쳐가 모습을 드러냅니다!!")
            for i in range(1, 10):
              list1.append("공사장에서 볼트를 발견했습니다...")
              stg.append("볼트")
            for i in range(1, 30):
              list1.append("공사장에서 낡은 고철을 발견했습니다...")
              stg.append("고철 조각")
            for i in range(1, 5):
              list1.append("공사장에서 공구상자를 발견했습니다...")
              stg.append("공구상자")
            for i in range(1, 10):
              list1.append("공사장에서 쓰다 만 전선을 발견했습니다...")
              stg.append("전선")
            ch1 = random.choice(list1)
            print(ch1)
            if ch1 == '어두운 그림자 속에서 소형 크리쳐가 모습을 드러냅니다!!':
              SCHP = 60
              print("소형 크리쳐 hp: ", SCHP)
              fight = input("1.싸운다, 2.도망친다 ")
              t=0
              if fight == "1":
                while SCHP > 0 and t == 0:
                  FOM = input("1.공격, 2.회피")
                  if FOM == "1":
                    if 'K5' in eq:
                      for f in range(1, 70):
                        lista.append("공격 성공!")
                      for f in range(1, 30):
                        lista.append("빗나감!")
                      As = random.choice(lista)
                      print(As)
                      if As == '공격 성공!':
                        Ammo = Ammo - 1
                        SCHP = SCHP - 19
                        print("소형 크리쳐 hp: ", SCHP)
                        print("탄약: ", Ammo)
                        lista.clear()
                      else:
                        Ammo = Ammo - 1
                        lista.clear()
                    if 'K2' in eq:
                      for f in range(1, 55):
                        lista.append("공격 성공!")
                      for f in range(1, 45):
                        lista.append("빗나감!")
                      As = random.choice(lista)
                      print(As)
                      if As == '공격 성공!':
                        Ammo = Ammo - 2
                        SCHP = SCHP - 30
                        print("소형 크리쳐 hp: ", SCHP)
                        print("탄약: ", Ammo)
                        lista.clear()
                      else:
                        Ammo = Ammo - 2
                        lista.clear()
                    if 'K3' in eq:
                      for f in range(1, 50):
                        lista.append("공격 성공!")
                      for f in range(1, 50):
                        lista.append("빗나감!")
                      As = random.choice(lista)
                      print(As)
                      if As == '공격 성공!':
                        Ammo = Ammo - 5
                        SCHP = SCHP - 50
                        print("소형 크리쳐 hp: ", SCHP)
                        print("탄약: ", Ammo)
                        lista.clear()
                      else:
                        Ammo = Ammo - 5
                        lista.clear()
                    if 'K14' in eq:
                      for f in range(1, 95):
                        lista.append("공격 성공!")
                      for f in range(1, 5):
                        lista.append("빗나감!")
                      As = random.choice(lista)
                      print(As)
                      if As == '공격 성공!':
                        Ammo = Ammo - 10
                        SCHP = SCHP - 100
                        print("소형 크리쳐 hp: ", SCHP)
                        print("탄약: ", Ammo)
                        lista.clear()
                      else:
                        print("빗나감!")
                        Ammo = Ammo - 10
                        lista.clear()
                    if 'M60' in eq:
                      for f in range(1, 65):
                        lista.append("공격 성공!")
                      for f in range(1, 35):
                        lista.append("빗나감!")
                      As = random.choice(lista)
                      print(As)
                      if As == '공격 성공!':
                        Ammo = Ammo - 5
                        SCHP = SCHP - 40
                        print("소형 크리쳐 hp: ", SCHP)
                        print("탄약: ", Ammo)
                        lista.clear()
                      else:
                        print("빗나감!")
                        Ammo = Ammo - 5
                        lista.clear()
                    if 'M16' in eq:
                      for f in range(1, 70):
                        lista.append("공격 성공!")
                      for f in range(1, 30):
                        lista.append("빗나감!")
                      As = random.choice(lista)
                      print(As)
                      if As == '공격 성공!':
                        Ammo = Ammo - 1
                        SCHP = SCHP - 25
                        print("소형 크리쳐 hp: ", SCHP)
                        print("탄약: ", Ammo)
                        lista.clear()
                      else:
                        print("빗나감!")
                        Ammo = Ammo - 1
                        lista.clear()
                    if 'M60-REVOLVER' in eq:
                      for f in range(1, 45):
                        lista.append("공격 성공!")
                      for f in range(1, 55):
                        lista.append("빗나감!")
                      As = random.choice(lista)
                      print(As)
                      if As == '공격 성공!':
                        Ammo = Ammo - 1
                        SCHP = SCHP - 40
                        print("소형 크리쳐 hp: ", SCHP)
                        print("탄약: ", Ammo)
                        lista.clear()
                      else:
                        print("빗나감!")
                        Ammo = Ammo - 1
                        lista.clear()
                  if SCHP <=0:
                    Gold = Gold + 20
                    print("골드 소지량: ", Gold)
                    t=t+1
                    list1.clear()
                    lista.clear()
                    mv    
              elif fight == "2":
                list1.clear()
                lista.clear()
                mv

      elif fm == "2":
        sleep = sleep - 35
        print("서울숲으로 이동합니다...")
        time.sleep(1)
        print("이동중...")
        time.sleep(1)
        print("이동중..")
        time.sleep(1)
        print("이동중...")
        print("도착했습니다.")

      elif fm == "3":
        sleep = sleep - 35
        print("교도소로 이동합니다...")
        time.sleep(1)
        print("이동중...")
        time.sleep(1)
        print("이동중..")
        time.sleep(1)
        print("이동중...")
        print("도착했습니다.")
        while c == 0:
          mv = input("1.조사한다., 2.쉘터로 돌아간다. ")
          if mv == "2":
            shel
            c = c + 1
          elif mv == "1":
            for i in range(1, 20):
              list1.append("어두운 그림자 속에서 소형 크리쳐가 모습을 드러냅니다!!")
            for i in range(1, 15):
              list1.append("기괴한 웃음 소리를 내며 부랑자가 모습을 드러냅니다!!")
            for i in range(1, 10):
              list1.append("먹이의 냄새를 맡고 중형 크리쳐가 모습을 드러냅니다!!")
            for i in range(1, 10):
              list1.append("공사장에서 볼트를 발견했습니다...")
              stg.append("볼트")
            for i in range(1, 30):
              list1.append("공사장에서 낡은 고철을 발견했습니다...")
              stg.append("고철 조각")
            for i in range(1, 5):
              list1.append("공사장에서 공구상자를 발견했습니다...")
              stg.append("공구상자")
            for i in range(1, 10):
              list1.append("공사장에서 쓰다 만 전선을 발견했습니다...")
              stg.append("전선")
            ch1 = random.choice(list1)
          print(ch1)

          if ch1 == '어두운 그림자 속에서 소형 크리쳐가 모습을 드러냅니다!!':
            SCHP = 60
            print("소형 크리쳐 hp: ", SCHP)
            fight = input("1.싸운다, 2.도망친다 ")
            if fight == "1":
              while SCHP >= 0:
                FOM = input("1.공격, 2.회피")
                if FOM == "1":
                  for f in range(1, 50):
                    lista.append("공격 성공!")
                  for f in range(1, 50):
                    lista.append("빗나감!")
                  print("탄약: ", Ammo)
                  As = random.choice(lista)
                  print(As)
                  if 'K5' in eq and As == '공격 성공!':
                    Ammo = Ammo - 1
                    SCHP = SCHP - 19
                    print("크리쳐 hp: ", SCHP)
                    print("탄약: ", Ammo)
                  elif 'k2' in eq and As == '공격 성공!':
                    Ammo = Ammo - 3
                    SCHP = SCHP - 28
                    print("크리쳐 hp: ", SCHP)
                    print("탄약: ", Ammo)
                  elif 'k3' in eq and As == '공격 성공!':
                    Ammo = Ammo - 5
                    SCHP = SCHP - 40
                    print("크리쳐 hp: ", SCHP)
                    print("탄약: ", Ammo)
                  if SCHP <= 0:
                    Gold = Gold + 5
                    SCHP = 60
                    list1.clear()
                    lista.clear()
                    mv
            elif fight == "2":
              list1.clear()
              lista.clear()
              mv

      elif fm == "4":
        sleep = sleep - 35
        print("공사장로 이동합니다...")
        time.sleep(1)
        print("이동중...")
        time.sleep(1)
        print("이동중..")
        time.sleep(1)
        print("이동중...")
        print("도착했습니다.")
        while c == 0:
          mv = input("1.조사한다., 2.쉘터로 돌아간다.")
          if mv == "2":
            shel
            c = c + 1
          elif mv == "1":
            for i in range(1, 20):
              list1.append("어두운 그림자 속에서 소형 크리쳐가 모습을 드러냅니다!!")
            for i in range(1, 15):
              list1.append("기괴한 웃음 소리를 내며 부랑자가 모습을 드러냅니다!!")
            for i in range(1, 10):
              list1.append("먹이의 냄새를 맡고 중형 크리쳐가 모습을 드러냅니다!!")
            for i in range(1, 10):
              list1.append("공사장에서 볼트를 발견했습니다...")
              stg.append("볼트")
            for i in range(1, 30):
              list1.append("공사장에서 낡은 고철을 발견했습니다...")
              stg.append("고철 조각")
            for i in range(1, 5):
              list1.append("공사장에서 공구상자를 발견했습니다...")
              stg.append("공구상자")
            for i in range(1, 10):
              list1.append("공사장에서 쓰다 만 전선을 발견했습니다...")
              stg.append("전선")
            ch1 = random.choice(list1)
          print(ch1)

          if ch1 == '어두운 그림자 속에서 소형 크리쳐가 모습을 드러냅니다!!':
            SCHP = 60
            print("소형 크리쳐 hp: ", SCHP)
            fight = input("1.싸운다, 2.도망친다 ")
            if fight == "1":
              while SCHP >= 0:
                FOM = input("1.공격, 2.회피")
                if FOM == "1":
                  for f in range(1, 50):
                    lista.append("공격 성공!")
                  for f in range(1, 50):
                    lista.append("빗나감!")
                  print("탄약: ", Ammo)
                  As = random.choice(lista)
                  print(As)
                  if 'K5' in eq and As == '공격 성공!':
                    Ammo = Ammo - 1
                    SCHP = SCHP - 19
                    print("크리쳐 hp: ", SCHP)
                    print("탄약: ", Ammo)
                  elif 'k2' in eq and As == '공격 성공!':
                    Ammo = Ammo - 3
                    SCHP = SCHP - 28
                    print("크리쳐 hp: ", SCHP)
                    print("탄약: ", Ammo)
                  elif 'k3' in eq and As == '공격 성공!':
                    Ammo = Ammo - 5
                    SCHP = SCHP - 40
                    print("크리쳐 hp: ", SCHP)
                    print("탄약: ", Ammo)
                  if SCHP <= 0:
                    Gold = Gold + 5
                    SCHP = 60
                    list1.clear()
                    lista.clear()
                    mv
            elif fight == "2":
              list1.clear()
              lista.clear()
              mv

      elif fm == "5":
        sleep = sleep - 35
        print("전자상가로 이동합니다...")
        time.sleep(1)
        print("이동중...")
        time.sleep(1)
        print("이동중..")
        time.sleep(1)
        print("이동중...")
        print("도착했습니다.")
        while c == 0:
          mv = input("1.조사한다., 2.쉘터로 돌아간다.")
          if mv == "2":
            shel
            c = c + 1
          elif mv == "1":
            for i in range(1, 20):
              list1.append("어두운 그림자 속에서 소형 크리쳐가 모습을 드러냅니다!!")
            for i in range(1, 15):
              list1.append("기괴한 웃음 소리를 내며 부랑자가 모습을 드러냅니다!!")
            for i in range(1, 10):
              list1.append("먹이의 냄새를 맡고 중형 크리쳐가 모습을 드러냅니다!!")
            for i in range(1, 10):
              list1.append("공사장에서 볼트를 발견했습니다...")
              stg.append("볼트")
            for i in range(1, 30):
              list1.append("공사장에서 낡은 고철을 발견했습니다...")
              stg.append("고철 조각")
            for i in range(1, 5):
              list1.append("공사장에서 공구상자를 발견했습니다...")
              stg.append("공구상자")
            for i in range(1, 10):
              list1.append("공사장에서 쓰다 만 전선을 발견했습니다...")
              stg.append("전선")
            ch1 = random.choice(list1)
          print(ch1)

          if ch1 == '어두운 그림자 속에서 소형 크리쳐가 모습을 드러냅니다!!':
            SCHP = 60
            print("소형 크리쳐 hp: ", SCHP)
            fight = input("1.싸운다, 2.도망친다 ")
            if fight == "1":
              while SCHP >= 0:
                FOM = input("1.공격, 2.회피")
                if FOM == "1":
                  for f in range(1, 50):
                    lista.append("공격 성공!")
                  for f in range(1, 50):
                    lista.append("빗나감!")
                  print("탄약: ", Ammo)
                  As = random.choice(lista)
                  print(As)
                  if 'K5' in eq and As == '공격 성공!':
                    Ammo = Ammo - 1
                    SCHP = SCHP - 19
                    print("크리쳐 hp: ", SCHP)
                    print("탄약: ", Ammo)
                  elif 'k2' in eq and As == '공격 성공!':
                    Ammo = Ammo - 3
                    SCHP = SCHP - 28
                    print("크리쳐 hp: ", SCHP)
                    print("탄약: ", Ammo)
                  elif 'k3' in eq and As == '공격 성공!':
                    Ammo = Ammo - 5
                    SCHP = SCHP - 40
                    print("크리쳐 hp: ", SCHP)
                    print("탄약: ", Ammo)
                  if SCHP <= 0:
                    Gold = Gold + 5
                    SCHP = 60
                    list1.clear()
                    lista.clear()
                    mv
                    t=0
            elif fight == "2":
              list1.clear()
              lista.clear()
              mv

#K2 = 30, 28, "K2"

#K5 = 19, 12, "K5"

#K3 = 40, 200, "K3"

#K14 = 200, 9, "K14"

#M16 = 29, 27, "M16"

#M60 = 100, 100, "M60"

#SW_m60 = 25, 6, "SW_m60"
