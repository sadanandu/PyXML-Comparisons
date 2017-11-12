# .\employeedb.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:e92452c8d3e28a9e27abfc9994d2007779e7f4c9
# Generated 2017-11-12 21:45:03.068296 by PyXB version 1.2.6 using Python 3.6.1.final.0
# Namespace AbsentNamespace0

from __future__ import unicode_literals
import pyxb
import pyxb.binding
import pyxb.binding.saxer
import io
import pyxb.utils.utility
import pyxb.utils.domutils
import sys
import pyxb.utils.six as _six
# Unique identifier for bindings created at the same time
_GenerationUID = pyxb.utils.utility.UniqueIdentifier('urn:uuid:a3745dc0-c7c4-11e7-ae04-0019d193b0e8')

# Version of PyXB used to generate the bindings
_PyXBVersion = '1.2.6'
# Generated bindings are not compatible across PyXB versions
if pyxb.__version__ != _PyXBVersion:
    raise pyxb.PyXBVersionError(_PyXBVersion)

# A holder for module-level binding classes so we can access them from
# inside class definitions where property names may conflict.
_module_typeBindings = pyxb.utils.utility.Object()

# Import bindings for namespaces imported into schema
import pyxb.binding.datatypes

# NOTE: All namespace declarations are reserved within the binding
Namespace = pyxb.namespace.CreateAbsentNamespace()
Namespace.configureCategories(['typeBinding', 'elementBinding'])

def CreateFromDocument (xml_text, default_namespace=None, location_base=None):
    """Parse the given XML and use the document element to create a
    Python instance.

    @param xml_text An XML document.  This should be data (Python 2
    str or Python 3 bytes), or a text (Python 2 unicode or Python 3
    str) in the L{pyxb._InputEncoding} encoding.

    @keyword default_namespace The L{pyxb.Namespace} instance to use as the
    default namespace where there is no default namespace in scope.
    If unspecified or C{None}, the namespace of the module containing
    this function will be used.

    @keyword location_base: An object to be recorded as the base of all
    L{pyxb.utils.utility.Location} instances associated with events and
    objects handled by the parser.  You might pass the URI from which
    the document was obtained.
    """

    if pyxb.XMLStyle_saxer != pyxb._XMLStyle:
        dom = pyxb.utils.domutils.StringToDOM(xml_text)
        return CreateFromDOM(dom.documentElement, default_namespace=default_namespace)
    if default_namespace is None:
        default_namespace = Namespace.fallbackNamespace()
    saxer = pyxb.binding.saxer.make_parser(fallback_namespace=default_namespace, location_base=location_base)
    handler = saxer.getContentHandler()
    xmld = xml_text
    if isinstance(xmld, _six.text_type):
        xmld = xmld.encode(pyxb._InputEncoding)
    saxer.parse(io.BytesIO(xmld))
    instance = handler.rootObject()
    return instance

