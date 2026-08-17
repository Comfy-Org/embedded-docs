# EasyCache

O nó EasyCache implementa um sistema de cache nativo para modelos, melhorando o desempenho ao reutilizar etapas previamente calculadas durante o processo de amostragem. Ele adiciona a funcionalidade EasyCache a um modelo com limites configuráveis para quando começar e parar de usar o cache durante a linha do tempo de amostragem.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Faixa |
|-----------|-----------|---------------|-------------|-------|
| `model` | O modelo ao qual adicionar o EasyCache. | MODEL | Sim | - |
| `reuse_threshold` | O limite para reutilizar etapas em cache (padrão: 0.2). | FLOAT | Sim | 0.0 - 3.0 |
| `start_percent` | A etapa relativa de amostragem para começar a usar o EasyCache (padrão: 0.15). | FLOAT | Sim | 0.0 - 1.0 |
| `end_percent` | A etapa relativa de amostragem para encerrar o uso do EasyCache (padrão: 0.95). | FLOAT | Sim | 0.0 - 1.0 |
| `verbose` | Se deve registrar informações detalhadas (padrão: False). | BOOLEAN | Sim | - |

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|---------------|-----------|---------------|
| `model` | O modelo com EasyCache. | MODEL |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EasyCache/pt-BR.md)

---
**Source fingerprint (SHA-256):** `3e10ac65f8df58ce8649fdf599e62bfb86f2d4166840bed5622c0aa2c419cd38`
