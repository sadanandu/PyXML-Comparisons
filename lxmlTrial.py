import lxml.etree as ET

#Creating an xml from scratch
root = ET.Element('root')
root.text = 'I am root cause'
root.tail = 'I am the tail'
one = ET.SubElement(root, 'one', font='large')
one.text = 'I am the one'
two = ET.SubElement(root, 'two', wrap='word')
box = ET.SubElement(root, 'buttonbox')
ET.SubElement(box, 'button').text = 'ok'
ET.SubElement(box, 'button').text = 'cancel'
#print root.getchildren()
#print ET.tostring(root)

#element acts as python list
##one = root[0]
##print one
##print len(root)
##if len(root):  #to check if element has children
##    print 'Has children'

#copying element from one tree to other will delink the element from first tree
##root1 = ET.Element('root1')
##print len(root)
###here one was appended to root previously
##root1.append(one)
##print len(root)

#Tree iteration useful for recursively traversing a tree/xml
##for node in root.iter():
##    print ET.tostring(node)

#parsing xml data

xmlString = '''
<MESSAGE>
  <SWIFT ID= 'first'><BLOCK_TRADE>N</BLOCK_TRADE>
  <BUY_AMOUNT>300.0</BUY_AMOUNT>
  <BUY_CURRENCY>EUR</BUY_CURRENCY>
  <BUY_DELIVERY_AGENT_OPTION>A</BUY_DELIVERY_AGENT_OPTION>
  <BUY_DELIVERY_AGENT_ACCOUNT>12345</BUY_DELIVERY_AGENT_ACCOUNT>
  <BUY_DELIVERY_AGENT_BIC>ABCDEF10</BUY_DELIVERY_AGENT_BIC>
  <BUY_DELIVERY_AGENT_NAME>LC CP CB</BUY_DELIVERY_AGENT_NAME>
  <BUY_DELIVERY_AGENT_ADDRESS>Pune  </BUY_DELIVERY_AGENT_ADDRESS>
  <BUY_INTERMEDIARY_OPTION>A</BUY_INTERMEDIARY_OPTION>
  <BUY_INTERMEDIARY_ACCOUNT>22223</BUY_INTERMEDIARY_ACCOUNT>
  <BUY_INTERMEDIARY_BIC>ABCDEF16</BUY_INTERMEDIARY_BIC>
  <BLOCK_TRADE>Y</BLOCK_TRADE>
  <BUY_INTERMEDIARY_NAME>LC Acquirer Intermediary1</BUY_INTERMEDIARY_NAME>
  <BUY_INTERMEDIARY_ADDRESS>Pune  </BUY_INTERMEDIARY_ADDRESS>
  <BUY_RECEIVING_AGENT_OPTION>A</BUY_RECEIVING_AGENT_OPTION>
  <BUY_RECEIVING_AGENT_ACCOUNT>22222</BUY_RECEIVING_AGENT_ACCOUNT>
  <BUY_RECEIVING_AGENT_BIC>ABCDEF11</BUY_RECEIVING_AGENT_BIC>
  <BUY_RECEIVING_AGENT_NAME>LC Acquirer CB</BUY_RECEIVING_AGENT_NAME>
  <BUY_RECEIVING_AGENT_ADDRESS>Pune  </BUY_RECEIVING_AGENT_ADDRESS>
  <CODEWORD_NEWLINE>codeword</CODEWORD_NEWLINE>
  <COUNTERPARTYS_REFERENCE/>
  <EXCHANGE_RATE>1.3</EXCHANGE_RATE>
  <BLOCK_TRADE>YN</BLOCK_TRADE>
  <NARRATIVE_SEPARATOR>newline</NARRATIVE_SEPARATOR>
  <NETWORK>SWIFT</NETWORK>
  <PARTY_A_OPTION>A</PARTY_A_OPTION>
  <PARTY_A_ACCOUNT>11111</PARTY_A_ACCOUNT>
  <PARTY_A_BIC>ABCDEF13</PARTY_A_BIC>
  <PARTY_A_NAME>LC Acquirer</PARTY_A_NAME>
  <PARTY_A_ADDRESS>Pune Pune India</PARTY_A_ADDRESS>
  <PARTY_B_OPTION>A</PARTY_B_OPTION>
  <PARTY_B_ACCOUNT>22222</PARTY_B_ACCOUNT>
  <PARTY_B_BIC>ABCDEF12</PARTY_B_BIC>
  <PARTY_B_NAME>LC CP</PARTY_B_NAME>
  <PARTY_B_ADDRESS>Pune Pune India</PARTY_B_ADDRESS>
  <RECEIVER_BIC>ABCDEF12</RECEIVER_BIC>
  <SCOPE_OF_OPERATION>BILA</SCOPE_OF_OPERATION>
  <SELL_AMOUNT>390.0</SELL_AMOUNT>
  <SELL_BENEFICIARY_INSTITUTION_OPTION>A</SELL_BENEFICIARY_INSTITUTION_OPTION>
  <SELL_BENEFICIARY_INSTITUTION_ACCOUNT>22222</SELL_BENEFICIARY_INSTITUTION_ACCOUNT>
  <SELL_BENEFICIARY_INSTITUTION_BIC>ABCDEF12</SELL_BENEFICIARY_INSTITUTION_BIC>
  <SELL_BENEFICIARY_INSTITUTION_NAME>LC CP</SELL_BENEFICIARY_INSTITUTION_NAME>
  <SELL_BENEFICIARY_INSTITUTION_ADDRESS>Pune Pune India</SELL_BENEFICIARY_INSTITUTION_ADDRESS>
  <SELL_CURRENCY>USD</SELL_CURRENCY>
  <SELL_DELIVERY_AGENT_OPTION>A</SELL_DELIVERY_AGENT_OPTION>
  <SELL_DELIVERY_AGENT_ACCOUNT>11111</SELL_DELIVERY_AGENT_ACCOUNT>
  <SELL_DELIVERY_AGENT_BIC>ABCDEF11</SELL_DELIVERY_AGENT_BIC>
  <SELL_DELIVERY_AGENT_NAME>LC Acquirer CB</SELL_DELIVERY_AGENT_NAME>
  <SELL_DELIVERY_AGENT_ADDRESS>Pune  </SELL_DELIVERY_AGENT_ADDRESS>
  <SELL_INTERMEDIARY_OPTION>A</SELL_INTERMEDIARY_OPTION>
  <SELL_INTERMEDIARY_ACCOUNT>22223</SELL_INTERMEDIARY_ACCOUNT>
  <SELL_INTERMEDIARY_BIC>ABCDEF15</SELL_INTERMEDIARY_BIC>
  <SELL_INTERMEDIARY_NAME>LC CP Intermediary1</SELL_INTERMEDIARY_NAME>
  <SELL_INTERMEDIARY_ADDRESS>Pune  </SELL_INTERMEDIARY_ADDRESS>
  <SELL_RECEIVING_AGENT_OPTION>A</SELL_RECEIVING_AGENT_OPTION>
  <SELL_RECEIVING_AGENT_ACCOUNT>22222</SELL_RECEIVING_AGENT_ACCOUNT>
  <SELL_RECEIVING_AGENT_BIC>ABCDEF10</SELL_RECEIVING_AGENT_BIC>
  <SELL_RECEIVING_AGENT_NAME>LC CP CB</SELL_RECEIVING_AGENT_NAME>
  <SELL_RECEIVING_AGENT_ADDRESS>Pune  </SELL_RECEIVING_AGENT_ADDRESS>
  <SENDER_BIC>ABCDEF13</SENDER_BIC>
  <SEQREF>FAC</SEQREF>
  <SPLIT_SETTLEMENT_INDICATOR>N</SPLIT_SETTLEMENT_INDICATOR>
  <SWIFT_MESSAGE_TYPE>300</SWIFT_MESSAGE_TYPE>
  <TERMS_CONDITIONS>ISDA AS PER 2013-03-27</TERMS_CONDITIONS>
  <TRADE_DATE>2013-02-01</TRADE_DATE>
  <TYPE_OF_OPERATION>NEWT</TYPE_OF_OPERATION>
  <VALUE_DATE>2013-02-04</VALUE_DATE>
  <VERSION>0</VERSION>
  <YOUR_REFERENCE/>
  <DROP_OPTIONAL_SEQUENCES_300/>
</SWIFT>
  <SWIFT ID = 'second'></SWIFT>
  <CONFIRMATION>
    <CONF_TEMPLATE_CHLNBR>SWIFT</CONF_TEMPLATE_CHLNBR>
    <SEQNBR>55</SEQNBR>
    <CONFIRMATION_SEQNBR>None</CONFIRMATION_SEQNBR>
    <EVENT_CHLNBR>New Trade</EVENT_CHLNBR>
    <RESET_RESNBR>None</RESET_RESNBR>
    <STATUS>Pending Document Generation</STATUS>
    <TRANSPORT>Network</TRANSPORT>
    <TRDNBR>2</TRDNBR>
    <CFWNBR>None</CFWNBR>
  </CONFIRMATION>
</MESSAGE>'''

