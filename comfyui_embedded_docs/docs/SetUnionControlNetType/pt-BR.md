# DefinirTipoUnionControlNet

O nó SetUnionControlNetType permite definir o tipo de controle de uma rede de controle usada para condicionamento. Ele recebe uma rede de controle existente, cria uma cópia modificada dela e armazena o tipo de controle selecionado nessa cópia, de modo que a original permaneça inalterada.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `control_net` | A rede de controle a ser copiada e modificada com o tipo de controle selecionado | CONTROL_NET | Sim | - |
| `type` | O tipo de controle a ser aplicado à rede de controle copiada. Selecione "auto" para deixar o tipo de controle indefinido, ou escolha um tipo específico entre os tipos disponíveis de rede de controle união (padrão: "auto") | COMBO | Sim | `"auto"`<br>`"openpose"`<br>`"depth"`<br>`"hed/pidi/scribble/ted"`<br>`"canny/softedge"`<br>`"normal/bms"`<br>`"seg"`<br>`"inpaint"`<br>`"lineart"`<br>`"s4"`<br>`"tile/color"`<br>`"blur"`<br>`"identity"` |

Nota: Quando `type` é "auto", a lista de tipos de controle na rede de controle copiada é limpa. Quando um tipo específico é selecionado, a rede de controle copiada armazena o número correspondente do tipo.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `control_net` | A cópia modificada da rede de controle com o tipo de controle selecionado aplicado | CONTROL_NET |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SetUnionControlNetType/pt-BR.md)

---
**Source fingerprint (SHA-256):** `db4b1a3cebafcff2be3172faa09cecbd5e19331376491c491cbe359013ed3da3`
