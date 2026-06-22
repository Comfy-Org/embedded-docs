# MoonvalleyImg2VideoNode

Esta documentação foi gerada por IA. Se você encontrar algum erro ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MoonvalleyImg2VideoNode/en.md)

O nó Moonvalley Marey Image to Video transforma uma imagem de referência em um vídeo usando a API Moonvalley. Ele recebe uma imagem de entrada e um prompt de texto para gerar um vídeo com resolução, configurações de qualidade e controles criativos especificados. O nó gerencia todo o processo, desde o upload da imagem até a geração e o download do vídeo.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `image` | A imagem de referência usada para gerar o vídeo | IMAGE | Sim | - |
| `prompt` | Descrição textual para a geração do vídeo (entrada multilinha) | STRING | Sim | - |
| `negative_prompt` | Texto do prompt negativo para excluir elementos indesejados (padrão: lista extensa de prompts negativos) | STRING | Não | - |
| `resolution` | Resolução do vídeo de saída (padrão: "16:9 (1920 x 1080)") | COMBO | Não | "16:9 (1920 x 1080)"<br>"9:16 (1080 x 1920)"<br>"1:1 (1152 x 1152)"<br>"4:3 (1536 x 1152)"<br>"3:4 (1152 x 1536)" |
| `prompt_adherence` | Escala de orientação para controle de geração (padrão: 4.5, passo: 1.0) | FLOAT | Não | 1.0 - 20.0 |
| `seed` | Valor da semente aleatória (padrão: 9, controle após geração ativado) | INT | Não | 0 - 4294967295 |
| `steps` | Número de etapas de remoção de ruído (padrão: 33, passo: 1) | INT | Não | 1 - 100 |

**Restrições:**

- A imagem de entrada deve ter dimensões entre 300x300 pixels e a altura/largura máxima permitida
- O comprimento do texto do prompt e do prompt negativo é limitado ao comprimento máximo de prompt do Moonvalley Marey

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `output` | A saída do vídeo gerado | VIDEO |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MoonvalleyImg2VideoNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `674e69a7f106f6f961f10c179008b7bb1147bf0e569c72d207a105f3fab2aaf5`
