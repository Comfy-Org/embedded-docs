# BriaRelight

Este nó altera a atmosfera e a direção da iluminação de uma imagem usando Bria. A imagem é renderizada novamente pelo Bria, portanto o resultado não fica alinhado pixel a pixel com a entrada; todo o quadro é regenerado com cerca de 1 megapixel.

## Entradas

### Entradas comuns

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `image` | A imagem cuja iluminação é alterada. Qualquer canal alfa é descartado antes de a imagem ser enviada. | IMAGE | Sim | - |
| `light_type` | Atmosfera de iluminação a aplicar. | COMBO | Sim | `"midday"`<br>`"blue hour light"`<br>`"low-angle sunlight"`<br>`"sunrise light"`<br>`"spotlight on subject"`<br>`"overcast light"`<br>`"soft overcast daylight lighting"`<br>`"cloud-filtered lighting"`<br>`"fog-diffused lighting"`<br>`"moonlight lighting"`<br>`"starlight nighttime"`<br>`"soft bokeh lighting"`<br>`"harsh studio lighting"` |
| `light_direction` | De onde a luz vem. Atmosferas de luz dura, como midday, spotlight on subject e harsh studio lighting, são as que mais reagem a isso. | COMBO | Sim | `"front"`<br>`"side"`<br>`"bottom"`<br>`"top-down"` |
| `moderation` | Configurações de moderação. Selecione `"true"` para exibir as opções de moderação, ou `"false"` para executar sem elas. | DYNAMIC_COMBO | Sim | `"false"`<br>`"true"` |

### Entradas de moderação

Estas opções aparecem quando `moderation` está definido como `"true"`.

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `visual_input_moderation` | Ativa a moderação de conteúdo na imagem de entrada. Padrão: false. | BOOLEAN | Não | `true`<br>`false` |
| `visual_output_moderation` | Ativa a moderação de conteúdo na imagem de saída gerada. Padrão: false. | BOOLEAN | Não | `true`<br>`false` |

Observação: o Bria renderiza novamente todo o quadro com cerca de 1 megapixel, portanto o resultado não fica alinhado pixel a pixel com a entrada.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `image` | A imagem reiluminada retornada pelo Bria. | IMAGE |
| `structured_prompt` | Descrição estruturada da imagem editada, para uma edição posterior com Bria FIBO Image Edit. | STRING |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BriaRelight/pt-BR.md)

---
**Source fingerprint (SHA-256):** `21fbe2186c99a7e8d99d5659ac25c3ab1a757492916dba4135487d4b293cb4f6`
