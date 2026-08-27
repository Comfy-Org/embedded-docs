# Flux.2 Image

Flux.2 Image

Gere imagens usando o modelo Flux.2 [pro] ou Flux.2 [max] a partir de um prompt de texto e imagens de referência opcionais. Este nó envia sua solicitação para a API BFL, consulta o resultado e retorna a imagem gerada como um tensor.

## Entradas

### Entradas comuns

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `modelo` | A versão do modelo Flux.2 a ser usada. Selecionar um modelo desbloqueia parâmetros adicionais para largura, altura e imagens de referência opcionais. | DYNAMIC_COMBO | Sim | "Flux.2 [pro]"<br>"Flux.2 [max]" |
| `prompt` | Prompt para a geração ou edição da imagem (padrão: string vazia). | STRING | Sim | N/A |
| `semente` | A semente aleatória usada para criar o ruído. Pode ser configurada para randomizar após cada geração (padrão: 0). | INT | Sim | 0 a 18446744073709551615 |

### Entradas do Flux.2 [pro] e Flux.2 [max]

Compartilhado por ambos os modelos — os conjuntos de parâmetros são idênticos.

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `largura` | A largura da imagem gerada em pixels (padrão: 1024). | INT | Sim | 256 a 2048 (passo 32) |
| `altura` | A altura da imagem gerada em pixels (padrão: 768). | INT | Sim | 256 a 2048 (passo 32) |

### Entradas de referência

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `model.images` | Imagem(ns) de referência opcional(is) para geração imagem-para-imagem. Até 8 imagens. Slot expansível: conecte de 1 a 8 itens (`image_1`...`image_8`). | IMAGE | Não | 0 a 8 imagens |

**Observação:**
- O número máximo de imagens de referência é 8. Se mais de 8 imagens forem fornecidas, um erro será gerado.
- Os valores de `model.width` e `model.height` afetam o custo da geração. O custo também depende do modelo selecionado e se imagens de referência são fornecidas.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `image` | A imagem gerada como um tensor, baixada do resultado da API BFL. | IMAGE |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Flux2ImageNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `2994564757e1c66ac6da7b45d227b27ceb0020ac6fc9e8cbe2b53fe9f70bc195`
