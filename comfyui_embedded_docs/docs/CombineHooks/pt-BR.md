> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CombineHooks/pt-BR.md)

O nó Combine Hooks [2] mescla dois grupos de hooks em um único grupo combinado. Ele recebe duas entradas opcionais de hooks e as combina usando a funcionalidade de combinação de hooks do ComfyUI. Isso permite consolidar múltiplas configurações de hooks para um processamento mais simplificado.

## Entradas

| Parâmetro | Tipo de Dados | Obrigatório | Intervalo | Descrição |
|-----------|---------------|-------------|-----------|-----------|
| `hooks_A` | HOOKS | Não | - | Primeiro grupo de hooks a ser combinado |
| `hooks_B` | HOOKS | Não | - | Segundo grupo de hooks a ser combinado |

**Observação:** Ambas as entradas são opcionais, mas pelo menos um grupo de hooks deve ser fornecido para que o nó funcione. Se apenas um grupo de hooks for fornecido, ele será retornado inalterado.

## Saídas

| Nome da Saída | Tipo de Dados | Descrição |
|---------------|---------------|-----------|
| `hooks` | HOOKS | Grupo de hooks combinado contendo todos os hooks de ambos os grupos de entrada |

---
**Source fingerprint (SHA-256):** `558ceef1cebedd0b7e045b7d1eb1afa4316ea6a3c35f982968af132dca164126`
