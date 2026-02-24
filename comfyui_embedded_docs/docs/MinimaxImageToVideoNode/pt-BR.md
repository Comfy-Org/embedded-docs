> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MinimaxImageToVideoNode/pt-BR.md)

Gera vídeos de forma síncrona com base em uma imagem, um prompt e parâmetros opcionais usando a API da MiniMax. Este nó utiliza uma imagem de entrada e uma descrição textual para criar uma sequência de vídeo, com várias opções de modelo e configurações disponíveis.

## Entradas

| Parâmetro | Tipo de Dados | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `image` | IMAGE | Sim | - | Imagem a ser usada como primeiro quadro da geração do vídeo |
| `prompt_text` | STRING | Sim | - | Prompt de texto para orientar a geração do vídeo (padrão: string vazia) |
| `model` | COMBO | Sim | "I2V-01-Director"<br>"I2V-01"<br>"I2V-01-live" | Modelo a ser usado para a geração do vídeo (padrão: "I2V-01") |
| `seed` | INT | Não | 0 a 18446744073709551615 | A semente aleatória usada para criar o ruído (padrão: 0) |

## Saídas

| Nome da Saída | Tipo de Dados | Descrição |
|-------------|-----------|-------------|
| `output` | VIDEO | A saída de vídeo gerada |
