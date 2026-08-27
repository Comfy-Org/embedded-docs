# EmptyTrellis2LatentStructure

Este nó cria uma estrutura latente vazia para o modelo Trellis2, onde todos os valores são definidos como zero. Ele produz um tensor latente 3D em branco com 32 canais na resolução de 16×16×16, dimensionado para o número especificado de itens no lote.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|---------------|-------------|-----------|
| `batch_size` | O número de imagens latentes no lote (padrão: 1). | INT | Sim | 1 a 4096 |

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|---------------|-------------|---------------|
| `LATENT` | Uma estrutura latente Trellis2 vazia. As amostras são um tensor preenchido com zeros com o formato (batch_size, 32, 16, 16, 16), e o tipo latente é definido como "trellis2". | LATENT |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyTrellis2LatentStructure/pt-BR.md)

---
**Source fingerprint (SHA-256):** `a551f0e05e58b025df03a3babee36f57fd900b5e02926fbdbd67a512ebead078`
