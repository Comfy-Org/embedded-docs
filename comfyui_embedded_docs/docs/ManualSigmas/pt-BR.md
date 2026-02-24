> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ManualSigmas/pt-BR.md)

O nó ManualSigmas permite que você defina manualmente uma sequência personalizada de níveis de ruído (sigmas) para o processo de amostragem. Você insere uma lista de números como uma string, e o nó os converte em um tensor que pode ser usado por outros nós de amostragem. Isso é útil para testes ou para criar cronogramas de ruído específicos.

## Entradas

| Parâmetro | Tipo de Dados | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `sigmas` | STRING | Sim | Quaisquer números separados por vírgula ou espaço | Uma string contendo os valores de sigma. O nó extrairá todos os números desta string. Por exemplo, "1, 0.5, 0.1" ou "1 0.5 0.1". O valor padrão é "1, 0.5". |

## Saídas

| Nome da Saída | Tipo de Dados | Descrição |
|-------------|-----------|-------------|
| `sigmas` | SIGMAS | O tensor contendo a sequência de valores de sigma extraídos da string de entrada. |
