# 효빈마켓
교육 과제로 한 개인마켓프로그램  

## 메인화면
![image](https://github.com/user-attachments/assets/8e790771-b7f1-46cf-a241-92656c9fb12d) 


### 회원가입 버튼을 눌렀을 경우. 처리되는 화면. (아이디, 비밀번호는 필수입력)<hr>
![image](https://github.com/user-attachments/assets/334d5d2a-f1d3-4432-a587-3fbc51bba42d)
![image](https://github.com/user-attachments/assets/36caca92-66a7-4232-950c-d727611613c5)
![image](https://github.com/user-attachments/assets/4ec3e1f4-f6b7-40c1-8bd3-76049eacad4b)

### 로그인 (비밀번호 틀렸을 경우 포함)<hr>
![image](https://github.com/user-attachments/assets/fa8ddc71-5f07-4dd6-a60d-a99871548307)
![image](https://github.com/user-attachments/assets/12747515-572c-4dd3-b664-2858e9f9657f)

## 사용자

### 사용자로 로그인시 보여지는 사용자 페이지
![image](https://github.com/user-attachments/assets/a1b7e234-a4da-4413-b17f-4ddb8760d202)


###### 구매 : 구매할 상품명을 Listbox에서 선택하고 수량을 정하여 버튼을 누르는 방식
![image](https://github.com/user-attachments/assets/93694a23-9977-4f38-a53e-8d17e0e64eb8)

###### 물품 구매
![image](https://github.com/user-attachments/assets/d8822677-a43e-4bf8-9faa-728f4a081ca8)

###### 회원정보수정 : 각 정보 중에서 바꾸고싶은 값만 바꾸는 방식 (바꾸지 않으면 해당 값은 기존 값 유지)
![image](https://github.com/user-attachments/assets/ebb594d7-1446-42d7-a22c-8e94262202aa)

###### 회원정보 변경
![image](https://github.com/user-attachments/assets/0c0c2267-e0f1-4344-b2c8-981336230ff6)

## 관리자

### 관리자계정을 만들기 위해 회원가입을 시도하여 그 중, 관리자 비밀번호를 입력
#### (설정된 관리자 비번 : tjfgyqls)<hr>
![image](https://github.com/user-attachments/assets/7fb4bb21-008e-459e-b0ab-98bb781b6792)

##### 방금 만든 관리자계정으로 로그인
![image](https://github.com/user-attachments/assets/e9df4002-65a1-478e-a92f-5e0e53ce2ab3)

### 관리자 페이지로 로그인시 보여지는 관리자 페이지<hr>
###### 관리자는 마켓에 상품을 추가할 수 있다. Entry의 값을 버튼으로 날려보내서 처리하는 과정.
![image](https://github.com/user-attachments/assets/b28432f0-1494-4e8d-ae13-964ed4b938dd)

###### 상품추가
![image](https://github.com/user-attachments/assets/e6f24bd7-bbce-4d82-b8a0-414837c689d8)

###### 판매내역을 확인하여 누가 구매를 했고, 그 시간대를 확인.
![image](https://github.com/user-attachments/assets/33c7b5a2-2252-425b-acd9-ac693cbdb811)

##### 방금 설효빈계정으로 물건을 산 기록 또한 기재
![image](https://github.com/user-attachments/assets/76204bf1-bc20-4da0-b1c2-62a9da023afd)





## market_front.py 

 ```
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
```

## market_back.py

```
import pymysql
import datetime as dt
from tkinter import messagebox
def connect_db(): #pymysql 사용해서 DB연결
    global connect , cursor
    connect = pymysql.connect(host='localhost',
                              user='root',
                              passwd='1234',
                              db='상품판매db',
                              charset='utf8');

    cursor = connect.cursor()

def close_db(): #DB 종료
    connect.commit()
    connect.close()
def insert_item(item_name, sell_price, buy_price): #상품 추가
    connect_db()
    sql = f'INSERT INTO 상품 (상품명,판매가,구매가) VALUES ("{item_name}","{sell_price}","{buy_price}");'

    try:
        cursor.execute(sql)
        messagebox.showinfo("상품 추가 도우미", "상품이 추가되었습니다.")

    except Exception as e:
        print(e)
        messagebox.showinfo("상품 추가 도우미","올바른 값을 입력하세요.")

    finally:
        close_db()


def look_sell_list(): #관리자가 확인 할 판매내역
    connect_db()
    sql = f'SELECT p.판매번호 , p.판매날짜 , g.id FROM 고객 g , 판매 p WHERE g.고객번호 = p.고객번호;'
    cursor.execute(sql)
    result = cursor.fetchall()
    result = list(result)

    return result

def login(id , pwd): #로그인 처리와 동시에 사용자 및 관리자 정보를 따로 담아냄.
    connect_db()

    sql = f'select * from 고객 where id = "{id}" and pass = "{pwd}";'

    cursor.execute(sql)
    res = cursor.fetchall()
    global user_num,user_id,user_pass,user_loc,user_mail,user_phone,user_cellphone,user_sex
    user_num = res[0][0]
    user_id = res[0][1]
    user_pass = res[0][2]
    user_loc = res[0][3]
    user_mail = res[0][4]
    user_phone = res[0][5]
    user_cellphone = res[0][6]
    user_sex = res[0][7]
    usertype = res[0][8]

    if usertype == '관리자':
        print("관리자로 로그인하셨습니다.")
        return 'admin',user_id
    elif usertype == '사용자':
        print("사용자로 로그인하셨습니다.")
        return 'user',user_id
    close_db()

def join_membership(id,pwd,loc,mail,phone,cellphone,sex,admin): #회원가입
    connect_db()
    info =[id,pwd,
           None if  loc =='' else f'{loc}',
           None if  mail == '' else f'{mail}',
           None if  phone == '' else f'{phone}',
           None if  cellphone == '' else f'{cellphone}',
           None if  sex == '' else f'{sex}',
           '관리자' if admin == 'tjfgyqls' else '사용자']

    sql = """INSERT INTO 고객 (id, pass, 주소, 우편번호, 전화번호, 휴대폰번호, 성별, 구분) VALUES (%s, %s, %s,%s, %s, %s,%s, %s)
    """
    cursor.execute(sql,info)
    close_db()
    messagebox.showinfo("안내","회원가입이 완료되었습니다.")
def item_name_list(): #프로그램상 상품번호로 처리하지만, 사용자에겐
    connect_db()
    sql = 'SELECT 상품명 FROM 상품;'
    cursor.execute(sql)
    res = cursor.fetchall()
    name_list = []
    for i in range(len(res)):
        name_list.append(res[i])
    close_db()
    return name_list
def buying(item_num,item_ea): #사용자가 구매하는 것과 동시에 판매이력에 남김. (판매 및 판매상세는 관리자만 확인 가능)
        connect_db()
        selectName_sql = f'SELECT 상품명 FROM 상품 WHERE 상품번호 = "{item_num}";'
        cursor.execute(selectName_sql)
        item_name = cursor.fetchall()[0][0]

        y = dt.datetime.now().year
        m = dt.datetime.now().month
        d = dt.datetime.now().day

        sell_sql = f'INSERT INTO 판매 (판매날짜,고객번호) VALUES ("{dt.date(y,m,d)}",{user_num})'
        cursor.execute(sell_sql)

        selectSell_sql = f'SELECT * FROM 판매;'
        cursor.execute(selectSell_sql)
        res = cursor.fetchall()
        sell_num_now = res[-1][0]

        insterSellinfo_sql = f'INSERT INTO 판매상세 (판매번호,상품번호,수량) VALUES ("{sell_num_now}","{item_num}","{item_ea}")'
        cursor.execute(insterSellinfo_sql)

        messagebox.showinfo("안내", "정상적으로 구매되었습니다!")
        close_db()

def update_user(new_id,new_pwd,new_loc,new_mail,new_phone,new_cellphone,new_sex): #사용자가 개인정보를 바꿀때
    connect_db()

    update_sql = 'UPDATE 고객 SET '
    id_sql = f'id = "{new_id}"'
    pwd_sql = f'pass = "{new_pwd}"'
    loc_sql=f'주소="{new_loc}"'
    mail_sql=f'우편번호="{new_mail}"'
    phone_sql=f'전화번호="{new_phone}"'
    cellphone_sql = f'휴대폰번호="{new_cellphone}"'
    sex_sql = f'성별="{new_sex}"'
    where_sql = f' WHERE 고객번호 = "{user_num}";'
    option =""

    if not new_id == "":
        option = id_sql
    if not new_pwd == "":
        if option == "":
            option = pwd_sql
        else:
            option = option + ',' + pwd_sql
    if not new_loc == "":
        if option == "":
            option = loc_sql
        else:
            option = option +',' + loc_sql
    if not new_mail == "":
        if option == "":
            option = mail_sql
        else:
            option = option +',' + mail_sql
    if not new_phone == "":
        if option == "":
            option = phone_sql
        else:
            option = option +',' + phone_sql
    if not new_cellphone == "":
        if option == "":
            option = cellphone_sql
        else:
            option = option +',' + cellphone_sql
    if not new_sex == "":
        if option == "":
            option = sex_sql
        else:
            option = option +',' + sex_sql

    sql = update_sql+option+where_sql
    cursor.execute(sql)
    messagebox.showinfo("안내", "회원정보가 변경되었습니다.")
    close_db()
```


