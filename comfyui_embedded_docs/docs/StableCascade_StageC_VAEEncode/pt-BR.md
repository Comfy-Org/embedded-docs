# StableCascade_StageC_VAEEncode

O nó StableCascade_StageC_VAEEncode processa uma imagem de entrada por meio de um codificador VAE para gerar representações latentes para o modelo Stable Cascade. Primeiro, ele redimensiona a imagem com base em um fator de compressão e na proporção de redução do VAE, depois codifica a imagem redimensionada. O nó gera dois tensores latentes: um para o estágio C (o resultado codificado real) e um para o estágio B (um espaço reservado preenchido com zeros).

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `image` | A imagem de entrada a ser codificada no espaço latente | IMAGE | Sim | - |
| `vae` | O modelo VAE usado para codificar a imagem | VAE | Sim | - |
| `compression` | O fator de compressão aplicado à imagem antes da codificação. As dimensões da imagem são divididas por esse valor e depois multiplicadas pela proporção de redução do VAE. (padrão: 42) | INT | Não | 4-128 |

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `stage_c` | A representação latente codificada para o estágio C do modelo Stable Cascade | LATENT |
| `stage_b` | Uma representação latente de espaço reservado para o estágio B. Atualmente retorna um tensor preenchido com zeros, com dimensões calculadas a partir do tamanho da imagem de entrada. | LATENT |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StableCascade_StageC_VAEEncode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `1679aaac77057fcc359e5428906d5227f6c2dde721aabbfb5a32c08738ac376c`
