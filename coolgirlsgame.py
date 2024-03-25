import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
from tkinter.ttk import *
import random
import json
import webbrowser

window = tk.Tk()
window.title('cool girls for u<3')
window.config(background='white')
icon = tk.PhotoImage(file=f'images/icons/icon.png')
window.iconphoto(False, icon)
window.geometry('1200x700+200+50')
window.resizable(False, False)
window.wm_attributes("-transparentcolor", "green")
window.attributes("-topmost",True)


# ============================Переменнные===================================


characters = ['mikasa', 'ioko', 'mitsuri', 'eris', 'silphy', 'roxy', 'rei', 'nami', 'hinata', 'nezuko', 'hori', 'frieren', 'fern', 'yudzuriha', 'makima', 'ai', 'kitagawa','rem','misato','sakura', 'zerotwo', 'emilia', 'toru', 'asuna','hutao', 'aska','yanka','speedwagoon','arbus', 'leon']


cm = 'Обычная'

ep = 'Эпическая'

my = 'Мифическая'

ni = 'НИЧЕРТА СЕБЕ'

with open('save.json', 'r', encoding='utf-8') as save_fl:
    save = json.load(save_fl)
crystals = save["crystals"]
active_characters = save['active_characters']
haved_characters = save['haved_characters']


# =================================Импорт фоток========================================

homepage_bg_image = tk.PhotoImage(file=f'images/backgrounds/homepage_bg.png')
immmmmmmmmmmmmmmm = f"images/backgrounds/homepage_bg.png"
home1 = Image.open(immmmmmmmmmmmmmmm).convert("1")
ssssssss = (1200, 700)
home1 = ImageTk.BitmapImage(home1.resize(ssssssss))
home2 = ImageTk.PhotoImage(Image.open(immmmmmmmmmmmmmmm).resize(ssssssss))
homepage_bg = tk.Label(window, image=home2, bd=0)
homepage_bg.place(x=0,y=0)

menu_bg_image = tk.PhotoImage(file=f'images/backgrounds/menu_bg.png')

character_ban_image = tk.PhotoImage(file=f'images/icons/character_ban_icon.png')

size = (220,410)
mikasa_im7g = f"images/characters/mikasa.png"
mikasa_c7 = ImageTk.PhotoImage(Image.open(mikasa_im7g).resize(size))  
mikasa_image = tk.Label(window, image=mikasa_c7, bd=0)

ioko_im7g = f"images/characters/ioko.png"
ioko_c7 = ImageTk.PhotoImage(Image.open(ioko_im7g).resize(size))      
ioko_image = tk.Label(window, image=ioko_c7, bd=0)

mitsuri_im7g = f"images/characters/mitsuri.png"
mitsuri_c7 = ImageTk.PhotoImage(Image.open(mitsuri_im7g).resize(size))
mitsuri_image = tk.Label(window, image=mitsuri_c7, bd=0)

eris_im7g = f"images/characters/eris.png"
eris_c7 = ImageTk.PhotoImage(Image.open(eris_im7g).resize(size))
eris_image = tk.Label(window, image=eris_c7, bd=0)

silphy_im7g = f"images/characters/silphy.png"
silphy_c7 = ImageTk.PhotoImage(Image.open(silphy_im7g).resize(size))
silphy_image = tk.Label(window, image=silphy_c7, bd=0)

roxy_im7g = f"images/characters/roxy.png"
roxy_c7 = ImageTk.PhotoImage(Image.open(roxy_im7g).resize(size))
roxy_image = tk.Label(window, image=roxy_c7, bd=0)

rei_im7g = f"images/characters/rei.png"
rei_c7 = ImageTk.PhotoImage(Image.open(rei_im7g).resize(size))
rei_image = tk.Label(window, image=rei_c7, bd=0)

nami_im7g = f"images/characters/nami.png"
nami_c7 = ImageTk.PhotoImage(Image.open(nami_im7g).resize(size))
nami_image = tk.Label(window, image=nami_c7, bd=0)

hinata_im7g = f"images/characters/hinata.png"
hinata_c7 = ImageTk.PhotoImage(Image.open(hinata_im7g).resize(size))
hinata_image = tk.Label(window, image=hinata_c7, bd=0)

nezuko_im7g = f"images/characters/nezuko.png"
nezuko_c7 = ImageTk.PhotoImage(Image.open(nezuko_im7g).resize(size))
nezuko_image = tk.Label(window, image=nezuko_c7, bd=0)

