> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MoonvalleyImg2VideoNode/pt-BR.md)

Esta documentação foi gerada por IA. Se você encontrar algum erro ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MoonvalleyImg2VideoNode/en.md)

O nó Moonvalley Marey Image to Video transforma uma imagem de referência em um vídeo usando a API Moonvalley. Ele recebe uma imagem de entrada e um prompt de texto para gerar um vídeo com resolução, configurações de qualidade e controles criativos especificados. O nó gerencia todo o processo, desde o upload da imagem até a geração e o download do vídeo.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Faixa | Descrição |
|-----------|--------------|-------------|-------|-----------|
| `image` | IMAGE | Sim | - | A imagem de referência usada para gerar o vídeo |
| `prompt` | STRING | Sim | - | Descrição textual para a geração do vídeo (entrada multilinha) |
| `negative_prompt` | STRING | Não | - | Texto do prompt negativo para excluir elementos indesejados (padrão: lista extensa de prompts negativos) |
| `resolution` | COMBO | Não | "16:9 (1920 x 1080)"<br>"9:16 (1080 x 1920)"<br>"1:1 (1152 x 1152)"<br>"4:3 (1536 x 1152)"<br>"3:4 (1152 x 1536)" | Resolução do vídeo de saída (padrão: "16:9 (1920 x 1080)") |
| `prompt_adherence` | FLOAT | Não | 1.0 - 20.0 | Escala de orientação para controle de geração (padrão: 4.5, passo: 1.0) |
| `seed` | INT | Não | 0 - 4294967295 | Valor da semente aleatória (padrão: 9, controle após geração ativado) |
| `steps` | INT | Não | 1 - 100 | Número de etapas de remoção de ruído (padrão: 33, passo: 1) |

**Restrições:**

- A imagem de entrada deve ter dimensões entre 300x300 pixels e a altura/largura máxima permitida
- O comprimento do texto do prompt e do prompt negativo é limitado ao comprimento máximo de prompt do Moonvalley Marey

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|---------------|--------------|-----------|
| `output` | VIDEO | A saída do vídeo gerado |

---
**Source fingerprint (SHA-256):** `674e69a7f106f6f961f10c179008b7bb1147bf0e569c72d207a105f3fab2aaf5`
