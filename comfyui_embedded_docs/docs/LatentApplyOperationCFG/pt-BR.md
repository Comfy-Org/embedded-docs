> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LatentApplyOperationCFG/pt-BR.md)

O nó LatentApplyOperationCFG aplica uma operação latente para modificar o processo de orientação por condicionamento (CFG) em um modelo. Ele funciona interceptando as saídas de condicionamento durante o processo de amostragem de orientação livre de classificador (CFG) e aplicando a operação especificada às representações latentes antes que elas sejam usadas para a geração.

## Entradas

| Parâmetro | Tipo de Dados | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `model` | MODEL | Sim | - | O modelo ao qual a operação CFG será aplicada |
| `operation` | LATENT_OPERATION | Sim | - | A operação latente a ser aplicada durante o processo de amostragem CFG |

## Saídas

| Nome da Saída | Tipo de Dados | Descrição |
|-------------|-----------|-------------|
| `model` | MODEL | O modelo modificado com a operação CFG aplicada ao seu processo de amostragem |
