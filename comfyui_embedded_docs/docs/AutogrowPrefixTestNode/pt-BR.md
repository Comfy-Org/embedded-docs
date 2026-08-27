# AutogrowPrefixTestNode

O AutogrowPrefixTestNode é um nó lógico que testa o recurso de entrada autogrow. Ele aceita um número dinâmico de entradas float, converte cada valor em texto, combina-os em uma string separada por vírgulas e gera essa string.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `autogrow` | Um grupo de entrada dinâmico que aceita entre 1 e 10 valores float. Cada valor é um número de ponto flutuante, e as entradas geradas são nomeadas com o prefixo `float`. | AUTOGROW | Sim | 1 a 10 entradas |

**Observação:** A entrada `autogrow` é uma entrada dinâmica especial. Você pode adicionar múltiplas entradas float a este grupo, de um mínimo de 1 até um máximo de 10. O nó processa todos os valores fornecidos e inclui cada entrada conectada na string de saída.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `output` | Uma única string contendo todos os valores float de entrada, separados por vírgulas. | STRING |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/AutogrowPrefixTestNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `9b815f59961a4c661815f44b9c78e15e9084db1e4be89d502b9d92438f18e70b`
