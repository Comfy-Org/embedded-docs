Esta documentação foi gerada por IA. Se você encontrar algum erro ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PikaStartEndFrameNode2_2/en.md)

O nó PikaFrames v2.2 gera um vídeo combinando seu primeiro e último quadro. Você carrega duas imagens para definir os pontos inicial e final, e a IA cria uma transição suave entre elas para produzir um vídeo completo.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `image_start` | A primeira imagem a ser combinada. | IMAGE | Sim | - |
| `image_end` | A última imagem a ser combinada. | IMAGE | Sim | - |
| `prompt_text` | Prompt de texto descrevendo o conteúdo desejado do vídeo. | STRING | Sim | - |
| `negative_prompt` | Texto descrevendo o que evitar no vídeo. | STRING | Sim | - |
| `seed` | Valor de semente aleatória para consistência na geração. | INT | Sim | - |
| `resolution` | Resolução do vídeo de saída. | STRING | Sim | - |
| `duration` | Duração do vídeo gerado. | INT | Sim | - |

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `output` | O vídeo gerado combinando os quadros inicial e final com transições de IA. | VIDEO |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PikaStartEndFrameNode2_2/pt-BR.md)

---
**Source fingerprint (SHA-256):** `0a26f6db754c61d1f35e3fd9faceb631a8103ce9ff38190a5dd637991914e238`
