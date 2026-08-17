# Estender Sigmas Intermediários

O nó ExtendIntermediateSigmas recebe uma sequência existente de valores de sigma e insere valores de sigma intermediários adicionais entre eles. Ele permite especificar quantos passos extras adicionar, o método de espaçamento para interpolação e limites opcionais de sigma inicial e final para controlar onde a extensão ocorre dentro da sequência de sigma.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `sigmas` | A sequência de sigma de entrada para estender com valores intermediários | SIGMAS | Sim | - |
| `steps` | Número de passos intermediários a inserir entre sigmas existentes; com N passos, N-1 valores de sigma intermediários são inseridos entre cada par elegível (padrão: 2) | INT | Sim | 1 a 100 |
| `start_at_sigma` | Limite superior de sigma para extensão - apenas estende sigmas abaixo deste valor (padrão: -1.0, que significa infinito) | FLOAT | Sim | -1.0 a 20000.0 |
| `end_at_sigma` | Limite inferior de sigma para extensão - apenas estende sigmas acima deste valor (padrão: 12.0) | FLOAT | Sim | 0.0 a 20000.0 |
| `spacing` | O método de interpolação para espaçar os valores de sigma intermediários: "linear" os distribui uniformemente, "cosine" e "sine" aplicam espaçamento curvo (padrão: "linear") | COMBO | Sim | `"linear"`<br>`"cosine"`<br>`"sine"` |

**Nota:** O nó só insere sigmas intermediários entre pares de sigmas existentes onde o sigma atual seja menor ou igual a `start_at_sigma` e maior ou igual a `end_at_sigma`. Quando `start_at_sigma` é definido como -1.0, ele é tratado como infinito, significando que apenas o limite inferior `end_at_sigma` se aplica.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `sigmas` | A sequência de sigma estendida com valores intermediários adicionais inseridos | SIGMAS |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ExtendIntermediateSigmas/pt-BR.md)

---
**Source fingerprint (SHA-256):** `d761e82ce055bc56a551d3e446117febb2cdbd6c0286ef620d0a078c96f047ba`
