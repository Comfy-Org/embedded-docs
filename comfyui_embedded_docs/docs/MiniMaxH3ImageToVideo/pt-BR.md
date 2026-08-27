# MiniMax H3 Imagem para Vídeo

Este nó prepara o condicionamento e o latente vazio necessários para gerar um vídeo com o modelo MiniMax H3. Ele recebe um prompt de texto e, opcionalmente, imagens para o primeiro e/ou último quadro do vídeo, e os converte em entradas do modelo. As imagens-chave são redimensionadas, codificadas e anexadas ao condicionamento no início e no final do vídeo.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
|-----------|-------------|-----------|----------|-------|
| `clip` | Modelo CLIP usado para tokenizar o prompt e codificar as imagens-chave em condicionamento. | CLIP | Sim |  |
| `vae` | Modelo VAE usado para codificar as imagens-chave no espaço latente quando imagens-chave são fornecidas. | VAE | Sim |  |
| `prompt` | Prompt de texto que descreve o vídeo a ser gerado. Suporta múltiplas linhas e prompts dinâmicos. | STRING | Sim |  |
| `largura` | Largura do vídeo em pixels (padrão: 1344). | INT | Sim | 32 to MAX_RESOLUTION (step 32) |
| `altura` | Altura do vídeo em pixels (padrão: 768). | INT | Sim | 32 to MAX_RESOLUTION (step 32) |
| `duração` | Contagem de quadros a 24 fps, arredondada para cima à grade 17k+5 do modelo (124 = ~5s; a faixa treinada é ~124-362, valores maiores não foram testados) (padrão: 124). | INT | Sim | 5 a 3600 (step 17) |
| `primeiro_quadro` | Imagem opcional usada como o primeiro quadro do vídeo. Ela é esticada para o tamanho total da tela, portanto sua proporção não é preservada. Somente a primeira imagem do lote de entrada é usada. | IMAGE | Não |  |
| `último_quadro` | Imagem opcional usada como o último quadro do vídeo. Ela é cortada para cobrir a tela preservando sua proporção. Somente a primeira imagem do lote de entrada é usada. | IMAGE | Não |  |

Quando `first_frame` e/ou `last_frame` são fornecidos, as imagens-chave são codificadas com o VAE e anexadas ao condicionamento no quadro 0 e no quadro final, respectivamente. Quando nenhum é fornecido, o nó trabalha apenas com o prompt. O `length` solicitado é arredondado para cima até a contagem de quadros válida mais próxima (17k + 5); portanto, a contagem efetiva de quadros pode ser ligeiramente maior que a solicitada.

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
|-------------|-------------|-----------|
| `positivo` | Condicionamento contendo o prompt codificado e, quando imagens-chave são fornecidas, os quadros-chave codificados e a contagem de quadros para o modelo MiniMax H3. | CONDITIONING |
| `latent` | Latente de áudio-vídeo vazio representando o conteúdo a ser gerado, com a largura, altura e contagem de quadros solicitadas. | LATENT |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MiniMaxH3ImageToVideo/pt-BR.md)

---
**Source fingerprint (SHA-256):** `d1bdf3f8c66ef20ff11c35203d2c266a88dcf8cc00c65dbb0aea2b1dd16befd6`
