> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StabilityUpscaleCreativeNode/pt-BR.md)

Melhora a resolução da imagem com alterações mínimas para 4K. Este nó utiliza a tecnologia de upscaling criativo da Stability AI para aumentar a resolução da imagem, preservando o conteúdo original e adicionando detalhes criativos sutis.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `image` | IMAGE | Sim | - | A imagem de entrada a ser melhorada em resolução |
| `prompt` | STRING | Sim | - | O que você deseja ver na imagem de saída. Um prompt forte e descritivo que defina claramente elementos, cores e assuntos levará a melhores resultados. (padrão: string vazia) |
| `creativity` | FLOAT | Sim | 0.1-0.5 | Controla a probabilidade de criar detalhes adicionais não fortemente condicionados pela imagem inicial. (padrão: 0.3) |
| `style_preset` | COMBO | Sim | Múltiplas opções disponíveis | Estilo desejado opcional para a imagem gerada. As opções incluem vários predefinições de estilo da Stability AI. |
| `seed` | INT | Sim | 0-4294967294 | A semente aleatória usada para criar o ruído. (padrão: 0) |
| `negative_prompt` | STRING | Não | - | Palavras-chave do que você não deseja ver na imagem de saída. Este é um recurso avançado. (padrão: string vazia) |

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|-------------|-----------|-------------|
| `image` | IMAGE | A imagem melhorada em resolução 4K |
