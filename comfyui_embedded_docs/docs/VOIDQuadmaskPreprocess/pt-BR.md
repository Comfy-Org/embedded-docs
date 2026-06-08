## Visão Geral

O nó VOIDQuadmaskPreprocess prepara uma máscara para inpaint VOID convertendo-a em uma "quadmask" especial de quatro níveis. Ele recebe uma máscara de entrada, opcionalmente dilata a região primária e quantiza os valores da máscara em quatro níveis distintos que representam diferentes regiões semânticas (objeto primário, sobreposição, área afetada e fundo). Por fim, ele inverte e normaliza a máscara para que os valores de saída estejam no intervalo [0, 1], onde 1.0 indica a área a ser removida e 0.0 indica a área a ser mantida.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `mask` | A máscara de entrada a ser pré-processada. | MASK | Sim | N/A |
| `dilate_width` | Raio de dilatação para a região primária da máscara. Um valor de 0 significa que nenhuma dilatação é aplicada. (padrão: 0) | INT | Não | 0 a 50 (passo: 1) |

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `quadmask` | A quadmask pré-processada com valores em [0, 1], representando quatro níveis discretos: 1.0 (objeto primário a remover), ~0.75 (sobreposição do primário e afetado), ~0.50 (região afetada) e 0.0 (fundo a manter). | MASK |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VOIDQuadmaskPreprocess/pt-BR.md)

---
**Source fingerprint (SHA-256):** `12dc5ab215b80d81289942457ce2ddffcb9ec41fc738a53ca5fbf1e9181ed439`
