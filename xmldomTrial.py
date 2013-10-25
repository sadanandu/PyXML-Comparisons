import xml.dom.minidom as dom

def CreatingXmlOnTheGo():
    implementation = dom.getDOMImplementation()
    doc = implementation.createDocument(None, 'root', None)
    root = doc.documentElement
    root.appendChild(doc.createTextNode('I am root cause'))
    one = doc.createElement('one')
    root.appendChild(one)
    two = doc.createElement('two')
    root.appendChild(two)
    buttonbox = doc.createElement('buttonbox')
    button1 = doc.createElement('button')
    buttonbox.appendChild(button1)
    button2 = doc.createElement('button')
    buttonbox.appendChild(button2)
    root.appendChild(buttonbox)
    print root.toxml()

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

    xml = dom.parseString(xmlString)
    print xml.toxml()

def ParsingXmlFromFile():
    xmlPath = '.\\xmlExample.xml'
    xml = dom.parse(xmlPath)
    return xml

def SearchingTags():
    doc = ParsingXmlFromFile()
    print doc.getElementsByTagName('SWIFT')
    swiftTags = doc.getElementsByTagName('SWIFT')
    swiftTags[0].setIdAttribute('ID')
    print doc.getElementsByTagName('SELL_RECEIVING_AGENT_ADDRESS')
    print doc.getElementById('first')

tagName = 'BUY_AMOUNT'
def GetValueOfTag():
    doc = ParsingXmlFromFile()
    tag = doc.getElementsByTagName(tagName)[0]
    for child in tag.childNodes:
        if child.nodeType == 3:
            print child.nodeValue

def AddNewNodeToDoc():
    doc = ParsingXmlFromFile()
    element = doc.createElement('SELL_AMOUNT')
    text = doc.createTextNode('101')
    element.appendChild(text)
    newLineNode = doc.createTextNode('\n     ')
    firstSwiftTag = doc.getElementsByTagName('SWIFT')[0]
    firstSwiftTag.insertBefore(newLineNode, firstSwiftTag.lastChild)
    firstSwiftTag.insertBefore(element, firstSwiftTag.lastChild)
    print doc.toxml()

def DeletingNode():
    doc = ParsingXmlFromFile()
    node = doc.getElementsByTagName(tagName)[0]
    node.parentNode.removeChild(node)
    print doc.toxml()

def ReplaceNode():
    doc = ParsingXmlFromFile()
    element = doc.createElement('SELL_AMOUNT')
    text = doc.createTextNode('101')
    element.appendChild(text)
    newLineNode = doc.createTextNode('\n     ')
    node = doc.getElementsByTagName(tagName)[0]
    swift = doc.getElementsByTagName('SWIFT')[0]
    swift.insertBefore(element, node)
    node.parentNode.removeChild(node)
    print doc.toxml()

def MergeXmls():
    doc = ParsingXmlFromFile()
    swift = doc.getElementsByTagName('SWIFT')[0]
    xmlString2 = '''
<SWIFT>
     <NEWTAG1>hello</NEWTAG1>
     <NEWTAG2>bye</NEWTAG2>
     <NEWTAG3>tata</NEWTAG3>
</SWIFT>'''

    secondXml = dom.parseString(xmlString2)
    swift.insertBefore(doc.createTextNode('\n     '), swift.lastChild)
    for eachTag in secondXml.firstChild.childNodes[1:-1]:
        importedNode = secondXml.importNode(eachTag, True)
        swift.insertBefore(importedNode, swift.lastChild)
    print swift.toxml()

#No XPATH support
#Need to install PyXML but this library is not maintained now


