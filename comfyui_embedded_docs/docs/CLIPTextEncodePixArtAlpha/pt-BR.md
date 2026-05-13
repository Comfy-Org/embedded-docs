> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPTextEncodePixArtAlpha/pt-BR.md)

# CLIPTextEncodePixArtAlpha

Codifica texto e define o condicionamento de resolução para PixArt Alpha. Este nó processa a entrada de texto e adiciona informações de largura e altura para criar dados de condicionamento especificamente para modelos PixArt Alpha. Não se aplica a modelos PixArt Sigma.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Faixa | Descrição |
|-----------|--------------|-------------|-------|-----------|
| `width` | INT | Sim | 0 a MAX_RESOLUTION | A dimensão de largura para condicionamento de resolução (padrão: 1024) |
| `height` | INT | Sim | 0 a MAX_RESOLUTION | A dimensão de altura para condicionamento de resolução (padrão: 1024) |
| `text` | STRING | Sim | - | Entrada de texto a ser codificada, suporta entrada multilinha e prompts dinâmicos |
| `clip` | CLIP | Sim | - | Modelo CLIP usado para tokenização e codificação |

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|---------------|--------------|-----------|
| `CONDITIONING` | CONDITIONING | Dados de condicionamento codificados com tokens de texto e informações de resolução |

---
**Source fingerprint (SHA-256):** `d15df3c7bcca10ec85f0689d6631a6b89aa89e609193c36b658b1bc97f90ee9a`
