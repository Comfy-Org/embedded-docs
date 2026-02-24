> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MinimaxTextToVideoNode/pt-BR.md)

Gera vídeos de forma síncrona com base em um prompt e parâmetros opcionais usando a API da MiniMax. Este nó cria conteúdo de vídeo a partir de descrições de texto conectando-se ao serviço de texto para vídeo da MiniMax.

## Entradas

| Parâmetro | Tipo de Dados | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `prompt_text` | STRING | Sim | - | Prompt de texto para orientar a geração do vídeo |
| `model` | COMBO | Não | "T2V-01"<br>"T2V-01-Director" | Modelo a ser usado para a geração de vídeo (padrão: "T2V-01") |
| `seed` | INT | Não | 0 a 18446744073709551615 | A semente aleatória usada para criar o ruído (padrão: 0) |

## Saídas

| Nome da Saída | Tipo de Dados | Descrição |
|-------------|-----------|-------------|
| `output` | VIDEO | O vídeo gerado com base no prompt de entrada |
