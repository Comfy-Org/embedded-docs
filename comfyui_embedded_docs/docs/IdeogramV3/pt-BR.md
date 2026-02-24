> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/IdeogramV3/pt-BR.md)

O nó Ideogram V3 gera imagens usando o modelo Ideogram V3. Ele suporta tanto a geração regular de imagens a partir de prompts de texto quanto a edição de imagens quando tanto uma imagem quanto uma máscara são fornecidas. O nó oferece vários controles para proporção de tela, resolução, velocidade de geração e imagens de referência de personagens opcionais.

## Entradas

| Parâmetro | Tipo de Dados | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `prompt` | STRING | Sim | - | Prompt para a geração ou edição da imagem (padrão: vazio) |
| `image` | IMAGE | Não | - | Imagem de referência opcional para edição de imagem |
| `mask` | MASK | Não | - | Máscara opcional para inpainting (as áreas brancas serão substituídas) |
| `aspect_ratio` | COMBO | Não | "1:1"<br>"16:9"<br>"9:16"<br>"4:3"<br>"3:4"<br>"3:2"<br>"2:3" | A proporção de tela para a geração da imagem. Ignorado se a resolução não estiver definida como Auto (padrão: "1:1") |
| `resolution` | COMBO | Não | "Auto"<br>"1024x1024"<br>"1152x896"<br>"896x1152"<br>"1216x832"<br>"832x1216"<br>"1344x768"<br>"768x1344"<br>"1536x640"<br>"640x1536" | A resolução para a geração da imagem. Se não estiver definida como Auto, isso substitui a configuração `aspect_ratio` (padrão: "Auto") |
| `magic_prompt_option` | COMBO | Não | "AUTO"<br>"ON"<br>"OFF" | Determina se o MagicPrompt deve ser usado na geração (padrão: "AUTO") |
| `seed` | INT | Não | 0-2147483647 | Semente aleatória para a geração (padrão: 0) |
| `num_images` | INT | Não | 1-8 | Número de imagens a serem geradas (padrão: 1) |
| `rendering_speed` | COMBO | Não | "DEFAULT"<br>"TURBO"<br>"QUALITY" | Controla a relação entre velocidade de geração e qualidade (padrão: "DEFAULT") |
| `character_image` | IMAGE | Não | - | Imagem a ser usada como referência de personagem |
| `character_mask` | MASK | Não | - | Máscara opcional para a imagem de referência do personagem |

**Restrições dos Parâmetros:**

- Quando tanto `image` quanto `mask` são fornecidos, o nó muda para o modo de edição
- Se apenas um dos parâmetros `image` ou `mask` for fornecido, ocorrerá um erro
- `character_mask` requer que `character_image` esteja presente
- O parâmetro `aspect_ratio` é ignorado quando `resolution` não está definida como "Auto"
- As áreas brancas na máscara serão substituídas durante o inpainting
- A máscara de personagem e a imagem de personagem devem ter o mesmo tamanho

## Saídas

| Nome da Saída | Tipo de Dados | Descrição |
|-------------|-----------|-------------|
| `output` | IMAGE | A(s) imagem(ns) gerada(s) ou editada(s) |
