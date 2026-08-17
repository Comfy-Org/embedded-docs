# MiniMax H3 Imagem para Vídeo

MiniMax H3 Image to Video prepara o condicionamento e o latente vazio necessários para gerar um vídeo com o modelo MiniMax H3. Ele recebe um prompt de texto e, opcionalmente, imagens para o primeiro e/ou último quadro do vídeo, e as converte em entradas do modelo. As imagens de quadro-chave são redimensionadas, codificadas e anexadas ao condicionamento no início e no final do vídeo.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `clip` | Modelo CLIP usado para tokenizar o prompt e codificar as imagens de quadro-chave em condicionamento. | CLIP | Sim |  |
| `vae` | Modelo VAE usado para codificar as imagens de quadro-chave no espaço latente quando imagens de quadro-chave são fornecidas. | VAE | Sim |  |
| `prompt` | Prompt de texto que descreve o vídeo a ser gerado. Suporta múltiplas linhas e prompts dinâmicos. | STRING | Sim |  |
| `width` | Largura do vídeo em pixels (padrão: 1344). | INT | Sim | 32 a MAX_RESOLUTION (passo 32) |
| `height` | Altura do vídeo em pixels (padrão: 768). | INT | Sim | 32 a MAX_RESOLUTION (passo 32) |
| `length` | Contagem de quadros a 24 fps, arredondada para cima conforme a grade 17k+5 do modelo (124 = ~5s; o intervalo de treinamento é de ~124 a 362; valores maiores não foram testados) (padrão: 124). | INT | Sim | 5 a 3600 (passo 17) |
| `first_frame` | Imagem opcional usada como primeiro quadro do vídeo. Ela é esticada para o tamanho total da tela, portanto sua proporção não é preservada. Apenas a primeira imagem do lote de entrada é usada. | IMAGE | Não |  |
| `last_frame` | Imagem opcional usada como último quadro do vídeo. Ela é cortada para cobrir a tela, preservando sua proporção. Apenas a primeira imagem do lote de entrada é usada. | IMAGE | Não |  |

Quando `first_frame` e/ou `last_frame` são fornecidos, as imagens de quadro-chave são codificadas com o VAE e anexadas ao condicionamento no quadro 0 e no quadro final, respectivamente. Quando nenhuma delas é fornecida, o nó trabalha apenas com o prompt.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `positive` | Condicionamento contendo o prompt codificado e, quando imagens de quadro-chave são fornecidas, os quadros-chave codificados posicionados no primeiro e no último quadro do vídeo para o modelo MiniMax H3. | CONDITIONING |
| `latent` | Latente vazio que representa o vídeo e sua faixa de áudio correspondente a serem gerados, com a largura, a altura e a contagem de quadros solicitadas. | LATENT |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MiniMaxH3ImageToVideo/pt-BR.md)

---
**Source fingerprint (SHA-256):** `d1bdf3f8c66ef20ff11c35203d2c266a88dcf8cc00c65dbb0aea2b1dd16befd6`
