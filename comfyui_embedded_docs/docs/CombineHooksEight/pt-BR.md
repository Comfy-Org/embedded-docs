O nó Combinar Ganchos [8] mescla até oito grupos de ganchos diferentes em um único grupo de ganchos combinado. Ele recebe múltiplas entradas de ganchos e as combina usando a funcionalidade de combinação de ganchos do ComfyUI. Isso permite consolidar várias configurações de ganchos para processamento simplificado em fluxos de trabalho avançados.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Tipo de Entrada | Padrão | Faixa |
| --- | --- | --- | --- | --- | --- |
| `hooks_A` | Primeiro grupo de ganchos a combinar | HOOKS | opcional | Nenhum | - |
| `hooks_B` | Segundo grupo de ganchos a combinar | HOOKS | opcional | Nenhum | - |
| `hooks_C` | Terceiro grupo de ganchos a combinar | HOOKS | opcional | Nenhum | - |
| `hooks_D` | Quarto grupo de ganchos a combinar | HOOKS | opcional | Nenhum | - |
| `hooks_E` | Quinto grupo de ganchos a combinar | HOOKS | opcional | Nenhum | - |
| `hooks_F` | Sexto grupo de ganchos a combinar | HOOKS | opcional | Nenhum | - |
| `hooks_G` | Sétimo grupo de ganchos a combinar | HOOKS | opcional | Nenhum | - |
| `hooks_H` | Oitavo grupo de ganchos a combinar | HOOKS | opcional | Nenhum | - |

**Observação:** Todos os parâmetros de entrada são opcionais. O nó combinará apenas os grupos de ganchos fornecidos, ignorando aqueles que ficarem vazios. Você pode fornecer de um a oito grupos de ganchos para combinação.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `HOOKS` | Um único grupo de ganchos combinado contendo todas as configurações de ganchos fornecidas | HOOKS |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CombineHooksEight/pt-BR.md)

---
**Source fingerprint (SHA-256):** `8cd13ec6710a9b2905c14301cfd15be616c00f1b4140451cdf0915f091c77197`