hori_im7g = f"images/characters/hori.png"
hori_c7 = ImageTk.PhotoImage(Image.open(hori_im7g).resize(size))
hori_image = tk.Label(window, image=hori_c7, bd=0)

frieren_im7g = f"images/characters/frieren.png"
frieren_c7 = ImageTk.PhotoImage(Image.open(frieren_im7g).resize(size))
frieren_image = tk.Label(window, image=frieren_c7, bd=0)

fern_im7g = f"images/characters/fern.png"
fern_c7 = ImageTk.PhotoImage(Image.open(fern_im7g).resize(size))
fern_image = tk.Label(window, image=fern_c7, bd=0)

yudzuriha_im7g = f"images/characters/yudzuriha.png"
yudzuriha_c7 = ImageTk.PhotoImage(Image.open(yudzuriha_im7g).resize(size))
yudzuriha_image = tk.Label(window, image=yudzuriha_c7, bd=0)

makima_im7g = f"images/characters/makima.png"
makima_c7 = ImageTk.PhotoImage(Image.open(makima_im7g).resize(size))
makima_image = tk.Label(window, image=makima_c7, bd=0)

ai_im7g = f"images/characters/ai.png"
ai_c7 = ImageTk.PhotoImage(Image.open(ai_im7g).resize(size))
ai_image = tk.Label(window, image=ai_c7, bd=0)

kitagawa_im7g = f"images/characters/kitagawa.png"
kitagawa_c7 = ImageTk.PhotoImage(Image.open(kitagawa_im7g).resize(size))
kitagawa_image = tk.Label(window, image=kitagawa_c7, bd=0)

rem_im7g = f"images/characters/rem.png"
rem_c7 = ImageTk.PhotoImage(Image.open(rem_im7g).resize(size))
rem_image = tk.Label(window, image=rem_c7, bd=0)

misato_im7g = f"images/characters/misato.png"
misato_c7 = ImageTk.PhotoImage(Image.open(misato_im7g).resize(size))
misato_image = tk.Label(window, image=misato_c7, bd=0)

sakura_im7g = f"images/characters/sakura.png"
sakura_c7 = ImageTk.PhotoImage(Image.open(sakura_im7g).resize(size))
sakura_image = tk.Label(window, image=sakura_c7, bd=0)

zerotwo_im7g = f"images/characters/zerotwo.png"
zerotwo_c7 = ImageTk.PhotoImage(Image.open(zerotwo_im7g).resize(size))
zerotwo_image = tk.Label(window, image=zerotwo_c7, bd=0)

emilia_im7g = f"images/characters/emilia.png"
emilia_c7 = ImageTk.PhotoImage(Image.open(emilia_im7g).resize(size))
emilia_image = tk.Label(window, image=emilia_c7, bd=0)

toru_im7g = f"images/characters/toru.png"
toru_c7 = ImageTk.PhotoImage(Image.open(toru_im7g).resize(size))
toru_image = tk.Label(window, image=toru_c7, bd=0)

asuna_im7g = f"images/characters/asuna.png"
asuna_c7 = ImageTk.PhotoImage(Image.open(asuna_im7g).resize(size))
asuna_image = tk.Label(window, image=asuna_c7, bd=0)

hutao_im7g = f"images/characters/hutao.png"
hutao_c7 = ImageTk.PhotoImage(Image.open(hutao_im7g).resize(size))
hutao_image = tk.Label(window, image=hutao_c7, bd=0)

aska_im7g = f"images/characters/aska.png"
aska_c7 = ImageTk.PhotoImage(Image.open(aska_im7g).resize(size))
aska_image = tk.Label(window, image=aska_c7, bd=0)

speedwagoon_im7g = f"images/characters/speedwagoon.png"
speedwagoon_c7 = ImageTk.PhotoImage(Image.open(speedwagoon_im7g).resize(size))
speedwagoon_image = tk.Label(window, image=speedwagoon_c7, bd=0)

arbus_im7g = f"images/characters/arbus.png"
arbus_c7 = ImageTk.PhotoImage(Image.open(arbus_im7g).resize(size))
arbus_image = tk.Label(window, image=arbus_c7, bd=0)

leon_im7g = f"images/characters/leon.png"
leon_c7 = ImageTk.PhotoImage(Image.open(leon_im7g).resize(size))
leon_image = tk.Label(window, image=leon_c7, bd=0)

