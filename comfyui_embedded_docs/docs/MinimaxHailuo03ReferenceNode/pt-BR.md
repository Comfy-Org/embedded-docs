# MinimaxHailuo03ReferenceNode

Este nó gera um vídeo usando o modelo MiniMax H3, utilizando imagens, vídeos e áudios de referência para condicionar o resultado. As referências são mencionadas no prompt pela ordem de conexão: "Image 1", "Image 2", "Video 1", "Audio 1" e assim por diante.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Intervalo |
|-----------|-------------|--------------|-------------|-----------|
| `modelo` | Modelo a ser usado para geração de vídeo (padrão: "MiniMax H3"). Selecionar "MiniMax H3" fornece as configurações `prompt`, `duration`, `resolution`, `ratio`, `reference_images`, `reference_videos` e `reference_audios` abaixo. | STRING | Sim | "MiniMax H3" |
| `prompt` | Descrição textual do vídeo a ser gerado. A mídia de referência pode ser mencionada por sua ordem, por exemplo "Image 1", "Image 2", "Video 1" ou "Audio 1". | STRING | Sim | Comprimento mínimo: 1 caractere |
| `duration` | Duração do vídeo gerado em segundos. | INT | Sim | Múltiplas opções disponíveis |
| `resolution` | Resolução de saída do vídeo gerado. | STRING | Sim | Múltiplas opções disponíveis |
| `ratio` | Proporção de aspecto do vídeo gerado. | STRING | Sim | Múltiplas opções disponíveis |
| `reference_images` | Imagens de referência de assunto ou estilo, mencionadas no prompt como "Image 1".."Image 9" na ordem de conexão. Até 9 imagens. | IMAGE | Não | 0 a 9 imagens |
| `reference_videos` | Vídeos de referência de movimento ou cena, mencionados no prompt como "Video 1".."Video 3" na ordem de conexão. Até 3 vídeos, cada um com 2 a 15 segundos, totalizando 15 segundos. | VIDEO | Não | 0 a 3 vídeos |
| `reference_audios` | Referências de áudio, mencionadas no prompt como "Audio 1".."Audio 3" na ordem de conexão. Até 3 clipes, cada um com 2 a 15 segundos, totalizando 15 segundos. Não podem ser usadas sem uma imagem ou vídeo de referência. | AUDIO | Não | 0 a 3 clipes |
| `semente` | Semente aleatória. A mesma solicitação com a mesma semente gera resultados semelhantes, mas não garantidamente idênticos (padrão: 42). | INT | Sim | 0 a 4294967295 |
| `marca d'água` | Se deve adicionar uma marca d'água AIGC ao vídeo (padrão: false). | BOOLEAN | Não | true<br>false |

### Restrições de Parâmetros

- É necessária pelo menos uma imagem de referência ou um vídeo de referência. Apenas áudio de referência não é aceito.
- Cada imagem de referência deve ter uma proporção de aspecto entre aproximadamente 0.4 e 2.5 (2:5 a 5:2) e uma largura e altura mínimas de 256 pixels.
- Cada vídeo de referência deve ter entre 2 e 15 segundos de duração, com uma taxa de quadros entre 23.976 e 60 FPS. A duração total de todos os vídeos de referência não pode exceder 15 segundos.
- Cada clipe de áudio de referência deve ter entre 2 e 15 segundos de duração. A duração total de todos os clipes de áudio de referência não pode exceder 15 segundos.

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
|---------------|-----------|--------------|
| `video` | O vídeo gerado. | VIDEO |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MinimaxHailuo03ReferenceNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `beca020333a544188e6c21829eb8e63415aa5299efc676438e85662a5f08660d`
