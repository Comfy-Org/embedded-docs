> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CombineHooksFour/pt-BR.md)

O nó Combinar Ganchos [4] mescla até quatro grupos de ganchos separados em um único grupo de ganchos combinado. Ele aceita qualquer combinação das quatro entradas de ganchos disponíveis e as combina usando o sistema de combinação de ganchos do ComfyUI. Isso permite consolidar múltiplas configurações de ganchos para processamento otimizado em fluxos de trabalho avançados.

## Entradas

| Parâmetro | Tipo de Dados | Tipo de Entrada | Padrão | Faixa | Descrição |
|-----------|---------------|-----------------|--------|-------|-----------|
| `hooks_A` | HOOKS | opcional | Nenhum | - | Primeiro grupo de ganchos a combinar |
| `hooks_B` | HOOKS | opcional | Nenhum | - | Segundo grupo de ganchos a combinar |
| `hooks_C` | HOOKS | opcional | Nenhum | - | Terceiro grupo de ganchos a combinar |
| `hooks_D` | HOOKS | opcional | Nenhum | - | Quarto grupo de ganchos a combinar |

**Observação:** Todas as quatro entradas de ganchos são opcionais. O nó combinará apenas os grupos de ganchos que forem fornecidos e retornará um grupo de ganchos vazio se nenhuma entrada estiver conectada.

## Saídas

| Nome da Saída | Tipo de Dados | Descrição |
|---------------|---------------|-----------|
| `HOOKS` | HOOKS | Grupo de ganchos combinado contendo todas as configurações de ganchos fornecidas |

---
**Source fingerprint (SHA-256):** `92a8038e7b5a7491afcbd48830a1e278fe4d697321fb874821ebf7edd09d5815`
