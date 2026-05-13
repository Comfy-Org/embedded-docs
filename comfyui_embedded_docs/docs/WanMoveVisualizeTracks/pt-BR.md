> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanMoveVisualizeTracks/pt-BR.md)

O nó WanMoveVisualizeTracks sobrepõe dados de rastreamento de movimento em uma sequência de imagens ou quadros de vídeo. Ele desenha representações visuais dos pontos rastreados, incluindo seus caminhos de movimento e posições atuais, tornando os dados de movimento visíveis e mais fáceis de analisar.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Faixa | Descrição |
|-----------|--------------|-------------|-------|-----------|
| `imagens` | IMAGE | Sim | - | A sequência de imagens de entrada ou quadros de vídeo para visualizar os rastros. |
| `trilhas` | TRACKS | Não | - | Os dados de rastreamento de movimento contendo caminhos de pontos e informações de visibilidade. Se não for fornecido, as imagens de entrada são retornadas sem alterações. |
| `resolução_da_linha` | INT | Sim | 1 - 1024 | O número de quadros anteriores a serem usados ao desenhar a linha de trajetória para cada rastro (padrão: 24). |
| `tamanho_do_círculo` | INT | Sim | 1 - 128 | O tamanho do círculo desenhado na posição atual de cada rastro (padrão: 12). |
| `opacidade` | FLOAT | Sim | 0.0 - 1.0 | A opacidade das sobreposições de rastro desenhadas (padrão: 0,75). |
| `largura_da_linha` | INT | Sim | 1 - 128 | A largura das linhas usadas para desenhar os caminhos dos rastros (padrão: 16). |

**Nota:** Se o número de imagens de entrada não corresponder ao número de quadros nos dados de `tracks` fornecidos, a sequência de imagens será repetida para corresponder ao comprimento dos rastros.

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|---------------|--------------|-----------|
| `IMAGE` | IMAGE | A sequência de imagens com os dados de rastreamento de movimento visualizados como sobreposições. Se nenhum `trilhas` for fornecido, as imagens de entrada originais são retornadas. |

---
**Source fingerprint (SHA-256):** `b32169a8c9d3a2dd74463c81f6bd7d9a4bc66486af156843f32b0874f0eaeb8f`
