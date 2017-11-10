import xml.dom.minidom as dm
import random
f = "C:\\Machine Learning\\PyPractice\\sample.xml"

implementation = dm.getDOMImplementation()
doc = implementation.createDocument(None, 'EmployeeDb', None)
root = doc.documentElement
#root.appendChild(doc.createTextNode('I am root cause'))
with open(f, 'w+') as fh:
    fh.write("<EMPLOYEEDB>")
    for each in range(500000):
        employee = doc.createElement('EMPLOYEE')
        #root.appendChild(employee)
        emp_id = doc.createElement('EMP_ID')
        emp_id.appendChild(doc.createTextNode(str(random.randint(1, 100))))
        employee.appendChild(emp_id)
        salary = doc.createElement('SALARY')
        salary.appendChild(doc.createTextNode(str(random.randint(1000, 10000))))
        employee.appendChild(salary)
        dept_num = doc.createElement('DEPT_NO')
        dept_num.appendChild(doc.createTextNode(str(random.randint(1, 5))))
        employee.appendChild(dept_num)
    #print(root.toxml())
        fh.write(employee.toxml())
    fh.write("</EMPLOYEEDB>")


