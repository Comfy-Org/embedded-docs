> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDanceImageNode/pt-BR.md)

O nó ByteDance Image gera imagens usando modelos da ByteDance por meio de uma API baseada em prompts de texto. Ele permite que você selecione diferentes modelos, especifique as dimensões da imagem e controle vários parâmetros de geração, como `seed` e `guidance_scale`. O nó se conecta ao serviço de geração de imagens da ByteDance e retorna a imagem criada.

## Entradas

| Parâmetro | Tipo de Dado | Tipo de Entrada | Padrão | Intervalo | Descrição |
|-----------|-----------|------------|---------|-------|-------------|
| `model` | MODEL | COMBO | seedream_3 | Opções de Text2ImageModelName | Nome do modelo |
| `prompt` | STRING | STRING | - | - | O prompt de texto usado para gerar a imagem |
| `size_preset` | STRING | COMBO | - | Rótulos de RECOMMENDED_PRESETS | Escolha um tamanho recomendado. Selecione "Custom" para usar a largura e altura abaixo |
| `width` | INT | INT | 1024 | 512-2048 (passo 64) | Largura personalizada para a imagem. O valor só funciona se `size_preset` estiver definido como `Custom` |
| `height` | INT | INT | 1024 | 512-2048 (passo 64) | Altura personalizada para a imagem. O valor só funciona se `size_preset` estiver definido como `Custom` |
| `seed` | INT | INT | 0 | 0-2147483647 (passo 1) | Semente a ser usada para a geração (opcional) |
| `guidance_scale` | FLOAT | FLOAT | 2.5 | 1.0-10.0 (passo 0.01) | Valores mais altos fazem a imagem seguir o prompt mais de perto (opcional) |
| `watermark` | BOOLEAN | BOOLEAN | True | - | Se deve adicionar uma marca d'água "AI generated" à imagem (opcional) |

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|-------------|-----------|-------------|
| `IMAGE` | IMAGE | A imagem gerada pela API da ByteDance |
