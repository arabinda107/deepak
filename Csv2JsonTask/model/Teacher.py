from model.Personnel import Personnel
class Teacher(Personnel):
    def __init__(self,id,fullName,gender,dob,age,adhar,city,contactNumber,empNo,classTeacher,doj,servicePeriod,previousSchool,post,salary,subjectTeaches):
        
        super().__init__(id,fullName,gender,dob,age,adhar,city,contactNumber)

        self.empNo=empNo
        self.classTeacher=classTeacher
        self.doj=doj
        self.servicePeriod=servicePeriod
        self.previousSchool=previousSchool
        self.post=post
        self.salary=salary
        self.subjectTeaches=subjectTeaches
        