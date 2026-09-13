# BriaRestorePhoto

Este nó repara fotografias antigas ou danificadas por meio da API da Bria. Ele remove granulação, arranhões e desfoque, neutraliza desvios de cor relacionados à idade, pode recortar suportes de cartão e bordas de estúdio, e redesenha rostos. O resultado é renderizado novamente com cerca de 1 megapixel, portanto não fica alinhado pixel a pixel com a entrada.

## Entradas

### Entradas comuns

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `image` | A fotografia a ser reparada. O canal alfa é descartado antes do upload. | IMAGE | Sim | - |
| `moderation` | Configurações de moderação para a solicitação. Selecionar `"true"` revela dois controles booleanos adicionais; selecionar `"false"` não envia sinalizadores de moderação. Padrão: `"false"`. | DYNAMIC_COMBO | Sim | `"false"`<br>`"true"` |

### Entradas de moderação

Essas entradas aparecem apenas quando `moderation` está definido como `"true"`.

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `visual_input_moderation` | Habilita a moderação de conteúdo visual na imagem de entrada. Padrão: false. | BOOLEAN | Não | true<br>false |
| `visual_output_moderation` | Habilita a moderação de conteúdo visual na imagem de saída. Padrão: false. | BOOLEAN | Não | true<br>false |

**Observação:** O nó renderiza novamente o quadro inteiro com cerca de 1 megapixel, portanto o resultado não fica alinhado pixel a pixel com a entrada. Use o nó Bria Increase Resolution para ampliar a imagem em vez deste nó.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `IMAGE` | A fotografia reparada retornada pela Bria. | IMAGE |
| `structured_prompt` | Descrição estruturada da imagem editada, para uma edição de acompanhamento com Bria FIBO Image Edit. | STRING |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BriaRestorePhoto/pt-BR.md)

---
**Source fingerprint (SHA-256):** `387ec3e049464f185e27f79d160ade2a4170ab238853064c008892d84523fa68`
