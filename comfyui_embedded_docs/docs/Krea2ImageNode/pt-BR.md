# Krea 2 Imagem

Esta documentação foi gerada por IA. Se você encontrar algum erro ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Krea2ImageNode/en.md)

## Visão Geral

O nó Krea 2 Image gera imagens utilizando o modelo de IA Krea 2. Ele suporta duas variantes do modelo: Medium para ilustrações expressivas e Large para fotorrealismo expressivo. Opcionalmente, você pode incluir um moodboard e até 10 referências de estilo de imagem para influenciar a imagem gerada.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `prompt` | Prompt de texto para a imagem. | STRING | Sim | N/A |
| `modelo` | Krea 2 Medium é ideal para ilustrações expressivas; Krea 2 Large é ideal para fotorrealismo expressivo. | DICT | Sim | Veja abaixo |
| `semente` | Semente aleatória para reprodutibilidade (padrão: 0). | INT | Sim | 0 a 2147483647 |

O parâmetro `model` é um dicionário com os seguintes subparâmetros:

| Subparâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `modelo` | Seleciona a variante do modelo Krea 2. | STRING | Sim | `"krea 2 medium"`<br>`"krea 2 large"` |
| `aspect_ratio` | A proporção de aspecto para a imagem gerada. | STRING | Sim | N/A |
| `resolution` | A resolução para a imagem gerada. | STRING | Sim | N/A |
| `creativity` | Controla o nível de criatividade da geração. | FLOAT | Sim | N/A |
| `moodboard_id` | O UUID de um moodboard do Krea para influenciar a imagem. Deve ser um UUID válido. | STRING | Não | N/A |
| `moodboard_strength` | A intensidade da influência do moodboard (padrão: 0,35). | FLOAT | Não | N/A |
| `style_reference` | Uma lista de referências de estilo de imagem. Cada referência deve ter uma `url` (STRING) e `strength` (FLOAT). | LIST | Não | 0 a 10 itens |

**Restrições:**
- `moodboard_id` deve ser um UUID válido (ex.: `"123e4567-e89b-12d3-a456-426614174000"`). Copie-o do site do Krea.
- `style_reference` aceita no máximo 10 referências de estilo de imagem.
- O `prompt` deve ter pelo menos 1 caractere.

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `image` | A imagem gerada como um tensor. | IMAGE |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Krea2ImageNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `6aeb2d935ef5df5699a19271c9ceb766892ef4b0e4f67bfa540bf12ffadf362d`
