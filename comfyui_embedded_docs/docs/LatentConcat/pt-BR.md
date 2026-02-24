> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LatentConcat/pt-BR.md)

O nó LatentConcat combina duas amostras latentes ao longo de uma dimensão especificada. Ele recebe duas entradas latentes e as concatena ao longo do eixo escolhido (dimensão x, y ou t). O nó ajusta automaticamente o tamanho do lote da segunda entrada para corresponder ao da primeira antes de realizar a operação de concatenação.

## Entradas

| Parâmetro | Tipo de Dados | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `samples1` | LATENT | Sim | - | A primeira amostra latente a ser concatenada |
| `samples2` | LATENT | Sim | - | A segunda amostra latente a ser concatenada |
| `dim` | COMBO | Sim | `"x"`<br>`"-x"`<br>`"y"`<br>`"-y"`<br>`"t"`<br>`"-t"` | A dimensão ao longo da qual as amostras latentes serão concatenadas. Valores positivos concatenam `samples1` antes de `samples2`, valores negativos concatenam `samples2` antes de `samples1` |

**Observação:** A segunda amostra latente (`samples2`) é automaticamente ajustada para corresponder ao tamanho do lote da primeira amostra latente (`samples1`) antes da concatenação.

## Saídas

| Nome da Saída | Tipo de Dados | Descrição |
|-------------|-----------|-------------|
| `output` | LATENT | As amostras latentes concatenadas resultantes da combinação das duas amostras de entrada ao longo da dimensão especificada |
