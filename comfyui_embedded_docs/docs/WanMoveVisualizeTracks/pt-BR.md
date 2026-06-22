# WanMoveVisualizeTracks

O nó WanMoveVisualizeTracks sobrepõe dados de rastreamento de movimento em uma sequência de imagens ou quadros de vídeo. Ele desenha representações visuais dos pontos rastreados, incluindo seus caminhos de movimento e posições atuais, tornando os dados de movimento visíveis e mais fáceis de analisar.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `imagens` | A sequência de imagens de entrada ou quadros de vídeo para visualizar os rastros. | IMAGE | Sim | - |
| `trilhas` | Os dados de rastreamento de movimento contendo caminhos de pontos e informações de visibilidade. Se não for fornecido, as imagens de entrada são retornadas sem alterações. | TRACKS | Não | - |
| `resolução_da_linha` | O número de quadros anteriores a serem usados ao desenhar a linha de trajetória para cada rastro (padrão: 24). | INT | Sim | 1 - 1024 |
| `tamanho_do_círculo` | O tamanho do círculo desenhado na posição atual de cada rastro (padrão: 12). | INT | Sim | 1 - 128 |
| `opacidade` | A opacidade das sobreposições de rastro desenhadas (padrão: 0,75). | FLOAT | Sim | 0.0 - 1.0 |
| `largura_da_linha` | A largura das linhas usadas para desenhar os caminhos dos rastros (padrão: 16). | INT | Sim | 1 - 128 |

**Nota:** Se o número de imagens de entrada não corresponder ao número de quadros nos dados de `tracks` fornecidos, a sequência de imagens será repetida para corresponder ao comprimento dos rastros.

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `IMAGE` | A sequência de imagens com os dados de rastreamento de movimento visualizados como sobreposições. Se nenhum `trilhas` for fornecido, as imagens de entrada originais são retornadas. | IMAGE |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanMoveVisualizeTracks/pt-BR.md)

---
**Source fingerprint (SHA-256):** `b32169a8c9d3a2dd74463c81f6bd7d9a4bc66486af156843f32b0874f0eaeb8f`
