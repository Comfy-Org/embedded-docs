# LatentApplyOperation

O nó LatentApplyOperation aplica uma operação especificada às amostras latentes. Ele recebe dados latentes e uma operação como entradas, copia as amostras latentes de entrada, aplica a operação ao tensor latente e retorna os dados latentes modificados. Este nó permite transformar ou manipular representações latentes no seu fluxo de trabalho.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `samples` | As amostras latentes a serem processadas pela operação | LATENT | Sim | - |
| `operation` | A operação a ser aplicada às amostras latentes | LATENT_OPERATION | Sim | - |

Observação: Este nó está marcado como experimental. A operação é aplicada ao tensor latente armazenado sob a chave `samples` da estrutura latente. As amostras latentes de entrada são copiadas antes da aplicação da operação, portanto os dados latentes de entrada originais não são modificados.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `output` | As amostras latentes modificadas após a aplicação da operação | LATENT |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LatentApplyOperation/pt-BR.md)

---
**Source fingerprint (SHA-256):** `cba55d019793fde8dcc0d4aeb4eb6020b6149f523c6bffc65d73c533aa2e2c6c`
