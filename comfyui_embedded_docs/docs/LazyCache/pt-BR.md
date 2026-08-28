# LazyCache

LazyCache é uma versão caseira do EasyCache que oferece uma implementação ainda mais fácil. Ele funciona com qualquer modelo no ComfyUI e adiciona funcionalidade de cache para reduzir a computação durante a amostragem. Embora geralmente tenha desempenho inferior ao EasyCache, pode ser mais eficaz em alguns casos raros e oferece compatibilidade universal.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `modelo` | O modelo ao qual adicionar o LazyCache. | MODEL | Sim | - |
| `limite_de_reutilização` | O limite para reutilizar etapas em cache (padrão: 0.2). | FLOAT | Não | 0.0 - 3.0 |
| `percentual_inicial` | A etapa relativa da amostragem para começar a usar o LazyCache (padrão: 0.15). | FLOAT | Não | 0.0 - 1.0 |
| `percentual_final` | A etapa relativa da amostragem para encerrar o uso do LazyCache (padrão: 0.95). | FLOAT | Não | 0.0 - 1.0 |
| `detalhado` | Se deve registrar informações detalhadas (padrão: False). | BOOLEAN | Não | - |

Nota: `reuse_threshold`, `start_percent`, `end_percent` e `verbose` são opções avançadas opcionais.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `model` | O modelo com a funcionalidade LazyCache adicionada. | MODEL |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LazyCache/pt-BR.md)

---
**Source fingerprint (SHA-256):** `78f9c13473567e068fc2be35b2f8f5aa459d43d3f13300a6ea858af98d3e2a44`
