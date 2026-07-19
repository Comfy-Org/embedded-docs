# Desenhar Sobreposição de Texto

Este nó desenha texto sobre uma imagem ou um lote de imagens. Ele cria uma sobreposição de texto com tamanho de fonte, cor, posição, alinhamento e contorno opcional personalizáveis, e então compõe o texto sobre as imagens originais.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
|-----------|-----------|--------------|-------------|-------|
| `imagens` | A imagem de entrada ou lote de imagens para desenhar o texto | IMAGE | Sim | |
| `texto` | O texto a ser sobreposto na imagem (padrão: "") | STRING | Sim | |
| `tamanho_da_fonte` | Tamanho da fonte como porcentagem da altura da imagem (padrão: 5.0) | FLOAT | Sim | 0.5 a 50.0 |
| `cor` | Cor do texto (padrão: "#ffffff") | STRING | Sim | |
| `posição` | Posição vertical do texto na imagem (padrão: "top") | COMBO | Sim | `"top"`<br>`"bottom"` |
| `alinhamento` | Alinhamento horizontal do texto (padrão: "left") | COMBO | Sim | `"left"`<br>`"center"`<br>`"right"` |
| `contorno` | Desenhar um contorno preto ao redor do texto (padrão: True) | BOOLEAN | Sim | |

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
|---------------|-----------|--------------|
| `imagens` | As imagens de entrada com a sobreposição de texto composta sobre elas | IMAGE |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TextOverlay/pt-BR.md)

---
**Source fingerprint (SHA-256):** `baffaa4ec9d3565e3533673658399271234def8c49e2e4a5f16767ec3f98cb22`
