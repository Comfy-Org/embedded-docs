> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanMoveVisualizeTracks/pt-BR.md)

O nó WanMoveVisualizeTracks sobrepõe dados de rastreamento de movimento a uma sequência de imagens ou quadros de vídeo. Ele desenha representações visuais dos pontos rastreados, incluindo seus caminhos de movimento e posições atuais, tornando os dados de movimento visíveis e mais fáceis de analisar.

## Entradas

| Parâmetro | Tipo de Dados | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `images` | IMAGE | Sim | - | A sequência de imagens de entrada ou quadros de vídeo sobre os quais visualizar os rastros. |
| `tracks` | TRACKS | Não | - | Os dados de rastreamento de movimento contendo caminhos de pontos e informações de visibilidade. Se não for fornecido, as imagens de entrada são passadas inalteradas. |
| `line_resolution` | INT | Sim | 1 - 1024 | O número de quadros anteriores a serem usados ao desenhar a linha do caminho de arrasto para cada rastro (padrão: 24). |
| `circle_size` | INT | Sim | 1 - 128 | O tamanho do círculo desenhado na posição atual de cada rastro (padrão: 12). |
| `opacity` | FLOAT | Sim | 0.0 - 1.0 | A opacidade das sobreposições de rastro desenhadas (padrão: 0.75). |
| `line_width` | INT | Sim | 1 - 128 | A largura das linhas usadas para desenhar os caminhos dos rastros (padrão: 16). |

**Observação:** Se o número de imagens de entrada não corresponder ao número de quadros nos dados de `tracks` fornecidos, a sequência de imagens será repetida para corresponder ao comprimento do rastro.

## Saídas

| Nome da Saída | Tipo de Dados | Descrição |
|-------------|-----------|-------------|
| `IMAGE` | IMAGE | A sequência de imagens com os dados de rastreamento de movimento visualizados como sobreposições. Se nenhum `tracks` foi fornecido, as imagens de entrada originais são retornadas. |
