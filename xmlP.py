import xml.etree.ElementTree as ElementTree
from copy import deepcopy
class Test:
	def __init__(self):
		self.out=""
	def treeToProg1(self,root):
	    if root is not None:
	        for child in root:
	            if child.text is not None:
	                self.out+=child.text
	            self.treeToProg1(child)   
	            if child.tail is not None:
	                self.out+=child.tail
	    return self.out
	def treeToProg(self,root):
	    if root is not None:
	    	if root.text is not None:
	    		self.out+=root.text
    		self.treeToProg1(root)
	    return self.out
class ProgramGen:
    def __init__(self):
        self.out=""

    def treeToProg(self,root):
        if root is not None:
            if root.text is not None:
                self.out+=root.text
            for child in root:
                self.treeToProg(child)   
            if root.tail is not None:
                self.out+=root.tail
        return self.out   


s="<program><statementListItem><statement><expressionStatement><expression><assignmentExpression><conditionalExpression><leftHandSideExpression><newExpression><memberExpression><primaryExpression><identifierName>x </identifierName></primaryExpression></memberExpression></newExpression></leftHandSideExpression></conditionalExpression>= <assignmentExpression><conditionalExpression><leftHandSideExpression><newExpression><memberExpression><primaryExpression><literal>&quot;1&quot; </literal></primaryExpression></memberExpression></newExpression></leftHandSideExpression></conditionalExpression><eos>; </eos></assignmentExpression><eos></eos></assignmentExpression></expression></expressionStatement></statement></statementListItem><statementListItem><statement><expressionStatement><expression><assignmentExpression><assignmentExpression><conditionalExpression><leftHandSideExpression><newExpression><memberExpression><primaryExpression><identifierName>x </identifierName></primaryExpression></memberExpression></newExpression></leftHandSideExpression></conditionalExpression><assignmentOperator>&lt;&lt;= </assignmentOperator><assignmentExpression><conditionalExpression><leftHandSideExpression><newExpression><memberExpression><primaryExpression><identifierName>undefined </identifierName></primaryExpression></memberExpression></newExpression></leftHandSideExpression></conditionalExpression><eos>; </eos></assignmentExpression></assignmentExpression>if ( <expression><assignmentExpression><conditionalExpression><conditionalExpression><leftHandSideExpression><newExpression><memberExpression><primaryExpression><identifierName>x </identifierName></primaryExpression></memberExpression></newExpression></leftHandSideExpression></conditionalExpression>!== <conditionalExpression><leftHandSideExpression><newExpression><memberExpression><primaryExpression><literal><numericLiteral>1 </numericLiteral></literal></primaryExpression></memberExpression></newExpression></leftHandSideExpression></conditionalExpression></conditionalExpression></assignmentExpression></expression>) </assignmentExpression></expression></expressionStatement></statement></statementListItem><statementListItem><statement><block>{ <statementList><statement><expressionStatement><expression><assignmentExpression><conditionalExpression><leftHandSideExpression><callExpression><memberExpression><primaryExpression><identifierName>$ERROR </identifierName></primaryExpression></memberExpression><arguments>( <argumentList><assignmentExpression><conditionalExpression><conditionalExpression><leftHandSideExpression><newExpression><memberExpression><primaryExpression><literal>&apos;#1: x = &quot;1&quot;; x &lt;&lt;= undefined; x === 1. Actual: &apos; </literal></primaryExpression></memberExpression></newExpression></leftHandSideExpression></conditionalExpression>+ <conditionalExpression><leftHandSideExpression><newExpression><memberExpression><primaryExpression>( <expression><assignmentExpression><conditionalExpression><leftHandSideExpression><newExpression><memberExpression><primaryExpression><identifierName>x </identifierName></primaryExpression></memberExpression></newExpression></leftHandSideExpression></conditionalExpression></assignmentExpression></expression>) </primaryExpression></memberExpression></newExpression></leftHandSideExpression></conditionalExpression></conditionalExpression></assignmentExpression></argumentList>) </arguments><eos>; </eos></callExpression></leftHandSideExpression></conditionalExpression><eos></eos></assignmentExpression></expression></expressionStatement></statement></statementList>} </block></statement></statementListItem><statementListItem><statement><expressionStatement><expression><assignmentExpression><conditionalExpression><leftHandSideExpression><newExpression><memberExpression><primaryExpression><identifierName>x </identifierName></primaryExpression></memberExpression></newExpression></leftHandSideExpression></conditionalExpression>= <assignmentExpression><conditionalExpression><leftHandSideExpression><newExpression><memberExpression><primaryExpression><identifierName>undefined </identifierName></primaryExpression></memberExpression></newExpression></leftHandSideExpression></conditionalExpression><eos>; </eos></assignmentExpression><eos></eos></assignmentExpression></expression></expressionStatement></statement></statementListItem><statementListItem><statement><expressionStatement><expression><assignmentExpression><assignmentExpression><conditionalExpression><leftHandSideExpression><newExpression><memberExpression><primaryExpression><identifierName>x </identifierName></primaryExpression></memberExpression></newExpression></leftHandSideExpression></conditionalExpression><assignmentOperator>&lt;&lt;= </assignmentOperator><assignmentExpression><conditionalExpression><leftHandSideExpression><newExpression><memberExpression><primaryExpression><literal>&quot;1&quot; </literal></primaryExpression></memberExpression></newExpression></leftHandSideExpression></conditionalExpression><eos>; </eos></assignmentExpression></assignmentExpression>if ( <expression><assignmentExpression><conditionalExpression><conditionalExpression><leftHandSideExpression><newExpression><memberExpression><primaryExpression><identifierName>x </identifierName></primaryExpression></memberExpression></newExpression></leftHandSideExpression></conditionalExpression>!== <conditionalExpression><leftHandSideExpression><newExpression><memberExpression><primaryExpression><literal><numericLiteral>0 </numericLiteral></literal></primaryExpression></memberExpression></newExpression></leftHandSideExpression></conditionalExpression></conditionalExpression></assignmentExpression></expression>) </assignmentExpression></expression></expressionStatement></statement></statementListItem><statementListItem><statement><block>{ <statementList><statement><expressionStatement><expression><assignmentExpression><conditionalExpression><leftHandSideExpression><callExpression><memberExpression><primaryExpression><identifierName>$ERROR </identifierName></primaryExpression></memberExpression><arguments>( <argumentList><assignmentExpression><conditionalExpression><conditionalExpression><leftHandSideExpression><newExpression><memberExpression><primaryExpression><literal>&apos;#2: x = undefined; x &lt;&lt;= &quot;1&quot;; x === 0. Actual: &apos; </literal></primaryExpression></memberExpression></newExpression></leftHandSideExpression></conditionalExpression>+ <conditionalExpression><leftHandSideExpression><newExpression><memberExpression><primaryExpression>( <expression><assignmentExpression><conditionalExpression><leftHandSideExpression><newExpression><memberExpression><primaryExpression><identifierName>x </identifierName></primaryExpression></memberExpression></newExpression></leftHandSideExpression></conditionalExpression></assignmentExpression></expression>) </primaryExpression></memberExpression></newExpression></leftHandSideExpression></conditionalExpression></conditionalExpression></assignmentExpression></argumentList>) </arguments><eos>; </eos></callExpression></leftHandSideExpression></conditionalExpression><eos></eos></assignmentExpression></expression></expressionStatement></statement></statementList>} </block></statement></statementListItem><statementListItem><statement><expressionStatement><expression><assignmentExpression><conditionalExpression><leftHandSideExpression><newExpression><memberExpression><primaryExpression><identifierName>x </identifierName></primaryExpression></memberExpression></newExpression></leftHandSideExpression></conditionalExpression>= <assignmentExpression><conditionalExpression><leftHandSideExpression><newExpression><memberExpression>new <memberExpression><primaryExpression><identifierName>String </identifierName></primaryExpression></memberExpression><arguments>( <argumentList><assignmentExpression><conditionalExpression><leftHandSideExpression><newExpression><memberExpression><primaryExpression><literal>&quot;1&quot; </literal></primaryExpression></memberExpression></newExpression></leftHandSideExpression></conditionalExpression></assignmentExpression></argumentList>) </arguments></memberExpression></newExpression></leftHandSideExpression></conditionalExpression><eos>; </eos></assignmentExpression><eos></eos></assignmentExpression></expression></expressionStatement></statement></statementListItem><statementListItem><statement><expressionStatement><expression><assignmentExpression><assignmentExpression><conditionalExpression><leftHandSideExpression><newExpression><memberExpression><primaryExpression><identifierName>x </identifierName></primaryExpression></memberExpression></newExpression></leftHandSideExpression></conditionalExpression><assignmentOperator>&lt;&lt;= </assignmentOperator><assignmentExpression><conditionalExpression><leftHandSideExpression><newExpression><memberExpression><primaryExpression><identifierName>undefined </identifierName></primaryExpression></memberExpression></newExpression></leftHandSideExpression></conditionalExpression><eos>; </eos></assignmentExpression></assignmentExpression>if ( <expression><assignmentExpression><conditionalExpression><conditionalExpression><leftHandSideExpression><newExpression><memberExpression><primaryExpression><identifierName>x </identifierName></primaryExpression></memberExpression></newExpression></leftHandSideExpression></conditionalExpression>!== <conditionalExpression><leftHandSideExpression><newExpression><memberExpression><primaryExpression><literal><numericLiteral>1 </numericLiteral></literal></primaryExpression></memberExpression></newExpression></leftHandSideExpression></conditionalExpression></conditionalExpression></assignmentExpression></expression>) </assignmentExpression></expression></expressionStatement></statement></statementListItem><statementListItem><statement><block>{ <statementList><statement><expressionStatement><expression><assignmentExpression><conditionalExpression><leftHandSideExpression><callExpression><memberExpression><primaryExpression><identifierName>$ERROR </identifierName></primaryExpression></memberExpression><arguments>( <argumentList><assignmentExpression><conditionalExpression><conditionalExpression><leftHandSideExpression><newExpression><memberExpression><primaryExpression><literal>&apos;#3: x = new String(&quot;1&quot;); x &lt;&lt;= undefined; x === 1. Actual: &apos; </literal></primaryExpression></memberExpression></newExpression></leftHandSideExpression></conditionalExpression>+ <conditionalExpression><leftHandSideExpression><newExpression><memberExpression><primaryExpression>( <expression><assignmentExpression><conditionalExpression><leftHandSideExpression><newExpression><memberExpression><primaryExpression><identifierName>x </identifierName></primaryExpression></memberExpression></newExpression></leftHandSideExpression></conditionalExpression></assignmentExpression></expression>) </primaryExpression></memberExpression></newExpression></leftHandSideExpression></conditionalExpression></conditionalExpression></assignmentExpression></argumentList>) </arguments><eos>; </eos></callExpression></leftHandSideExpression></conditionalExpression><eos></eos></assignmentExpression></expression></expressionStatement></statement></statementList>} </block></statement></statementListItem><statementListItem><statement><expressionStatement><expression><assignmentExpression><conditionalExpression><leftHandSideExpression><newExpression><memberExpression><primaryExpression><identifierName>x </identifierName></primaryExpression></memberExpression></newExpression></leftHandSideExpression></conditionalExpression>= <assignmentExpression><conditionalExpression><leftHandSideExpression><newExpression><memberExpression><primaryExpression><identifierName>undefined </identifierName></primaryExpression></memberExpression></newExpression></leftHandSideExpression></conditionalExpression><eos>; </eos></assignmentExpression><eos></eos></assignmentExpression></expression></expressionStatement></statement></statementListItem><statementListItem><statement><expressionStatement><expression><assignmentExpression><assignmentExpression><conditionalExpression><leftHandSideExpression><newExpression><memberExpression><primaryExpression><identifierName>x </identifierName></primaryExpression></memberExpression></newExpression></leftHandSideExpression></conditionalExpression><assignmentOperator>&lt;&lt;= </assignmentOperator><assignmentExpression><conditionalExpression><leftHandSideExpression><newExpression><memberExpression>new <memberExpression><primaryExpression><identifierName>String </identifierName></primaryExpression></memberExpression><arguments>( <argumentList><assignmentExpression><conditionalExpression><leftHandSideExpression><newExpression><memberExpression><primaryExpression><literal>&quot;1&quot; </literal></primaryExpression></memberExpression></newExpression></leftHandSideExpression></conditionalExpression></assignmentExpression></argumentList>) </arguments></memberExpression></newExpression></leftHandSideExpression></conditionalExpression><eos>; </eos></assignmentExpression></assignmentExpression>if ( <expression><assignmentExpression><conditionalExpression><conditionalExpression><leftHandSideExpression><newExpression><memberExpression><primaryExpression><identifierName>x </identifierName></primaryExpression></memberExpression></newExpression></leftHandSideExpression></conditionalExpression>!== <conditionalExpression><leftHandSideExpression><newExpression><memberExpression><primaryExpression><literal><numericLiteral>0 </numericLiteral></literal></primaryExpression></memberExpression></newExpression></leftHandSideExpression></conditionalExpression></conditionalExpression></assignmentExpression></expression>) </assignmentExpression></expression></expressionStatement></statement></statementListItem><statementListItem><statement><block>{ <statementList><statement><expressionStatement><expression><assignmentExpression><conditionalExpression><leftHandSideExpression><callExpression><memberExpression><primaryExpression><identifierName>$ERROR </identifierName></primaryExpression></memberExpression><arguments>( <argumentList><assignmentExpression><conditionalExpression><conditionalExpression><leftHandSideExpression><newExpression><memberExpression><primaryExpression><literal>&apos;#4: x = undefined; x &lt;&lt;= new String(&quot;1&quot;); x === 0. Actual: &apos; </literal></primaryExpression></memberExpression></newExpression></leftHandSideExpression></conditionalExpression>+ <conditionalExpression><leftHandSideExpression><newExpression><memberExpression><primaryExpression>( <expression><assignmentExpression><conditionalExpression><leftHandSideExpression><newExpression><memberExpression><primaryExpression><identifierName>x </identifierName></primaryExpression></memberExpression></newExpression></leftHandSideExpression></conditionalExpression></assignmentExpression></expression>) </primaryExpression></memberExpression></newExpression></leftHandSideExpression></conditionalExpression></conditionalExpression></assignmentExpression></argumentList>) </arguments><eos>; </eos></callExpression></leftHandSideExpression></conditionalExpression><eos></eos></assignmentExpression></expression></expressionStatement></statement></statementList>} </block></statement></statementListItem></program>"
s1="<program><statementListItem><statement><variableStatement>var <variableDeclarationList><variableDeclaration><identifierBinding><identifierReference><identifierName>a </identifierName></identifierReference></identifierBinding><initialiser>= <assignmentExpression><conditionalExpression><leftHandSideExpression><newExpression><memberExpression><primaryExpression><literal><numericLiteral>100 </numericLiteral></literal></primaryExpression></memberExpression></newExpression></leftHandSideExpression></conditionalExpression></assignmentExpression></initialiser></variableDeclaration></variableDeclarationList><eos>;</eos></variableStatement></statement></statementListItem><statementListItem><statement><emptyStatement>; </emptyStatement></statement></statementListItem><statementListItem><statement><variableStatement>var <variableDeclarationList><variableDeclaration><identifierBinding><identifierReference><identifierName>b </identifierName></identifierReference></identifierBinding><initialiser>= <assignmentExpression><conditionalExpression><leftHandSideExpression><newExpression><memberExpression><primaryExpression><literal><numericLiteral>100 </numericLiteral></literal></primaryExpression></memberExpression></newExpression></leftHandSideExpression></conditionalExpression></assignmentExpression></initialiser></variableDeclaration></variableDeclarationList></variableStatement></statement></statementListItem><statementListItem><statement><emptyStatement>; </emptyStatement></statement></statementListItem></program>"
et = ElementTree.fromstring(s1)
et1 = ElementTree.fromstring(s)
nt="statementListItem"

