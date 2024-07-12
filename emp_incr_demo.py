eid=int(input("Enter Employ id "))
ename=(input("Enter Employ name"))
esal=int(input("Enter Employ Sallary"))
deptno=int(input("Enter Department no"))
comm=int(input("Enter a comm"))

if esal>15000 and deptno==1 and comm!=0:
    esal=esal+5000
    print(eid, ":::",ename, "  ",esal,"  ",deptno)
else:
    print("the person is then not eligible for increment")





