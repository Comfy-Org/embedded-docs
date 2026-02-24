> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RunwayFirstLastFrameNode/pt-BR.md)

O nó Runway First-Last-Frame to Video gera vídeos fazendo upload de quadros-chave inicial e final junto com um prompt de texto. Ele cria transições suaves entre os quadros de início e fim fornecidos usando o modelo Gen-3 da Runway. Isso é particularmente útil para transições complexas onde o quadro final difere significativamente do quadro inicial.

## Entradas

| Parâmetro | Tipo de Dados | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `prompt` | STRING | Sim | N/A | Prompt de texto para a geração (padrão: string vazia) |
| `start_frame` | IMAGE | Sim | N/A | Quadro inicial a ser usado para o vídeo |
| `end_frame` | IMAGE | Sim | N/A | Quadro final a ser usado para o vídeo. Suportado apenas para gen3a_turbo. |
| `duration` | COMBO | Sim | Múltiplas opções disponíveis | Seleção da duração do vídeo a partir das opções de Duration disponíveis |
| `ratio` | COMBO | Sim | Múltiplas opções disponíveis | Seleção da proporção de aspecto a partir das opções RunwayGen3aAspectRatio disponíveis |
| `seed` | INT | Não | 0-4294967295 | Semente aleatória para a geração (padrão: 0) |

**Restrições dos Parâmetros:**

- O `prompt` deve conter pelo menos 1 caractere
- Tanto o `start_frame` quanto o `end_frame` devem ter dimensões máximas de 7999x7999 pixels
- Tanto o `start_frame` quanto o `end_frame` devem ter proporções de aspecto entre 0.5 e 2.0
- O parâmetro `end_frame` é suportado apenas ao usar o modelo gen3a_turbo

## Saídas

| Nome da Saída | Tipo de Dados | Descrição |
|-------------|-----------|-------------|
| `output` | VIDEO | O vídeo gerado, fazendo a transição entre os quadros inicial e final |
