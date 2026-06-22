# CLIPAdd

O nó CLIPAdd combina dois modelos CLIP mesclando seus patches de chave. Ele cria uma cópia do primeiro modelo CLIP e, em seguida, adiciona a maioria dos patches de chave do segundo modelo, excluindo IDs de posição e parâmetros de escala logit. Isso permite combinar características de diferentes modelos CLIP, preservando a estrutura do primeiro modelo.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Tipo de Entrada | Padrão | Faixa |
| --- | --- | --- | --- | --- | --- |
| `clip1` | O modelo CLIP principal que será usado como base para a mesclagem | CLIP | Obrigatório | - | - |
| `clip2` | O modelo CLIP secundário que fornece patches adicionais a serem adicionados | CLIP | Obrigatório | - | - |

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `CLIP` | Retorna um modelo CLIP mesclado combinando características de ambos os modelos de entrada | CLIP |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPAdd/pt-BR.md)

---
**Source fingerprint (SHA-256):** `935d450d25d90dc623e3f2b39b251359a9066c9e1fdd2a70384982fb26a21864`
