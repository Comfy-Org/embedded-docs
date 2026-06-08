Esta documentação foi gerada por IA. Se você encontrar algum erro ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MediaPipeFaceMask/en.md)

## Visão Geral

Este nó cria uma máscara binária (uma imagem em preto e branco) com base nos pontos faciais detectados pelo MediaPipe. Ele desenha formas poligonais preenchidas para cada região facial detectada, produzindo uma máscara por quadro em um lote. Quando múltiplos rostos são detectados no mesmo quadro, suas máscaras são combinadas em uma única máscara.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `face_landmarks` | Os dados de pontos faciais de um nó de detecção facial MediaPipe. | FACE_LANDMARKS | Sim | - |
| `regions` | Seleciona quais regiões faciais incluir na máscara. `"all"` cria uma máscara a partir da união de todas as regiões faciais (contorno facial, lábios, olhos, íris). `"custom"` permite ativar ou desativar cada região individualmente. Padrão: `"all"` | COMBO | Sim | `"all"`<br>`"custom"` |

Quando `regions` está definido como `"custom"`, os seguintes parâmetros booleanos adicionais ficam disponíveis:

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `face_oval` | Incluir a região do contorno facial na máscara. Padrão: Verdadeiro | BOOLEAN | Não | Verdadeiro/Falso |
| `lips` | Incluir a região dos lábios na máscara. Padrão: Verdadeiro | BOOLEAN | Não | Verdadeiro/Falso |
| `eyes` | Incluir a região dos olhos na máscara. Padrão: Verdadeiro | BOOLEAN | Não | Verdadeiro/Falso |
| `irises` | Incluir a região das íris na máscara. Padrão: Verdadeiro | BOOLEAN | Não | Verdadeiro/Falso |

**Nota:** Ao usar o modo `"all"`, a máscara inclui todas as regiões combinadas. Como o contorno facial envolve as outras regiões, selecionar `"all"` produz efetivamente o mesmo resultado que selecionar apenas o contorno facial.

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `MASK` | Um tensor de máscara binária onde as regiões faciais são brancas (valor 1.0) e o fundo é preto (valor 0.0). A máscara tem as mesmas dimensões da imagem de entrada e contém uma máscara por quadro no lote. | MASK |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MediaPipeFaceMask/pt-BR.md)

---
**Source fingerprint (SHA-256):** `92270002a42ed59bc75e676a6881e1899186d3c8a1bb4dd4c0d39b3762b5bb66`
