from model.Personnel import Personnel
class Student(Personnel):
    def __init__(self,id,fullName,gender,dob,age,adhar,city,contactNumber,rollNumber,className,totalMarks,grade,secPercent,hsStream):
        super().__init__(id,fullName,gender,dob,age,adhar,city,contactNumber)

        self.rollNumber=rollNumber
        self.className=className
        self.totalMarks=totalMarks
        self.grade=grade
        self.secPercent=secPercent
        self.hsStream=hsStream
    


