xml_file= "C:\\Machine Learning\\PyPractice\\sample.xml"

import employee
import xml.etree.ElementTree as ET
employees = []
for event, node in ET.iterparse(xml_file):
    if event.title() == 'End' and node.tag == "EMPLOYEE":
        emp = str(ET.tostring(node))
        employees.append(employee.EmployeeType(emp))
'''
import pyxb.binding.saxer
import io

saxer = pyxb.binding.saxer.make_parser()
print(saxer)
handler = saxer.getContentHandler()
print(handler)
xmlt = open(xml_file, "r").read()
saxer.parse(io.StringIO(xmlt))
print(saxer)
print(handler)
print(1)
instance = handler.rootObject()'''
#x = employee.CreateFromDocument(xml_file)
#print(x)


    
