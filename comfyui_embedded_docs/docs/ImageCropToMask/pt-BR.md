# ImageCropToMask

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Faixa |
|-----------|-------------|-----------|----------|-------|
| `images` | A imagem de entrada ou lote de imagens a serem recortadas. | IMAGE | Sim | — |
| `masks` | A máscara ou lote de máscaras que define a área do assunto. Uma única máscara é aplicada a todas as imagens; caso contrário, o tamanho do lote de máscaras deve corresponder ao tamanho do lote de imagens. Se a resolução da máscara for diferente da resolução da imagem, a máscara é redimensionada automaticamente para corresponder. | MASK | Sim | — |
| `width` | Largura da saída em pixels. (padrão: 1024) | INT | Sim | 64 to 4096 (step 8) |
| `height` | Altura da saída em pixels. (padrão: 1024) | INT | Sim | 64 to 4096 (step 8) |
| `pad_factor` | Margem extra ao redor da caixa delimitadora da máscara como um multiplicador. (padrão: 1.0) | FLOAT | Sim | 1.0 to 2.0 (step 0.01) |
| `grow_mask` | Aumenta ou diminui a máscara por este número de pixels antes do recorte. Valores positivos expandem a máscara, valores negativos a reduzem. (padrão: 0) | INT | Sim | -32 to 32 (step 1) |
| `background` | Cor de fundo atrás do assunto mascarado. (padrão: #000000) | COLOR | Sim | — |

Nota: A região de recorte é centralizada na caixa delimitadora da máscara e sua proporção corresponde a `width` / `height`. O nó detecta e corrige automaticamente uma máscara invertida (pixels de primeiro plano nas bordas, fundo no centro). Se a máscara não contiver pixels de primeiro plano, o nó tenta a máscara invertida; se esta também estiver vazia, ele registra um aviso e recorta a imagem inteira. Um erro é gerado quando o tamanho do lote de máscaras não corresponde ao tamanho do lote de imagens e não é uma única máscara.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `images` | As imagens compostas recortadas (assunto mascarado sobre a cor de fundo escolhida), redimensionadas para `width` x `height`. O tamanho do lote corresponde ao lote de imagens de entrada. | IMAGE |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageCropToMask/pt-BR.md)

---
**Source fingerprint (SHA-256):** `fcc14b5db7318699526dd544d404f78f9d1ab362b73769276f113f2b1062b214`
