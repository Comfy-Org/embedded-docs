# CLIPTextEncodePixArtAlpha

Codifica o texto e define o condicionamento de resolução para PixArt Alpha. Este nó processa a entrada de texto e adiciona informações de largura e altura para criar dados de condicionamento especificamente para modelos PixArt Alpha. Ele não se aplica a modelos PixArt Sigma.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `width` | A dimensão de largura para condicionamento de resolução (padrão: 1024) | INT | Sim | 0 a MAX_RESOLUTION |
| `height` | A dimensão de altura para condicionamento de resolução (padrão: 1024) | INT | Sim | 0 a MAX_RESOLUTION |
| `text` | Texto de entrada a ser codificado, suporta entrada de múltiplas linhas e prompts dinâmicos | STRING | Sim | - |
| `clip` | Modelo CLIP usado para tokenização e codificação | CLIP | Sim | - |

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `CONDITIONING` | Dados de condicionamento codificados com tokens de texto e informações de resolução | CONDITIONING |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPTextEncodePixArtAlpha/pt-BR.md)

---
**Source fingerprint (SHA-256):** `d25a4117d39e3528cd0f64bc34462cd7b4076c67cb4e454c77fcc66490f89be6`
