# MiniMax H3 Imagem para Vídeo

Este nó prepara o condicionamento e o latent vazio necessários para gerar um vídeo com o modelo MiniMax H3. Ele recebe um prompt de texto e, opcionalmente, imagens para o primeiro e/ou último quadro do vídeo, e os converte em entradas do modelo. As imagens-chave são redimensionadas, codificadas e anexadas ao condicionamento no início e no final do vídeo.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Faixa |
|-----------|-------------|-----------|----------|-------|
| `clip` | Modelo CLIP usado para tokenizar o prompt e codificar as imagens-chave em condicionamento. | CLIP | Sim |  |
| `vae` | Modelo VAE usado para codificar as imagens-chave no espaço latente quando imagens-chave são fornecidas. | VAE | Sim |  |
| `prompt` | Prompt de texto que descreve o vídeo a ser gerado. Suporta múltiplas linhas e prompts dinâmicos. | STRING | Sim |  |
| `largura` | Largura do vídeo em pixels (padrão: 1344). | INT | Sim | 32 a MAX_RESOLUTION (passo 32) |
| `altura` | Altura do vídeo em pixels (padrão: 768). | INT | Sim | 32 a MAX_RESOLUTION (passo 32) |
| `duração` | Número de quadros a 24 fps, ajustado para cima na grade 17k+5 do modelo (124 = ~5s; a faixa treinada é ~124-362; durações maiores não são testadas) (padrão: 124). | INT | Sim | 5 a 3600 (passo 17) |
| `primeiro_quadro` | Imagem opcional usada como o primeiro quadro do vídeo. Ela é esticada para o tamanho total da tela, portanto sua proporção de aspecto não é preservada. Apenas a primeira imagem do lote de entrada é usada. | IMAGE | Não |  |
| `último_quadro` | Imagem opcional usada como o último quadro do vídeo. Ela é recortada para cobrir a tela preservando sua proporção de aspecto. Apenas a primeira imagem do lote de entrada é usada. | IMAGE | Não |  |

Quando `first_frame` e/ou `last_frame` são fornecidos, as imagens-chave são codificadas com o VAE e anexadas ao condicionamento no quadro 0 e no quadro final, respectivamente. Quando nenhum é fornecido, o nó trabalha apenas com o prompt.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `positive` | Condicionamento contendo o prompt codificado e, quando imagens-chave são fornecidas, os quadros-chave codificados e a contagem de quadros para o modelo MiniMax H3. | CONDITIONING |
| `latent` | Latente vazio representando o vídeo a ser gerado, com a largura, altura e contagem de quadros solicitadas. | LATENT |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MiniMaxH3ImageToVideo/pt-BR.md)

---
**Source fingerprint (SHA-256):** `46efc87bd46f4a86cb6df37c75f960419a2a98b34480e7dc0023c9d87903870b`
