> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CombineHooksEight/pt-BR.md)

O nó Combinar Ganchos [8] mescla até oito grupos de ganchos diferentes em um único grupo de ganchos combinado. Ele recebe múltiplas entradas de ganchos e as combina usando a funcionalidade de combinação de ganchos do ComfyUI. Isso permite consolidar várias configurações de ganchos para processamento simplificado em fluxos de trabalho avançados.

## Entradas

| Parâmetro | Tipo de Dados | Tipo de Entrada | Padrão | Faixa | Descrição |
|-----------|---------------|-----------------|--------|-------|-----------|
| `hooks_A` | HOOKS | opcional | Nenhum | - | Primeiro grupo de ganchos a combinar |
| `hooks_B` | HOOKS | opcional | Nenhum | - | Segundo grupo de ganchos a combinar |
| `hooks_C` | HOOKS | opcional | Nenhum | - | Terceiro grupo de ganchos a combinar |
| `hooks_D` | HOOKS | opcional | Nenhum | - | Quarto grupo de ganchos a combinar |
| `hooks_E` | HOOKS | opcional | Nenhum | - | Quinto grupo de ganchos a combinar |
| `hooks_F` | HOOKS | opcional | Nenhum | - | Sexto grupo de ganchos a combinar |
| `hooks_G` | HOOKS | opcional | Nenhum | - | Sétimo grupo de ganchos a combinar |
| `hooks_H` | HOOKS | opcional | Nenhum | - | Oitavo grupo de ganchos a combinar |

**Observação:** Todos os parâmetros de entrada são opcionais. O nó combinará apenas os grupos de ganchos fornecidos, ignorando aqueles que ficarem vazios. Você pode fornecer de um a oito grupos de ganchos para combinação.

## Saídas

| Nome da Saída | Tipo de Dados | Descrição |
|---------------|---------------|-----------|
| `HOOKS` | HOOKS | Um único grupo de ganchos combinado contendo todas as configurações de ganchos fornecidas |

---
**Source fingerprint (SHA-256):** `8cd13ec6710a9b2905c14301cfd15be616c00f1b4140451cdf0915f091c77197`
