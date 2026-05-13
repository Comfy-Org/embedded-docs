> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EasyCache/pt-BR.md)

O nó EasyCache implementa um sistema de cache nativo para modelos, com o objetivo de melhorar o desempenho ao reutilizar etapas previamente computadas durante o processo de amostragem. Ele adiciona a funcionalidade EasyCache a um modelo, com limites configuráveis para quando iniciar e parar o uso do cache durante a linha do tempo de amostragem.

## Entradas

| Parâmetro | Tipo de Dados | Obrigatório | Faixa | Descrição |
|-----------|---------------|-------------|-------|-----------|
| `model` | MODEL | Sim | - | O modelo ao qual adicionar o EasyCache. |
| `reuse_threshold` | FLOAT | Não | 0.0 - 3.0 | O limite para reutilizar etapas em cache (padrão: 0.2). |
| `start_percent` | FLOAT | Não | 0.0 - 1.0 | A etapa relativa de amostragem para iniciar o uso do EasyCache (padrão: 0.15). |
| `end_percent` | FLOAT | Não | 0.0 - 1.0 | A etapa relativa de amostragem para encerrar o uso do EasyCache (padrão: 0.95). |
| `verbose` | BOOLEAN | Não | - | Se deve registrar informações detalhadas (padrão: False). |

## Saídas

| Nome da Saída | Tipo de Dados | Descrição |
|---------------|---------------|-----------|
| `model` | MODEL | O modelo com a funcionalidade EasyCache adicionada. |

---
**Source fingerprint (SHA-256):** `e9d9bf5ecae8034b562f1a27acf528d1f3241d7d28621beba149d3e9bd66a247`
