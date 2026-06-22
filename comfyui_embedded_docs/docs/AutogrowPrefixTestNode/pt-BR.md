# AutogrowPrefixTestNode

O **AutogrowPrefixTestNode** é um nó lógico projetado para testar o recurso de entrada de crescimento automático. Ele aceita um número dinâmico de entradas do tipo float, combina seus valores em uma string separada por vírgulas e gera essa string como saída.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `autogrow` | Um grupo de entrada dinâmico que pode aceitar entre 1 e 10 valores float. Cada entrada no grupo é do tipo FLOAT com valor mínimo de 1 e valor máximo de 10. | AUTOGROW | Sim | 1 a 10 entradas |

**Observação:** A entrada `autogrow` é uma entrada dinâmica especial. Você pode adicionar várias entradas float a este grupo, até o máximo de 10. O nó processará todos os valores fornecidos. Cada entrada float individual é limitada a uma faixa de 1 a 10.

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `output` | Uma única string contendo todos os valores float de entrada, separados por vírgulas. | STRING |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/AutogrowPrefixTestNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `7ae65365f77399a2ad8358b5a1eab3f2caa39331e53dec474cdd7f2751bfff4b`
