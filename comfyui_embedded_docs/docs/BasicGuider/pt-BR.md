> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BasicGuider/pt-BR.md)

O nó BasicGuider cria um mecanismo de orientação simples para o processo de amostragem. Ele recebe um modelo e dados de condicionamento como entradas e produz um objeto orientador que pode ser usado para guiar o processo de geração durante a amostragem. Este nó fornece a funcionalidade fundamental de orientação necessária para geração controlada.

## Entradas

| Parâmetro | Tipo de Dado | Tipo de Entrada | Padrão | Intervalo | Descrição |
|-----------|-----------|------------|---------|-------|-------------|
| `model` | MODEL | obrigatório | - | - | O modelo a ser usado para orientação |
| `conditioning` | CONDITIONING | obrigatório | - | - | Os dados de condicionamento que orientam o processo de geração |

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|-------------|-----------|-------------|
| `GUIDER` | GUIDER | Um objeto orientador que pode ser usado durante o processo de amostragem para guiar a geração |
