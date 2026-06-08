Este nó gera imagens de forma síncrona usando o modelo Stable Diffusion 3.5 da Stability AI. Ele cria imagens com base em prompts de texto e também pode modificar imagens existentes quando fornecidas como entrada. O nó suporta várias proporções de aspecto e predefinições de estilo para personalizar a saída.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `prompt` | O que você deseja ver na imagem de saída. Um prompt forte e descritivo que defina claramente elementos, cores e assuntos levará a melhores resultados. (padrão: string vazia) | STRING | Sim | - |
| `model` | O modelo Stable Diffusion 3.5 a ser usado para geração. | COMBO | Sim | `sd3.5-large`<br>`sd3.5-large-turbo`<br>`sd3.5-medium` |
| `proporção` | Proporção de aspecto da imagem gerada. (padrão: 1:1) | COMBO | Sim | `16:9`<br>`1:1`<br>`21:9`<br>`2:3`<br>`3:2`<br>`4:5`<br>`5:4`<br>`9:16`<br>`9:21` |
| `estilo predefinido` | Estilo desejado opcional da imagem gerada. Selecione "None" para nenhuma predefinição de estilo. | COMBO | Não | `3d-model`<br>`analog-film`<br>`anime`<br>`cinematic`<br>`comic-book`<br>`digital-art`<br>`enhance`<br>`fantasy-art`<br>`isometric`<br>`line-art`<br>`low-poly`<br>`modeling-compound`<br>`neon-punk`<br>`origami`<br>`photographic`<br>`pixel-art`<br>`tile-texture`<br>`None` |
| `cfg_scale` | O quão estritamente o processo de difusão adere ao texto do prompt (valores mais altos mantêm sua imagem mais próxima do prompt). (padrão: 4.0) | FLOAT | Sim | 1.0 a 10.0 |
| `semente` | A semente aleatória usada para criar o ruído. (padrão: 0) | INT | Sim | 0 a 4294967294 |
| `imagem` | Imagem de entrada opcional para geração imagem-para-imagem. Quando fornecida, o nó alterna para o modo imagem-para-imagem e o parâmetro `proporção` é ignorado. | IMAGE | Não | - |
| `prompt negativo` | Palavras-chave do que você não deseja ver na imagem de saída. Este é um recurso avançado. (padrão: string vazia) | STRING | Não | - |
| `redução de ruído da imagem` | Redução de ruído da imagem de entrada; 0.0 produz uma imagem idêntica à entrada, 1.0 é como se nenhuma imagem tivesse sido fornecida. (padrão: 0.5) Este parâmetro é usado apenas quando uma `imagem` é fornecida. | FLOAT | Não | 0.0 a 1.0 |

**Nota:** Quando uma `image` é fornecida, o nó alterna para o modo de geração imagem-para-imagem e o parâmetro `aspect_ratio` é determinado automaticamente a partir da imagem de entrada. Quando nenhuma `image` é fornecida, o parâmetro `image_denoise` é ignorado.

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `imagem` | A imagem gerada ou modificada. | IMAGE |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StabilityStableImageSD_3_5Node/pt-BR.md)

---
**Source fingerprint (SHA-256):** `80dbb27f19bb3286ee988f020f7f65623a73d7cac77ca0cdfc7a428254102aa3`
