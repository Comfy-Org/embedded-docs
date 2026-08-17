# TripoSplat Pré-processar Imagem

Este nó recorta cada imagem de entrada para um quadrado centralizado sobre fundo preto e, em seguida, adiciona preenchimento para atingir o tamanho de saída especificado. Ele foi projetado para preparar imagens para o modelo 3D TripoSplat, garantindo enquadramento quadrado consistente e erosão opcional do canal alfa para evitar artefatos nas bordas.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Faixa |
|-----------|-------------|---------------|-------------|-------|
| `image` | A(s) imagem(ns) de entrada para pré-processamento | IMAGE | Sim | - |
| `mask` | Máscara alfa para a imagem, usada para determinar a região de recorte | MASK | Sim | - |
| `erode_radius` | Eroda o canal alfa por este raio de pixels antes do recorte (evita sangramento nas bordas). Padrão: 1 | INT | Sim | 0 a 16 |
| `size` | Tamanho da imagem quadrada. O modelo é treinado em 1024; outros tamanhos funcionam, mas estão fora da distribuição. Padrão: 1024 | INT | Sim | 256 a 4096 (passo de 16) |

**Nota:** A entrada `mask` é obrigatória e deve ser fornecida. Se a máscara tiver um tamanho de lote diferente da imagem, ela é automaticamente repetida para corresponder. Se as dimensões da máscara diferirem das dimensões da imagem, a máscara é redimensionada para corresponder à imagem usando interpolação bilinear. O tamanho da saída é automaticamente arredondado para baixo até o múltiplo de 16 mais próximo, para garantir compatibilidade com os requisitos de passo do patch DINOv3 e do VAE Flux2. Um erro é gerado se a máscara não contiver pixels de primeiro plano.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|---------------|-------------|---------------|
| `image` | A(s) imagem(ns) pré-processada(s) recortada(s) em um quadrado centralizado sobre fundo preto com preenchimento | IMAGE |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoSplatPreprocessImage/pt-BR.md)

---
**Source fingerprint (SHA-256):** `ec66941846398ee6637576b11ae9d2f9576f6b05ed2ef730cdbf99a68fe9b838`