##doc =  ET.fromstring(xmlString)
##print doc.find('SWIFT')
##print doc.findall('SWIFT')
##print doc.findall('SELL_RECEIVING_AGENT_ADDRESS')
##print doc.find('SELL_RECEIVING_AGENT_ADDRESS')
##for each in doc.getiterator('sELL_RECEIVING_AGENT_ADDRESS'):
##    print each

#Using XMLParsers
parser = ET.XMLParser(remove_blank_text=True)
parser.feed('<root>')
parser.feed('<child1>hello</child1>')
parser.feed('<child2>bye</child2>')
parser.feed('</root>')
root = parser.close()
#print ET.tostring(root)

xml = ET.fromstring(xmlString, parser)
#print ET.tostring(xml)

##
###Creating / parsing XML
##xmlPath = 'C:\Users\Sadanand.Upase\Downloads\confirmation_55_0.xml'
xml = ET.fromstring(xmlString)
##xml1 = ET.parse(xmlPath) #returns an elementTree instance which should not be used as argument for tostring
##root = xml1.getroot()
##print ET.tostring(xml)
##print ET.tostring(root)
##
##
###Printing xml elements  and getElementsByTagName
###looks for this parent's children only and returns first element with name given
element = xml.find('SWIFT')
##print ET.tostring(element)
###looks for this parent's children only and returns list of all matching elements
##elements = xml.getchildren()[0].findall('BLOCK_TRADE')
##print elements
##findText can help you get the value of a tag
text = xml.getchildren()[0].findtext('SELL_RECEIVING_AGENT_OPTION')
text = element.findtext('SELL_RECEIVING_AGENT_OPTION')
print text
###you can also make use of XPATH
##text = xml.findtext('./SWIFT/SELL_RECEIVING_AGENT_OPTION')
##print text
##
###Adding or removing attribute
###gets value of attribute
##print element.get('ID')
###prints all attributes attrib is a dictionary.
##print element.attrib, element.keys(), element.items()
###adds a new attribute
##element.set('ID1', 'secondID')
##print element.attrib, element.keys(), element.items()
###to remove attribute you have to pop that attribute from attrib dictionary
##element.attrib.pop('ID1')
##print element.attrib, element.keys(), element.items()
##
###remove/replace/insert a node
##element.remove(element.find('SEQREF'))
##assert element.findall('SEQREF') == []
##element.insert(10, ET.Element('SEQREF'))
##assert element.find('SEQREF') != []
###no direct API to replace a node need to remove a node and insert a new node at its place
##
#merging two xmls disturbs the formatting
xmlString2 = '''
<SWIFT>
    <NEWTAG1>hello</NEWTAG1>
    <NEWTAG2>bye</NEWTAG2>
    <NEWTAG3>tata</NEWTAG3>
</SWIFT>'''
##
##secondXml = ET.fromstring(xmlString2)
##for eachNode in secondXml.getchildren():
##    element.append(eachNode)
##print ET.tostring(element)
##
##
###XPATH support
###finds a tag named SELL_RECEIVING_AGENT_ADDRESS
##tag = xml.find('./SWIFT/SELL_RECEIVING_AGENT_ADDRESS')
##print ET.tostring(tag)
###finds all children of  current tag
##tags = xml.findall("./*")
##print tags
##
##
###XML Parser customization
##parser = ET.XMLParser(remove_blank_text=True)
##swift2 = ET.fromstring(xmlString2, parser)
##print ET.tostring(swift2)
