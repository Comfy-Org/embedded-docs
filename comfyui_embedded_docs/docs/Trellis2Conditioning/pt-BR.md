# Trellis2Conditioning

O nó Trellis2Conditioning converte uma imagem de entrada em dados de condicionamento para o modelo TRELLIS.2. Ele usa um modelo de visão CLIP para codificar a imagem em dois conjuntos de características (nas escalas 512 e 1024) e os empacota como um par de condicionamento positivo, além de criar um par de condicionamento negativo preenchido com zeros, que serve como referência vazia.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `clip_vision_model` | O modelo de visão CLIP usado para codificar a imagem em características de condicionamento. | CLIP_VISION | Sim | Qualquer modelo de visão CLIP disponível |
| `imagem` | Imagem pré-processada de ImageCropToMask (pad_factor=1.0 para TRELLIS.2). | IMAGE | Sim | Qualquer imagem |

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `positivo` | Condicionamento contendo as características da imagem codificadas nas escalas 512 e 1024, usado como o condicionamento positivo para o modelo TRELLIS.2. | CONDITIONING |
| `negativo` | Condicionamento preenchido com zeros, com a mesma forma do condicionamento positivo, usado como referência negativa vazia. | CONDITIONING |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Trellis2Conditioning/pt-BR.md)

---
**Source fingerprint (SHA-256):** `467698e58558ceca9ac633d63aacf360a1eb674ac4ebd47de7423f85e62c0fe6`
