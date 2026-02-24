> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RunwayImageToVideoNodeGen3a/pt-BR.md)

O nó Runway Image to Video (Gen3a Turbo) gera um vídeo a partir de um único quadro inicial usando o modelo Gen3a Turbo da Runway. Ele recebe um prompt de texto e uma imagem de quadro inicial, e então cria uma sequência de vídeo com base na duração e proporção de aspecto especificadas. Este nó se conecta à API da Runway para processar a geração remotamente.

## Entradas

| Parâmetro | Tipo de Dados | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `prompt` | STRING | Sim | N/A | Prompt de texto para a geração (padrão: "") |
| `start_frame` | IMAGE | Sim | N/A | Quadro inicial a ser usado para o vídeo |
| `duration` | COMBO | Sim | Múltiplas opções disponíveis | Seleção da duração do vídeo a partir das opções disponíveis |
| `ratio` | COMBO | Sim | Múltiplas opções disponíveis | Seleção da proporção de aspecto a partir das opções disponíveis |
| `seed` | INT | Não | 0-4294967295 | Semente aleatória para a geração (padrão: 0) |

**Restrições dos Parâmetros:**

- O `start_frame` deve ter dimensões que não excedam 7999x7999 pixels
- O `start_frame` deve ter uma proporção de aspecto entre 0.5 e 2.0
- O `prompt` deve conter pelo menos um caractere (não pode estar vazio)

## Saídas

| Nome da Saída | Tipo de Dados | Descrição |
|-------------|-----------|-------------|
| `output` | VIDEO | A sequência de vídeo gerada |
