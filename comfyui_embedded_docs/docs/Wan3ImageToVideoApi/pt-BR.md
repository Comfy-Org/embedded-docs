# Wan 3.0 Imagem para Vídeo

Este nó gera um vídeo a partir de uma imagem de primeiro quadro usando o modelo Wan 3.0. Você pode, opcionalmente, fornecer uma imagem de último quadro para controlar como o vídeo termina; o modelo então cria um vídeo que faz a transição do primeiro quadro para o último quadro.

## Entradas

### Entradas comuns

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|---------------|-------------|-----------|
| `Modelo` | Seleciona a variante do modelo Wan 3.0 a ser usada e determina quais configurações específicas do modelo são exibidas abaixo. | DYNAMIC_COMBO | Sim | "wan3.0-video"<br>"wan3.0-video-prime" |
| `first_frame` | Imagem do primeiro quadro. É necessária exatamente uma imagem. | IMAGE | Sim | Imagem única |
| `last_frame` | Imagem do último quadro. O modelo gera um vídeo que faz a transição do primeiro para o último quadro. Opcional; se fornecida, é necessária exatamente uma imagem. | IMAGE | Não | Imagem única |
| `Semente` | Semente usada para a geração (padrão: 42). | INT | Sim | 0 - 2147483647 |
| `Marca-d'água` | Se deve adicionar uma marca d'água gerada por IA ao resultado (padrão: false). | BOOLEAN | Sim | true<br>false |

### Entradas do wan3.0-video e do wan3.0-video-prime

Estas configurações específicas do modelo são compartilhadas por ambas as opções de modelo e aparecem quando um modelo é selecionado.

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|---------------|-------------|-----------|
| `prompt` | Prompt que descreve os elementos e as características visuais. Suporta inglês e chinês. Pode ser deixado vazio (padrão: vazio). | STRING | Sim | Até 20000 caracteres |
| `resolution` | Resolução do vídeo de saída. | COMBO | Sim | "1080P"<br>"720P"<br>"480P" |
| `ratio` | Proporção de aspecto do vídeo de saída. Com "adaptive", as dimensões de saída são derivadas do primeiro quadro. | COMBO | Sim | "adaptive"<br>"16:9"<br>"9:16"<br>"1:1"<br>"4:3"<br>"3:4" |
| `duration` | Duração da saída em segundos. Com "auto", o modelo escolhe uma duração que se ajusta ao prompt. | COMBO | Sim | "auto"<br>"2" - "30" |
| `audio` | Se o vídeo de saída contém uma trilha de áudio (padrão: true). | BOOLEAN | Sim | true<br>false |
| `prompt_extend` | Se deve aprimorar o prompt com assistência de IA (padrão: true). | BOOLEAN | Sim | true<br>false |

Nota: O nó aceita exatamente uma imagem `first_frame` e, opcionalmente, uma imagem `last_frame`. Se mais de uma imagem for conectada a qualquer uma das entradas, um erro será gerado. Quando `last_frame` é fornecida, o vídeo gerado faz a transição do primeiro quadro para o último quadro. O `prompt` é limitado a 20.000 caracteres.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|---------------|-----------|---------------|
| `video` | O vídeo gerado. Contém uma trilha de áudio quando a opção `audio` está habilitada. | VIDEO |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Wan3ImageToVideoApi/pt-BR.md)

---
**Source fingerprint (SHA-256):** `ff9fce554fa7aa5fc8729b5f84b2f8bf89e8e7772ce1c32b1307d0dc4882200c`
