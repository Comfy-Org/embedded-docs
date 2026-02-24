> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDanceSeedreamNode/pt-BR.md)

O nó ByteDance Seedream 4 oferece capacidades unificadas de geração de texto para imagem e edição precisa com base em uma única frase, com resolução de até 4K. Ele pode criar novas imagens a partir de prompts de texto ou editar imagens existentes usando instruções textuais. O nó suporta tanto a geração de uma única imagem quanto a geração sequencial de múltiplas imagens relacionadas.

## Entradas

| Parâmetro | Tipo de Dado | Tipo de Entrada | Padrão | Intervalo | Descrição |
|-----------|-----------|------------|---------|-------|-------------|
| `model` | MODEL | COMBO | "seedream-4-0-250828" | ["seedream-4-0-250828"] | Nome do modelo |
| `prompt` | STRING | STRING | "" | - | Prompt de texto para criar ou editar uma imagem. |
| `image` | IMAGE | IMAGE | - | - | Imagem(ns) de entrada para geração de imagem para imagem. Lista de 1 a 10 imagens para geração com referência única ou múltipla. |
| `size_preset` | STRING | COMBO | Primeiro preset de RECOMMENDED_PRESETS_SEEDREAM_4 | Todos os rótulos de RECOMMENDED_PRESETS_SEEDREAM_4 | Selecione um tamanho recomendado. Selecione 'Custom' para usar a largura e altura abaixo. |
| `width` | INT | INT | 2048 | 1024-4096 (passo 64) | Largura personalizada para a imagem. O valor só funciona se `size_preset` estiver definido como `Custom` |
| `height` | INT | INT | 2048 | 1024-4096 (passo 64) | Altura personalizada para a imagem. O valor só funciona se `size_preset` estiver definido como `Custom` |
| `sequential_image_generation` | STRING | COMBO | "disabled" | ["disabled", "auto"] | Modo de geração de imagens em grupo. 'disabled' gera uma única imagem. 'auto' permite que o modelo decida se deve gerar múltiplas imagens relacionadas (ex: cenas de uma história, variações de personagem). |
| `max_images` | INT | INT | 1 | 1-15 | Número máximo de imagens a serem geradas quando sequential_image_generation='auto'. O total de imagens (entrada + geradas) não pode exceder 15. |
| `seed` | INT | INT | 0 | 0-2147483647 | Semente a ser usada para a geração. |
| `watermark` | BOOLEAN | BOOLEAN | True | - | Se deve adicionar uma marca d'água "Gerado por IA" à imagem. |
| `fail_on_partial` | BOOLEAN | BOOLEAN | True | - | Se habilitado, aborta a execução se alguma imagem solicitada estiver faltando ou retornar um erro. |

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|-------------|-----------|-------------|
| `IMAGE` | IMAGE | Imagem(ns) gerada(s) com base nos parâmetros de entrada e no prompt |
