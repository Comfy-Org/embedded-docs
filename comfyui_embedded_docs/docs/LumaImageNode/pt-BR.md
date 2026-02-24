> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LumaImageNode/pt-BR.md)

Gera imagens de forma síncrona com base em um prompt e em uma proporção de aspecto. Este nó cria imagens usando descrições textuais e permite controlar as dimensões e o estilo da imagem por meio de várias entradas de referência.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `prompt` | STRING | Sim | - | Prompt para a geração da imagem (padrão: string vazia) |
| `model` | COMBO | Sim | Múltiplas opções disponíveis | Seleção do modelo para geração de imagem |
| `aspect_ratio` | COMBO | Sim | Múltiplas opções disponíveis | Proporção de aspecto para a imagem gerada (padrão: proporção 16:9) |
| `seed` | INT | Sim | 0 a 18446744073709551615 | Semente para determinar se o nó deve ser executado novamente; os resultados reais são não determinísticos independentemente da semente (padrão: 0) |
| `style_image_weight` | FLOAT | Não | 0.0 a 1.0 | Peso da imagem de estilo. Ignorado se nenhuma `style_image` for fornecida (padrão: 1.0) |
| `image_luma_ref` | LUMA_REF | Não | - | Conexão do nó Luma Reference para influenciar a geração com imagens de entrada; até 4 imagens podem ser consideradas |
| `style_image` | IMAGE | Não | - | Imagem de referência de estilo; apenas 1 imagem será usada |
| `character_image` | IMAGE | Não | - | Imagens de referência de personagem; pode ser um lote de múltiplas imagens, até 4 imagens podem ser consideradas |

**Restrições dos Parâmetros:**

- O parâmetro `image_luma_ref` pode aceitar até 4 imagens de referência
- O parâmetro `character_image` pode aceitar até 4 imagens de referência de personagem
- O parâmetro `style_image` aceita apenas 1 imagem de referência de estilo
- O parâmetro `style_image_weight` só é usado quando `style_image` é fornecido

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|-------------|-----------|-------------|
| `output` | IMAGE | A imagem gerada com base nos parâmetros de entrada |
