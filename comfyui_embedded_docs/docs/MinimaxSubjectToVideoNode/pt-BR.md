> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MinimaxSubjectToVideoNode/pt-BR.md)

Gera vídeos de forma síncrona com base em uma imagem, um prompt e parâmetros opcionais usando a API da MiniMax. Este nó utiliza uma imagem de um assunto e uma descrição textual para criar um vídeo usando o serviço de geração de vídeo da MiniMax.

## Entradas

| Parâmetro | Tipo de Dados | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `subject` | IMAGE | Sim | - | Imagem do assunto a ser referenciada para a geração do vídeo |
| `prompt_text` | STRING | Sim | - | Prompt de texto para orientar a geração do vídeo (padrão: string vazia) |
| `model` | COMBO | Não | "S2V-01"<br> | Modelo a ser usado para a geração de vídeo (padrão: "S2V-01") |
| `seed` | INT | Não | 0 a 18446744073709551615 | A semente aleatória usada para criar o ruído (padrão: 0) |

## Saídas

| Nome da Saída | Tipo de Dados | Descrição |
|-------------|-----------|-------------|
| `output` | VIDEO | O vídeo gerado com base na imagem do assunto e no prompt fornecidos |
