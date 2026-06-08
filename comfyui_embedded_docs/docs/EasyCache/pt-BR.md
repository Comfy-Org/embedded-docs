O nó EasyCache implementa um sistema de cache nativo para modelos, com o objetivo de melhorar o desempenho ao reutilizar etapas previamente computadas durante o processo de amostragem. Ele adiciona a funcionalidade EasyCache a um modelo, com limites configuráveis para quando iniciar e parar o uso do cache durante a linha do tempo de amostragem.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `modelo` | O modelo ao qual adicionar o EasyCache. | MODEL | Sim | - |
| `limite_de_reutilização` | O limite para reutilizar etapas em cache (padrão: 0.2). | FLOAT | Não | 0.0 - 3.0 |
| `percentual_inicial` | A etapa relativa de amostragem para iniciar o uso do EasyCache (padrão: 0.15). | FLOAT | Não | 0.0 - 1.0 |
| `percentual_final` | A etapa relativa de amostragem para encerrar o uso do EasyCache (padrão: 0.95). | FLOAT | Não | 0.0 - 1.0 |
| `detalhado` | Se deve registrar informações detalhadas (padrão: False). | BOOLEAN | Não | - |

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `modelo` | O modelo com a funcionalidade EasyCache adicionada. | MODEL |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EasyCache/pt-BR.md)

---
**Source fingerprint (SHA-256):** `e9d9bf5ecae8034b562f1a27acf528d1f3241d7d28621beba149d3e9bd66a247`