def characetrs_repalce():
    global active_character1,active_character2,active_character3
    active1 = active_character1.get()
    active2 = active_character2.get()
    active3 = active_character3.get()
    homepage_fg()
    if active1 == active2:
        aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa= 0
    elif active1 == active3:
        aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa= 0
    elif active2 == active3:
        aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa= 0
    else:
        active_characters.pop(0)
        active_characters.insert(0, active2)
        active_characters.pop(1)
        active_characters.insert(1, active1)
        active_characters.pop(2)
        active_characters.insert(2, active3)
    homepage_chplace()

class character():
    def __init__(self, eng_name, name, rarity, description, image):
        global cm, ep,my,ni,mikasa_im7g,ioko_im7g,mitsuri_im7g,eris_im7g,silphy_im7g,roxy_im7g,rei_im7g,nami_im7g,robin_im7g,yamato_im7g,hinata_im7g,nezuko_im7g,hori_im7g,matsumoto_im7g,frieren_im7g,fern_im7g,yudzuriha_im7g,makima_im7g,ai_im7g,kitagawa_im7g,rem_im7g,misato_im7g,sakura_im7g,zerotwo_im7g,emilia_im7g,toru_im7g,asuna_im7g,hutao_im7g,aska_im7g,yanka_im7g,speedwagoon_im7g,arbus_im7g,leon_im7g
        self.nick = eng_name
        self.name = name
        self.des = description
        self.rarity = rarity
        self.lvl = save[f"{self.nick}" + "_lvl"]
        self.wimage = image
        if self.rarity == cm:
            self.hp = 2500 + self.lvl*0.05*10000
            self.atk = 2500 + self.lvl*0.05*10000
            self.c = 'grey'
            self.gg1 = tk.Label(window, text = f'Lvl {self.lvl}, {self.hp}♥️{self.atk}⚔️', bg='#28b834')
            self.gg2 = tk.Label(window, text = f'{self.rarity}', bg='#28b834', foreground=self.c, font=('Verdana', 15))
        elif self.rarity == ep:
            self.hp = 5000 + self.lvl*0.05*20000
            self.atk = 5000 + self.lvl*0.05*20000
            self.c = 'purple'
            self.gg1 = tk.Label(window, text = f'Lvl {self.lvl}, {self.hp}♥️{self.atk}⚔️', bg='#28b834')
            self.gg2 = tk.Label(window, text = f'{self.rarity}', bg='#28b834', foreground=self.c, font=('Verdana', 15))
        elif self.rarity == my:
            self.hp = 10000 + self.lvl*0.05*30000
            self.atk = 10000 + self.lvl*0.05*30000
            self.c = 'red'
            self.gg1 = tk.Label(window, text = f'Lvl {self.lvl}, {self.hp}♥️{self.atk}⚔️', bg='#28b834')
            self.gg2 = tk.Label(window, text = f'{self.rarity}', bg='#28b834', foreground=self.c, font=('Verdana', 15))
        elif self.rarity == ni:
            self.hp = 20000 + self.lvl*0.05*50000
            self.atk = 20000 + self.lvl*0.05*50000
            self.c = 'gold'
            self.gg1 = tk.Label(window, text = f'Lvl {self.lvl}, {self.hp}♥️{self.atk}⚔️', bg='#28b834')
            self.gg2 = tk.Label(window, text = f'{self.rarity}', bg='#28b834', foreground=self.c, font=('Verdana', 15))
        
    def lvl_up(self):
        if self.lvl <22:
            self.lvl = self.lvl + 1
    
    def lvl_s(self):
        return (self.lvl - 1)
    
    def add(self):
        if self.name in haved_characters:
            if self.lvl !=20:
                self.lvl +=1
                if self.rarity == cm:
                    self.hp = 2500 + self.lvl*0.05*10000
                    self.atk = 2500 + self.lvl*0.05*10000
                elif self.rarity == ep:
                    self.hp = 5000 + self.lvl*0.05*20000
                    self.atk = 5000 + self.lvl*0.05*20000
                elif self.rarity == my:
                    self.hp = 10000 + self.lvl*0.05*30000
                    self.atk = 10000 + self.lvl*0.05*30000
                elif self.rarity == ni:
                    self.hp = 20000 + self.lvl*0.05*50000
                    self.atk = 20000 + self.lvl*0.05*50000
        else:
            haved_characters.append(self.name)                                                                                                                                                                                                                                                                                                                                                                                       
            if self.lvl == 0:
                self.lvl = self.lvl + 1
    
    def save(self):
        # lvl = f'{self}_lvl'
        # locals()[lvl] = self.lvl
        return f'{self.nick}_lvl = {self.lvl}\n'
    
    def info_place(self,xxxxx,yyyyy):
        if self.rarity == cm:
            self.gg1.place(x = xxxxx+10,y=yyyyy)
            self.gg2.place(x = xxxxx+33,y=yyyyy+20)
        elif self.rarity == ep:
            self.gg1.place(x = xxxxx+10,y=yyyyy)
            self.gg2.place(x = xxxxx+25,y=yyyyy+20)
        elif self.rarity == my:
            self.gg1.place(x = xxxxx+8,y=yyyyy)
            self.gg2.place(x = xxxxx+15,y=yyyyy+20)
        elif self.rarity == ni:
            self.gg1.place(x = xxxxx+6,y=yyyyy)
            self.gg2.place(x = xxxxx,y=yyyyy+20)
    
    def homepage_44(self):
        if self.name in active_characters:
            if active_characters.index(self.name) == 0:  
                self.wimage.place(x=490,y=140)        
                self.info_place(520,550)
            elif active_characters.index(self.name) == 1:
                self.wimage.place(x=240,y=140)        
                self.info_place(270,550)
            elif active_characters.index(self.name) == 2:
                self.wimage.place(x=740,y=140)        
                self.info_place(770,550)
    
    def _fg(self):
        if self.name in active_characters:
            self.wimage.place_forget()
            self.gg1.place_forget()
            self.gg2.place_forget()

