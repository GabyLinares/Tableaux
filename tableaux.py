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
	pila = []
	for c in A:
		# print("Examinando " + str(c))
		if c in letrasProposicionales:
			# print(u"El símbolo es letra proposicional")
			pila.append(Tree(c, None, None))
		elif c == '-':
			# print("Negamos")
			formulaAux = Tree(c, None, pila[-1])
			del pila[-1]
			pila.append(formulaAux)
		elif c in conectivos:
			# print("Unimos mediante conectivo")
			formulaAux = Tree(c, pila[-1], pila[-2])
			del pila[-1]
			del pila[-1]
			pila.append(formulaAux)
		else:
			print(u"Hay un problema: el símbolo " + str(c) + " no se reconoce")
	return pila[-1]

def Inorder2Tree(A):
	if len(A) == 1:
		return Tree(A[0], None, None)
	elif A[0] == '-':
		return Tree(A[0], None, Inorder2Tree(A[1:]))
	elif A[0] == "(":
		counter = 0 #Contador de parentesis
		for i in range(1, len(A)):
			if A[i] == "(":
				counter += 1
			elif A[i] == ")":
				counter -=1
			elif (A[i] in ['Y', 'O', '>', '=']) and (counter == 0):
				return Tree(A[i], Inorder2Tree(A[1:i]), Inorder2Tree(A[i + 1:-1]))
	else:
		return -1

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

def imprime_listaHojas(L):
	for h in L:
		print(imprime_hoja(h))

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

print("PAR COMPLEMENTARIO\n")
print(par_complementario(l1))
print(par_complementario(l2))
print(par_complementario(l3))
print(par_complementario(l4), "\n")

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

print("ES LITERAL\n")
l5 = Tree('-',None,Tree('p',None,None))
l6 = Tree('-',None,Tree('Y',Tree('p',None,None),Tree('q',None,None)))
l7 = Tree('alpha',None,None)
l8 = Tree('O',Tree('k',None,None),Tree('Y',Tree('i',None,None),Tree('j',None,None)))
A =  Tree('-',None,Tree('-',None,Tree('p',None,None)))

print(es_literal(l5))
print(es_literal(l6))
print(es_literal(l7))
print(es_literal(A))
print(es_literal(l8), "\n")

def no_literales(l):
	# Esta función determina si una lista de fórmulas contiene
	# solo literales
	# Input: l, una lista de fórmulas como árboles
	# Output: None/f, tal que f no es literales
    x = True
    for i in l:
        if (es_literal(i) == True):
            x = False
        else:
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
    
    if es_literal(f) == False:
    #REGLAS ALFA
    
        if f.label == '-':
           if f.right.label == '-':
                  return '1ALFA'
           elif f.right.label == 'O':
                  return '3ALFA'
           elif f.right.label == '>':
                  return '4ALFA'
        elif f.label == 'Y':
            return '2ALFA'
        
        #REGLAS BETA
        
        if f.label == '-':
            if f.right.label == 'Y':
                return '1BETA'
        elif f.label == 'O':
            return '2BETA'
        elif f.label == '>':
            return '3BETA'
    else:
        return 'ERROR EN LA CLASIFICACIÓN'

print("CLASIFICACIÓN\n")
A1 = Tree('-',None,Tree('O',Tree('>',Tree('m',None,None),Tree('n',None,None)),Tree('-',None,Tree('l',None,None))))
A2 = Tree('-',None,Tree('pq>',None,None))
A3 = Tree('Y',Tree('>',Tree('x',None,None),Tree('z',None,None)),Tree('O',Tree('-',None,Tree('w',None,None)),Tree('-',None,Tree('y',None,None))))
A4 = Tree('O',Tree('-',None,Tree('s',None,None)),Tree('Y',Tree('t',None,None),Tree('>',Tree('u',None,None),Tree('v',None,None))))
A5 = Tree('-',None,Tree('>',Tree('-',None,Tree('1',None,None)),Tree('Y',Tree('-',None,Tree('3',None,None)),Tree('2',None,None))))
A6 = Tree('-',None,Tree('Y',Tree('-',None,Tree('a',None,None)),Tree('-',None,Tree('b',None,None))))
A7 = Tree('-',None,Tree('-',None,Tree('-',None,Tree('O',Tree('p',None,None),Tree('q',None,None)))))
A8 = Tree('>',Tree('Y',Tree('p',None,None),Tree('>',Tree('p',None,None),Tree('q',None,None))),Tree('q',None,None))

print(clasificacion(A1))
print(clasificacion(A2))
print(clasificacion(A3))
print(clasificacion(A4))
print(clasificacion(A5))
print(clasificacion(A6))
print(clasificacion(A7))
print(clasificacion(A8), "\n")

# def clasifica_y_extiende(f, h):
# 	# Extiende listaHojas de acuerdo a la regla respectiva
# 	# Input: f, una fórmula como árbol
# 	# 		 h, una hoja (lista de fórmulas como árboles)
# 	# Output: no tiene output, pues modifica la variable global listaHojas

# 	global listaHojas

# 	print("Formula:", Inorder(f))
# 	print("Hoja:", imprime_hoja(h))

# 	assert(f in h), "La formula no esta en la lista!"

# 	clase = clasificacion(f)
# 	print("Clasificada como:", clase)
# 	assert(clase != None), "Formula incorrecta " + imprime_hoja(h)

# 	if clase == 'Alfa1':
# 		aux = [x for x in h if x != f] + [f.right.right]
# 		listaHojas.remove(h)
# 		listaHojas.append(aux)
# 	elif clase == 'Alfa2':
# 		pass
# 	# Aqui el resto de casos

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

    if clase == 'ALFA1':
        aux = [x for x in h]
        listaHojas.remove(h)
        aux.remove(f)
        aux += [f.right.right]
        listaHojas.append(aux)
        
    elif clase == 'ALFA2':
        aux = [x for x in h]
        listaHojas.remove(h)
        aux.remove(f)
        aux += [f.right , f.left]
        listaHojas.append(aux)
        
    elif clase == 'ALFA3':
        aux = [x for x in h]
        listaHojas.remove(h)
        aux.remove(f)
        aux += [Tree('-',None,f.right.right), Tree('-',None, f.right.left)]
        listaHojas.append(aux)
        
    elif clase == 'ALFA4':
        aux = [x for x in h]
        listaHojas.remove(h)
        aux.remove(f)
        aux += [f.right.right, Tree('-',None, f.right.left)]
        listaHojas.append(aux)
	
    elif clase == 'BETA1':
        aux = [x for x in h]
        listaHojas.remove(h)
        aux.remove(f)
        listaHojas.append([Tree('-',None,f.right.right)])
        listaHojas.append([Tree('-',None, f.right.left)])
        
    elif clase == 'BETA2':
        aux = [x for x in h]
        listaHojas.remove(h)
        aux.remove(f)
        listaHojas.append([f.right]) 
        listaHojas.append([f.left])
        
    elif clase == 'BETA3':
        aux = [x for x in h]
        listaHojas.remove(h)
        aux.remove(f)
        listaHojas.append([Tree('-',None,f.right.right)])
        listaHojas.append([f.right.left])


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

	while (len(listaHojas) > 0):
		h = choice(listaHojas)
		print("Trabajando con hoja:\n", imprime_hoja(h))
		x = no_literales(h)
		if x == None:
			if par_complementario(h):
				listaHojas.remove(h)
			else:
				listaInterpsVerdaderas.append(h)
				listaHojas.remove(h)
		else:
			clasifica_y_extiende(x, h)

	return listaInterpsVerdaderas
