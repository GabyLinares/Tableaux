#-*-coding: utf-8-*-
from random import choice
##############################################################################
# Variables globales
##############################################################################

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

def StringtoTree(A):
    # Crea una formula como tree dada una formula como cadena escrita en notacion polaca inversa
    # Input: A, lista de caracteres con una formula escrita en notacion polaca inversa
             # letrasProposicionales, lista de letras proposicionales
    # Output: formula como tree

	# OJO: DEBE INCLUIR SU CÓDIGO DE STRING2TREE EN ESTA PARTE!!!!!

	p = letrasProposicionales[0] # ELIMINE ESTA LINEA LUEGO DE INCLUIR EL CODIGO DE STRING2TREE
	return Tree(p, None, None) # ELIMINE ESTA LINEA LUEGO DE INCLUIR EL CODIGO DE STRING2TREE

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
    
l = Tree('-', None, Tree('p', None, None))
m = Tree('p', None, None)

print(Inorder(complemento(l)))
print(Inorder(complemento(m)))

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
	# Output: True/False
	if f.left == None:
        	return True
	return False

def no_literales(l):
	# Esta función determina si una lista de fórmulas contiene
	# solo literales
	# Input: l, una lista de fórmulas como árboles
	# Output: None/f, tal que f no es literal
	return False

def clasifica_y_extiende(f):
	# clasifica una fórmula como alfa o beta y extiende listaHojas
	# de acuerdo a la regla respectiva
	# Input: f, una fórmula como árbol
	# Output: no tiene output, pues modifica la variable global listaHojas
	global listaHojas

def Tableaux(f):

	# Algoritmo de creacion de tableau a partir de lista_hojas
	# Imput: - f, una fórmula como string en notación polaca inversa
	# Output: interpretaciones: lista de listas de literales que hacen
	#		 verdadera a f
	global listaHojas
	global listaInterpsVerdaderas

	A = string2Tree(f)
	listaHojas = [[A]]

	return listaInterpsVerdaderas


