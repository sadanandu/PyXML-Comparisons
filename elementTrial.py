import xml.etree.ElementTree as ET

def CreatingXmlOnTheGo():
    root = ET.Element('root')
    root.text = 'I am root cause'
    root.tail = 'I am the tail'
    one = ET.SubElement(root, 'one', font='large')
    one.text = 'I am the one'
    two = ET.SubElement(root, 'two', wrap='word')
    box = ET.SubElement(root, 'buttonbox')
    ET.SubElement(box, 'button').text = 'ok'
    ET.SubElement(box, 'button').text = 'cancel'
    print ET.tostring(root)

def CreatingXmlFromString():
    xmlString = '''
    <MESSAGE>
      <SWIFT ID = 'first'>
          <BLOCK_TRADE>N</BLOCK_TRADE>
          <BUY_AMOUNT>300.0</BUY_AMOUNT>
          <BUY_CURRENCY>EUR</BUY_CURRENCY>
          <BUY_DELIVERY_AGENT_OPTION>A</BUY_DELIVERY_AGENT_OPTION>
          <BUY_DELIVERY_AGENT_ACCOUNT>12345</BUY_DELIVERY_AGENT_ACCOUNT>
          <BUY_DELIVERY_AGENT_BIC>ABCDEF10</BUY_DELIVERY_AGENT_BIC>
          <BUY_DELIVERY_AGENT_NAME>LC CP CB</BUY_DELIVERY_AGENT_NAME>
          <BUY_DELIVERY_AGENT_ADDRESS>Pune  </BUY_DELIVERY_AGENT_ADDRESS>
          <BUY_INTERMEDIARY_OPTION>A</BUY_INTERMEDIARY_OPTION>
          <BUY_INTERMEDIARY_ACCOUNT>22223</BUY_INTERMEDIARY_ACCOUNT>
      </SWIFT>
      <SWIFT ID = 'second'>
      </SWIFT>
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
    doc =  ET.fromstring(xmlString)
    print ET.tostring(doc)

def ParsingXmlFromFile():
    xmlPath = '.\\xmlExample.xml'
    xml = ET.parse(xmlPath) #returns ElementTree instance can't be used as argument for tostring.
    return xml

def SearchingTags():
    doc = ParsingXmlFromFile()
    ##looks for this parent's children only and returns first element with name given
    print doc.find('SWIFT')
    ##looks for this parent's children only and returns list of all matching elements
    print doc.findall('SWIFT')
    for each in doc.getiterator('BUY_DELIVERY_AGENT_NAME'):
        print each

tagName = 'BUY_AMOUNT'
pathForTag = './SWIFT/BUY_AMOUNT'
def GetValueOfTag():
    doc = ParsingXmlFromFile()
    ##XPATH support is present
    print doc.findtext(pathForTag)
    ##Can't find anything because findtext looks for children of current part
    print doc.findtext(tagName)


def AddNewNodeToDoc():
    doc = ParsingXmlFromFile()
    root = doc.getroot()
    firstSwiftTag = doc.find('SWIFT')
    element = ET.Element('SELL_AMOUNT')
    firstSwiftTag.insert(10, element)
    print ET.tostring(root)

AddNewNodeToDoc()
##element acts as python list
##one = root[0]
##print one
##print len(root)
##if len(root):  #to check if element has children
##    print 'Has children'

###Same element can appear in two different trees causing a change in one tree to reflect in other tree also
##root1 = ET.Element('root1')
##root1.append(one)
##one = root1[0]
##one.attrib['font'] = 'small'
##orgOne = root[0]
##assert one.attrib['font'] == orgOne.attrib['font']


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
##
###merging two xmls disturbs the formatting
##xmlString2 = '''
##<SWIFT>
##    <NEWTAG1>hello</NEWTAG1>
##    <NEWTAG2>bye</NEWTAG2>
##    <NEWTAG3>tata</NEWTAG3>
##</SWIFT>'''
##
##secondXml = ET.fromstring(xmlString2)
##for eachNode in secondXml.getchildren():
##    element.append(eachNode)
###print ET.tostring(element)
##
##
###XPATH support
###finds a tag named SELL_RECEIVING_AGENT_ADDRESS
##tag = xml.find('./SWIFT/SELL_RECEIVING_AGENT_ADDRESS')
##print ET.tostring(tag)
###finds all children of  current tag
##tags = xml.findall("./*")
##print tags