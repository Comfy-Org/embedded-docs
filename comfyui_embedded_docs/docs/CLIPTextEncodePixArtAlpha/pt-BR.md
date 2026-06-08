# CLIPTextEncodePixArtAlpha

Codifica texto e define o condicionamento de resolução para PixArt Alpha. Este nó processa a entrada de texto e adiciona informações de largura e altura para criar dados de condicionamento especificamente para modelos PixArt Alpha. Não se aplica a modelos PixArt Sigma.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `largura` | A dimensão de largura para condicionamento de resolução (padrão: 1024) | INT | Sim | 0 a MAX_RESOLUTION |
| `altura` | A dimensão de altura para condicionamento de resolução (padrão: 1024) | INT | Sim | 0 a MAX_RESOLUTION |
| `texto` | Entrada de texto a ser codificada, suporta entrada multilinha e prompts dinâmicos | STRING | Sim | - |
| `clip` | Modelo CLIP usado para tokenização e codificação | CLIP | Sim | - |

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `CONDITIONING` | Dados de condicionamento codificados com tokens de texto e informações de resolução | CONDITIONING |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPTextEncodePixArtAlpha/pt-BR.md)

---
**Source fingerprint (SHA-256):** `d15df3c7bcca10ec85f0689d6631a6b89aa89e609193c36b658b1bc97f90ee9a`
