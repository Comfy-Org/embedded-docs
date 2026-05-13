> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GetVideoComponents/pt-BR.md)

O nó **Get Video Components** extrai todos os elementos principais de um arquivo de vídeo. Ele separa o vídeo em quadros individuais, extrai a trilha de áudio e fornece as informações de taxa de quadros do vídeo. Isso permite que você trabalhe com cada componente de forma independente para processamento ou análise posterior.

## Entradas

| Parâmetro | Tipo de Dados | Obrigatório | Faixa | Descrição |
|-----------|---------------|-------------|-------|-----------|
| `vídeo` | VIDEO | Sim | - | O vídeo do qual extrair os componentes. |

## Saídas

| Nome da Saída | Tipo de Dados | Descrição |
|---------------|---------------|-----------|
| `images` | IMAGE | Os quadros individuais extraídos do vídeo como imagens separadas. |
| `audio` | AUDIO | A trilha de áudio extraída do vídeo. |
| `fps` | FLOAT | A taxa de quadros do vídeo em quadros por segundo. |

---
**Source fingerprint (SHA-256):** `7b8419d6614d5be0ec15ccfeb48ee9813c74b28b0b405d62c03496c133c92f53`
