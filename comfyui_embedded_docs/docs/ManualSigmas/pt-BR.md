# Sigmas Manuais

O nó ManualSigmas permite que você defina manualmente uma sequência personalizada de níveis de ruído (sigmas) para o processo de amostragem. Você insere uma lista de números como uma string, e o nó os converte em um tensor que pode ser usado por outros nós de amostragem. Isso é útil para testar ou criar cronogramas de ruído específicos.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `sigmas` | Uma string contendo os valores sigma. O nó extrairá todos os números dessa string. Por exemplo, "1, 0.5, 0.1" ou "1 0.5 0.1". O valor padrão é "1, 0.5". | STRING | Sim | Qualquer número separado por vírgula ou espaço |

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `sigmas` | O tensor contendo a sequência de valores sigma extraídos da string de entrada. | SIGMAS |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ManualSigmas/pt-BR.md)

---
**Source fingerprint (SHA-256):** `b815633dfea8f529f487f46b2d0464fa8c1045df8c4d4ef586bd36ad6f4a28db`
