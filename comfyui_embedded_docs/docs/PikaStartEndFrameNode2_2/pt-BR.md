> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PikaStartEndFrameNode2_2/pt-BR.md)

Esta documentação foi gerada por IA. Se você encontrar algum erro ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PikaStartEndFrameNode2_2/en.md)

O nó PikaFrames v2.2 gera um vídeo combinando seu primeiro e último quadro. Você carrega duas imagens para definir os pontos inicial e final, e a IA cria uma transição suave entre elas para produzir um vídeo completo.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Faixa | Descrição |
|-----------|--------------|-------------|-------|-----------|
| `image_start` | IMAGE | Sim | - | A primeira imagem a ser combinada. |
| `image_end` | IMAGE | Sim | - | A última imagem a ser combinada. |
| `prompt_text` | STRING | Sim | - | Prompt de texto descrevendo o conteúdo desejado do vídeo. |
| `negative_prompt` | STRING | Sim | - | Texto descrevendo o que evitar no vídeo. |
| `seed` | INT | Sim | - | Valor de semente aleatória para consistência na geração. |
| `resolution` | STRING | Sim | - | Resolução do vídeo de saída. |
| `duration` | INT | Sim | - | Duração do vídeo gerado. |

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|---------------|--------------|-----------|
| `output` | VIDEO | O vídeo gerado combinando os quadros inicial e final com transições de IA. |

---
**Source fingerprint (SHA-256):** `0a26f6db754c61d1f35e3fd9faceb631a8103ce9ff38190a5dd637991914e238`
