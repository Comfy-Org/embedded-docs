> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyHunyuanLatentVideo/pt-BR.md)

O nó `EmptyHunyuanLatentVideo` é semelhante ao nó `EmptyLatentImage`. Você pode considerá-lo como uma tela em branco para geração de vídeo, onde largura, altura e duração definem as propriedades da tela, e o tamanho do lote determina quantas telas serão criadas. Este nó cria telas vazias prontas para tarefas subsequentes de geração de vídeo.

## Entradas

| Parâmetro    | Tipo Comfy | Descrição                                                                                |
| ----------- | ---------- | ------------------------------------------------------------------------------------------ |
| `width`     | `INT`      | Largura do vídeo, padrão 848, mínimo 16, máximo `nodes.MAX_RESOLUTION`, incremento 16.        |
| `height`    | `INT`      | Altura do vídeo, padrão 480, mínimo 16, máximo `nodes.MAX_RESOLUTION`, incremento 16.       |
| `length`    | `INT`      | Duração do vídeo, padrão 25, mínimo 1, máximo `nodes.MAX_RESOLUTION`, incremento 4.          |
| `batch_size`| `INT`      | Tamanho do lote, padrão 1, mínimo 1, máximo 4096.                                           |

## Saídas

| Parâmetro | Tipo Comfy | Descrição                                                                               |
| --------- | ---------- | ----------------------------------------------------------------------------------------- |
| `samples` | `LATENT`   | Amostras latentes de vídeo geradas contendo tensores zerados, prontas para tarefas de processamento e geração. |
