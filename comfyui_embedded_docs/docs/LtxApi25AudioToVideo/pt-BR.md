# LtxApi25AudioToVideo

Este nó gera um vídeo que segue uma trilha de áudio usando o modelo LTX 2.5. O áudio determina a duração do vídeo (entre 2 e 20 segundos), e você pode opcionalmente fornecer uma imagem para usar como primeiro quadro. O vídeo é gerado por meio do serviço de API LTX 2.5.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `audio` | Trilha de áudio que orienta o vídeo. A duração do áudio (2 a 20 segundos) define a duração do vídeo. | AUDIO | Sim | 2 a 20 segundos |
| `model` | A versão do modelo LTX 2.5 a ser usada. A resolução é escolhida junto com o modelo; ambos os modelos oferecem as mesmas opções de resolução (1920x1080 ou 1080x1920). | COMBO | Sim | "LTX-2.5 (Fast)"<br>"LTX-2.5 (Pro)" |
| `prompt` | Uma descrição em texto que orienta o conteúdo do vídeo gerado (padrão: ""). Deve conter pelo menos 1 caractere e no máximo 10000 caracteres. | STRING | Sim | 1 a 10000 caracteres |
| `seed` | Um número que controla a aleatoriedade da geração. A mesma `seed` produz o mesmo resultado (padrão: 42). | INT | Sim | Qualquer número inteiro |
| `image` | Primeiro quadro opcional a ser usado no vídeo. Apenas uma imagem é suportada. | IMAGE | Não | Uma única imagem |

## Notas sobre restrições

- A duração do áudio deve estar entre 2 e 20 segundos; o nó gera um erro se estiver fora desse intervalo.
- O parâmetro `prompt` é obrigatório e não pode ficar vazio.
- Apenas uma única imagem de entrada é aceita quando `image` é fornecida.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `video` | O vídeo gerado, conduzido pela trilha de áudio fornecida. | VIDEO |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LtxApi25AudioToVideo/pt-BR.md)

---
**Source fingerprint (SHA-256):** `ae0d0123c0421f645448496d30a53a21aba1728310180719a4c4599eca8351c5`
