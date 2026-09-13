# LazyCache

LazyCache é uma versão experimental e caseira do EasyCache que adiciona cache durante a amostragem para reduzir a computação. Ele foi projetado para compatibilidade universal com modelos no ComfyUI, embora geralmente tenha desempenho pior que o EasyCache e possa funcionar melhor apenas em casos raros.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `modelo` | O modelo ao qual adicionar o LazyCache. | MODEL | Sim | - |
| `limite_de_reutilização` | O limiar para reutilizar etapas em cache. Padrão: 0.2. | FLOAT | Sim | 0.0 - 3.0 (passo 0.01) |
| `percentual_inicial` | A etapa relativa de amostragem para iniciar o uso do LazyCache. Padrão: 0.15. | FLOAT | Sim | 0.0 - 1.0 (passo 0.01) |
| `percentual_final` | A etapa relativa de amostragem para encerrar o uso do LazyCache. Padrão: 0.95. | FLOAT | Sim | 0.0 - 1.0 (passo 0.01) |
| `detalhado` | Se deve registrar informações detalhadas. Padrão: False. | BOOLEAN | Sim | - |

Nota: `reuse_threshold`, `start_percent`, `end_percent` e `verbose` são marcados como entradas avançadas.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `model` | O modelo com a funcionalidade LazyCache adicionada. | MODEL |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LazyCache/pt-BR.md)

---
**Source fingerprint (SHA-256):** `78f9c13473567e068fc2be35b2f8f5aa459d43d3f13300a6ea858af98d3e2a44`
