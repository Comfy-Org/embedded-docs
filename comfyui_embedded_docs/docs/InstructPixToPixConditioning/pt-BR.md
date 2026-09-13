# InstructPixToPixConditioning

O nó InstructPixToPixConditioning prepara dados de condicionamento para edição de imagem InstructPix2Pix, combinando prompts de texto positivos e negativos com dados de imagem. Ele codifica a imagem de entrada por meio de um VAE em uma representação latente e anexa esse latente tanto ao condicionamento positivo quanto ao negativo, além de retornar um latente vazio correspondente. As dimensões da imagem são automaticamente recortadas para múltiplos de 8 pixels para que o VAE possa processá-las.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `positive` | Dados de condicionamento positivo contendo prompts de texto e configurações para as características desejadas da imagem | CONDITIONING | Sim | - |
| `negative` | Dados de condicionamento negativo contendo prompts de texto e configurações para as características indesejadas da imagem | CONDITIONING | Sim | - |
| `vae` | Modelo VAE usado para codificar imagens de entrada em representações latentes | VAE | Sim | - |
| `pixels` | Imagem de entrada a ser processada e codificada no espaço latente | IMAGE | Sim | - |

**Nota:** As dimensões da imagem de entrada são ajustadas automaticamente por recorte central para múltiplos de 8 pixels tanto em largura quanto em altura, para garantir compatibilidade com o processo de codificação do VAE.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `positive` | Dados de condicionamento positivo com o latente da imagem codificada anexado como `concat_latent_image` | CONDITIONING |
| `negative` | Dados de condicionamento negativo com o latente da imagem codificada anexado como `concat_latent_image` | CONDITIONING |
| `latent` | Tensor latente de zeros com as mesmas dimensões da imagem codificada | LATENT |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/InstructPixToPixConditioning/pt-BR.md)

---
**Source fingerprint (SHA-256):** `e9a5a05cdeafe9337ca2033111f1ad4f7314fa33d71a4764f62919857efc79f4`
