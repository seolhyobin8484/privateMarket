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


