#!/usr/bin/env python
# Four spaces as indentation [no tabs]
import sys
import Queue

import ppretty as ppretty

from common import *


# ==========================================
# PathFinder A Star
# ==========================================

class PathFinder_A_Star:
    def __init__(self):
        # TODO initialize your attributes here if needed
        self.solvable = False
        self.lista_solucao = []
        self.dicionario = {}
        pass

    class Nodo:
        def __init__(self, x, y, distancia):
            self.x = x
            self.y = y
            self.distancia = distancia

        def __str__(self):
            return "x:" + str(self.x) + ", y:" + str(self.y) + ", dist:" + str(self.distancia)

    # ------------------------------------------
    # Cost
    # ------------------------------------------

    def chave_dicionario(self, x, y):
        return str(x) + ',' + str(y)

    def menor_caminho(self, map, lista_sucessores):
        # TODO priority function to use with the PriorityQueue
        # You are free not to use this function
        # (it is not tested in the unit test)
        limite = map.width + map.height
        nodo_menor_caminho = self.Nodo(0, 0, limite)
        pos_nodo_menor_caminho = 0
        cont = 0
        for l in lista_sucessores:
            # if not self.chave_dicionario(l.x, l.y) in self.dicionario:
            status_nodo_atual = l
            # if status_nodo_atual != -1:
            if status_nodo_atual.distancia < nodo_menor_caminho.distancia:
                nodo_menor_caminho = l
                print("escolhido " + str(nodo_menor_caminho))
                pos_nodo_menor_caminho = cont
            else:
                lista_sucessores.pop(cont)
            cont += 1

        # if len(lista_sucessores) != 0:
        lista_sucessores.pop(pos_nodo_menor_caminho)
        # print ("nodo_menor_caminho",nodo_menor_caminho.x, nodo_menor_caminho.y, nodo_menor_caminho.distancia)
        return nodo_menor_caminho

    # ------------------------------------------
    # Heuristic
    # ------------------------------------------

    def heuristica(self, map, x_atual, y_atual):
        # TODO heuristic function
        # You are free not to use this function
        # (it is not graded in the unit test)
        data = map.data
        distancia = 0
        status_pos = data[y_atual][x_atual]
        if status_pos == 1:
            distancia = -1  # caso seja um local inacessivel (TILE_CLOSED), o campo nao possui distancia pro destino
        elif status_pos == 0:
            distancia = abs(map.goal.y - y_atual) + abs(map.goal.x - x_atual)
        nodo = self.Nodo(x_atual, y_atual, distancia)

        # print("heuristica ------------------> x:" + str(x_atual) +", y:"+ str(y_atual) + ", dist:" + str(nodo.distancia))

        return nodo

    # ------------------------------------------
    # Solve
    # ------------------------------------------

    def solve(self, map):
        # TODO returns a list of movements (may be empty) 
        # if plan found, otherwise return None
        print("Nodo inicial " + str(map.start.x) + ", "+ str(map.start.y))
        nodo = self.heuristica(map, map.start.x, map.start.y)
        lista_coordenadas = []

        if nodo.distancia == 0:
            self.solvable = True
        else:
            lista_coordenadas = self.procura_caminho(map, nodo, self.Nodo(-1, -1, -1), lista_coordenadas)

        print("\nResposta:")
        for n in lista_coordenadas:
            print ("nodo_menor_caminho", n.x, n.y, n.distancia)
        return self.transforma_coordenadas_em_movimento(map, lista_coordenadas)

    # ------------------------------------------
    # Percorre os caminhos, procurando o melhor
    # ------------------------------------------
    def procura_caminho(self, map, nodo_atual, nodo_pai, lista_coordenadas):
        # self.dicionario[self.chave_dicionario(nodo.x, nodo.y)] = nodo.distancia
        lista_coordenadas.append(nodo_atual)
        lista_sucessores = map.successors(nodo_atual.x, nodo_atual.y)
        lista_sucessores_com_heuristica = []

        print "lista coordenadas"
        for l in lista_coordenadas:
            print (str(l))

        if nodo_atual.distancia == 0:
            return lista_coordenadas

        if len(lista_sucessores) != 0:
            for l in lista_sucessores:
                if not self.chave_dicionario(l.x, l.y) in self.dicionario and l.x != nodo_pai.x and l.y != nodo_pai.y:
                    menor_caminho = self.heuristica(map, l.x, l.y)
                    lista_sucessores_com_heuristica.append(menor_caminho)
                else:
                    lista_sucessores.remove(l)
                    continue

            while len(lista_sucessores_com_heuristica) != 0:
                print ("sucessores: ")
                for l in lista_sucessores_com_heuristica:
                    print ("x:" + str(l.x) + ", y:" + str(l.y) + " dist:"+ str(l.distancia))
                menor_caminho = self.menor_caminho(map, lista_sucessores_com_heuristica)
                print "menor caminho: x:" + str(menor_caminho.x) + ", y:" + str(menor_caminho.y) + " dist:" + str(menor_caminho.distancia)
                return self.procura_caminho(map, menor_caminho, nodo_atual, lista_coordenadas)
        else:
            self.dicionario[(self.chave_dicionario(nodo_atual.x, nodo_atual.y))] = nodo_atual.distancia
            lista_coordenadas.remove(nodo_atual)
        return
        # ////////////////////////////////////////////////////////////////////////////////////////


        # print("dicionario")
        # for k in self.dicionario.items():
        #     print(k)

        # if len(lista_sucessores) == 0:
        #     lista_coordenadas.remove(nodo)
        #     # if not len(self.dicionario) != 0:
        #     self.dicionario.pop[(self.chave_dicionario(nodo.x, nodo.y))] = nodo.distancia
        #     return
        #
        # if nodo.distancia == 0:
        #     self.solvable = True
        #     return lista_coordenadas
        #
        # for l in lista_sucessores:
        #     menor_caminho = self.heuristica(map, l.x, l.y)
        #     lista_sucessores_com_heuristica.append(menor_caminho)
        #
        # while len(lista_sucessores_com_heuristica) != 0:
        #
        #     menor_caminho = self.menor_caminho(map, lista_sucessores_com_heuristica)
        #
        #     # if not self.chave_dicionario(menor_caminho.x, menor_caminho.y) in self.dicionario:
        #     lista_coordenadas.append(menor_caminho)
        #     self.dicionario[self.chave_dicionario(menor_caminho.x, menor_caminho.y)] = menor_caminho.distancia
        #     return self.procura_caminho(map, menor_caminho, lista_coordenadas)
        #     # else:
        #     #     continue
        # return

    def transforma_coordenadas_em_movimento(self, map, lista_coordenadas):
        lista_movimentos = []
        for l in lista_coordenadas:
            if l.x == map.start.x:
                if (map.start.y - l.y) > 0:
                    lista_movimentos.append(MOVE_UP)
                else:
                    lista_movimentos.append(MOVE_DOWN)
            else:
                if (map.start.x - l.x) > 0:
                    lista_movimentos.append(MOVE_LEFT)
                else:
                    lista_movimentos.append(MOVE_RIGHT)

        print lista_movimentos.__str__()
        return lista_movimentos

    # ------------------------------------------
    # Get solvable
    # ------------------------------------------

    def get_solvable(self, map):
        # TODO returns True if plan found, 
        # otherwise returns False
        return self.solvable

    # ------------------------------------------
    # Get max tree height
    # ------------------------------------------

    def get_max_tree_height(self, map):
        # TODO returns max tree height if plan found, 
        # otherwise, returns None
        return None

    # ------------------------------------------
    # Get min moves
    # ------------------------------------------

    def get_min_moves(self, map):
        # TODO returns size of minimal plan to reach goal if plan found, 
        # otherwise returns None
        return None


# ------------------------------------------
# Main
# ------------------------------------------

if __name__ == '__main__':
    if len(sys.argv) == 2:
        map_name = sys.argv[1]
    else:
        map_name = DEFAULT_MAP
    print "Loading map: " + map_name
    plan = PathFinder_A_Star().solve(read_map(map_name))
    if plan == None:
        print "No plan was found"
    else:
        print "Plan found:"
        for i, move in enumerate(plan):
            if move == MOVE_UP:
                print i, ": Move Up"
            elif move == MOVE_DOWN:
                print i, ": Move Down"
            elif move == MOVE_LEFT:
                print i, ": Move Left"
            elif move == MOVE_RIGHT:
                print i, ": Move Right"
            else:
                print i, ": Movement unknown = ", move
