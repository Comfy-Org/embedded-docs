> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/InstructPixToPixConditioning/pt-BR.md)

O nó InstructPixToPixConditioning prepara dados de condicionamento para a edição de imagens InstructPix2Pix, combinando *prompts* de texto positivos e negativos com dados de imagem. Ele processa as imagens de entrada por meio de um codificador VAE para criar representações latentes e anexa esses latentes aos dados de condicionamento positivo e negativo. O nó ajusta automaticamente as dimensões da imagem recortando-as para múltiplos de 8 pixels, garantindo compatibilidade com o processo de codificação VAE.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `positive` | CONDITIONING | Sim | - | Dados de condicionamento positivo contendo *prompts* de texto e configurações para as características desejadas da imagem |
| `negative` | CONDITIONING | Sim | - | Dados de condicionamento negativo contendo *prompts* de texto e configurações para as características indesejadas da imagem |
| `vae` | VAE | Sim | - | Modelo VAE usado para codificar as imagens de entrada em representações latentes |
| `pixels` | IMAGE | Sim | - | Imagem de entrada a ser processada e codificada no espaço latente |

**Observação:** As dimensões da imagem de entrada são ajustadas automaticamente pelo recorte para o múltiplo de 8 pixels mais próximo, tanto na largura quanto na altura, para garantir compatibilidade com o processo de codificação VAE.

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|-------------|-----------|-------------|
| `positive` | CONDITIONING | Dados de condicionamento positivo com a representação latente da imagem anexada |
| `negative` | CONDITIONING | Dados de condicionamento negativo com a representação latente da imagem anexada |
| `latent` | LATENT | Tensor latente vazio com as mesmas dimensões da imagem codificada |
