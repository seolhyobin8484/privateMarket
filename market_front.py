import tkinter.ttk
from tkinter import *
import market_back
from tkinter import messagebox

#메인 화면
window = Tk()
image = PhotoImage(file='image_or_png\\images.png')
window.title('효빈 마켓')
market_title = Label(window,image=image, text='효빈 마트', font=('궁서체', 30),compound="center")

market_title.pack()

#관리자인지 유저인지 판별
def login_check_info():
    try:
        id_E.bind("<Return>")
        pw_E.bind("<Return>")
        if market_back.login(id_E.get(),pw_E.get())[0] == 'admin':
            messagebox.showinfo("안내",f"반갑습니다. {market_back.login(id_E.get(),pw_E.get())[1]}님.")
            admin_menu()
        elif market_back.login(id_E.get(),pw_E.get())[0] == 'user':
            messagebox.showinfo("안내", f"반갑습니다. {market_back.login(id_E.get(), pw_E.get())[1]}님.")
            user_menu()
    except IndexError:
        messagebox.showinfo("오류",f"아이디나 패스워드를 다시 확인해주세요.")
        id_E.bind("<Return>")
        pw_E.bind("<Return>")

def admin_radio_btn(): #Var의 값에 따라 reset_add에 매개변수 담아서 호출
    if ad_var.get() == 1:
        reset_add(1)
    if ad_var.get() == 2:
        reset_add(2)

def reset_add(ad_var): #버튼을 눌렀을때 기존에 생성된 창을 지우고 값에 맞는 창을 보여줌.
    
    if ad_var == 1:
        sell_viewer.pack_forget()

        item_name_L.pack(padx=4, pady=3)
        item_name_insert.pack(padx=5, pady=3)
        sell_price_L.pack(padx=4, pady=3)
        sell_price_insert.pack(padx=5, pady=3)
        buying_price_L.pack(padx=4, pady=3)
        buying_price_insert.pack(padx=5, pady=3)
        insert_item_Btn.pack(padx=4, pady=3)


    if ad_var == 2:
        item_name_L.pack_forget()
        item_name_insert.pack_forget()
        sell_price_L.pack_forget()
        sell_price_insert.pack_forget()
        buying_price_L.pack_forget()
        buying_price_insert.pack_forget()
        insert_item_Btn.pack_forget()

        sell_viewer.pack()

def admin_menu(): #관리자 창


    global item_name_insert, sell_price_insert, buying_price_insert, buying_price, admin_screen, item_name_L, sell_price_L, buying_price_L,insert_item_Btn,sell_viewer
    admin_screen = Toplevel()
    admin_screen.geometry('500x500')
    admin_screen.title("관리자 페이지")

    # 상품추가
    item_name_insert = Entry(admin_screen)
    sell_price_insert = Entry(admin_screen)
    buying_price_insert = Entry(admin_screen)

    item_name_L = Label(admin_screen,text="상품명")
    sell_price_L = Label(admin_screen,text="판매가")
    buying_price_L = Label(admin_screen,text="구매가")

    insert_item_Btn = Button(admin_screen, text="추가",
                             command=lambda: market_back.insert_item(item_name_insert.get(), sell_price_insert.get(),
                                                                   buying_price_insert.get()))

    #판매내역
    sell_viewer = tkinter.ttk.Treeview(admin_screen,columns=["#1","#2","#3"])
    sell_viewer["show"] = "headings"
    sell_viewer.column("#1",width=70)
    sell_viewer.heading("#1",text="판매번호")
    sell_viewer.column("#2",width=150)
    sell_viewer.heading("#2",text="판매날짜",anchor=CENTER)
    sell_viewer.column("#3",width=70)
    sell_viewer.heading("#3", text="고객명", anchor=CENTER)

    sell_list_data = market_back.look_sell_list()

    for i in sell_list_data:
        sell_viewer.insert('', 'end', values=(i[0], i[1], i[2]))

    #관리자 화면 버튼
    global ad_var
    ad_var = IntVar()
    insert_item_RdBtn = Radiobutton(admin_screen,text="상품추가",variable=ad_var,value=1,command=admin_radio_btn)
    select_sell_RdBtn = Radiobutton(admin_screen,text="판매내역확인",variable=ad_var,value=2, command=admin_radio_btn)

    insert_item_RdBtn.pack()
    select_sell_RdBtn.pack()


def buying_item(): #판매번호와 갯수담아서 buying 호출
    market_back.buying(int(item_name_list.curselection()[0]),item_ea_E.get())

def update_userinfo(): # 회원가입시 sql로 처리하는 함수로 매개변수를 담아 호출
        market_back.update_user(user_id_E.get(),user_pwd_E.get(),user_loc_E.get(),user_mail_E.get()
                                ,user_phone_E.get(),user_cellphone_E.get(),user_sex_E.get())
def user_radio_btn(): # Var의 값에 따라 reset_add에 매개변수 담아서 호출
    if user_var.get() == 1:
        reset_user(1)
    if user_var.get() == 2:
        reset_user(2)


