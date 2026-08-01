# MinimaxHailuo03FirstLastFrameNode

Este nó gera um vídeo a partir de uma imagem de primeiro quadro e uma imagem opcional de último quadro usando o modelo MiniMax H3. O vídeo segue a proporção das imagens fornecidas e, quando um último quadro é fornecido, anima do primeiro quadro em direção ao último quadro.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `model` | Modelo a ser usado para geração de vídeo. Este combo inclui a escolha do modelo ("MiniMax H3"), um prompt de texto descrevendo o vídeo a ser gerado, a resolução de saída e a duração do vídeo. O prompt deve conter pelo menos um caractere que não seja espaço em branco. | COMBO | Sim | "MiniMax H3" |
| `first_frame` | Imagem do primeiro quadro para o vídeo. A proporção do vídeo gerado segue esta imagem. Deve ter pelo menos 256x256 pixels com uma proporção largura-altura entre 0.4 e 2.5. | IMAGE | Sim | - |
| `last_frame` | Imagem opcional do último quadro para o vídeo. Quando fornecida, o vídeo começa no primeiro quadro e termina nesta imagem. Deve atender aos mesmos requisitos de tamanho e proporção que `first_frame`. | IMAGE | Não | - |
| `seed` | Semente aleatória. A mesma solicitação com a mesma semente produz resultados semelhantes, mas não garantidamente idênticos. Inclui uma opção "control after generate" para randomizar após cada geração. Padrão: 42. | INT | Sim | 0 a 4294967295 |
| `watermark` | Se deve adicionar uma marca d'água AIGC ao vídeo. Este é um parâmetro avançado. Padrão: False. | BOOLEAN | Sim | True<br>False |

**Nota sobre restrições:**
- O prompt de texto dentro do combo `model` não pode estar vazio; prompts contendo apenas espaços em branco são rejeitados.
- Qualquer imagem de quadro fornecida (`first_frame` e, se usado, `last_frame`) deve ter pelo menos 256 pixels de largura e 256 pixels de altura, com uma proporção largura-altura entre 0.4 e 2.5 (aproximadamente 2:5 a 5:2).
- `last_frame` é opcional. Quando omitido, o vídeo é gerado apenas a partir do primeiro quadro.
- A proporção do vídeo de saída é determinada pelas imagens fornecidas, não por uma configuração de proporção separada.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `video` | O vídeo gerado criado a partir do primeiro quadro e do último quadro opcional usando o modelo MiniMax H3. | VIDEO |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MinimaxHailuo03FirstLastFrameNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `f4cb9217eb346019680c64b30c1beacce16f0050616b7b76265edc5840f6b21e`
