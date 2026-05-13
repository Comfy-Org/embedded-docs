> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MinimaxTextToVideoNode/pt-BR.md)

Gera vídeos de forma síncrona com base em um prompt e parâmetros opcionais usando a API da MiniMax. Este nó cria conteúdo de vídeo a partir de descrições textuais ao se conectar ao serviço de texto-para-vídeo da MiniMax.

## Entradas

| Parâmetro | Tipo de Dados | Obrigatório | Faixa | Descrição |
|-----------|---------------|-------------|-------|-----------|
| `prompt_texto` | STRING | Sim | - | Prompt de texto para guiar a geração do vídeo |
| `modelo` | COMBO | Não | "T2V-01"<br>"T2V-01-Director" | Modelo a ser usado para geração de vídeo (padrão: "T2V-01") |
| `semente` | INT | Não | 0 a 18446744073709551615 | Semente aleatória usada para criar o ruído (padrão: 0) |

## Saídas

| Nome da Saída | Tipo de Dados | Descrição |
|---------------|---------------|-----------|
| `output` | VIDEO | O vídeo gerado com base no prompt de entrada |

---
**Source fingerprint (SHA-256):** `bdbd8f9defc4c626f07b36c1ba9859155fa90a2d7ef9a491c30dac4d003d39be`
