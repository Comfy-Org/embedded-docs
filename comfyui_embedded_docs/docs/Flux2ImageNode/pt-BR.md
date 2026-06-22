# Flux.2 Image

Gere imagens usando o modelo Flux.2 [pro] ou Flux.2 [max] a partir de um prompt de texto e imagens de referência opcionais. Este nó envia sua solicitação para a API BFL, consulta o resultado e retorna a imagem gerada como um tensor.

# Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `prompt` | Prompt para geração ou edição da imagem (padrão: string vazia). | STRING | Sim | N/A |
| `modelo` | A versão do modelo Flux.2 a ser utilizada. Selecionar um modelo desbloqueia parâmetros adicionais para largura, altura e imagens de referência opcionais. | COMBO | Sim | `"Flux.2 [pro]"`<br>`"Flux.2 [max]"` |
| `semente` | A semente aleatória usada para criar o ruído. Pode ser configurada para randomizar após cada geração (padrão: 0). | INT | Sim | 0 a 18446744073709551615 |

**Parâmetros Adicionais (desbloqueados pela seleção do `model`):**

Ao selecionar um modelo, os seguintes parâmetros ficam disponíveis:

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `model.width` | A largura da imagem gerada em pixels. | INT | Sim | 256 a 1440 |
| `model.height` | A altura da imagem gerada em pixels. | INT | Sim | 256 a 1440 |
| `model.images` | Imagens de referência opcionais para guiar a geração. Suporta no máximo 8 imagens. | IMAGE | Não | 0 a 8 imagens |

**Restrições:**
- O número máximo de imagens de referência é 8. Se mais de 8 imagens forem fornecidas, um erro será gerado.
- Os valores de `model.width` e `model.height` afetam o custo da geração (veja a lógica do selo de preço no código-fonte).

# Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `image` | A imagem gerada como um tensor, baixada do resultado da API BFL. | IMAGE |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Flux2ImageNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `664ddf45d42f64e4882cc959018f7874915325f2d46519c6bb9a0c5a501228f7`
