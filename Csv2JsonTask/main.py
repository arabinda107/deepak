import csv
import os
import os.path
from datetime import date
from datetime import datetime
from model.Personnel import Personnel
from model.Student import Student
from model.Teacher import Teacher
from model.PersonnelRecords import StudentRecords,TecherRecords
from  model.MyJsonEncoder import MyEncoder


def getFullname(firstname,lastname):
    fullname=firstname+" "+lastname
    return fullname
def genderDetect(gender):
    if gender=="m":
        gender='Male'
    else:
        gender='Female'
    return gender
def durationCal(dob):
    my_date = dob
    b_date = datetime.strptime(my_date, '%m/%d/%Y')
    days=(datetime.today()-b_date).days
    years=int(days/365)
    month=int(int(days%365)/30)
    s=str(years)+" Yrs "+str(month)+" Months"
    return s
def gradeCal(m):
    percentage=m*0.1
    
    if percentage>=90:
        grade="A+"
    elif percentage>=80 and percentage<90:
        grade="A"
    elif percentage>=70 and percentage<80:
        grade="B+"
    elif percentage>=60 and percentage<70:
        grade="B"
    elif percentage>=50 and percentage<60:
        grade="C"
    else:
        grade="D"

    return grade
def dateformat():
    today = date.today()
    x=str(today)
    res_str =x.replace('-', '') 
    return res_str

studentRecordCount=0
teacherRecordCount=0
data=[]
data2=[]

with open('/home/arabinda/ARABINDA/FUJISTU/Csv2JsonTask/resource/master-data2.csv','r') as file:
    reader=csv.reader(file)
    for line in reader:
        if line[1]=='student':

            studentRecordCount+=1
            fullname=getFullname(line[2],line[3])
            gen=genderDetect(line[4])
            age=durationCal(line[5])
            grade=gradeCal(int(line[14]))

            student=Student(id=int(line[0]),dob=line[5],age=age,adhar=line[16],city=line[15],contactNumber=line[17],rollNumber=int(line[12]),fullName=fullname,gender=gen,className=line[8],totalMarks=int(line[14]),grade=grade,secPercent=int(line[21]),hsStream=line[20])
            data.append(student)
        else:
            if line[1]=='teacher':
                teacherRecordCount+=1
                servicePeriod=durationCal(line[7])
                fullname=getFullname(line[2],line[3])
                gen=genderDetect(line[4])
                age=durationCal(line[5])
                salary="{:,}".format(int(line[10]))
                teacher=Teacher(id=int(line[0]),dob=line[5],age=age,adhar=line[16],city=line[15],contactNumber=line[17],fullName=fullname,gender=gen,servicePeriod=servicePeriod,empNo=line[13],classTeacher=line[11],doj=line[7],previousSchool=line[6],post=line[9],subjectTeaches=line[19],salary=salary)
                data2.append(teacher)  

studentrecord=StudentRecords(studentRecordCount,data)
x=MyEncoder().encode(studentrecord)
filen=dateformat()
filename="student_record_"+filen+".json" 
path = '/home/arabinda/deepak/'

if not os.path.exists(path):
    os.makedirs(path)
with open(os.path.join(path, filename), 'w') as temp_file:
    temp_file.write(x)



teacherrecord=TecherRecords(teacherRecordCount,data2)
y=MyEncoder().encode(teacherrecord)
filen=dateformat()
filename="teacher_record_"+filen+".json" 
path = '/home/arabinda/deepak/'
if not os.path.exists(path):
    os.makedirs(path)
with open(os.path.join(path, filename), 'w') as temp_file:
    temp_file.write(y)




            








