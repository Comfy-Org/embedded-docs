# TripoSplat Pré-processar Imagem

Este nó recorta cada imagem de entrada para um quadrado centralizado em fundo preto e adiciona preenchimento (padding) para atingir o tamanho de saída especificado. Ele foi projetado para preparar imagens para o modelo 3D TripoSplat, garantindo enquadramento quadrado consistente e erosão opcional do alfa mate (alpha matte) para evitar artefatos nas bordas.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Faixa |
|-----------|-------------|-----------|----------|-------|
| `imagem` | A(s) imagem(ns) de entrada para pré-processar. | IMAGE | Sim | - |
| `mask` | Máscara alfa da imagem, usada para determinar a região de recorte. | MASK | Sim | - |
| `raio_de_erosão` | Erosão do alfa mate por este raio de pixel antes do recorte (evita vazamento de borda). Padrão: 1. Defina como 0 para desativar a erosão. | INT | Sim | 0 a 16 |
| `tamanho` | Tamanho quadrado da imagem. O modelo é treinado em 1024; outros tamanhos funcionam, mas ficam fora da distribuição. Padrão: 1024. | INT | Sim | 256 a 4096 (step of 16) |

**Observação:** O parâmetro `mask` é obrigatório e deve ser fornecido. Se a máscara tiver um tamanho de lote diferente do da imagem, ela é repetida automaticamente para corresponder. Se as dimensões da máscara forem diferentes das da imagem, a máscara é redimensionada para corresponder à imagem usando interpolação bilinear. O tamanho de saída é automaticamente arredondado para baixo até o múltiplo de 16 mais próximo (mínimo 16) para garantir compatibilidade com os requisitos de patch do DINOv3 e de stride da VAE do Flux2. O nó gera um erro se a máscara não contiver pixels de primeiro plano (máscara vazia). Quando `erode_radius` é 0, nenhuma erosão é aplicada. O recorte quadrado é centralizado na caixa delimitadora alfa da máscara e dimensionado para 1,2 vezes a maior dimensão da caixa delimitadora; qualquer área fora dos limites da imagem é preenchida com preto.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `imagem` | A(s) imagem(ns) pré-processada(s) recortada(s) em um quadrado centralizado sobre fundo preto com preenchimento, na resolução `size` solicitada. | IMAGE |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoSplatPreprocessImage/pt-BR.md)

---
**Source fingerprint (SHA-256):** `ec66941846398ee6637576b11ae9d2f9576f6b05ed2ef730cdbf99a68fe9b838`