def homepage_chplace():
    global active_character1,active_character2,active_character3,mikasa_im7g,ioko_im7g,mitsuri_im7g,eris_im7g,silphy_im7g,roxy_im7g,rei_im7g,nami_im7g,robin_im7g,yamato_im7g,hinata_im7g,nezuko_im7g,hori_im7g,matsumoto_im7g,frieren_im7g,fern_im7g,yudzuriha_im7g,makima_im7g,ai_im7g,kitagawa_im7g,rem_im7g,misato_im7g,sakura_im7g,zerotwo_im7g,emilia_im7g,toru_im7g,asuna_im7g,hutao_im7g,aska_im7g,yanka_im7g,speedwagoon_im7g,arbus_im7g,leon_im7g,mikasa_image,ioko_image,mitsuri_image,eris_image,silphy_image,roxy_image,rei_image,nami_image,robin_image,yamato_image,hinata_image,nezuko_image,hori_image,matsumoto_image,frieren_image,fern_image,yudzuriha_image,makima_image,ai_image,kitagawa_image,rem_image,misato_image,sakura_image,zerotwo_image,emilia_image,toru_image,asuna_image,hutao_image,aska_image,yanka_image,speedwagoon_image,arbus_image,leon_image
    dlksadjlksah = 0
    while dlksadjlksah != 2:
        dlksadjlksah +=1
        if '' in active_characters:
            if len(haved_characters) >= 4:
                haved_characters.pop(1)
                active_characters.pop(1)
                active_characters.append(haved_characters[2])
    for i in echaracters:
        i.homepage_44()
    active_character1 = ttk.Combobox(window, values=haved_characters)
    active_character1.current(haved_characters.index(active_characters[1]))
    active_character1.place(x=280,y=140)
    active_character2 = ttk.Combobox(window, values=haved_characters)
    active_character2.current(haved_characters.index(active_characters[0]))
    active_character2.place(x=530,y=140)
    active_character3 = ttk.Combobox(window, values=haved_characters)
    active_character3.current(haved_characters.index(active_characters[2]))
    active_character3.place(x=780,y=140)
    change_btn.place(x=950,y=140)
    autor_lbl.place(x=1070, y=675)

def homepage_fg():
    global mikasa_im7g,ioko_im7g,mitsuri_im7g,eris_im7g,silphy_im7g,roxy_im7g,rei_im7g,nami_im7g,hinata_im7g,nezuko_im7g,hori_im7g,frieren_im7g,fern_im7g,yudzuriha_im7g,makima_im7g,ai_im7g,kitagawa_im7g,rem_im7g,misato_im7g,sakura_im7g,zerotwo_im7g,emilia_im7g,toru_im7g,asuna_im7g,hutao_im7g,aska_im7g,yanka_im7g,speedwagoon_im7g,arbus_im7g,leon_im7g,mikasa_image,ioko_image,mitsuri_image,eris_image,silphy_image,roxy_image,rei_image,nami_image,robin_image,yamato_image,hinata_image,nezuko_image,hori_image,matsumoto_image,frieren_image,fern_image,yudzuriha_image,makima_image,ai_image,kitagawa_image,rem_image,misato_image,sakura_image,zerotwo_image,emilia_image,toru_image,asuna_image,hutao_image,aska_image,yanka_image,speedwagoon_image,arbus_image,leon_image
    for i in echaracters:
        i._fg()
    active_character1.place_forget()
    active_character2.place_forget()
    active_character3.place_forget()
    change_btn.place_forget()
    autor_lbl.place_forget()
    tgc_btn.place_forget()



