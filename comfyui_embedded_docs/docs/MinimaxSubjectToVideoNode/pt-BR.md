Gera um vídeo de forma síncrona com base em uma imagem de assunto e um prompt de texto usando a API do MiniMax. Este nó recebe uma imagem de um assunto e uma descrição para criar um vídeo que anima ou apresenta esse assunto de acordo com o prompt.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `subject` | Imagem do assunto a ser referenciada para a geração do vídeo | IMAGE | Sim | - |
| `prompt_text` | Prompt de texto para guiar a geração do vídeo (padrão: string vazia) | STRING | Sim | - |
| `model` | Modelo a ser usado para a geração do vídeo (padrão: "S2V-01") | COMBO | Não | "S2V-01" |
| `seed` | Semente aleatória usada para criar o ruído (padrão: 0) | INT | Não | 0 a 18446744073709551615 |

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `output` | O vídeo gerado com base na imagem de assunto e no prompt fornecidos | VIDEO |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MinimaxSubjectToVideoNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `69651367e6c452ec1f3a4765b74a28cc6b579288f3319ed70fa7c16a1ced0dbc`
