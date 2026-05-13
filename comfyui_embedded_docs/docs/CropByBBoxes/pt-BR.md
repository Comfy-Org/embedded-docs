> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CropByBBoxes/pt-BR.md)

O nó CropByBBoxes extrai e redimensiona regiões retangulares específicas de um lote de imagens de entrada. Ele utiliza coordenadas de caixas delimitadoras fornecidas para definir a área a ser recortada de cada imagem. As regiões recortadas são então redimensionadas para uma dimensão de saída especificada, com opções para esticar o recorte ou preenchê-lo para preservar sua proporção original.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Intervalo | Descrição |
|-----------|--------------|-------------|-----------|-----------|
| `imagem` | IMAGE | Sim | - | O lote de imagens de entrada a ser recortado. |
| `caixas delimitadoras` | BOUNDINGBOX | Sim | - | A lista de caixas delimitadoras que definem as regiões a serem recortadas. Esta entrada é forçada, ou seja, deve estar conectada. |
| `largura_de_saida` | INT | Não | 64 - 4096 | A largura para a qual cada recorte é redimensionado (padrão: 512). |
| `altura_de_saida` | INT | Não | 64 - 4096 | A altura para a qual cada recorte é redimensionado (padrão: 512). |
| `preenchimento` | INT | Não | 0 - 1024 | Preenchimento extra em pixels adicionado em cada lado da caixa delimitadora antes do recorte (padrão: 0). |
| `keep_aspect` | COMBO | Não | `"stretch"`<br>`"pad"` | Define se o recorte deve ser esticado para caber no tamanho de saída ou preenchido com pixels pretos para preservar sua proporção original (padrão: "stretch"). |

**Observação:** O nó processa um quadro de imagem por vez. Se várias caixas delimitadoras forem fornecidas para um único quadro, ele calcula uma única região de recorte que é a união (o menor retângulo que contém todas as caixas) de todas as caixas fornecidas. Se uma região de recorte calculada for inválida (por exemplo, largura ou altura zero), o nó criará um recorte alternativo a partir do centro-superior da imagem.

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|---------------|--------------|-----------|
| `imagem` | IMAGE | Todas as regiões recortadas e redimensionadas, empilhadas em um único lote de imagens. |

---
**Source fingerprint (SHA-256):** `9c0b3078405567911731c42e1873c57c77363e21ef6805769730667c811b0a0b`
