> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanMoveTracksFromCoords/pt-BR.md)

O nó WanMoveTracksFromCoords cria um conjunto de trilhas de movimento a partir de uma lista de pontos de coordenadas. Ele converte uma string formatada em JSON de coordenadas em um formato de tensor que pode ser usado por outros nós de processamento de vídeo e pode, opcionalmente, aplicar uma máscara para controlar a visibilidade das trilhas ao longo do tempo.

## Entradas

| Parâmetro | Tipo de Dados | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `track_coords` | STRING | Sim | N/A | Uma string formatada em JSON contendo os dados de coordenadas para as trilhas. O valor padrão é uma lista vazia (`"[]"`). |
| `track_mask` | MASK | Não | N/A | Uma máscara opcional. Quando fornecida, o nó a utiliza para determinar a visibilidade de cada trilha por quadro. |

**Observação:** A entrada `track_coords` espera uma estrutura JSON específica. Deve ser uma lista de trilhas, onde cada trilha é uma lista de quadros, e cada quadro é um objeto com as coordenadas `x` e `y`. O número de quadros deve ser consistente em todas as trilhas.

## Saídas

| Nome da Saída | Tipo de Dados | Descrição |
|-------------|-----------|-------------|
| `tracks` | TRACKS | Os dados de trilha gerados, contendo as coordenadas do caminho e as informações de visibilidade para cada trilha. |
| `track_length` | INT | O número total de quadros nas trilhas geradas. |
