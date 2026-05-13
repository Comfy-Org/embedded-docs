> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageCropV2/pt-BR.md)

O nó Image Crop extrai uma seção retangular de uma imagem de entrada. Você define a região a ser mantida especificando as coordenadas do canto superior esquerdo, sua largura e altura. O nó então retorna a porção recortada da imagem original.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Faixa | Descrição |
|-----------|--------------|-------------|-------|-----------|
| `imagem` | IMAGE | Sim | N/A | A imagem de entrada a ser recortada. |
| `região_de_corte` | BOUNDINGBOX | Sim | N/A | Define a área retangular a ser extraída da imagem. É especificada por `x` (início horizontal), `y` (início vertical), `width` (largura) e `height` (altura). Se a região definida ultrapassar as bordas da imagem, será automaticamente ajustada para caber dentro das dimensões da imagem. |

**Observação sobre Restrições de Região:** A região de recorte é automaticamente limitada para permanecer dentro dos limites da imagem de entrada. Se a coordenada `x` ou `y` especificada for maior que a largura ou altura da imagem, ela será definida para a posição máxima válida. A largura e altura do recorte resultante serão ajustadas para que a região não exceda as bordas da imagem.

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|---------------|--------------|-----------|
| `imagem` | IMAGE | A seção recortada da imagem de entrada original. |

---
**Source fingerprint (SHA-256):** `9d3543aa8396ae2ab0353accc3c89ae6be6495f6fdcefbb5439fa865a5d3059f`
