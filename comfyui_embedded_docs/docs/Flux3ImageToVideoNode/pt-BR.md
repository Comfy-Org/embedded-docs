# Flux3ImageToVideoNode

O Flux 3 Image to Video anima de 1 a 10 imagens com o FLUX 3. Cada imagem se torna um quadro do clipe: uma imagem o abre, duas fazem uma transição da primeira para a segunda, e as demais são distribuídas ao longo do clipe ou fixadas nos tempos que você escolher.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Como a cena deve se mover e soar; o prompt é interpretado e expandido antes da geração. Deve conter pelo menos um caractere. | STRING | Sim | Texto multilinha (padrão: vazio) |
| `keyframes` | 1 a 10 imagens, na ordem de reprodução. Cada uma com no mínimo 256x256 pixels. Cada keyframe se torna um ponto no clipe. | IMAGE | Sim | 1 a 10 imagens |
| `placement` | "spread across the clip" permite que o FLUX 3 posicione as imagens (uma abre o clipe, duas se tornam seu início e fim); "at times" fixa cada imagem em um segundo que você escolher. | STRING | Sim | `"spread across the clip"` (padrão)<br>`"at times"` |
| `times` | Um tempo em segundos por imagem, separados por vírgula e em ordem crescente, ex.: '0, 2.5, 5'. Necessário quando `placement` for `"at times"`. | STRING | Não | Segundos separados por vírgula (padrão: "0") |
| `aspect_ratio` | Proporção de tela da saída. "auto" escolhe uma a partir do prompt e das entradas. | STRING | Sim | `"auto"` (padrão)<br>mais outras opções disponíveis |
| `duration` | Duração do clipe em segundos. "auto" ajusta a duração ao conteúdo. | STRING | Sim | `"auto"` (padrão)<br>mais outras opções disponíveis |
| `resolution` | Resolução da saída. | STRING | Sim | `"720p"` (padrão)<br>`"1080p"` |
| `generate_audio` | Gerar áudio sincronizado (ambiente, fala, efeitos). Desativado produz um vídeo sem trilha de áudio. | BOOLEAN | Sim | true / false (padrão: true) |
| `safety_tolerance` | Tolerância de moderação, 0 é o mais rigoroso. Solicitações que enviam imagens ou vídeo são limitadas a 2, independentemente do valor definido aqui. | INT | Sim | 0 a 4 (padrão: 2, configuração avançada) |
| `seed` | Semente para determinar se o nó deve ser executado novamente; o FLUX 3 escolhe sua própria semente, então os resultados reais são não determinísticos independentemente desse valor. | INT | Sim | 0 a 4294967295 (padrão: 42, com controle após a geração) |

Observação: `keyframes` é obrigatório — o nó gera um erro se nenhuma imagem de keyframe for conectada. Quando `placement` for `"spread across the clip"` e 3 ou mais imagens forem fornecidas, `duration` deve ser definido com um valor explícito (não `"auto"`); caso contrário, o nó gera um erro. Quando `placement` for `"at times"`, `times` deve fornecer um tempo em segundos para cada imagem, em ordem crescente. Solicitações que enviam imagens são limitadas a uma tolerância de moderação de 2, independentemente do valor definido.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `video` | O clipe de vídeo gerado a partir das imagens de keyframe com a proporção de tela, duração, resolução e configuração de áudio escolhidas. | VIDEO |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Flux3ImageToVideoNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `3b9472194020ec98cd4e8c60463cdd0e9dc074ec6cbc1fc03d313894fa570ba8`
