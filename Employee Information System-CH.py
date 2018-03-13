import os;
def search():
     #查询格式: Find name,age from staff_table where age > 22
     print("-----进入查询功能-----")
     data1 = search1.split(" ")
     time = 0
     list=[]
     f = open("Info", mode="r+")
     if search1 == ("Find name,age from staff_table where age > %s" %(data1[7])) or search1 == ("Find name,age from staff_table where age < %s" %(data1[7])) :

        for line in f:
            i = line.split(",")
            set=[i[1],i[2]]

            if data1[6]== ">":
                if i[2] > data1[7]:
                    list.append(set)
                    time+=1

            elif data1[6]== "<":
                if i[2] < data1[7]:
                    list.append(set)
                    time+=1

    #查询格式: Find * from staff_table where enroll_date like "2013"
     elif search1 == ("Find * from staff_table where enroll_date like %s" % (data1[7])):

            year = data1[7].strip('"')
            for line in f:
                i = line.split(",")
                if year==i[5].split("-")[0]:
                    list.append(i)
                    time+=1

    #查询格式: Find * from staff_table where dept = IT
     elif search1 == ("Find * from staff_table where dept = %s" %(data1[7])):

         for line in f:
            i = line.split(",")
            if i[4]==data1[7]:
                list.append(i)
                time+=1

     for t in list:
         t=",".join(t)
         print (t)
     print("共查询到" + str(time) + "条信息")

def add():
    #查询格式：add staff_table Alex Li,25,134435344,IT,2015-10-29
     print("-----进入添加功能-----")
     data1 = search1.split(" ")
     data1[3]=data1[2]+' '+data1[3]
     phone=data1[3].split(",")
     f=open("Info",mode="r+")
     time=0

     for line in f:
         i = line.split(",")
         time+=1
         if phone[2]==i[3]:
            print("该手机号已注册！")
            return 0

     hu=data1[3].split(",")
     hu.insert(0,str(time+1))
     hu = ','.join(hu)
     f.write("\n")
     f.write(hu)
     print("员工信息添加成功！")

def edit():
    # 查询格式：UPDATE staff_table SET dept = "Marketing" WHERE dept = "IT"
     print("-----进入修改功能-----")
     data1 = search1.split(" ")
     f = open("Info", mode="r+")
     f1 = open("New", mode="w")
     time = 0

     if search1==("UPDATE staff_table SET dept = "+data1[5]+" WHERE dept = "+data1[9]):


         for line in f:
             i=line.split(",")

             if data1[5].strip('"') == i[4]:
                  time+=1
                  i[4]=data1[9].strip('"')

             i = ','.join(i)
             f1.write(i)
             f1.flush()

     # 查询格式：UPDATE staff_table SET age = 25 WHERE name = "Alex Li"
     elif search1 == ("UPDATE staff_table SET age = " + data1[5] + " WHERE name = " + data1[9]+" "+data1[10]):
          data1[9] = data1[9] + " " + data1[10]

          for line in f:
              i=line.split(",")

              if data1[9].strip('"')==i[1] and i[2]!=data1[5]:
                  time+=1
                  i[2]=data1[5]

              i = ','.join(i)
              f1.write(i)
              f1.flush()

     if time != 0:
          print("修改成功！")
          print("已修改%s条数据" % (time))

     else:
          print("未查询到相关信息")

     os.remove("Info")
     os.rename("New", "Info")
     f1.close()

def delete():
    #查询格式：delfrom staff where id = 3
     data1 = search1.split(" ")
     print("-----进入删除功能-----")

     if search1==("delfrom staff where id = "+data1[5]):
         f=open("Info",mode="r+")
         f1=open("New",mode="w")
         time=0

         for line in f:
             i=line.split(",")
             if i[0]==data1[5]:
                 time+=1
                 i=""
             i = ','.join(i)
             f1.write(i)
             f1.flush()

         if time != 0:
             print("删除成功！")
             print("已删除%s条数据" % (time))

         else:
             print("未查询到相关信息")

         os.remove("Info")
         os.rename("New", "Info")
         f1.close()

menu="""
     1：查询
     2：添加
     3：删除
     4：修改
     5：退出
"""

selection={
     "1":search,
     "2":add,
     "3":delete,
     "4":edit
}

while True:
      print(menu)
      choice=input("请输入序号:")

      if choice=="5":
           print("成功退出程序！")
           break

      elif selection.get(choice):
           search1 = input("请输入内容：")
           selection.get(choice)()
