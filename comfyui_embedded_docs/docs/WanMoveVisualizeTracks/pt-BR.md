# WanMoveVisualizeTracks

O nó WanMoveVisualizeTracks desenha dados de rastreamento de movimento em uma sequência de imagens ou quadros de vídeo. Ele coloca um círculo na posição atual de cada ponto rastreado e desenha uma linha de trajetória com desvanecimento mostrando para onde o ponto se moveu nos quadros recentes. Se nenhum dado de rastreamento for fornecido, as imagens de entrada são retornadas inalteradas.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `images` | A sequência de imagens de entrada ou quadros de vídeo nos quais os rastreamentos serão visualizados. | IMAGE | Sim | - |
| `tracks` | Os dados de rastreamento de movimento contendo posições dos pontos e informações de visibilidade. Se não for fornecido, as imagens de entrada passam inalteradas. | TRACKS | Não | - |
| `line_resolution` | O número de quadros anteriores a ser usado ao desenhar a linha de trajetória para cada rastreamento (padrão: 24). | INT | Sim | 1 - 1024 |
| `circle_size` | O tamanho do círculo desenhado na posição atual de cada ponto rastreado (padrão: 12). | INT | Sim | 1 - 128 |
| `opacity` | A opacidade das sobreposições de rastreamento desenhadas (padrão: 0.75). | FLOAT | Sim | 0.0 - 1.0 |
| `line_width` | A largura das linhas usadas para desenhar os caminhos dos rastreamentos (padrão: 16). | INT | Sim | 1 - 128 |

**Nota:** Se o número de imagens de entrada não corresponder ao número de quadros nos dados de `tracks` fornecidos, a sequência de imagens de entrada é repetida para se alinhar aos dados de rastreamento.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `IMAGE` | A sequência de imagens com os dados de rastreamento de movimento desenhados como sobreposições. Se nenhum `tracks` for fornecido, as imagens de entrada originais são retornadas inalteradas. | IMAGE |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanMoveVisualizeTracks/pt-BR.md)

---
**Source fingerprint (SHA-256):** `d94bfde28dfdad682edcc81b1c63408f1352e0dbc94af4d043d750e8cd4c099b`