# ===============================Персонажи====================================

mikasa = character("mikasa", "Микаса", cm, "Шинкует титанов канцелярскими ножичками", mikasa_image)
ioko = character("ioko", "Йоко", cm, "Крутая тян с винтовкой😎", ioko_image)
mitsuri = character("mitsuri", "Мицури", cm, "Одна шинкует титанов, эта демонов...", mitsuri_image)
silphy = character("silphy", "Сильфи", cm, "Эльфийка и просто заботливая жена", silphy_image)   
roxy = character("roxy", "Рокси", cm, "Великовозрастная лоли-маг", roxy_image)
eris = character("eris", "Эрис", cm, "Даст вам по лбу, чтоб не втыкали", eris_image)
rei = character("rei", "Рей", cm, "Кто я? Аянами Рей.  А кто ты?", rei_image)
nami = character("nami", "Нами", cm, "Гугл карты", nami_image) 
hinata = character("hinata", "Хината", cm, "Я девушка Наруто туц туц туц", hinata_image)
nezuko = character("nezuko", "Незуко", cm, "Девушка-демон с бамбуком во рту ", nezuko_image)
hori = character("hori", "Хори", cm, "Добрая и милая", hori_image)
frieren = character("frieren", "Фрирен", cm, "Выпадет только спустя 1000 лет со смерти героя Гиммеля", frieren_image)
fern = character("fern", "Ферн", cm, "Хозяйственная девушка-маг, без \nкоторой Фрирен попала бы \nв рабство", fern_image)
yudzuriha = character("yudzuriha", "Юдзуриха", cm, "Хитрая и ловкая татарка", yudzuriha_image)
makima = character("makima", "Макима", ep, "Кук... кулко.. куко.. клуко... куколд короче", makima_image)
ai = character("ai", "Аи", ep, "Японский идол с двумя детьми", ai_image)
kitagawa = character("kitagawa", "Китагва", ep, "Косплеит вайфушек хикканов", kitagawa_image)
rem = character("rem", "Рэм", ep, "Шикарная горничная-демон, умеющая размахивать валыной", rem_image)
misato = character('misato', 'Мисато', ep, 'На меня глядит игриво пиво пиво пиво пиво', misato_image)
sakura = character("sakura", "Сакура", ep, "Я (не)девушка наруто туц туц туц", sakura_image)
zerotwo = character("zerotwo", "02", ep, "ААА СЛАДКОЕЖКА С РОЖКАМИ", zerotwo_image)
emilia = character("emilia", "Эмилия", my, "ЧЕРТОВСКИ ОБАЯТЕЛЬНАЯ ПОЛУЭЛЬФИЙКА", emilia_image)
toru = character("toru", "Тору", my, "Миленькая горничная с рожками, вайфушка хикканов", toru_image)
asuna = character("asuna", "Асуна", my, "Женщина мечты: и от бандитов защитит, и колбаску для оливье накрошит.", asuna_image)
hutao = character("hutao", "Ху Тао", my, "Прекрасная девушка, чьи нежные ручки отправят вас в могилу",hutao_image)
aska = character("aska", "Аска", my, "Не такая как все, любит любителей арбузов",aska_image)
speedwagoon = character("speedwagoon", "Спидвагон", ni, "Просто лучшая вайфу",speedwagoon_image)
arbus = character("arbus", "Орбус", ni, "Ненавидим любителем любителей арбузов",arbus_image)
leon = character("leon", "Леон", ni, "Любит сосать", leon_image)
echaracters = [mikasa, ioko, mitsuri, eris, silphy, roxy, rei, nami, hinata, nezuko, hori, frieren, fern, yudzuriha, makima, ai, kitagawa, rem, misato, sakura, zerotwo, emilia, toru, asuna, hutao, aska, speedwagoon, arbus, leon]
echaracters_atk = [mikasa.atk, ioko.atk, mitsuri.atk, eris.atk, silphy.atk, roxy.atk, rei.atk, nami.atk, hinata.atk, nezuko.atk, hori.atk, frieren.atk, fern.atk, yudzuriha.atk, makima.atk, ai.atk, kitagawa.atk, rem.atk, misato.atk, sakura.atk, zerotwo.atk, emilia.atk, toru.atk, asuna.atk, hutao.atk, aska.atk, speedwagoon.atk, arbus.atk, leon.atk]
cm_characters = [mikasa, ioko, mitsuri, eris, silphy, roxy, rei, nami, hinata, nezuko, hori, frieren, fern, yudzuriha, ]
ep_characters = [makima, ai, kitagawa, rem, sakura, zerotwo, misato]
my_characters = [emilia, toru, asuna, hutao, aska ]
ni_characters = [speedwagoon, arbus, leon, ]

