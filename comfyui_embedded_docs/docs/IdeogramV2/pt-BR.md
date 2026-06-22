# Ideogram V2

O nó Ideogram V2 gera imagens usando o modelo de IA Ideogram V2. Ele recebe prompts de texto e várias configurações de geração para criar imagens por meio de um serviço de API. O nó suporta diferentes proporções de aspecto, resoluções e opções de estilo para personalizar as imagens geradas.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `prompt` | Prompt para a geração da imagem (padrão: string vazia) | STRING | Sim | - |
| `turbo` | Se deve usar o modo turbo (geração mais rápida, qualidade potencialmente inferior) (padrão: False) | BOOLEAN | Não | - |
| `aspect_ratio` | A proporção de aspecto para a geração da imagem. Ignorado se a resolução não estiver definida como AUTO. (padrão: "1:1") | COMBO | Não | "1:1"<br>"16:9"<br>"9:16"<br>"4:3"<br>"3:4"<br>"3:2"<br>"2:3" |
| `resolution` | A resolução para a geração da imagem. Se não estiver definida como AUTO, substitui a configuração de `aspect_ratio`. (padrão: "Auto") | COMBO | Não | "Auto"<br>"1024x1024"<br>"1152x896"<br>"896x1152"<br>"1216x832"<br>"832x1216"<br>"1344x768"<br>"768x1344"<br>"1536x640"<br>"640x1536" |
| `magic_prompt_option` | Determina se o MagicPrompt deve ser usado na geração (padrão: "AUTO") | COMBO | Não | "AUTO"<br>"ON"<br>"OFF" |
| `seed` | Semente aleatória para a geração (padrão: 0) | INT | Não | 0-2147483647 |
| `style_type` | Tipo de estilo para a geração (apenas V2) (padrão: "NONE") | COMBO | Não | "AUTO"<br>"GENERAL"<br>"REALISTIC"<br>"DESIGN"<br>"RENDER_3D"<br>"ANIME" |
| `negative_prompt` | Descrição do que deve ser excluído da imagem (padrão: string vazia) | STRING | Não | - |
| `num_images` | Número de imagens a serem geradas (padrão: 1) | INT | Não | 1-8 |

**Observação:** Quando `resolution` não está definido como "Auto", ele substitui a configuração de `aspect_ratio`. O parâmetro `num_images` tem um limite máximo de 8 imagens por geração.

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `output` | A(s) imagem(ns) gerada(s) pelo modelo Ideogram V2 | IMAGE |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/IdeogramV2/pt-BR.md)

---
**Source fingerprint (SHA-256):** `c0ba21cb62ad75212c960e2bf6730a39c6479c7389a58c50968c66cc8964f5e3`
