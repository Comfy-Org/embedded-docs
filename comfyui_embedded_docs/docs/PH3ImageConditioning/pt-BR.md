# p-h3-image Conditioning

Este nó transforma um prompt em condicionamento e um latent vazio para uma única imagem estática com p-h3-image. Sem imagens, é texto para imagem; com imagens conectadas, `image_1` é a imagem que está sendo editada e os outros slots atuam como referências, às quais o prompt se refere como `<Picture 1>`, `<Picture 2>` e assim por diante. O sampler precisa de um modelo com patch aplicado pelo nó MiniMax H3 sigma shift, com ambos os valores de shift em 1.0.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `clip` | O modelo CLIP p-h3-image usado para tokenizar o prompt, incluindo quaisquer imagens de referência, e para codificar o condicionamento. | CLIP | Sim | - |
| `prompt` | O que gerar, ou como editar `image_1`. Com imagens conectadas, uma instrução curta recebe `Edit <Picture 1>. ` como prefixo. Uma instrução que já começa com `Edit <Picture` ou um briefing de edição produzido por um ampliador de prompt é usado exatamente como escrito. | STRING | Sim | - |
| `width` | Largura de saída em pixels. 0 usa a largura de `image_1` após o escalonamento, ou 2912 quando nenhuma imagem está conectada (padrão: 0). | INT | Sim | 0 a MAX_RESOLUTION |
| `height` | Altura de saída em pixels. 0 usa a altura de `image_1` após o escalonamento, ou 2912 quando nenhuma imagem está conectada (padrão: 0). | INT | Sim | 0 a MAX_RESOLUTION |
| `vae` | VAE do p-h3-image. Com ele, as imagens também são ancoradas como latentes de referência; sem ele, apenas condicionam o codificador de texto. | VAE | Não | - |
| `images` | Grupo expansível de até 9 imagens, de `image_1` a `image_9`. `image_1` é a imagem que está sendo editada; os slots restantes são referências. | AUTOGROW | Não | 0 a 9 imagens |

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `positive` | Condicionamento para o sampler p-h3-image. Quando imagens estão conectadas, também carrega os latents de referência empacotados. | CONDITIONING |
| `latent` | Latent vazio para um único quadro estático, incluindo os dois latents de áudio que o modelo espera. | LATENT |

**Nota:** Com imagens conectadas e sem `vae`, as imagens ainda orientam o prompt pelo codificador de texto, mas não são ancoradas como latentes de referência.

**Observação:** O condicionamento cobre um único quadro. Para vídeo ou áudio, use os nós de vídeo MiniMax H3.

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PH3ImageConditioning/pt-BR.md)

---
**Source fingerprint (SHA-256):** `19db44388a093dd9a90e9d2911741c732cef3e9e39664ad29dee125765f5f887`
