# DefinirTipoUnionControlNet

O nó SetUnionControlNetType permite escolher qual tipo de controle uma rede de controle utiliza. Ele recebe uma rede de controle existente e cria uma cópia modificada com o tipo de controle selecionado, mantendo a rede de controle original inalterada. Quando "auto" é selecionado, o tipo de controle armazenado é limpo para que o tipo possa ser detectado automaticamente.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `control_net` | A rede de controle a ser modificada com uma nova configuração de tipo | CONTROL_NET | Sim | - |
| `tipo` | O tipo de rede de controle a ser aplicado. Use "auto" para detecção automática de tipo ou selecione um tipo específico de rede de controle nas opções disponíveis (padrão: "auto") | COMBO | Sim | `"auto"`<br>`"openpose"`<br>`"depth"`<br>`"hed/pidi/softedge"`<br>`"canny"`<br>`"scribble"`<br>`"seg"`<br>`"tile"`<br>`"inpaint"`<br>`"lineart"`<br>`"blur"`<br>`"mlsd"`<br>`"normalbae"`<br>`"mask"` |

Quando `type` está definido como `"auto"`, o nó limpa o tipo de controle armazenado para que o tipo possa ser detectado automaticamente. Quando um tipo específico é selecionado, o nó armazena o tipo de controle correspondente na cópia da rede de controle.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `control_net` | A rede de controle modificada com a configuração de tipo especificada aplicada | CONTROL_NET |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SetUnionControlNetType/pt-BR.md)

---
**Source fingerprint (SHA-256):** `db4b1a3cebafcff2be3172faa09cecbd5e19331376491c491cbe359013ed3da3`
