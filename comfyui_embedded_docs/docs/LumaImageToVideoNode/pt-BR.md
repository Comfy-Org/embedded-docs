> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LumaImageToVideoNode/pt-BR.md)

Gera vídeos de forma síncrona com base em um prompt, imagens de entrada e um tamanho de saída. Este nó cria vídeos usando a API Luma, fornecendo prompts de texto e imagens opcionais de início e fim para definir o conteúdo e a estrutura do vídeo.

## Entradas

| Parâmetro | Tipo de Dados | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `prompt` | STRING | Sim | - | Prompt para a geração do vídeo (padrão: "") |
| `model` | COMBO | Sim | Múltiplas opções disponíveis | Seleciona o modelo de geração de vídeo dentre os modelos Luma disponíveis |
| `resolution` | COMBO | Sim | Múltiplas opções disponíveis | Resolução de saída para o vídeo gerado (padrão: 540p) |
| `duration` | COMBO | Sim | Múltiplas opções disponíveis | Duração do vídeo gerado |
| `loop` | BOOLEAN | Sim | - | Define se o vídeo gerado deve ser em loop (padrão: Falso) |
| `seed` | INT | Sim | 0 a 18446744073709551615 | Semente para determinar se o nó deve ser executado novamente; os resultados reais são não determinísticos independentemente da semente. (padrão: 0) |
| `first_image` | IMAGE | Não | - | Primeiro quadro do vídeo gerado. (opcional) |
| `last_image` | IMAGE | Não | - | Último quadro do vídeo gerado. (opcional) |
| `luma_concepts` | CUSTOM | Não | - | Conceitos de Câmera opcionais para ditar o movimento da câmera via o nó Luma Concepts. (opcional) |

**Nota:** Pelo menos um dos parâmetros `first_image` ou `last_image` deve ser fornecido. O nó lançará uma exceção se ambos estiverem ausentes.

## Saídas

| Nome da Saída | Tipo de Dados | Descrição |
|-------------|-----------|-------------|
| `output` | VIDEO | O arquivo de vídeo gerado |
