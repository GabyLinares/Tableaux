#-*-coding: utf-8-*-
from random import choice
##############################################################################
# Variables globales
##############################################################################

# Crea los conectivos
conectivos = ['Y', 'O', '>', '=']
# Crea las letras minúsculas a-z
letrasProposicionales = [chr(x) for x in range(97, 123)]
# inicializa la lista de interpretaciones
listaInterpsVerdaderas = []
# inicializa la lista de hojas
listaHojas = []

##############################################################################
# Definición de objeto tree y funciones de árboles
##############################################################################

class Tree(object):
	def __init__(self, label, left, right):
		self.left = left
		self.right = right
		self.label = label

def Inorder(f):
    # Imprime una formula como cadena dada una formula como arbol
    # Input: tree, que es una formula de logica proposicional
    # Output: string de la formula
	if f.right == None:
		return f.label
	elif f.label == '-':
		return f.label + Inorder(f.right)
	else:
		return "(" + Inorder(f.left) + f.label + Inorder(f.right) + ")"

def String2Tree(A):
	# Crea una formula como tree dada una formula como cadena escrita en notacion polaca inversa
	# Input: - A, lista de caracteres con una formula escrita en notacion polaca inversa
	#        - letrasProposicionales, lista de letras proposicionales
	#        - conectivos, lista de conectivos
	# Output: formula como tree

	# OJO: DEBE INCLUIR SU CÓDIGO DE STRING2TREE EN ESTA PARTE!!!!!

	pass

##############################################################################
# Definición de funciones de tableaux
##############################################################################

def imprime_hoja(H):
	cadena = "{"
	primero = True
	for f in H:
		if primero == True:
			primero = False
		else:
			cadena += ", "
		cadena += Inorder(f)
	return cadena + "}"

def complemento(l):
    if l.label == '-':
        return l.right
    else :
        return Tree('-', None, l)
    
l = Tree('-', None, Tree('q', None, None))
m = Tree('p', None, None)

#print(Inorder(complemento(l)))
#print(Inorder(complemento(m)))
    

def par_complementario(l):
 	# Esta función determina si una lista de solo literales
 	# contiene un par complementario
 	# Input: l, una lista de literales
 	# Output: True/False
    inorder_literales = []
    for i in l:
        inorder_literales.append(Inorder(i))
    for x in l:
        if Inorder(complemento(x)) in inorder_literales:
            return True
            break
    return False
            
l1 = [Tree('-',None,Tree('Z1',None,None)), Tree('S1',None,None), Tree('-',None,Tree('S10',None,None)), Tree('Z10',None,None)]
l2 = [Tree('b',None,None), Tree('-',None,Tree('a',None,None)), Tree('-',None,Tree('c',None,None)), Tree('a',None,None), Tree('d',None,None)]
l3 = [Tree('-',None,Tree('q',None,None)), Tree('-',None,Tree('p',None,None)), Tree('q',None,None), Tree('-',None,Tree('r',None,None))]
l4 = [Tree('1',None,None), Tree('2',None,None), Tree('-',None,Tree('3',None,None)), Tree('1',None,None)]

print(par_complementario(l1))
print(par_complementario(l2))
print(par_complementario(l3))
print(par_complementario(l4))


def es_literal(f):
	# Esta función determina si el árbol f es un literal
	# Input: f, una fórmula como árbol
	# Output: True/Fals
	# Esta función determina si el árbol f es un literal
    A1 = f.right
    if f.right == None:
        return True
    elif (f.label=='-'):
          if A1.right == None:
              return True
    return False
  
    
    
def no_literales(l):
    # Esta función determina si una lista de fórmulas contiene
    # solo literales
    # Input: l, una lista de fórmulas como árboles
    # Output: None/f, tal que f no es literales
    x = False
    for i in l:
        if (es_literal(i)== False):
            x = True
            break
    return x
	

print("NO LITERALES\n")
l9 = [Tree('-',None,Tree('A1',None,None)),Tree('A2',None,None),Tree('-',None,Tree('A3',None,None)),Tree('A4',None,None),Tree('-',None,Tree('A5',None,None)),Tree('A6',None,None)]
l10 = [Tree('q',None,None),Tree('-',None,Tree('p',None,None)),Tree('-',None,Tree('-',None,Tree('p',None,None))),Tree('-',None,Tree('q',None,None))]
l11 = [Tree('p',None,None),Tree('q',None,None),Tree('O',Tree('p',None,None),Tree('q',None,None)),Tree('-',None,Tree('q',None,None)),Tree('-',None,Tree('p',None,None))]
l12 = [Tree('-',None,Tree('p',None,None)),Tree('p',None,None),Tree('-',None,Tree('q',None,None)),Tree('q',None,None)]

print(no_literales(l9))
print(no_literales(l10))
print(no_literales(l11))
print(no_literales(l12), "\n")

def clasificacion(f):
	# clasifica una fórmula como alfa o beta
	# Input: f, una fórmula como árbol
	# Output: string de la clasificación de la formula

	pass

def clasifica_y_extiende(f, h):
	# Extiende listaHojas de acuerdo a la regla respectiva
	# Input: f, una fórmula como árbol
	# 		 h, una hoja (lista de fórmulas como árboles)
	# Output: no tiene output, pues modifica la variable global listaHojas

	global listaHojas

	print("Formula:", Inorder(f))
	print("Hoja:", imprime_hoja(h))

	assert(f in h), "La formula no esta en la lista!"

	clase = clasificacion(f)
	print("Clasificada como:", clase)
	assert(clase != None), "Formula incorrecta " + imprime_hoja(h)

	if clase == 'Alfa1':
		aux = [x for x in h]
		listaHojas.remove(h)
		aux.remove(f)
		aux += [f.right.right]
		listaHojas.append(aux)
	elif clase == 'Alfa2':
		pass
	# Aqui el resto de casos


def Tableaux(f):

	# Algoritmo de creacion de tableau a partir de lista_hojas
	# Imput: - f, una fórmula como string en notación polaca inversa
	# Output: interpretaciones: lista de listas de literales que hacen
	#		 verdadera a f

	global listaHojas
	global listaInterpsVerdaderas

	A = String2Tree(f)
	print(u'La fórmula introducida es:\n', Inorder(A))

	listaHojas = [[A]]

	pass

#BEGINNING-OF-EXECUTION

print ("")
print ("Prueba es literal")
print ("")




print ("")
print ("Ejercicio es literal")
print ("")

print (es_literal(Tree('alpha',None,None)))
print (es_literal(Tree('O',Tree('k',None,None),Tree('Y',Tree('i',None,None),Tree('j',None,None)))))
print (es_literal(Tree('-',None,Tree('Y',Tree('p',None,None),Tree('q',None,None)))))
print (es_literal(Tree('-',None,Tree('p',None,None))))

print ("")
print ("Prueba no_literales")
print ("")

A1 = Tree('p',None,None)
A2 = Tree('q',None,None)
L1 = [A1,A2]
L2 = [Tree('-',None,Tree('p',None,None)) , Tree('q',None,None)]
L3 = [Tree('-',None,Tree('-',None,Tree('p',None,None)))]
L4 = [ Tree('-',None,Tree('-',None,Tree('p',None,None)))]

print (no_literales(L1))
print (no_literales(L2))
print (no_literales(L3))
print (no_literales(L4))

print ("")
print ("Ejercicio no_literales")
print ("")



