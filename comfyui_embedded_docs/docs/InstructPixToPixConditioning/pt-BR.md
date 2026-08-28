# InstructPixToPixConditioning

O nó InstructPixToPixConditioning prepara dados de condicionamento para edição de imagens InstructPix2Pix, combinando prompts de texto positivos e negativos com os dados da imagem. Ele processa as imagens de entrada por meio de um codificador VAE para criar representações latentes e anexa esses latentes tanto aos dados de condicionamento positivos quanto aos negativos. O nó lida automaticamente com as dimensões da imagem, aplicando um recorte centralizado para múltiplos de 8 pixels, garantindo compatibilidade com o processo de codificação do VAE.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `positivo` | Dados de condicionamento positivos contendo prompts de texto e configurações para as características desejadas da imagem | CONDITIONING | Sim | - |
| `negativo` | Dados de condicionamento negativos contendo prompts de texto e configurações para as características indesejadas da imagem | CONDITIONING | Sim | - |
| `vae` | Modelo VAE usado para codificar as imagens de entrada em representações latentes | VAE | Sim | - |
| `pixels` | Imagem de entrada a ser processada e codificada no espaço latente | IMAGE | Sim | - |

**Nota:** As dimensões da imagem de entrada são ajustadas automaticamente por recorte centralizado para múltiplos de 8 pixels, tanto na largura quanto na altura, garantindo compatibilidade com o processo de codificação do VAE.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `positivo` | Dados de condicionamento positivos com a representação latente da imagem anexada | CONDITIONING |
| `negativo` | Dados de condicionamento negativos com a representação latente da imagem anexada | CONDITIONING |
| `latent` | Tensor latente vazio com as mesmas dimensões da imagem codificada | LATENT |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/InstructPixToPixConditioning/pt-BR.md)

---
**Source fingerprint (SHA-256):** `e9a5a05cdeafe9337ca2033111f1ad4f7314fa33d71a4764f62919857efc79f4`
