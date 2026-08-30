# Wan 3.0 Referência para Vídeo

Este nó gera um vídeo a partir de um prompt de texto e de imagens, vídeos e áudio de referência opcionais, usando o modelo Wan 3.0. As mídias de referência podem ser combinadas livremente e mencionadas no prompt como @Image1, @Video1 e @Audio1. O nó envia a solicitação de geração para a API Wan e retorna o vídeo finalizado.

## Entradas

### Entradas comuns

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `Modelo` | Seleciona a variante do modelo Wan 3.0 usada para a geração. | DYNAMIC_COMBO | Sim | `wan3.0-video`<br>`wan3.0-video-prime` |
| `Semente` | Semente a ser usada para a geração. Padrão: 42. | INT | Sim | 0 a 2147483647 |
| `Marca-d'água` | Se deve adicionar uma marca d'água gerada por IA ao resultado. Padrão: false. | BOOLEAN | Sim | true<br>false |

### Entradas do wan3.0-video e wan3.0-video-prime

Ambas as opções de modelo compartilham o mesmo conjunto de parâmetros.

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Prompt que descreve os elementos e recursos visuais. Suporta inglês e chinês. Refira-se às mídias de referência conectadas como @Image1, @Video1, @Audio1, numeradas por tipo na ordem de entrada. Padrão: vazio. | STRING | Sim | Até 20.000 caracteres |
| `resolution` | Resolução do vídeo de saída. | COMBO | Sim | "1080P"<br>"720P"<br>"480P" |
| `ratio` | Proporção de aspecto do vídeo de saída. Com "adaptive", as dimensões de saída são derivadas da mídia de entrada. | COMBO | Sim | "adaptive"<br>"16:9"<br>"9:16"<br>"1:1"<br>"4:3"<br>"3:4" |
| `duration` | Duração da saída em segundos. Com "auto", o modelo escolhe uma duração que se ajusta ao prompt e às mídias de referência. A duração combinada dos vídeos de referência e da saída não deve exceder 30 segundos. | COMBO | Sim | "auto"<br>"2" a "30" (segundos inteiros) |
| `audio` | Se o vídeo de saída contém uma trilha de áudio. Padrão: true. | BOOLEAN | Sim | true<br>false |
| `prompt_extend` | Se deve aprimorar o prompt com assistência de IA. Padrão: true. | BOOLEAN | Sim | true<br>false |

### Entradas de referência

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `reference_images` | Slot expansível: conecte de 1 a 10 imagens de referência. As referências são numeradas como image1 a image10 na ordem de entrada. | IMAGE | Não | 0 a 10 imagens |
| `reference_videos` | Slot expansível: conecte de 1 a 5 vídeos de referência. As referências são numeradas como video1 a video5 na ordem de entrada. | VIDEO | Não | 0 a 5 vídeos |
| `reference_audios` | Slot expansível: conecte de 1 a 5 clipes de áudio de referência. As referências são numeradas como audio1 a audio5 na ordem de entrada. | AUDIO | Não | 0 a 5 clipes de áudio |

**Restrições:**

- O prompt deve conter pelo menos um caractere não vazio, ou pelo menos uma imagem, um vídeo ou um áudio de referência deve estar conectado.
- As tags de referência no prompt devem corresponder às entradas conectadas. Por exemplo, @Image1 refere-se à primeira imagem de referência conectada, @Video2 ao segundo vídeo de referência conectado e @Audio1 ao primeiro áudio de referência conectado. As tags são numeradas separadamente por tipo, na ordem de entrada.
- Cada imagem de referência conectada deve conter exatamente uma imagem, não um lote.
- Cada vídeo de referência deve ter 15 segundos ou menos. A duração total de todos os vídeos de referência não deve exceder 15 segundos.
- Cada áudio de referência deve ter 15 segundos ou menos. A duração total de todos os áudios de referência não deve exceder 15 segundos.
- Quando `duration` não for "auto", a duração total de todos os vídeos de referência somada à duração de saída selecionada não deve exceder 30 segundos.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `video` | O arquivo de vídeo gerado. Inclui uma trilha de áudio quando o parâmetro `audio` está habilitado. | VIDEO |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Wan3ReferenceToVideoApi/pt-BR.md)

---
**Source fingerprint (SHA-256):** `09caa8142d71235417a3dfc5676c5f6accc2af1287fad3b7050844dd9453cc64`
