# Clarity AI Crystal Upscale

Amplie uma imagem com o Crystal Upscaler da Clarity AI, um upscaler de alta fidelidade que se mantém fiel ao original enquanto restaura rostos, pele e texturas finas. A imagem é enviada para a API da Clarity AI e o resultado ampliado é retornado como uma imagem.

Selecionar um `model` revela os parâmetros específicos desse modelo.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `model` | Modelo a ser usado. Selecionar um modelo revela os parâmetros específicos dele: `image`, `scale_factor` e `creativity`. | DYNAMIC_COMBO | Sim | `"crystal-upscaler"` |
| `image` | A imagem a ser ampliada. Deve conter exatamente uma imagem; lotes de imagens não são suportados. | IMAGE | Sim | N/A |
| `scale_factor` | Fator pelo qual multiplicar a largura e a altura da imagem. A saída é limitada a 100 megapixels (padrão: 2.0). | FLOAT | Sim | 1.0 a 200.0 (passo: 0.1) |
| `creativity` | Valores mais altos permitem que o modelo reconstrua mais detalhes em vez de preservar estritamente o original. Não tem efeito em imagens cujo lado menor tenha 256 pixels ou menos (padrão: 0). | INT | Sim | 0 a 10 |

**Nota:** A imagem de entrada deve ter pelo menos 2x2 pixels. A saída é limitada a 100 megapixels e 65535 pixels por lado; um resultado maior gera um erro, então use uma imagem menor ou um `scale_factor` mais baixo.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `IMAGE` | A imagem ampliada. | IMAGE |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ClarityCrystalUpscaleNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `38c90cf7054a93477ee63c356c3fdf8ba38c7edaf1a337da7ac366cd9d746d9e`
