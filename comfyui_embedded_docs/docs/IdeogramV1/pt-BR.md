# Ideogram V1

Esta documentação foi gerada por IA. Se encontrar algum erro ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/IdeogramV1/en.md)

O nó IdeogramV1 gera imagens usando o modelo Ideogram V1 por meio de uma API. Ele recebe prompts de texto e várias configurações de geração para criar uma ou mais imagens com base na sua entrada. O nó suporta diferentes proporções de aspecto e modos de geração para personalizar a saída.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `prompt` | Prompt para a geração da imagem (padrão: vazio) | STRING | Sim | - |
| `turbo` | Se deve usar o modo turbo (geração mais rápida, qualidade potencialmente inferior) (padrão: False) | BOOLEAN | Sim | - |
| `aspect_ratio` | A proporção de aspecto para a geração da imagem (padrão: "1:1") | COMBO | Não | "1:1"<br>"16:9"<br>"9:16"<br>"4:3"<br>"3:4"<br>"3:2"<br>"2:3" |
| `magic_prompt_option` | Determina se o MagicPrompt deve ser usado na geração (padrão: "AUTO") | COMBO | Não | "AUTO"<br>"ON"<br>"OFF" |
| `seed` | Valor de semente aleatório para a geração (padrão: 0) | INT | Não | 0-2147483647 |
| `negative_prompt` | Descrição do que deve ser excluído da imagem (padrão: vazio) | STRING | Não | - |
| `num_images` | Número de imagens a serem geradas (padrão: 1) | INT | Não | 1-8 |

**Nota:** O parâmetro `num_images` tem um limite máximo de 8 imagens por solicitação de geração.

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `output` | A(s) imagem(ns) gerada(s) pelo modelo Ideogram V1 | IMAGE |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/IdeogramV1/pt-BR.md)

---
**Source fingerprint (SHA-256):** `7e453cd54b5db48588ed899b0754e0d06fdcfbaed248d13fb74b7049f0f25b8f`
