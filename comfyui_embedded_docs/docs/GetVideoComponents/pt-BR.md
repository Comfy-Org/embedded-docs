O nó **Get Video Components** extrai todos os elementos principais de um arquivo de vídeo. Ele separa o vídeo em quadros individuais, extrai a trilha de áudio e fornece as informações de taxa de quadros do vídeo. Isso permite que você trabalhe com cada componente de forma independente para processamento ou análise posterior.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `vídeo` | O vídeo do qual extrair os componentes. | VIDEO | Sim | - |

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `images` | Os quadros individuais extraídos do vídeo como imagens separadas. | IMAGE |
| `audio` | A trilha de áudio extraída do vídeo. | AUDIO |
| `fps` | A taxa de quadros do vídeo em quadros por segundo. | FLOAT |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GetVideoComponents/pt-BR.md)

---
**Source fingerprint (SHA-256):** `7b8419d6614d5be0ec15ccfeb48ee9813c74b28b0b405d62c03496c133c92f53`
