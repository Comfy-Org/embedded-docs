# BriaReseason

Este nó move uma imagem para uma estação diferente usando Bria. Toda a cena é renderizada novamente, então o cenário pode mudar além da própria estação. A Bria renderiza novamente o quadro inteiro em cerca de 1 megapixel, então o resultado não fica alinhado pixel a pixel com a entrada.

## Entradas

### Entradas comuns

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `image` | A imagem a ser movida para outra estação. Qualquer canal alfa é removido antes que a imagem seja enviada. | IMAGE | Sim | - |
| `season` | Estação a aplicar. | COMBO | Sim | `"spring"`<br>`"summer"`<br>`"autumn"`<br>`"winter"` |
| `moderation` | Configurações de moderação. Seleciona se as opções de moderação de conteúdo estão configuradas para esta solicitação. | DYNAMIC_COMBO | Sim | `"false"`<br>`"true"` |

### Entradas de moderação

Essas opções aparecem quando `moderation` está definido como `"true"`.

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `visual_input_moderation` | Habilita a moderação de conteúdo na imagem de entrada (padrão: false). | BOOLEAN | Não | true<br>false |
| `visual_output_moderation` | Habilita a moderação de conteúdo na imagem de saída gerada (padrão: false). | BOOLEAN | Não | true<br>false |

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `IMAGE` | A imagem renderizada novamente na estação selecionada. | IMAGE |
| `structured_prompt` | Descrição estruturada da imagem editada, para uma edição subsequente com Bria FIBO Image Edit. | STRING |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BriaReseason/pt-BR.md)

---
**Source fingerprint (SHA-256):** `3bb9ee1c00c91759cc6f972e2ba8708ae73a186f4b66bf6669937e561efad0a4`