menu_icon = Image.open(f'images/icons/menu_icon.png')
menu_icon.thumbnail((55,55))
menu_icon = ImageTk.PhotoImage(menu_icon)

casino_icon = Image.open(f'images/icons/casino_icon.png')
casino_icon.thumbnail((55,55))
casino_icon = ImageTk.PhotoImage(casino_icon)

play_icon = Image.open(f'images/icons/play_icon.png')
play_icon.thumbnail((296, 92))
play_icon = ImageTk.PhotoImage(play_icon)

tg4_image = Image.open(f'images/icons/tg4.png')
tg4_image.thumbnail((25, 25))
tg4_image = ImageTk.PhotoImage(tg4_image)

back_icon = Image.open(f'images/icons/back_icon.jpg')
back_icon.thumbnail((55, 55))
back_icon = ImageTk.PhotoImage(back_icon)

character_banner_icon = Image.open(f'images/icons/character_banner_icon.png')
character_banner_icon.thumbnail((65,240))
character_banner_icon = ImageTk.PhotoImage(character_banner_icon)


# ==========================Команды для кнопок==================================


def menu_btn_cmd():
    menu_btn.place_forget()

    menu_bg.place(x=0,y=0)
    
    back_btn.place(x=30,y=20)
    
    crystals_lbl.place_forget()
    if '' in haved_characters:
        if haved_characters == ['Хори', '', '']:
            wm4 ['text']=f'Персонажей {len(haved_characters)-2}/{len(echaracters)}'
        else: wm4 ['text']=f'Персонажей {len(haved_characters)-1}/{len(echaracters)}'
    else:
        wm4 ['text']=f'Персонажей {len(haved_characters)}/{len(echaracters)}'
    wm4.place(x=30,y=150)
    tgc_btn.place(x=10,y=660)
    

def back_btn_cmd():
    menu_bg.place_forget()
    
    back_btn.place_forget()
    
    menu_btn.place(x=30,y=20)
    crystals_lbl.place(x=115, y=45)
    wm4.place_forget()
    tgc_btn.place_forget()

def casinoresplace():
    list_lbl.place(x=980,y=87)
    result1.place(x=930,y=112)
    result2.place(x=930,y=132)
    result3.place(x=930,y=152)
    result4.place(x=930,y=172)
    result5.place(x=930,y=192)
    result6.place(x=930,y=212)
    result7.place(x=930,y=232)
    result8.place(x=930,y=252)
    result9.place(x=930,y=272)
    result10.place(x=930,y=292)

def casinoresplacefg():
    list_lbl.place_forget()
    result1.place_forget()
    result2.place_forget()
    result3.place_forget()
    result4.place_forget()
    result5.place_forget()
    result6.place_forget()
    result7.place_forget()
    result8.place_forget()
    result9.place_forget()
    result10.place_forget()

def casino_btn_cmd():
    for v in [homepage_bg, menu_btn,casino_btn,play_btn]:
        v.place_forget()
    back_tm_btn.place(x=30,y=20)
    character_banner_btn.place(x=25, y=95)
    character_ban.place(x=180,y=85)
    character_banner_roll1.place(x=500,y=618)
    character_banner_roll10.place(x=650,y=618)
    character_banner_lbl.place(x=200,y=35)
    crystals_lbl['bg'] = 'white'
    casinoresplace()
    homepage_fg()
    back_btn_cmd()

