> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVPreprocess/pt-BR.md)

O nó LTXVPreprocess aplica pré-processamento de compressão em imagens. Ele recebe imagens de entrada e as processa com um nível de compressão especificado, gerando as imagens processadas com as configurações de compressão aplicadas.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Faixa | Descrição |
|-----------|--------------|-------------|-------|-----------|
| `image` | IMAGE | Sim | - | A imagem de entrada a ser processada |
| `img_compression` | INT | Não | 0-100 | Quantidade de compressão a ser aplicada na imagem (padrão: 35) |

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|---------------|--------------|-----------|
| `output_image` | IMAGE | A imagem de saída processada com a compressão aplicada |

---
**Source fingerprint (SHA-256):** `2c5fbde5d011bdf3313ca05508f58a13eaae0bdff12f3659fef281c0045e480d`
