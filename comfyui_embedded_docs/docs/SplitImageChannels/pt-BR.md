# Split Image Channels

Divide uma imagem em seus canais vermelho, verde e azul e retorna o canal alfa como uma máscara. Cada saída de cor é uma imagem em escala de cinza de três canais, portanto é pré-visualizada e salva como uma imagem normal. Use-a para inspecionar ou editar um único canal ou para extrair a transparência de uma imagem.

## Entradas

| Parâmetro | Descrição | Tipo de dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `image` | A imagem a ser dividida. Uma entrada de canal único (escala de cinza) é expandida para que todas as três saídas de cor carreguem os mesmos dados. | IMAGE | Sim | - |

## Saídas

| Nome da saída | Descrição | Tipo de dados |
| --- | --- | --- |
| `red` | O canal vermelho, como uma imagem em escala de cinza de três canais. | IMAGE |
| `green` | O canal verde, como uma imagem em escala de cinza de três canais. | IMAGE |
| `blue` | O canal azul, como uma imagem em escala de cinza de três canais. | IMAGE |
| `alpha` | Alfa como uma máscara, invertido da mesma forma que em Load Image, de modo que 1 marca pixels totalmente transparentes. Uma imagem sem canal alfa retorna uma máscara totalmente zerada. | MASK |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SplitImageChannels/pt-BR.md)

---
**Source fingerprint (SHA-256):** `0f300d2e86c74e856001eb82da26c871c94c1dae5ec73a4504ca258420fbcf52`
