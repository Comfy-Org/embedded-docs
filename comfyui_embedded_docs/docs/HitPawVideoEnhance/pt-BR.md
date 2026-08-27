# HitPaw Video Enhance

## Entradas

### Entradas comuns

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `modelo` | O modelo de IA a ser usado para aprimoramento de vídeo. Selecionar um modelo revela um parâmetro `resolution` aninhado. Os modelos disponíveis e suas resoluções compatíveis variam. | DYNAMIC_COMBO | Sim | `"Portrait Restore Model (1x)"`<br>`"Portrait Restore Model (2x)"`<br>`"General Restore Model (1x)"`<br>`"General Restore Model (2x)"`<br>`"General Restore Model (4x)"`<br>`"Ultra HD Model (2x)"`<br>`"Generative Model (1x)"` |
| `vídeo` | O arquivo de vídeo de entrada a ser aprimorado. | VIDEO | Sim | N/A |

### Entradas do Portrait Restore, General Restore e Ultra HD Model

Essas opções de resolução são compartilhadas por Portrait Restore Model (1x), Portrait Restore Model (2x), General Restore Model (1x), General Restore Model (2x), General Restore Model (4x) e Ultra HD Model (2x).

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `resolução` | A resolução de destino do vídeo aprimorado. Selecionar `"original"` mantém a resolução do vídeo de entrada. | COMBO | Sim | `"original"`<br>`"720p"`<br>`"1080p"`<br>`"2K/QHD"`<br>`"4K/UHD"`<br>`"8K"` |

### Entradas do Generative Model (1x)

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `resolução` | A resolução de destino do vídeo aprimorado. Selecionar `"original"` mantém a resolução do vídeo de entrada. A opção `"8K"` não está disponível para este modelo. | COMBO | Sim | `"original"`<br>`"720p"`<br>`"1080p"`<br>`"2K/QHD"`<br>`"4K/UHD"` |

**Notas:**

* O `video` de entrada deve ter entre 0,5 segundo e 60 minutos (3600 segundos) de duração.
* A `resolution` selecionada deve ser pelo menos tão grande quanto as dimensões do vídeo de entrada. Para vídeos quadrados, ela deve ser pelo menos tão grande quanto a largura e a altura do vídeo. Para vídeos não quadrados, ela deve ser pelo menos tão grande quanto a menor dimensão do vídeo. Se a resolução de destino for menor, um erro é gerado. Selecionar `"original"` mantém a resolução do vídeo de entrada.
* Quando uma resolução diferente de `"original"` é selecionada, vídeos não quadrados são redimensionados de modo que sua menor dimensão corresponda à resolução selecionada, preservando a proporção. Vídeos quadrados são redimensionados de modo que ambas as dimensões correspondam ao tamanho quadrado de destino da resolução selecionada (por exemplo, `"4K/UHD"` produz 2048×2048).

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `video` | O arquivo de vídeo aprimorado. | VIDEO |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HitPawVideoEnhance/pt-BR.md)

---
**Source fingerprint (SHA-256):** `42803c7137d62dbce5021cd2bd9b9fba1a89c80e7b3f237f8a0eb03858c49967`
