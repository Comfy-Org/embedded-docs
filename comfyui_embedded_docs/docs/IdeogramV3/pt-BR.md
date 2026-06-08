O nó Ideogram V3 gera imagens utilizando o modelo Ideogram V3. Ele suporta tanto a geração regular de imagens a partir de prompts de texto quanto a edição de imagens quando uma imagem e uma máscara são fornecidas. O nó oferece vários controles para proporção de aspecto, resolução, velocidade de geração e imagens de referência de personagem opcionais.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `prompt` | Prompt para a geração ou edição da imagem (padrão: vazio) | STRING | Sim | - |
| `imagem` | Imagem de referência opcional para edição de imagem | IMAGE | Não | - |
| `máscara` | Máscara opcional para inpaint (áreas brancas serão substituídas) | MASK | Não | - |
| `proporção` | A proporção de aspecto para geração de imagem. Ignorado se a resolução não estiver definida como Auto (padrão: "1:1") | COMBO | Não | "1:1"<br>"16:9"<br>"9:16"<br>"4:3"<br>"3:4"<br>"3:2"<br>"2:3" |
| `resolução` | A resolução para geração de imagem. Se não estiver definida como Auto, substitui a configuração de proporção de aspecto (padrão: "Auto") | COMBO | Não | "Auto"<br>"1024x1024"<br>"1152x896"<br>"896x1152"<br>"1216x832"<br>"832x1216"<br>"1344x768"<br>"768x1344"<br>"1536x640"<br>"640x1536" |
| `opção_magic_prompt` | Determina se o MagicPrompt deve ser usado na geração (padrão: "AUTO") | COMBO | Não | "AUTO"<br>"ON"<br>"OFF" |
| `semente` | Semente aleatória para geração (padrão: 0) | INT | Não | 0-2147483647 |
| `número_de_imagens` | Número de imagens a serem geradas (padrão: 1) | INT | Não | 1-8 |
| `velocidade_de_renderização` | Controla a relação entre velocidade de geração e qualidade (padrão: "DEFAULT") | COMBO | Não | "DEFAULT"<br>"TURBO"<br>"QUALITY" |
| `imagem_personagem` | Imagem a ser usada como referência de personagem | IMAGE | Não | - |
| `máscara_personagem` | Máscara opcional para a imagem de referência de personagem | MASK | Não | - |

**Restrições dos Parâmetros:**

- Quando tanto `image` quanto `mask` são fornecidos, o nó alterna para o modo de edição
- Se apenas um dos parâmetros `image` ou `mask` for fornecido, ocorrerá um erro
- `character_mask` requer que `character_image` esteja presente
- O parâmetro `aspect_ratio` é ignorado quando `resolution` não está definido como "Auto"
- Áreas brancas na máscara serão substituídas durante o inpaint
- A máscara de personagem e a imagem de personagem devem ter o mesmo tamanho

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `output` | A(s) imagem(ns) gerada(s) ou editada(s) | IMAGE |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/IdeogramV3/pt-BR.md)

---
**Source fingerprint (SHA-256):** `0d0058cc8483c453100d8d9dfcb9a31ae5e686f38ced77ed7e472cd083c3464b`
