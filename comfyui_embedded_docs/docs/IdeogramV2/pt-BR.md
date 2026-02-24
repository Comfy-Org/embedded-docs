> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/IdeogramV2/pt-BR.md)

O nó Ideogram V2 gera imagens usando o modelo de IA Ideogram V2. Ele recebe prompts de texto e várias configurações de geração para criar imagens por meio de um serviço de API. O nó suporta diferentes proporções de tela, resoluções e opções de estilo para personalizar as imagens de saída.

## Entradas

| Parâmetro | Tipo de Dados | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `prompt` | STRING | Sim | - | Prompt para a geração da imagem (padrão: string vazia) |
| `turbo` | BOOLEAN | Não | - | Se deve usar o modo turbo (geração mais rápida, potencialmente com qualidade inferior) (padrão: Falso) |
| `aspect_ratio` | COMBO | Não | "1:1"<br>"16:9"<br>"9:16"<br>"4:3"<br>"3:4"<br>"3:2"<br>"2:3" | A proporção de tela para a geração da imagem. Ignorado se a resolução não estiver definida como AUTO. (padrão: "1:1") |
| `resolution` | COMBO | Não | "Auto"<br>"1024x1024"<br>"1152x896"<br>"896x1152"<br>"1216x832"<br>"832x1216"<br>"1344x768"<br>"768x1344"<br>"1536x640"<br>"640x1536" | A resolução para a geração da imagem. Se não estiver definida como AUTO, isso substitui a configuração `aspect_ratio`. (padrão: "Auto") |
| `magic_prompt_option` | COMBO | Não | "AUTO"<br>"ON"<br>"OFF" | Determina se o MagicPrompt deve ser usado na geração (padrão: "AUTO") |
| `seed` | INT | Não | 0-2147483647 | Semente aleatória para a geração (padrão: 0) |
| `style_type` | COMBO | Não | "AUTO"<br>"GENERAL"<br>"REALISTIC"<br>"DESIGN"<br>"RENDER_3D"<br>"ANIME" | Tipo de estilo para a geração (somente V2) (padrão: "NONE") |
| `negative_prompt` | STRING | Não | - | Descrição do que excluir da imagem (padrão: string vazia) |
| `num_images` | INT | Não | 1-8 | Número de imagens a serem geradas (padrão: 1) |

**Observação:** Quando `resolution` não está definida como "Auto", ela substitui a configuração `aspect_ratio`. O parâmetro `num_images` tem um limite máximo de 8 imagens por geração.

## Saídas

| Nome da Saída | Tipo de Dados | Descrição |
|-------------|-----------|-------------|
| `output` | IMAGE | A(s) imagem(ns) gerada(s) pelo modelo Ideogram V2 |
