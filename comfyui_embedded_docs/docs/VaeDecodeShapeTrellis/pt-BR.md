# VaeDecodeShapeTrellis

Este nó decodifica representações latentes de forma Trellis2 em uma malha 3D. Ele usa uma VAE para converter dados latentes de forma esparsa em geometria de malha e também gera dados de subdivisão de forma produzidos durante a decodificação. O nó suporta entradas latentes únicas e em lote e ajusta automaticamente a orientação da malha para o sistema de coordenadas esperado.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Intervalo |
|-----------|-------------|--------------|-------------|-----------|
| `samples` | As amostras latentes a serem decodificadas, incluindo o tensor de amostra e os dados de coordenadas esparsas. O dicionário latente também pode conter campos opcionais: `coord_counts` para formas em lote, `coord_resolution` para controlar a resolução da malha e `model_frame` para orientação das coordenadas. | LATENT | Sim | Nenhum |
| `vae` | O modelo VAE usado para decodificar o latente de forma em uma malha. | VAE | Sim | Nenhum |

### Notas sobre `samples`

- A entrada `samples` é um dicionário latente que deve conter o tensor `samples` e as coordenadas esparsas `coords`.
- Se `coord_counts` estiver presente, ele deve ser um tensor 1D de inteiros não negativos, e a soma de todas as contagens deve ser igual ao número total de linhas de coordenadas. Cada contagem representa uma forma no lote.
- Se `coord_resolution` for fornecido, a resolução da malha é calculada como `coord_resolution * 16`. Caso contrário, o buffer de resolução integrado da VAE é usado (valor padrão: 1024).
- Se `model_frame` estiver definido como `"z_up"`, os vértices da malha decodificada são rotacionados de um sistema de coordenadas Z-up para a convenção Y-up usada pelo glTF. O valor padrão é `"y_up"`.

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
|---------------|-------------|--------------|
| `mesh` | A malha 3D decodificada, contendo posições de vértices e índices de faces. | MESH |
| `shape_subdivides` | Dados de subdivisão de forma produzidos em cada etapa do processo de decodificação. | SHAPE_SUBDIVIDES |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VaeDecodeShapeTrellis/pt-BR.md)

---
**Source fingerprint (SHA-256):** `50f1b8200bd750671473278aaf94e6b08d6f9a6a72d5d1dc882ea7ab87084681`
