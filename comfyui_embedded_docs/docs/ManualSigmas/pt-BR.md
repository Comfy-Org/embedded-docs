# Sigmas Manuais

O nó **ManualSigmas** permite que você defina manualmente uma sequência personalizada de níveis de ruído (sigmas) para o processo de amostragem. Você insere uma lista de números como uma string, e o nó a converte em um tensor que pode ser usado por outros nós de amostragem. Isso é útil para testar ou criar agendamentos de ruído específicos.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `sigmas` | Uma string contendo os valores de sigma. O nó extrai todos os números dessa string, incluindo decimais e valores negativos. Por exemplo, "1, 0.5, 0.1" ou "1 0.5 0.1". Padrão: "1, 0.5". | STRING | Sim | Quaisquer valores numéricos separados por vírgula ou espaço |

Observação: Este nó está marcado como experimental.

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `sigmas` | Um tensor contendo a sequência de valores de sigma extraídos da string de entrada. | SIGMAS |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ManualSigmas/pt-BR.md)

---
**Source fingerprint (SHA-256):** `19d938ef0eac7343a3138393a039f63632b0763e3884636653c06b91b6f44ed6`
