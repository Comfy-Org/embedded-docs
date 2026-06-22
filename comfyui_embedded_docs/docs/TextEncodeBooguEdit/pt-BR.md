# TextEncodeBooguEdit

Este nó prepara o condicionamento para edição de imagens com Boogu. Ele processa imagens de referência para criar saídas de condicionamento positivo e negativo. A imagem de referência é usada duas vezes: tokens visuais da imagem são adicionados apenas ao condicionamento positivo para amplificar a instrução de edição, enquanto um latent de referência do VAE é adicionado tanto ao condicionamento positivo quanto ao negativo, de modo que se anule sob CFG, preservando a identidade da imagem original.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
|-----------|-------------|--------------|-------------|-------|
| `clip` | O modelo CLIP usado para codificação de texto | CLIP | Sim | |
| `prompt` | O prompt de texto descrevendo a edição desejada | STRING | Sim | |
| `negative_prompt` | O prompt de texto descrevendo o que evitar na edição | STRING | Não | |
| `vae` | O modelo VAE usado para codificar imagens de referência no espaço latente | VAE | Não | |
| `imagens` | Imagem(ns) de referência para editar. Boogu foca em uma referência por amostra; mais são permitidas. | IMAGE | Não | Até 16 imagens |

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
|---------------|-----------|--------------|
| `positive` | Condicionamento contendo tanto o prompt de texto com tokens visuais quanto os latents de referência | CONDITIONING |
| `negative` | Condicionamento contendo o prompt de texto negativo e os latents de referência | CONDITIONING |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TextEncodeBooguEdit/pt-BR.md)

---
**Source fingerprint (SHA-256):** `170979acf5b2e9f25f96231a4b23a4376cfddcd4bda2fdd6e03528417e6931b0`
