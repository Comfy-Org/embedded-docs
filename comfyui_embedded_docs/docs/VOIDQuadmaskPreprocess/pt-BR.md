> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VOIDQuadmaskPreprocess/pt-BR.md)

Esta documentação foi gerada por IA. Se você encontrar algum erro ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VOIDQuadmaskPreprocess/en.md)

## Visão Geral

O nó VOIDQuadmaskPreprocess prepara uma máscara para inpaint VOID convertendo-a em uma "quadmask" especial de quatro níveis. Ele recebe uma máscara de entrada, opcionalmente dilata a região primária e então quantiza os valores da máscara em quatro níveis distintos que representam diferentes regiões semânticas (objeto primário, sobreposição, área afetada e fundo). Por fim, ele inverte e normaliza a máscara para que os valores de saída estejam no intervalo [0, 1], onde 1.0 indica a área a ser removida e 0.0 indica a área a ser mantida.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Faixa | Descrição |
|-----------|--------------|-------------|-------|-----------|
| `mask` | MASK | Sim | N/A | A máscara de entrada a ser pré-processada. |
| `dilate_width` | INT | Não | 0 a 50 (passo: 1) | Raio de dilatação para a região primária da máscara. Um valor de 0 significa que nenhuma dilatação é aplicada. (padrão: 0) |

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|---------------|--------------|-----------|
| `quadmask` | MASK | A quadmask pré-processada com valores em [0, 1], representando quatro níveis discretos: 1.0 (objeto primário a remover), ~0,75 (sobreposição do primário e afetado), ~0,50 (região afetada) e 0,0 (fundo a manter). |