li=[]
for r in et.iter(nt):
	li.append(r)

print li
li1=[]
for r in et1.iter(nt):
	li1.append(r)

print li1

import random

importPlaceholder= random.choice(li)
importPlaceholder1= random.choice(li1)



child1 = importPlaceholder.getchildren()
child1DeepCopy=deepcopy(child1)
child2 = importPlaceholder1.getchildren()
child2DeepCopy=deepcopy(child2)

while len(child1):
	ch=child1[0]
	importPlaceholder.remove(ch)

# while len(child2):
# 	ch=child2[0]
# 	importPlaceholder1.remove(ch)

# for ch in child2DeepCopy:
# 	importPlaceholder.append(ch)


# for ch in child1DeepCopy:
# 	importPlaceholder1.append(ch)

etTemp = ElementTree.fromstring("<MutationNode> "+ "spandan" +" </MutationNode>")
importPlaceholder.append(etTemp)

t=ProgramGen()
print t.treeToProg(et)
print 
# t=ProgramGen()
# print t.treeToProg(et1)
# for importPlaceholder in li:
# 	print importPlaceholder
# 	t=ProgramGen()
# 	print t.treeToProg(importPlaceholder)
# 	print "\n"

# t=Test()
# print t.treeToProg(et1)

# <program><statementListItem><statement><variableStatement>var <variableDeclarationList><variableDeclaration><identifierBinding><identifierReference><identifierName>s </identifierName></identifierReference></identifierBinding><initialiser>= <assignmentExpression><conditionalExpression><leftHandSideExpression><newExpression><memberExpression><primaryExpression><literal><numericLiteral>100 </numericLiteral></literal></primaryExpression></memberExpression></newExpression></leftHandSideExpression></conditionalExpression></assignmentExpression></initialiser></variableDeclaration></variableDeclarationList></variableStatement></statement></statementListItem><statementListItem><statement><emptyStatement>; </emptyStatement></statement></statementListItem><statementListItem><statement><variableStatement>var <variableDeclarationList><variableDeclaration><identifierBinding><identifierReference><identifierName>b </identifierName></identifierReference></identifierBinding><initialiser>= <assignmentExpression><conditionalExpression><leftHandSideExpression><newExpression><memberExpression><primaryExpression><literal><numericLiteral>100 </numericLiteral></literal></primaryExpression></memberExpression></newExpression></leftHandSideExpression></conditionalExpression></assignmentExpression></initialiser></variableDeclaration></variableDeclarationList></variableStatement></statement></statementListItem><statementListItem><statement><emptyStatement>; </emptyStatement></statement></statementListItem></program>
# <program><statementListItem><statement><variableStatement>var <variableDeclarationList><variableDeclaration><identifierBinding><identifierReference><identifierName>a </identifierName></identifierReference></identifierBinding><initialiser>= <assignmentExpression><conditionalExpression><leftHandSideExpression><newExpression><memberExpression><primaryExpression><literal><numericLiteral>100 </numericLiteral></literal></primaryExpression></memberExpression></newExpression></leftHandSideExpression></conditionalExpression></assignmentExpression></initialiser></variableDeclaration></variableDeclarationList></variableStatement></statement></statementListItem><statementListItem><statement><emptyStatement>; </emptyStatement></statement></statementListItem><statementListItem><statement><variableStatement>var <variableDeclarationList><variableDeclaration><identifierBinding><identifierReference><identifierName>z </identifierName></identifierReference></identifierBinding><initialiser>= <assignmentExpression><conditionalExpression><leftHandSideExpression><newExpression><memberExpression><primaryExpression><literal><numericLiteral>100 </numericLiteral></literal></primaryExpression></memberExpression></newExpression></leftHandSideExpression></conditionalExpression></assignmentExpression></initialiser></variableDeclaration></variableDeclarationList></variableStatement></statement></statementListItem><statementListItem><statement><emptyStatement>; </emptyStatement></statement></statementListItem></program>