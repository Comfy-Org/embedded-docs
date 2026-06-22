# LTXVAddGuide

Esta documentação foi gerada por IA. Se você encontrar algum erro ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVAddGuide/en.md)

O nó LTXVAddGuide adiciona orientação de condicionamento de vídeo a sequências latentes, codificando imagens ou vídeos de entrada e incorporando-os como quadros-chave nos dados de condicionamento. Ele processa a entrada através de um codificador VAE e posiciona estrategicamente os latentes resultantes em posições de quadro especificadas, atualizando tanto o condicionamento positivo quanto o negativo com informações dos quadros-chave. O nó lida com restrições de alinhamento de quadros e permite controle sobre a intensidade da influência do condicionamento.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `positive` | Entrada de condicionamento positivo a ser modificada com orientação de quadro-chave | CONDITIONING | Sim | - |
| `negative` | Entrada de condicionamento negativo a ser modificada com orientação de quadro-chave | CONDITIONING | Sim | - |
| `vae` | Modelo VAE usado para codificar os quadros de imagem/vídeo de entrada | VAE | Sim | - |
| `latent` | Sequência latente de entrada que receberá os quadros de condicionamento | LATENT | Sim | - |
| `image` | Imagem ou vídeo para condicionar o vídeo latente. Deve ter 8*n + 1 quadros. Se o vídeo não tiver 8*n + 1 quadros, ele será cortado para o valor mais próximo de 8*n + 1 quadros. | IMAGE | Sim | - |
| `frame_idx` | Índice do quadro para iniciar o condicionamento. Para imagens de quadro único ou vídeos com 1 a 8 quadros, qualquer valor de `frame_idx` é aceitável. Para vídeos com 9 ou mais quadros, `frame_idx` deve ser divisível por 8, caso contrário, será arredondado para baixo até o múltiplo de 8 mais próximo. Valores negativos são contados a partir do final do vídeo. (padrão: 0) | INT | Não | -9999 a 9999 |
| `strength` | Intensidade da influência do condicionamento, onde 1.0 aplica condicionamento total e 0.0 não aplica condicionamento (padrão: 1.0) | FLOAT | Não | 0.0 a 1.0 |

**Nota:** A imagem/vídeo de entrada deve ter uma contagem de quadros seguindo o padrão 8*n + 1 (por exemplo, 1, 9, 17, 25 quadros). Se a entrada exceder esse padrão, ela será automaticamente cortada para a contagem de quadros válida mais próxima.

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `positive` | Condicionamento positivo atualizado com informações de orientação de quadro-chave | CONDITIONING |
| `negative` | Condicionamento negativo atualizado com informações de orientação de quadro-chave | CONDITIONING |
| `latent` | Sequência latente com quadros de condicionamento incorporados e máscara de ruído atualizada | LATENT |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVAddGuide/pt-BR.md)

---
**Source fingerprint (SHA-256):** `e7f4e6ed25cddd4b50b98341c63fc9915afc4956317ac7a5a9121fdc53c03a2d`
