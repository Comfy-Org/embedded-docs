> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MinimaxImageToVideoNode/pt-BR.md)

Gera vídeos de forma síncrona com base em uma imagem e um prompt, além de parâmetros opcionais, utilizando a API da MiniMax. Este nó recebe uma imagem de entrada e uma descrição textual para criar uma sequência de vídeo, com várias opções de modelo e configurações disponíveis.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Faixa | Descrição |
|-----------|--------------|-------------|-------|-----------|
| `image` | IMAGE | Sim | - | Imagem a ser usada como primeiro quadro da geração de vídeo |
| `prompt_text` | STRING | Sim | - | Prompt textual para guiar a geração do vídeo (padrão: string vazia) |
| `model` | COMBO | Sim | "I2V-01-Director"<br>"I2V-01"<br>"I2V-01-live" | Modelo a ser usado para a geração de vídeo (padrão: "I2V-01") |
| `seed` | INT | Não | 0 a 18446744073709551615 | Semente aleatória usada para criar o ruído (padrão: 0) |

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|---------------|--------------|-----------|
| `output` | VIDEO | A saída de vídeo gerada |

---
**Source fingerprint (SHA-256):** `9ad1659352e363361f09d6a7a0e24835056b20cc84532247251f516b0ac284e8`