def reset_user(user_var): #버튼을 눌렀을때 기존에 생성된 창을 지우고 값에 맞는 창을 보여줌.
    if user_var == 1:
        user_id_L.pack_forget(), user_id_E.pack_forget()
        user_pwd_L.pack_forget(), user_pwd_E.pack_forget()
        user_loc_L.pack_forget(), user_loc_E.pack_forget()
        user_mail_L.pack_forget(), user_mail_E.pack_forget()
        user_phone_L.pack_forget(), user_phone_E.pack_forget()
        user_cellphone_L.pack_forget(), user_cellphone_E.pack_forget()
        user_sex_L.pack_forget(), user_sex_E.pack_forget()
        update_Btn.pack_forget()

        item_name_list.pack()
        item_ea_L.pack(),item_ea_E.pack()
        buy_Btn.pack()

    if user_var == 2:
        item_name_list.pack_forget()
        buy_Btn.pack_forget()
        item_ea_L.pack_forget(),item_ea_E.pack_forget()
        update_Btn.pack_forget()

        user_id_L.pack(),user_id_E.pack()
        user_pwd_L.pack(),user_pwd_E.pack()
        user_loc_L.pack(),user_loc_E.pack()
        user_mail_L.pack(),user_mail_E.pack()
        user_phone_L.pack(),user_phone_E.pack()
        user_cellphone_L.pack(),user_cellphone_E.pack()
        user_sex_L.pack(),user_sex_E.pack()
        update_Btn.pack()
def user_menu(): #사용자 창
    global user_screen, var_user, buying_RdBtn, update_userinfo_RdBtn, item_name_list, user_var, buy_Btn, item_ea_E, item_ea_L
    user_screen = Toplevel()
    user_screen.geometry('500x500')
    user_screen.title("사용자 페이지")

    item_name_list = Listbox(user_screen, height=0, selectmode="browse")
    for i in range(len(market_back.item_name_list())):
        item_name_list.insert(i, market_back.item_name_list()[i])
    item_ea_E = Entry(user_screen)
    item_ea_L = Label(user_screen, text="수량")
    buy_Btn = Button(user_screen, text="구매", command=buying_item)


    #개인정보수정
    global user_id_E,user_pwd_E,user_loc_E,user_mail_E,user_phone_E,user_cellphone_E,\
    user_sex_E,user_id_L,user_pwd_L,user_loc_L,user_mail_L,user_phone_L,user_cellphone_L,\
    user_sex_L,update_Btn
    user_id_E = Entry(user_screen)
    user_pwd_E = Entry(user_screen)
    user_loc_E = Entry(user_screen)
    user_mail_E = Entry(user_screen)
    user_phone_E = Entry(user_screen)
    user_cellphone_E = Entry(user_screen)
    user_sex_E = Entry(user_screen)

    user_id_L = Label(user_screen, text="아이디(이름)")
    user_pwd_L = Label(user_screen, text="비밀번호")
    user_loc_L = Label(user_screen, text="주소")
    user_mail_L = Label(user_screen, text="우편번호")
    user_phone_L = Label(user_screen, text="전화번호")
    user_cellphone_L = Label(user_screen, text="휴대폰번호")
    user_sex_L = Label(user_screen, text="성별")
    update_Btn = Button(user_screen, text="변경", command=update_userinfo)


    #유저 메인화면
    user_var = IntVar()
    buying_RdBtn = Radiobutton(user_screen, text="구매", variable=user_var, value=1, command=user_radio_btn)
    update_userinfo_RdBtn = Radiobutton(user_screen, text="회원정보수정", variable=user_var, value=2, command=user_radio_btn)


    buying_RdBtn.pack()
    update_userinfo_RdBtn.pack()
def join_checking(): #회원가입시 필수 입력해야하는 값 (DB에서 id,pass는 NN으로 설정되어있다.)
    if id_E.get() == "" or pwd_E.get() =="":
        messagebox.showinfo("오류","*은 필수 입력란입니다.")
    else:
        market_back.join_membership(id_E.get(),pwd_E.get(),loc_E.get(),mail_E.get(),phone_E.get(),cellphone_E.get(),sex_E.get(),admin_chk_E.get())

def join_player(): #회원가입
    global id_E, pwd_E, loc_E, mail_E, phone_E, cellphone_E,sex_E,admin_chk_E
    join_screen = Toplevel()
    join_screen.geometry('500x500')
    id_L = Label(join_screen,text="*아이디(이름)")
    id_E = Entry(join_screen)
    pwd_L = Label(join_screen,text="*비밀번호")
    pwd_E = Entry(join_screen)
    loc_L = Label(join_screen,text="지역")
    loc_E = Entry(join_screen)
    mail_L = Label(join_screen, text="우편번호")
    mail_E = Entry(join_screen)
    phone_L = Label(join_screen, text="전화번호")
    phone_E = Entry(join_screen)
    cellphone_L = Label(join_screen, text="휴대폰번호")
    cellphone_E = Entry(join_screen)
    sex_L = Label(join_screen, text="성별")
    sex_E = Entry(join_screen)
    admin_chk_L = Label(join_screen, text="관리자 비밀번호")
    admin_chk_E = Entry(join_screen)
    join = Button(join_screen,text="가입", command=join_checking)

    id_L.pack(),id_E.pack()
    pwd_L.pack(),pwd_E.pack()
    loc_L.pack(),loc_E.pack()
    mail_L.pack(),mail_E.pack()
    phone_L.pack(),phone_E.pack()
    cellphone_L.pack(),cellphone_E.pack()
    sex_L.pack(),sex_E.pack()
    admin_chk_L.pack(),admin_chk_E.pack()
    join.pack()

#첫 메인화면 버튼 및 엔트리
id_E = Entry(window)
pw_E = Entry(window)
login_Btn = Button(text="로그인", command=login_check_info)
join_Btn = Button(text="회원가입", command=join_player)

id_E.pack()
pw_E.pack()
login_Btn.pack()
join_Btn.pack()

window.mainloop()