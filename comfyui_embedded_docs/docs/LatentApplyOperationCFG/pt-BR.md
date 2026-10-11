# LatentApplyOperationCFG

O nó LatentApplyOperationCFG aplica uma operação latente dentro da etapa de classifier-free guidance (CFG) do processo de amostragem de um modelo. Ele intercepta as saídas de condicionamento produzidas antes do CFG, aplica a operação conectada aos valores latentes e retorna o modelo com esse comportamento de amostragem modificado.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `modelo` | O modelo ao qual a operação CFG será aplicada | MODEL | Sim | - |
| `operação` | A operação latente a ser aplicada durante o processo de amostragem CFG | LATENT_OPERATION | Sim | - |
| `start_percent` | Fração do agendamento de denoising em que a operação começa a ser aplicada; 0 é o início do agendamento (padrão: 0.0) | FLOAT | Não | 0.0 a 1.0 (passo 0.001) |
| `end_percent` | Fração do agendamento de denoising em que a operação deixa de ser aplicada; 1 é o fim do agendamento (padrão: 1.0) | FLOAT | Não | 0.0 a 1.0 (passo 0.001) |

Nota: Este nó está marcado como experimental. A operação é aplicada às saídas de condicionamento do modelo durante o processo de amostragem CFG. Quando duas saídas de condicionamento estão presentes, a operação é aplicada à diferença entre a primeira e a segunda saída, e a segunda saída é adicionada de volta ao resultado. Quando apenas uma saída de condicionamento está presente, a operação é aplicada diretamente a ela. A operação só é executada entre os pontos `start_percent` e `end_percent` do agendamento de denoising, portanto pode ser limitada a uma parte do agendamento; fora dessa janela, as saídas de condicionamento são retornadas sem alterações.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `model` | O modelo modificado com a operação CFG aplicada ao seu processo de amostragem | MODEL |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LatentApplyOperationCFG/pt-BR.md)

---
**Source fingerprint (SHA-256):** `6a5f59f02eaec38334c63d871e48e89aa983a5ac2ca10801161cdc9e13cacdf2`
