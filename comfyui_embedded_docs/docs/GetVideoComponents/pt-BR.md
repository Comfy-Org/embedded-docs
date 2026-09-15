# Obter Componentes do Vídeo

O nó Get Video Components extrai todos os elementos principais de um arquivo de vídeo. Ele separa o vídeo em quadros individuais, extrai a faixa de áudio e fornece a taxa de quadros, a profundidade de bits e o espaço de cor do vídeo. Isso permite que você trabalhe com cada componente independentemente para processamento ou análise adicional.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `vídeo` | O vídeo do qual extrair os componentes. | VIDEO | Sim | - |

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `images` | Os quadros individuais extraídos do vídeo como imagens separadas. | IMAGE |
| `audio` | A faixa de áudio extraída do vídeo. | AUDIO |
| `fps` | A taxa de quadros do vídeo em quadros por segundo. | FLOAT |
| `bit_depth` | A profundidade de bits do vídeo. | COMBO |
| `color_space` | O espaço de cor do vídeo. | COMBO |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GetVideoComponents/pt-BR.md)

---
**Source fingerprint (SHA-256):** `b57dbf1120105885d17361f07ec96c078aac9ae9a84beb63319885df679e4f81`