def CreateFromDOM (node, default_namespace=None):
    """Create a Python instance from the given DOM node.
    The node tag must correspond to an element declaration in this module.

    @deprecated: Forcing use of DOM interface is unnecessary; use L{CreateFromDocument}."""
    if default_namespace is None:
        default_namespace = Namespace.fallbackNamespace()
    return pyxb.binding.basis.element.AnyCreateFromDOM(node, default_namespace)


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('C:\\Machine Learning\\PyPractice\\employeedb.xsd', 4, 6)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element EMPLOYEE uses Python identifier EMPLOYEE
    __EMPLOYEE = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'EMPLOYEE'), 'EMPLOYEE', '__AbsentNamespace0_CTD_ANON_EMPLOYEE', True, pyxb.utils.utility.Location('C:\\ProgramData\\Anaconda3\\employee.xsd', 2, 0), )

    
    EMPLOYEE = property(__EMPLOYEE.value, __EMPLOYEE.set, None, None)

    _ElementMap.update({
        __EMPLOYEE.name() : __EMPLOYEE
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON = CTD_ANON


# Complex type EmployeeType with content type ELEMENT_ONLY
class EmployeeType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type EmployeeType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'EmployeeType')
    _XSDLocation = pyxb.utils.utility.Location('C:\\ProgramData\\Anaconda3\\employee.xsd', 3, 0)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element EMPID uses Python identifier EMPID
    __EMPID = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'EMPID'), 'EMPID', '__AbsentNamespace0_EmployeeType_EMPID', False, pyxb.utils.utility.Location('C:\\ProgramData\\Anaconda3\\employee.xsd', 5, 2), )

    
    EMPID = property(__EMPID.value, __EMPID.set, None, None)

    
    # Element SALARY uses Python identifier SALARY
    __SALARY = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'SALARY'), 'SALARY', '__AbsentNamespace0_EmployeeType_SALARY', False, pyxb.utils.utility.Location('C:\\ProgramData\\Anaconda3\\employee.xsd', 6, 2), )

    
    SALARY = property(__SALARY.value, __SALARY.set, None, None)

    
    # Element DEPT_ID uses Python identifier DEPT_ID
    __DEPT_ID = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'DEPT_ID'), 'DEPT_ID', '__AbsentNamespace0_EmployeeType_DEPT_ID', False, pyxb.utils.utility.Location('C:\\ProgramData\\Anaconda3\\employee.xsd', 7, 2), )

    
    DEPT_ID = property(__DEPT_ID.value, __DEPT_ID.set, None, None)

    _ElementMap.update({
        __EMPID.name() : __EMPID,
        __SALARY.name() : __SALARY,
        __DEPT_ID.name() : __DEPT_ID
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.EmployeeType = EmployeeType
Namespace.addCategoryObject('typeBinding', 'EmployeeType', EmployeeType)


EMPLOYEEDB = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'EMPLOYEEDB'), CTD_ANON, location=pyxb.utils.utility.Location('C:\\Machine Learning\\PyPractice\\employeedb.xsd', 3, 2))
Namespace.addCategoryObject('elementBinding', EMPLOYEEDB.name().localName(), EMPLOYEEDB)

EMPLOYEE = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'EMPLOYEE'), EmployeeType, location=pyxb.utils.utility.Location('C:\\ProgramData\\Anaconda3\\employee.xsd', 2, 0))
Namespace.addCategoryObject('elementBinding', EMPLOYEE.name().localName(), EMPLOYEE)



CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'EMPLOYEE'), EmployeeType, scope=CTD_ANON, location=pyxb.utils.utility.Location('C:\\ProgramData\\Anaconda3\\employee.xsd', 2, 0)))

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('C:\\Machine Learning\\PyPractice\\employeedb.xsd', 6, 14))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'EMPLOYEE')), pyxb.utils.utility.Location('C:\\Machine Learning\\PyPractice\\employeedb.xsd', 6, 14))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON._Automaton = _BuildAutomaton()




EmployeeType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'EMPID'), pyxb.binding.datatypes.string, scope=EmployeeType, location=pyxb.utils.utility.Location('C:\\ProgramData\\Anaconda3\\employee.xsd', 5, 2)))

EmployeeType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'SALARY'), pyxb.binding.datatypes.string, scope=EmployeeType, location=pyxb.utils.utility.Location('C:\\ProgramData\\Anaconda3\\employee.xsd', 6, 2)))

EmployeeType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'DEPT_ID'), pyxb.binding.datatypes.string, scope=EmployeeType, location=pyxb.utils.utility.Location('C:\\ProgramData\\Anaconda3\\employee.xsd', 7, 2)))

def _BuildAutomaton_ ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_
    del _BuildAutomaton_
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(EmployeeType._UseForTag(pyxb.namespace.ExpandedName(None, 'EMPID')), pyxb.utils.utility.Location('C:\\ProgramData\\Anaconda3\\employee.xsd', 5, 2))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(EmployeeType._UseForTag(pyxb.namespace.ExpandedName(None, 'SALARY')), pyxb.utils.utility.Location('C:\\ProgramData\\Anaconda3\\employee.xsd', 6, 2))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(EmployeeType._UseForTag(pyxb.namespace.ExpandedName(None, 'DEPT_ID')), pyxb.utils.utility.Location('C:\\ProgramData\\Anaconda3\\employee.xsd', 7, 2))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
EmployeeType._Automaton = _BuildAutomaton_()

