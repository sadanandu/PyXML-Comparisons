from __future__ import unicode_literals

import employee, employeedb
import xml.etree.ElementTree as ET
import xml.sax.expatreader
import time
import os
import pyxb.binding.saxer
from pyxb.utils import saxutils
import sqlite3


xml_file= "C:\\Machine Learning\\PyPractice\\e1.xml"

def parse_xml_to_get_employee_objets():
    employees = []
    print("FileSize" + str(os.stat(xml_file).st_size))
    print("StartTime" + str(time.time()))
    for event, node in ET.iterparse(xml_file):
        if event.title() == 'End' and node.tag == "EMPLOYEE":
            emp = ET.tostring(node) #This returns a byte string
            #Decoding bytes stream before sending it for parsing using pyxb module
            #CreateFromDocument() will create a binding for any XML fragment that is a top-level element in the schema.
            #Hence changed the schema to have EMPLOYEE as top
            #level schema in another file and used employee module to parse individual 
            #employee tags.
            employees.append(employee.CreateFromDocument(emp.decode('UTF-8'))) 
    print("EndTime" + str(time.time()))
    print(employees)
    return employees

def get_connection():
    return sqlite3.connect("employee.db")

def create_database(conn):
    query = "CREATE TABLE EMPLOYEE (emp_id INTEGER, salary INTEGER, dept_id INTEGER)"
    execute_query(conn ,query)
    
def execute_query(conn, query):
    cursor = conn.cursor()
    cursor.execute(query)
    conn.commit()

def get_records_generator(records):
    for record in records:
        yield (record.EMPID, record.SALARY, record.DEPT_ID)

def insert_records_into_db(records):
    conn = get_connection()
    insert_query = "INSERT INTO EMPLOYEE values(?, ?, ?)"
    cursor =conn.cursor()
    cursor.executemany(insert_query, get_records_generator(records))
    conn.commit()

'''
conn = get_connection()
create_database(conn)
insert_records_into_db(records)'''
try:
    employees = parse_xml_to_get_employee_objets()
except Exception as e:
    print(e)

'''Below code will parse the whole document
print("Now from document")
xmlt = open(xml_file, "r").read()
print(type(xmlt))
print(xmlt)
x = employee.CreateFromDocument(xmlt)
print(x)'''

    
