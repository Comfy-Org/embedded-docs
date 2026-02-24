> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PrimitiveInt/pt-BR.md)

O nó PrimitiveInt fornece uma maneira simples de trabalhar com valores inteiros em seu fluxo de trabalho. Ele recebe uma entrada inteira e emite o mesmo valor, sendo útil para passar parâmetros inteiros entre nós ou definir valores numéricos específicos para outras operações.

## Entradas

| Parâmetro | Tipo de Dados | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `value` | INT | Sim | -9223372036854775807 a 9223372036854775807 | O valor inteiro a ser emitido |

## Saídas

| Nome da Saída | Tipo de Dados | Descrição |
|-------------|-----------|-------------|
| `output` | INT | O valor inteiro de entrada, passado inalterado |