def back_tm_btn_cmd():
    for v in [back_tm_btn,character_banner_btn,character_ban,character_banner_roll1,character_banner_roll10, character_banner_lbl]:
        v.place_forget()
    menu_btn.place(x=30,y=20)
    casino_btn.place(x=1115,y=20)
    play_btn.place(x=452,y=20)
    homepage_bg.place(x=0,y=0)
    crystals_lbl['bg'] = '#32E8E6'
    crystals_lbl.place(x=115, y=45)
    casinoresplacefg()
    homepage_chplace()

kakaklkaslksalks = [mikasa_image,ioko_image,mitsuri_image,eris_image,silphy_image,roxy_image,rei_image,nami_image,hinata_image,nezuko_image,hori_image,frieren_image,fern_image,yudzuriha_image,makima_image,ai_image,kitagawa_image,rem_image,misato_image,sakura_image,zerotwo_image,emilia_image,toru_image,asuna_image,hutao_image,aska_image,speedwagoon_image,arbus_image,leon_image]

def character_banner_btn_cmd():
    character_ban.place(x=180,y=85)
    character_banner_roll1.place(x=500,y=618)
    character_banner_roll10.place(x=650,y=618)
    character_banner_lbl.place(x=200,y=35)

def weapon_banner_btn_cmd():
    character_banner_roll1.place_forget()
    character_banner_roll10.place_forget()
    character_banner_lbl.place_forget()
    character_ban.place_forget()

def croll():
    ch = 1000 - random.randint(1,1000)
    if 1<ch<=11:
        result = random.choice(my_characters)
    elif 11<ch<61:
        result = random.choice(ep_characters)
    elif ch <= 1:
        result = random.choice(ni_characters)
    else:
        result = random.choice(cm_characters)
    result.add()
    return result

def _4roll1():
    global crystals,result1,result2,result3,result4,result5,result6,result7,result8,result9,result10
    if crystals >= 100:
        result = croll()
        crystals-=100
        crystals_lbl['text'] = f'{crystals}💎'
        result1['text'] = f'Вы получили {result.name}!'
        result1['fg'] = result.c
        result2['text'] = ''
        result3['text'] = ''
        result4['text'] = ''
        result5['text'] = ''
        result6['text'] = ''
        result7['text'] = ''
        result8['text'] = ''
        result9['text'] = ''
        result10['text'] = ''
        for i in echaracters:
            i.gg1['text'] = f'Lvl {i.lvl}, {i.hp}♥️{i.atk}⚔️'

def _4roll10():
    global crystals,result1,result2,result3,result4,result5,result6,result7,result8,result9,result10
    if crystals >= 1000:
        crystals-=1000
        crystals_lbl['text'] = f'{crystals}💎'
        for i in[result1,result2,result3,result4,result5,result6,result7,result8,result9,result10]:
            z = croll()
            i['text'] = f'Вы получили {z.name}!'
            i['fg'] = z.c
        for i in echaracters:
            i.gg1['text'] = f'Lvl {i.lvl}, {i.hp}♥️{i.atk}⚔️'
        

def war():
    global crystals
    your_hp = 0
    for i in echaracters:
        if i.name in active_characters:
            your_hp = your_hp + i.hp
    if random.randint(0,100)>33:
        add_crystals = your_hp*0.001
        wall2 = round(add_crystals)
        add_crystals += random.randint(0,wall2)
        crystals += round(add_crystals)
        crystals_lbl['text'] = f'{crystals}💎 + {round(add_crystals)}💎'
    else:
        crystals_lbl['text'] = f'{crystals}💎 Вы проиграли:)'       
        

# =================================Виджеты=============================================

character_ban = tk.Canvas(window, height=510, width=970)
character_ban.create_image(0,0, image=character_ban_image, anchor='nw')

menu_btn = tk.Button(window, image=menu_icon,
                     command=menu_btn_cmd
                     )
menu_btn.place(x=30,y=20)

casino_btn = tk.Button(window, image=casino_icon,
                       command=casino_btn_cmd
                       )
casino_btn.place(x=1115,y=20)

character_banner_btn = tk.Button(window, image=character_banner_icon,
                                 command=character_banner_btn_cmd
                                 )

play_btn = tk.Button(window, image=play_icon, command = war)
play_btn.place(x=452,y=20)

menu_bg = tk.Canvas(window, height=700, width=234)
menu_bg.create_image(0,0, image=menu_bg_image, anchor='nw')

back_btn = tk.Button(window, image=back_icon,
                     command=back_btn_cmd
                     )

back_tm_btn = tk.Button(window, image=back_icon,
                     command=back_tm_btn_cmd
                     )

