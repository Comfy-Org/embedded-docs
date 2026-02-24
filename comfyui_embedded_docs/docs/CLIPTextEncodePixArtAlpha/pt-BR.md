> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPTextEncodePixArtAlpha/pt-BR.md)

Codifica texto e define o condicionamento de resolução para PixArt Alpha. Este nó processa entrada de texto e adiciona informações de largura e altura para criar dados de condicionamento especificamente para modelos PixArt Alpha. Não se aplica a modelos PixArt Sigma.

## Entradas

| Parâmetro | Tipo de Dados | Tipo de Entrada | Padrão | Intervalo | Descrição |
|-----------|-----------|------------|---------|-------|-------------|
| `width` | INT | Input | 1024 | 0 a MAX_RESOLUTION | A dimensão de largura para o condicionamento de resolução |
| `height` | INT | Input | 1024 | 0 a MAX_RESOLUTION | A dimensão de altura para o condicionamento de resolução |
| `text` | STRING | Input | - | - | Entrada de texto a ser codificada, suporta entrada de múltiplas linhas e prompts dinâmicos |
| `clip` | CLIP | Input | - | - | Modelo CLIP usado para tokenização e codificação |

## Saídas

| Nome da Saída | Tipo de Dados | Descrição |
|-------------|-----------|-------------|
| `CONDITIONING` | CONDITIONING | Dados de condicionamento codificados com tokens de texto e informações de resolução |
