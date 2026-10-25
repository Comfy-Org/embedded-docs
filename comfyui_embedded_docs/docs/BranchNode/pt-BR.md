# Branch

Branch seleciona uma entre várias entradas conectadas pelo nome e a repassa para a saída. Ele funciona como um comutador preguiçoso: apenas a ramificação selecionada é avaliada, então as demais ramificações podem permanecer desconectadas ou conter saídas que você não deseja calcular. Cada nova conexão adiciona outra entrada de ramificação, as entradas podem ser renomeadas ao clicar duas vezes nelas, e a ramificação ativa é escolhida no seletor `branch`.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `autogrow` | As ramificações conectadas. Cada conexão adiciona uma nova entrada de ramificação, até 32; todas as ramificações devem usar o mesmo tipo de dados, que se torna o tipo de saída. | AUTOGROW | Sim | 1 a 32 ramificações |
| `branch` | Nome da ramificação repassada para a saída. As opções são os nomes das entradas de ramificação conectadas, e uma entrada pode ser renomeada ao clicar duas vezes nela. | STRING | Sim | Nomes das ramificações conectadas |
| `branch_names` | Lista interna dos nomes das ramificações conectadas, mantida em sincronia pelo frontend. Ela mapeia o nome selecionado para sua ramificação e não deve ser editada manualmente. | ARRAY | Sim | - |

**Nota:** Apenas a ramificação selecionada é solicitada, então as demais ramificações não são avaliadas. O nó lança um erro quando o nome selecionado não está conectado.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `output` | O valor da ramificação selecionada, repassado sem alterações. | MATCH_TYPE |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BranchNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `2b4dca360c1b459a9f05eb54fedb7cdea6842fb0c606ee6f937ed00f715ee23a`
