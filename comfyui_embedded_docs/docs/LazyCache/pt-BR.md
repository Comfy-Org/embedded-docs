# LazyCache

Esta documentação foi gerada por IA. Se você encontrar algum erro ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LazyCache/en.md)

LazyCache é uma versão caseira do EasyCache que oferece uma implementação ainda mais simples. Funciona com qualquer modelo no ComfyUI e adiciona funcionalidade de cache para reduzir a computação durante a amostragem. Embora geralmente tenha desempenho inferior ao EasyCache, pode ser mais eficaz em alguns casos raros e oferece compatibilidade universal.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `modelo` | O modelo ao qual adicionar o LazyCache. | MODEL | Sim | - |
| `limite_de_reutilização` | O limite para reutilizar etapas em cache (padrão: 0.2). | FLOAT | Não | 0.0 - 3.0 |
| `percentual_inicial` | A etapa de amostragem relativa para iniciar o uso do LazyCache (padrão: 0.15). | FLOAT | Não | 0.0 - 1.0 |
| `percentual_final` | A etapa de amostragem relativa para encerrar o uso do LazyCache (padrão: 0.95). | FLOAT | Não | 0.0 - 1.0 |
| `detalhado` | Se deve registrar informações detalhadas (padrão: False). | BOOLEAN | Não | - |

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `modelo` | O modelo com a funcionalidade LazyCache adicionada. | MODEL |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LazyCache/pt-BR.md)

---
**Source fingerprint (SHA-256):** `72a5e85b7cf517e88583fc1b75d3ab4a5d40fe8604d50c34f555e677d2ea9e51`
