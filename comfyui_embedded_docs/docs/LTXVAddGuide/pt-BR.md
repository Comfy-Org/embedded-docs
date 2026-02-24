> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVAddGuide/pt-BR.md)

O nó LTXVAddGuide adiciona orientação de condicionamento de vídeo a sequências latentes, codificando imagens ou vídeos de entrada e incorporando-os como quadros-chave aos dados de condicionamento. Ele processa a entrada por meio de um codificador VAE e posiciona estrategicamente os latentes resultantes em posições de quadro especificadas, enquanto atualiza tanto o condicionamento positivo quanto o negativo com informações dos quadros-chave. O nó lida com restrições de alinhamento de quadros e permite o controle sobre a força da influência do condicionamento.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `positive` | CONDITIONING | Sim | - | Entrada de condicionamento positivo a ser modificada com a orientação de quadros-chave |
| `negative` | CONDITIONING | Sim | - | Entrada de condicionamento negativo a ser modificada com a orientação de quadros-chave |
| `vae` | VAE | Sim | - | Modelo VAE usado para codificar os quadros da imagem/vídeo de entrada |
| `latent` | LATENT | Sim | - | Sequência latente de entrada que receberá os quadros de condicionamento |
| `image` | IMAGE | Sim | - | Imagem ou vídeo para condicionar o vídeo latente. Deve ter 8*n + 1 quadros. Se o vídeo não tiver 8*n + 1 quadros, ele será recortado para o número mais próximo de 8*n + 1 quadros. |
| `frame_idx` | INT | Não | -9999 a 9999 | Índice do quadro para iniciar o condicionamento. Para imagens de quadro único ou vídeos com 1-8 quadros, qualquer valor de `frame_idx` é aceitável. Para vídeos com 9+ quadros, `frame_idx` deve ser divisível por 8, caso contrário será arredondado para baixo para o múltiplo de 8 mais próximo. Valores negativos são contados a partir do final do vídeo. (padrão: 0) |
| `strength` | FLOAT | Não | 0.0 a 1.0 | Força da influência do condicionamento, onde 1.0 aplica o condicionamento total e 0.0 não aplica nenhum condicionamento (padrão: 1.0) |

**Observação:** A imagem/vídeo de entrada deve ter uma contagem de quadros que siga o padrão 8*n + 1 (por exemplo, 1, 9, 17, 25 quadros). Se a entrada exceder esse padrão, ela será automaticamente recortada para a contagem de quadros válida mais próxima.

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|-------------|-----------|-------------|
| `positive` | CONDITIONING | Condicionamento positivo atualizado com informações de orientação de quadros-chave |
| `negative` | CONDITIONING | Condicionamento negativo atualizado com informações de orientação de quadros-chave |
| `latent` | LATENT | Sequência latente com quadros de condicionamento incorporados e máscara de ruído atualizada |
