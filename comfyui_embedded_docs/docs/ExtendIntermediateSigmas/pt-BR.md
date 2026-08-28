# Estender Sigmas Intermediários

O nó ExtendIntermediateSigmas recebe uma sequência existente de valores de sigma e insere valores intermediários adicionais entre eles. Ele permite especificar quantos passos extras adicionar, o método de espaçamento para interpolação e limites opcionais de sigma inicial e final para controlar onde a extensão ocorre dentro da sequência de sigmas.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `sigmas` | A sequência de sigmas de entrada para estender com valores intermediários | SIGMAS | Sim | - |
| `passos` | Controla o número de valores intermediários de sigma inseridos entre cada par de sigmas existentes. O intervalo entre dois sigmas é dividido em `steps` partes, produzindo `steps - 1` novos valores por par (padrão: 2, que insere um valor por par) | INT | Sim | 1 a 100 |
| `iniciar_em_sigma` | Limite superior de sigma para a extensão - estende apenas sigmas abaixo deste valor (padrão: -1.0, que significa infinito) | FLOAT | Sim | -1.0 a 20000.0 |
| `terminar_em_sigma` | Limite inferior de sigma para a extensão - estende apenas sigmas acima deste valor (padrão: 12.0) | FLOAT | Sim | 0.0 a 20000.0 |
| `espaçamento` | O método de interpolação para espaçar os valores intermediários de sigma (padrão: "linear") | COMBO | Sim | `"linear"`<br>`"cosine"`<br>`"sine"` |

**Nota:** O nó insere sigmas intermediários apenas entre pares de sigmas existentes onde o sigma atual é menor ou igual a `start_at_sigma` e maior ou igual a `end_at_sigma`. Quando `start_at_sigma` é definido como -1.0, ele é tratado como infinito, o que significa que apenas o limite inferior `end_at_sigma` é aplicado.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `sigmas` | A sequência de sigmas estendida com valores intermediários adicionais inseridos | SIGMAS |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ExtendIntermediateSigmas/pt-BR.md)

---
**Source fingerprint (SHA-256):** `d761e82ce055bc56a551d3e446117febb2cdbd6c0286ef620d0a078c96f047ba`
