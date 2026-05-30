> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Krea2ImageNode/pt-BR.md)

Esta documentação foi gerada por IA. Se você encontrar algum erro ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Krea2ImageNode/en.md)

## Visão Geral

O nó Krea 2 Image gera imagens utilizando o modelo de IA Krea 2. Ele suporta duas variantes do modelo: Medium para ilustrações expressivas e Large para fotorrealismo expressivo. Opcionalmente, você pode incluir um moodboard e até 10 referências de estilo de imagem para influenciar a imagem gerada.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Faixa | Descrição |
|-----------|--------------|-------------|-------|-----------|
| `prompt` | STRING | Sim | N/A | Prompt de texto para a imagem. |
| `modelo` | DICT | Sim | Veja abaixo | Krea 2 Medium é ideal para ilustrações expressivas; Krea 2 Large é ideal para fotorrealismo expressivo. |
| `semente` | INT | Sim | 0 a 2147483647 | Semente aleatória para reprodutibilidade (padrão: 0). |

O parâmetro `model` é um dicionário com os seguintes subparâmetros:

| Subparâmetro | Tipo de Dado | Obrigatório | Faixa | Descrição |
|--------------|--------------|-------------|-------|-----------|
| `modelo` | STRING | Sim | `"krea 2 medium"`<br>`"krea 2 large"` | Seleciona a variante do modelo Krea 2. |
| `aspect_ratio` | STRING | Sim | N/A | A proporção de aspecto para a imagem gerada. |
| `resolution` | STRING | Sim | N/A | A resolução para a imagem gerada. |
| `creativity` | FLOAT | Sim | N/A | Controla o nível de criatividade da geração. |
| `moodboard_id` | STRING | Não | N/A | O UUID de um moodboard do Krea para influenciar a imagem. Deve ser um UUID válido. |
| `moodboard_strength` | FLOAT | Não | N/A | A intensidade da influência do moodboard (padrão: 0,35). |
| `style_reference` | LIST | Não | 0 a 10 itens | Uma lista de referências de estilo de imagem. Cada referência deve ter uma `url` (STRING) e `strength` (FLOAT). |

**Restrições:**
- `moodboard_id` deve ser um UUID válido (ex.: `"123e4567-e89b-12d3-a456-426614174000"`). Copie-o do site do Krea.
- `style_reference` aceita no máximo 10 referências de estilo de imagem.
- O `prompt` deve ter pelo menos 1 caractere.

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|---------------|--------------|-----------|
| `image` | IMAGE | A imagem gerada como um tensor. |

---
**Source fingerprint (SHA-256):** `6aeb2d935ef5df5699a19271c9ceb766892ef4b0e4f67bfa540bf12ffadf362d`
