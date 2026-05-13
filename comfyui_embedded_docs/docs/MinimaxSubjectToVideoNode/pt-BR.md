> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MinimaxSubjectToVideoNode/pt-BR.md)

Gera um vídeo de forma síncrona com base em uma imagem de assunto e um prompt de texto usando a API do MiniMax. Este nó recebe uma imagem de um assunto e uma descrição para criar um vídeo que anima ou apresenta esse assunto de acordo com o prompt.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Faixa | Descrição |
|-----------|--------------|-------------|-------|-----------|
| `subject` | IMAGE | Sim | - | Imagem do assunto a ser referenciada para a geração do vídeo |
| `prompt_text` | STRING | Sim | - | Prompt de texto para guiar a geração do vídeo (padrão: string vazia) |
| `model` | COMBO | Não | "S2V-01" | Modelo a ser usado para a geração do vídeo (padrão: "S2V-01") |
| `seed` | INT | Não | 0 a 18446744073709551615 | Semente aleatória usada para criar o ruído (padrão: 0) |

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|---------------|--------------|-----------|
| `output` | VIDEO | O vídeo gerado com base na imagem de assunto e no prompt fornecidos |

---
**Source fingerprint (SHA-256):** `69651367e6c452ec1f3a4765b74a28cc6b579288f3319ed70fa7c16a1ced0dbc`
