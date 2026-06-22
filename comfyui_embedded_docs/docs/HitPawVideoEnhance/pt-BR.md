# HitPaw Video Enhance

Esta documentação foi gerada por IA. Se você encontrar algum erro ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HitPawVideoEnhance/en.md)

O nó HitPaw Video Enhance utiliza uma API externa para melhorar a qualidade de vídeos. Ele aumenta a resolução de vídeos de baixa qualidade para uma resolução superior, remove artefatos visuais e reduz ruídos. O custo do processamento é calculado por segundo do vídeo de entrada.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `modelo` | O modelo de IA a ser usado para aprimoramento de vídeo. Selecionar um modelo revela um parâmetro `resolution` aninhado. Os modelos disponíveis e suas resoluções suportadas variam. | DYNAMIC COMBO | Sim | Múltiplas opções disponíveis |
| `model.resolution` | A resolução alvo para o vídeo aprimorado. Algumas opções podem não estar disponíveis dependendo do `modelo` selecionado. | COMBO | Sim | `"original"`<br>`"720p"`<br>`"1080p"`<br>`"2k/qhd"`<br>`"4k/uhd"`<br>`"8k"` |
| `vídeo` | O arquivo de vídeo de entrada a ser aprimorado. | VIDEO | Sim | N/A |

**Restrições:**

* O `video` de entrada deve ter duração entre 0,5 segundos e 60 minutos (3600 segundos).
* A `resolution` selecionada deve ser maior que as dimensões do vídeo de entrada. Se o vídeo for quadrado, a resolução selecionada deve ser maior que sua largura/altura. Para vídeos não quadrados, a resolução selecionada deve ser maior que a dimensão mais curta do vídeo. Se a resolução alvo for menor, um erro será gerado. Escolha `"original"` para manter a resolução do vídeo de entrada.

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `vídeo` | O arquivo de vídeo aprimorado. | VIDEO |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HitPawVideoEnhance/pt-BR.md)

---
**Source fingerprint (SHA-256):** `0f329cbf61784474ee5b97a92d28a3e2383dc40e208f8a8317f3c4f60b43e5b2`
