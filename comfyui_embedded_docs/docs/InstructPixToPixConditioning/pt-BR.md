# InstructPixToPixConditioning

O nó InstructPixToPixConditioning prepara dados de condicionamento para edição de imagens InstructPix2Pix, combinando uma imagem de entrada com condicionamentos de prompt de texto positivo e negativo. Ele codifica a imagem com o VAE em uma representação latente, anexa esse latente a ambos os conjuntos de condicionamento e cria um latente preenchido com zeros de dimensões correspondentes. Se a largura ou altura da imagem não for múltipla de 8 pixels, a imagem é cortada automaticamente antes da codificação.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `positive` | Dados de condicionamento positivo contendo prompts de texto e configurações para características desejadas da imagem. | CONDITIONING | Sim | - |
| `negative` | Dados de condicionamento negativo contendo prompts de texto e configurações para características indesejadas da imagem. | CONDITIONING | Sim | - |
| `vae` | Modelo VAE usado para codificar a imagem de entrada em uma representação latente. | VAE | Sim | - |
| `pixels` | Imagem de entrada a ser processada e codificada no espaço latente. | IMAGE | Sim | - |

**Nota:** A imagem de entrada é automaticamente cortada para um múltiplo de 8 pixels em largura e altura, arredondando para baixo, para garantir compatibilidade com o processo de codificação do VAE.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `positive` | Dados de condicionamento positivo com o latente da imagem codificada anexado. | CONDITIONING |
| `negative` | Dados de condicionamento negativo com o latente da imagem codificada anexado. | CONDITIONING |
| `latent` | Tensor latente preenchido com zeros e com as mesmas dimensões da imagem codificada. | LATENT |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/InstructPixToPixConditioning/pt-BR.md)

---
**Source fingerprint (SHA-256):** `e9a5a05cdeafe9337ca2033111f1ad4f7314fa33d71a4764f62919857efc79f4`
