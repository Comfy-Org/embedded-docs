> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RunwayImageToVideoNodeGen4/pt-BR.md)

O nó Runway Image to Video (Gen4 Turbo) gera um vídeo a partir de um único quadro inicial usando o modelo Gen4 Turbo da Runway. Ele recebe um prompt de texto e uma imagem de quadro inicial, e então cria uma sequência de vídeo com base nas configurações de duração e proporção de aspecto fornecidas. O nó gerencia o upload do quadro inicial para a API da Runway e retorna o vídeo gerado.

## Entradas

| Parâmetro | Tipo de Dados | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `prompt` | STRING | Sim | - | Prompt de texto para a geração (padrão: string vazia) |
| `start_frame` | IMAGE | Sim | - | Quadro inicial a ser usado para o vídeo |
| `duration` | COMBO | Sim | Múltiplas opções disponíveis | Seleção da duração do vídeo a partir das opções de duração disponíveis |
| `ratio` | COMBO | Sim | Múltiplas opções disponíveis | Seleção da proporção de aspecto a partir das opções de proporção do Gen4 Turbo disponíveis |
| `seed` | INT | Não | 0 a 4294967295 | Semente aleatória para a geração (padrão: 0) |

**Restrições dos Parâmetros:**

- A imagem `start_frame` deve ter dimensões que não excedam 7999x7999 pixels
- A imagem `start_frame` deve ter uma proporção de aspecto entre 0,5 e 2,0
- O `prompt` deve conter pelo menos um caractere

## Saídas

| Nome da Saída | Tipo de Dados | Descrição |
|-------------|-----------|-------------|
| `output` | VIDEO | O vídeo gerado com base no quadro de entrada e no prompt |
