> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Flux2ImageNode/pt-BR.md)

# Visão Geral

Gere imagens usando os modelos Flux.2 [pro] ou Flux.2 [max] a partir de um prompt de texto e imagens de referência opcionais. Este nó envia sua solicitação para a API BFL, consulta o resultado e retorna a imagem gerada como um tensor.

# Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `prompt` | STRING | Sim | N/A | Prompt para geração ou edição da imagem (padrão: string vazia). |
| `model` | COMBO | Sim | `"Flux.2 [pro]"`<br>`"Flux.2 [max]"` | A versão do modelo Flux.2 a ser utilizada. Selecionar um modelo desbloqueia parâmetros adicionais para largura, altura e imagens de referência opcionais. |
| `seed` | INT | Sim | 0 a 18446744073709551615 | A semente aleatória usada para criar o ruído. Pode ser configurada para randomizar após cada geração (padrão: 0). |

**Parâmetros Adicionais (desbloqueados pela seleção de `model`):**

Ao selecionar um modelo, os seguintes parâmetros ficam disponíveis:

| Parâmetro | Tipo de Dado | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `model.width` | INT | Sim | 256 a 1440 | A largura da imagem gerada em pixels. |
| `model.height` | INT | Sim | 256 a 1440 | A altura da imagem gerada em pixels. |
| `model.images` | IMAGE | Não | 0 a 8 imagens | Imagens de referência opcionais para guiar a geração. Suporta no máximo 8 imagens. |

**Restrições:**
- O número máximo de imagens de referência é 8. Se mais de 8 imagens forem fornecidas, um erro será gerado.
- Os valores de `model.width` e `model.height` afetam o custo da geração (consulte a lógica do selo de preço no código-fonte).

# Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|-------------|-----------|-------------|
| `image` | IMAGE | A imagem gerada como um tensor, baixada do resultado da API BFL. |