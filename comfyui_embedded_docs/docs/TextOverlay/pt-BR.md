# Desenhar Sobreposição de Texto

Este nó desenha texto sobre uma imagem ou um lote de imagens. Ele suporta texto personalizado, tamanho da fonte, cor, posição, alinhamento e um contorno opcional, compondo o texto sobre a imagem original.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
|-----------|-------------|--------------|-------------|-------|
| `imagens` | A imagem de entrada ou lote de imagens para desenhar o texto. | IMAGE | Sim | |
| `texto` | A string de texto a ser sobreposta. Suporta caracteres de nova linha (`\n`) e tabulação (`\t`). Padrão: "" | STRING | Sim | |
| `tamanho_da_fonte` | Tamanho da fonte como porcentagem da altura da imagem. Padrão: 5.0 | FLOAT | Sim | 0.5 a 50.0 |
| `cor` | Cor do texto. Padrão: "#ffffff" (branco) | STRING | Sim | |
| `posição` | Posição vertical do texto na imagem. Padrão: "top" | COMBO | Sim | "top"<br>"bottom" |
| `alinhamento` | Alinhamento horizontal do texto. Padrão: "left" | COMBO | Sim | "left"<br>"center"<br>"right" |
| `contorno` | Desenhar um contorno preto ao redor do texto. Padrão: Verdadeiro | BOOLEAN | Sim | |

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
|---------------|-------------|--------------|
| `imagens` | A imagem ou lote de imagens com o texto sobreposto composto sobre elas. | IMAGE |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TextOverlay/pt-BR.md)

---
**Source fingerprint (SHA-256):** `baffaa4ec9d3565e3533673658399271234def8c49e2e4a5f16767ec3f98cb22`
