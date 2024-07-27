# FlyFood
## Descrição do projeto
Estamos no ano de 2025 e o trânsito está caótico. As empresas de delivery não conseguem fazer entregas em tempo aceitável, e o custo com entregadores está alto devido à valorização da mão-de-obra humana. Para resolver esse problema, um ex-aluno do BSI-UFRPE criou a FlyFood, uma empresa de entregas utilizando drones.

Esses drones podem receber uma rota de entregas e executá-la precisamente, otimizando o tempo de entrega. No entanto, a capacidade das baterias dos drones ainda é um desafio. Por isso, é crucial otimizar ao máximo o trajeto do drone para concluir todas as entregas dentro do ciclo da bateria.

## Objetivo
Desenvolver um algoritmo de roteamento que defina o menor trajeto para a realização de todas as entregas do drone. Para simplificar, trabalhamos com uma matriz que representa os pontos da cidade.

## Formato da Matriz
A matriz representa os pontos da cidade onde:

- O ponto superior esquerdo é o (0,0).
- R é o ponto de origem e retorno do drone.
- 0 indica um ponto sem entrega.
- A, B, C, etc., são pontos de entrega.

Por exemplo:

4 5

0 | 0 | 0 | 0 | D

0 | A | 0 | 0 | 0

0 | 0 | 0 | 0 | C

R | 0 | B | 0 | 0

Neste exemplo:

A está em (1,1)

B está em (3,2)

C está em (2,4)

D está em (0,4)

R está em (3,0), que é o ponto de origem e retorno do drone.
## Requisitos
O drone só pode percorrer a matriz na horizontal ou vertical (não na diagonal). O objetivo é determinar a ordem dos pontos de entrega que minimize a distância total percorrida pelo drone.

## Resultados
O script irá ler a matriz do arquivo, calcular o menor percurso para o drone realizar todas as entregas e retornar ao ponto de origem, e imprimir o resultado no terminal.

