# BriaReplaceImageBackground

Este nó substitui o plano de fundo de uma imagem por um novo gerado pela Bria. O novo plano de fundo pode ser descrito com um prompt de texto ou guiado por imagens de referência. Os pixels do sujeito são preservados enquanto o plano de fundo é gerado ao redor deles.

## Entradas

### Entradas comuns

| Parâmetro | Descrição | Tipo de dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `image` | A imagem de entrada cujo plano de fundo será substituído. | IMAGE | Sim | |
| `fundo` | Descreva o novo plano de fundo com um prompt ou guie-o com imagens de referência. | DYNAMIC_COMBO | Sim | `"prompt"`<br>`"reference images"` |
| `original_quality` | Retorna o tamanho exato em pixels da entrada em vez de dimensionar o resultado para cerca de 1 megapixel. Uma entrada grande, então, retorna uma imagem grande. (padrão: false) | BOOLEAN | Não | `true`<br>`false` |
| `semente` | A mesma seed geralmente retorna o mesmo plano de fundo; o refinamento automático do prompt ainda pode variá-lo. (padrão: 42) | INT | Não | 0 a 2147483647 |
| `moderação` | Configurações de moderação. (padrão: "false") | DYNAMIC_COMBO | Não | `"false"`<br>`"true"` |

### Entradas do prompt

Exibidas quando `background` está definido como `"prompt"`.

| Parâmetro | Descrição | Tipo de dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Descrição do novo plano de fundo. Um código de cor hexadecimal como #FF5733 produz um plano de fundo de cor sólida. Deve ter pelo menos 1 caractere. | STRING | Sim | |
| `mode` | `high_control` segue o prompt com mais fidelidade, `base` é um padrão equilibrado e `fast` troca detalhe por velocidade. | COMBO | Sim | `"high_control"`<br>`"base"`<br>`"fast"` |
| `refine_prompt` | Reescreve o prompt para melhores resultados, o que também traduz prompts que não estejam em inglês. Desative para enviar o prompt exatamente como escrito. (padrão: true) | BOOLEAN | Não | `true`<br>`false` |

### Entradas de imagens de referência

Exibidas quando `background` está definido como `"reference images"`.

| Parâmetro | Descrição | Tipo de dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `ref_images` | Slot expansível: conecte de 1 a 10 imagens que orientam o novo plano de fundo; elas não precisam ter o mesmo tamanho. Cada referência altera o resultado, então algumas consistentes superam muitas conflitantes. Uma entrada em lote conta uma vez por imagem. | IMAGE | Sim | 1 a 10 imagens |
| `enhance_ref_images` | Processamento extra das imagens de referência para melhores resultados. (padrão: true) | BOOLEAN | Não | `true`<br>`false` |

### Entradas de moderação

Exibidas quando `moderation` está definido como `"true"`.

| Parâmetro | Descrição | Tipo de dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `prompt_content_moderation` | Ativa a moderação para o conteúdo do prompt. (padrão: false) | BOOLEAN | Não | `true`<br>`false` |
| `visual_input_moderation` | Ativa a moderação para a entrada visual. (padrão: false) | BOOLEAN | Não | `true`<br>`false` |
| `visual_output_moderation` | Ativa a moderação para a saída visual. (padrão: false) | BOOLEAN | Não | `true`<br>`false` |

**Observação:** A entrada `ref_images` aceita no máximo 10 imagens; fornecer mais de 10 retorna um erro. O campo `prompt` deve conter pelo menos 1 caractere. Quando `original_quality` é false, a imagem de entrada é reduzida para cerca de 1 megapixel antes do processamento.

## Saídas

| Nome da saída | Descrição | Tipo de dados |
|-------------|-------------|-----------|
| `image` | A imagem com o novo plano de fundo. | IMAGE |
| `refined_prompt` | O prompt a partir do qual a Bria gerou; vazio no caminho de imagens de referência. | STRING |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BriaReplaceImageBackground/pt-BR.md)

---
**Source fingerprint (SHA-256):** `62c29d61983c9656d2ea2954518404c62d76961c3deba0e10d63e787d0b0b106`
