# TripoSplat Pré-processar Imagem

Este nó recorta cada imagem de entrada para um quadrado centralizado em fundo preto e, em seguida, adiciona preenchimento para atingir o tamanho de saída especificado. Ele foi projetado para preparar imagens para o modelo 3D TripoSplat, garantindo enquadramento quadrado consistente e erosão opcional do canal alfa para evitar artefatos nas bordas.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
|-----------|-----------|--------------|-------------|-------|
| `imagem` | A(s) imagem(ns) de entrada para pré-processar | IMAGE | Sim | - |
| `mask` | Máscara alfa para a imagem, usada para determinar a região de recorte | MASK | Sim | - |
| `raio_de_erosão` | Erodir o canal alfa por este raio em pixels antes do recorte (evita sangramento nas bordas). Padrão: 1 | INT | Sim | 0 a 16 |
| `tamanho` | Tamanho da imagem quadrada. O modelo é treinado em 1024; outros tamanhos funcionam, mas estão fora da distribuição. Padrão: 1024 | INT | Sim | 256 a 4096 (passo de 16) |

**Observação:** A entrada `mask` é obrigatória e deve ser fornecida. Se a máscara tiver um tamanho de lote diferente da imagem, ela é automaticamente repetida para corresponder. Se as dimensões da máscara diferirem das dimensões da imagem, a máscara é redimensionada para corresponder à imagem usando interpolação bilinear.

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
|---------------|-----------|--------------|
| `imagem` | A(s) imagem(ns) pré-processada(s) recortada(s) para um quadrado centralizado em fundo preto com preenchimento | IMAGE |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoSplatPreprocessImage/pt-BR.md)

---
**Source fingerprint (SHA-256):** `3f33dbc3a99ccb23ede767915a28fabdfa388edb8d5782edea3f8d03e5965b2a`
