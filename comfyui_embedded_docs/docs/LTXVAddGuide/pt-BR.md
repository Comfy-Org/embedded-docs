# LTXVAddGuide

O nó LTXVAddGuide adiciona orientação de condicionamento de vídeo a sequências latentes, codificando imagens ou vídeos de entrada e incorporando-os como keyframes nos dados de condicionamento. Ele processa a entrada por meio de um codificador VAE e posiciona estrategicamente os latents resultantes em posições de quadro especificadas, atualizando tanto o condicionamento positivo quanto o negativo com informações de keyframe. O nó lida com restrições de alinhamento de quadros e permite controlar a força da influência do condicionamento.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `positive` | Entrada de condicionamento positivo a ser modificada com a orientação por keyframes | CONDITIONING | Sim | - |
| `negative` | Entrada de condicionamento negativo a ser modificada com a orientação por keyframes | CONDITIONING | Sim | - |
| `vae` | Modelo VAE usado para codificar os quadros de imagem/vídeo de entrada | VAE | Sim | - |
| `latent` | Sequência latente de entrada que receberá os quadros de condicionamento | LATENT | Sim | - |
| `image` | Imagem ou vídeo para condicionar o vídeo latente. Deve ter 8*n + 1 quadros. Se o vídeo não tiver 8*n + 1 quadros, ele será cortado para o valor mais próximo de 8*n + 1 quadros. | IMAGE | Sim | - |
| `frame_idx` | Índice do quadro no qual o condicionamento começará. Para imagens de quadro único ou vídeos com 1 a 8 quadros, qualquer valor de `frame_idx` é aceitável. Para vídeos com 9 ou mais quadros, `frame_idx` deve ser divisível por 8; caso contrário, será arredondado para baixo até o múltiplo de 8 mais próximo. Valores negativos são contados a partir do final do vídeo. (padrão: 0) | INT | Sim | -9999 a 9999 |
| `strength` | Força da influência do condicionamento, em que 1.0 aplica condicionamento total e 0.0 não aplica condicionamento (padrão: 1.0) | FLOAT | Sim | 0.0 a 10.0 |
| `attention_mask` | Máscara espacial opcional no espaço dos pixels. Controla a influência do condicionamento por região por meio da autoatenção, multiplicada pela `strength`. | MASK | Não | - |
| `iclora_parameters` | Parâmetros IC-LoRA opcionais de um nó Get IC-LoRA Parameters. Usados para ajustar o processamento da orientação conforme exigido por determinados IC-LoRAs (por exemplo, aqueles com `reference_downscale_factor` > 1). Quando encadeados, cada LTXVAddGuide usa apenas os parâmetros conectados a ele. | IC_LORA_PARAMETERS | Não | - |

**Observação:** A imagem/vídeo de entrada deve ter uma contagem de quadros seguindo o padrão 8*n + 1 (por exemplo, 1, 9, 17, 25 quadros). Se a entrada exceder esse padrão, ela será automaticamente cortada para a contagem de quadros válida mais próxima.

**Observação sobre `iclora_parameters`:** Ao usar parâmetros IC-LoRA com `reference_downscale_factor` maior que 1, as dimensões espaciais latentes (largura e altura) devem ser divisíveis por esse fator. O nó gerará um erro se essa condição não for atendida.

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `positive` | Condicionamento positivo atualizado com informações de orientação por keyframes | CONDITIONING |
| `negative` | Condicionamento negativo atualizado com informações de orientação por keyframes | CONDITIONING |
| `latent` | Sequência latente com quadros de condicionamento incorporados e máscara de ruído atualizada | LATENT |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVAddGuide/pt-BR.md)

---
**Source fingerprint (SHA-256):** `3e0d1422fbd1b5b3e4c69e641af2ecdb5ae8de3f4368b336917a0dce4286771e`
