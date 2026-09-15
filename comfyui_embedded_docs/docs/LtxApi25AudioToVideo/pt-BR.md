# LTX 2.5 Áudio para Vídeo

Este nó gera um vídeo que acompanha uma faixa de áudio usando o modelo LTX 2.5. O áudio determina a duração do vídeo (entre 2 e 20 segundos), e você pode, opcionalmente, fornecer uma imagem para usar como primeiro quadro. O vídeo é gerado por meio do serviço de API do LTX 2.5.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `áudio` | Faixa de áudio que orienta o vídeo. Sua duração (2-20 segundos) define a duração do vídeo. | AUDIO | Sim | 2-20 segundos |
| `modelo` | A versão do modelo LTX 2.5 a ser usada. Selecionar um modelo também revela a subopção `resolution` para esse modelo. | COMBO | Sim | "LTX-2.5 (Fast)"<br>"LTX-2.5 (Pro)" |
| `resolution` | A resolução de saída do vídeo gerado. Esta subopção é exibida sob o `model` selecionado (padrão: "1920x1080"). Ambos os modelos oferecem as mesmas opções de resolução. | COMBO | Sim | "1920x1080"<br>"1080x1920" |
| `prompt` | Uma descrição textual que orienta o conteúdo do vídeo gerado (padrão: ""). Deve conter pelo menos 1 caractere e no máximo 10000 caracteres. | STRING | Sim | 1-10000 caracteres |
| `semente` | Um número que controla a aleatoriedade da geração. A mesma seed produz o mesmo resultado (padrão: 42). | INT | Sim | Qualquer inteiro |
| `imagem` | Primeiro quadro opcional a ser usado para o vídeo. Apenas uma imagem é suportada. | IMAGE | Não | Imagem única |

Observações sobre restrições:
- A duração do áudio deve estar entre 2 e 20 segundos; o nó gera um erro se estiver fora desse intervalo.
- O prompt é obrigatório e não pode estar vazio; deve ter entre 1 e 10000 caracteres.
- Apenas uma única imagem de entrada é aceita quando `image` é fornecido.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `video` | O vídeo gerado, orientado pela faixa de áudio fornecida. | VIDEO |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LtxApi25AudioToVideo/pt-BR.md)

---
**Source fingerprint (SHA-256):** `ae0d0123c0421f645448496d30a53a21aba1728310180719a4c4599eca8351c5`