tgc_btn = tk.Button(window, image=tg4_image,
                     command=lambda: webbrowser.open_new('https://t.me/+106DUeTYokNjMDA6')
                     )

change_btn = tk.Button(window, text ='Поменять',command=characetrs_repalce)



character_banner_roll1 = tk.Button(window, text='Крутить 1 раз\nЦена: 100💎',
                                   bg='grey',
                                   fg='white',
                                   padx=5,
                                   justify='center',
                                   font=('Arial'),
                                   command=_4roll1
                                   )

character_banner_roll10 = tk.Button(window, text='Крутить 10 раз\nЦена: 1000💎',
                                   bg='pink',
                                   padx=5,
                                   justify='center',
                                   font=('Arial'),
                                   command=_4roll10
                                   )



crystals_lbl = tk.Label(window, text=f'{crystals}💎',
                        font=('Arial'),
                        background= '#32e8e6'
                        )
crystals_lbl.place(x=115, y=45)

autor_lbl = tk.Label(window, text=f'created by xealmi',
                        font=('Arial'),
                        background= '#28b834', fg ='#0fa01b'
                        )

character_banner_lbl = tk.Label(window, text=f'Персонажи',
                        font=('Arial', 30),
                        bg = 'white'
                        )

wm4 = tk.Label(window, text=f'Персонажей {len(haved_characters)}/{len(echaracters)}', font=('Arial', 15),bg='grey')

list_lbl = tk.Label(window, text='Вы получили:',bg = 'white', font=('Arial', 13))
result1 = tk.Label(window, text='',bg = 'white', font=('Arial', 10))
result2 = tk.Label(window, text='',bg = 'white', font=('Arial', 10))
result3 = tk.Label(window, text='',bg = 'white', font=('Arial', 10))
result4 = tk.Label(window, text='',bg = 'white', font=('Arial', 10))
result5 = tk.Label(window, text='',bg = 'white', font=('Arial', 10))
result6 = tk.Label(window, text='',bg = 'white', font=('Arial', 10))
result7 = tk.Label(window, text='',bg = 'white', font=('Arial', 10))
result8 = tk.Label(window, text='',bg = 'white', font=('Arial', 10))
result9 = tk.Label(window, text='',bg = 'white', font=('Arial', 10))
result10 = tk.Label(window, text='',bg = 'white', font=('Arial', 10))

homepage_chplace()
# fern.lplace(135,10)
# mikasa.lplace(413,10)
# ==================================мейнлуууп==================================================
def on_closing():
    if messagebox.askokcancel("Close(типо санта close)", "Ты хочешь выйти(за меня)?"):
        resave_list = {
            "crystals" : crystals, 
            "active_characters" : active_characters, 
            "haved_characters" : haved_characters , 
            "mikasa_lvl": mikasa.lvl, 
            "ioko_lvl": ioko.lvl, 
            "mitsuri_lvl": mitsuri.lvl, 
            "eris_lvl": eris.lvl, 
            "silphy_lvl": silphy.lvl, 
            "roxy_lvl": roxy.lvl, 
            "rei_lvl": rei.lvl, 
            "nami_lvl": nami.lvl, 
            "hinata_lvl": hinata.lvl, 
            "nezuko_lvl": nezuko.lvl, 
            "hori_lvl": hori.lvl,
            "frieren_lvl": frieren.lvl, 
            "fern_lvl": fern.lvl, 
            "yudzuriha_lvl": yudzuriha.lvl, 
            "makima_lvl": makima.lvl, 
            "ai_lvl": ai.lvl, 
            "kitagawa_lvl": kitagawa.lvl, 
            "rem_lvl": rem.lvl, 
            "misato_lvl": misato.lvl, 
            "sakura_lvl": sakura.lvl, 
            "zerotwo_lvl": zerotwo.lvl, 
            "emilia_lvl": emilia.lvl,
            "toru_lvl": toru.lvl,
            "asuna_lvl": asuna.lvl, 
            "hutao_lvl": hutao.lvl,
            "aska_lvl": aska.lvl,
            "speedwagoon_lvl": speedwagoon.lvl, 
            "arbus_lvl": arbus.lvl, 
            "leon_lvl": leon.lvl
            }
        with open('save.json', 'w') as save_fl:
            json.dump(resave_list, save_fl, indent=4)
        window.destroy()
window.protocol("WM_DELETE_WINDOW", on_closing)

window.mainloop()