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

def GetSetAttribute():
    doc = ParsingXmlFromFile()
    root = doc.getroot()
    firstSwiftTag = doc.find('SWIFT')
    print firstSwiftTag.get('ID')
    firstSwiftTag.set('EmptyTag', 'False')
    print firstSwiftTag.attrib
    print firstSwiftTag.get('EmptyTag')

tagName = 'BUY_AMOUNT'
def DeletingNode():
    doc = ParsingXmlFromFile()
    root = doc.getroot()
    root.find('SWIFT').remove(root.find('SWIFT').find(tagName))
    print ET.tostring(root)

tagName = 'BUY_AMOUNT'
def ReplaceNode():
    doc = ParsingXmlFromFile()
    root = doc.getroot()
    print 'Before Replacing'
    print ET.tostring(root)
    firstSwiftTag = root.find('SWIFT')
    targetNode = firstSwiftTag.find(tagName)
    indexOfTargetNode = [index for index, node in enumerate(firstSwiftTag)  if targetNode == node][0]
    newNode = ET.Element('SELL_AMOUNT')
    newNode.text = '101'
    firstSwiftTag.insert(indexOfTargetNode, newNode)
    firstSwiftTag.remove(targetNode)
    print 'After Replacing'
    print ET.tostring(root)

def MergeXmls():
    doc = ParsingXmlFromFile()
    originalRoot = doc.getroot()
    print 'Before merging'
    print ET.tostring(originalRoot)
    originalSwiftTag = originalRoot.find('SWIFT')
    xmlString2 = '''
<SWIFT>
     <NEWTAG1>hello</NEWTAG1>
     <NEWTAG2>bye</NEWTAG2>
     <NEWTAG3>tata</NEWTAG3>
</SWIFT>'''

    xmlToBeMerged = ET.fromstring(xmlString2)
    #appending all children of current tag
    for eachTag in xmlToBeMerged.findall('./*'):
        originalSwiftTag.append(eachTag)
    print 'After Merging'
    print ET.tostring(originalRoot)

def UseXPathSupport():
    doc = ParsingXmlFromFile()
    root = doc.getroot()
    print 'All children of root'
    print root.findall('./*')
    print 'BUY_INTERMEDIARY_OPTION from root'
    print root.find('./SWIFT/BUY_INTERMEDIARY_OPTION')

def PythonicUseOfET():
    doc = ParsingXmlFromFile()
    root = doc.getroot()
    print 'Root acts as a list of elements'
    for aChild in root:
        print aChild
