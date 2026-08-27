# ImageCropToMask

Recorta uma imagem para a caixa delimitadora da sua máscara, produzindo um assunto centralizado sobre uma cor de fundo sólida. O nó compõe a imagem mascarada sobre o fundo escolhido e redimensiona o resultado para as dimensões de saída especificadas, tornando-o adequado para pipelines 3D que esperam um assunto centralizado, sem fundo, em resolução fixa.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Faixa |
|-----------|-------------|-----------|----------|-------|
| `imagens` | A imagem de entrada ou lote de imagens a serem recortadas. | IMAGE | Sim | — |
| `máscaras` | A máscara ou lote de máscaras que define a área do assunto. Uma única máscara é aplicada a todas as imagens; caso contrário, o tamanho do lote de máscaras deve corresponder ao tamanho do lote de imagens. Se a resolução da máscara for diferente da resolução da imagem, a máscara é automaticamente redimensionada para corresponder. | MASK | Sim | — |
| `largura` | Largura de saída em pixels. (padrão: 1024) | INT | Sim | 64 a 4096 (passo 8) |
| `altura` | Altura de saída em pixels. (padrão: 1024) | INT | Sim | 64 a 4096 (passo 8) |
| `pad_factor` | Margem extra ao redor da caixa delimitadora da máscara como um multiplicador. (padrão: 1.0) | FLOAT | Sim | 1.0 a 2.0 (passo 0.01) |
| `grow_mask` | Expande ou contrai a máscara nessa quantidade de pixels antes do recorte. Valores positivos expandem a máscara, valores negativos a contraem. (padrão: 0) | INT | Sim | -32 a 32 (passo 1) |
| `plano de fundo` | Cor de fundo atrás do assunto mascarado. (padrão: #000000) | COLOR | Sim | — |

Nota: A região de recorte é centralizada na caixa delimitadora da máscara e sua proporção corresponde a `width` / `height`. O nó detecta e corrige automaticamente uma máscara invertida (pixels de primeiro plano nas bordas, fundo no centro). Se a máscara não contiver pixels de primeiro plano, o nó tenta a máscara invertida; se essa também estiver vazia, ele registra um aviso e recorta a imagem inteira. Um erro é gerado quando o tamanho do lote de máscaras não corresponde ao tamanho do lote de imagens e não é uma única máscara.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `imagens` | As imagens compostas recortadas (assunto mascarado sobre a cor de fundo escolhida), redimensionadas para `width` x `height`. O tamanho do lote corresponde ao lote de imagens de entrada. | IMAGE |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageCropToMask/pt-BR.md)

---
**Source fingerprint (SHA-256):** `fcc14b5db7318699526dd544d404f78f9d1ab362b73769276f113f2b1062b214`
