# Integrantes

Eduardo Fonseca da Silva - 00577262 - Turma B  
Estevan Kuster - 00334328 - Turma B  
Pedro de Sene Bavaresco - 00333563 - Turma B  

# Tic-Tac-Toe misere

### (i) O minimax sempre ganha ou empata jogando contra o randomplayer?
Embora não constitua uma prova formal, foram realizadas 100 partidas, alternando a ordem dos jogadores (branco e preto). Os resultados foram:
- Empates: 35
- Vitórias do minimax: 65
- Vitórias do randomplayer: 0

Conclusão: O agente minimax nunca perdeu para o randomplayer, confirmando sua capacidade de, no mínimo, empatar contra esse oponente fraco.

### (ii) O minimax sempre empata consigo mesmo?
Sim. Em 100 partidas entre dois agentes minimax, todos os jogos terminaram em empate.

### (iii) O minimax não perde para você quando você usa a sua melhor estratégia?
Não. Foram realizados 5 jogos contra o minimax, e todos os jogos terminaram em empate.
Conclusão: O agente minimax não perdeu nenhuma partida, o que sugere desempenho ótimo no jogo Misère Tic-Tac-Toe.

# Othello

## Partidas do Mini-Torneio:
Foram realizadas partidas entre três heurísticas distintas:
- Contagem de peças: avalia o estado pelo número absoluto de discos do jogador.
- Valor posicional: utiliza uma matriz de pesos para avaliar posições estratégicas (bordas, cantos, etc.).
- Heurística customizada: combina os fatores de mobilidade, estabilidade e valor posicional.

### Contagem de peças X Valor posicional:

#### Contagem de peças (B) x Valor Posicional (W)
- Contagem de peças: 29
- Valor Posicional: 35
- VITÓRIA: Valor Posicional (W)

#### Valor Posicional (B) x Contagem de Peças (W)
- Valor Posicional: 24
- Contagem de peças: 40
- VITÓRIA: Valor Posicional (B)

### Contagem de peças X Heurística Customizada:

#### Contagem de peças (B) x Heurística Customizada (W)
- Contagem de peças: 30
- Heurística Customizada: 34
- VITÓRIA: Heurística Customizada (W)

#### Heurística Customizada (B) x Contagem de Peças (W)
- Heurística Customizada: 50
- Contagem de peças: 14
- VITÓRIA: Heurística Customizada (B)


### Valor Posicional X Heurística Customizada:

#### Valor Posicional (B) x Heurística Customizada (W)
- Valor Posicional: 29
- Heurística Customizada: 35
- VITÓRIA: Heurística Customizada (W)

#### Heurística Customizada (B) x Valor Posicional (W)
- Heurística Customizada: 46
- Valor Posicional: 18
- VITÓRIA: Heurística Customizada (B)


### Resultado
A heurística customizada venceu todas as partidas disputadas, destacando-se como a abordagem mais eficaz entre as avaliadas. Isso era esperado, uma vez que ela incorpora múltiplos aspectos estratégicos do jogo (mobilidade, estabilidade e valor posicional), em contraste com a simples contagem de peças, que se mostrou ineficaz e foi derrotada em todas as partidas.


## Referência
A implementação da heurística customizada foi inspirada parcialmente nas ideias descritas neste artigo:
[Jacky Choi, How to write an Othello AI with Alpha-Beta Search](https://medium.com/@jackychoi26/how-to-write-an-othello-ai-with-alpha-beta-search-58131ffe67eb)
