> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/InstructPixToPixConditioning/pt-BR.md)

O nó InstructPixToPixConditioning prepara dados de condicionamento para edição de imagens InstructPix2Pix, combinando prompts de texto positivos e negativos com dados de imagem. Ele processa imagens de entrada por meio de um codificador VAE para criar representações latentes e anexa esses latentes aos dados de condicionamento positivos e negativos. O nó lida automaticamente com as dimensões da imagem, cortando-as para múltiplos de 8 pixels, garantindo compatibilidade com o processo de codificação VAE.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Faixa | Descrição |
|-----------|--------------|-------------|-------|-----------|
| `positive` | CONDITIONING | Sim | - | Dados de condicionamento positivo contendo prompts de texto e configurações para características desejadas da imagem |
| `negative` | CONDITIONING | Sim | - | Dados de condicionamento negativo contendo prompts de texto e configurações para características indesejadas da imagem |
| `vae` | VAE | Sim | - | Modelo VAE usado para codificar imagens de entrada em representações latentes |
| `pixels` | IMAGE | Sim | - | Imagem de entrada a ser processada e codificada no espaço latente |

**Observação:** As dimensões da imagem de entrada são ajustadas automaticamente, cortando para o múltiplo mais próximo de 8 pixels em largura e altura, garantindo compatibilidade com o processo de codificação VAE.

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|---------------|--------------|-----------|
| `positive` | CONDITIONING | Dados de condicionamento positivo com representação de imagem latente anexada |
| `negative` | CONDITIONING | Dados de condicionamento negativo com representação de imagem latente anexada |
| `latent` | LATENT | Tensor latente vazio com as mesmas dimensões da imagem codificada |

---
**Source fingerprint (SHA-256):** `4b2383c9d64efdb558758359bf544fc5a1be65c12b23b54152e2df79a6dd8d79`
