# Flux 3 Imagem para Vídeo

Flux 3 Image to Video anima de 1 a 10 imagens com FLUX 3. Cada imagem se torna um quadro do clipe: uma imagem abre, duas fazem uma transição da primeira para a segunda, e mais são distribuídas ao longo do clipe ou fixadas nos tempos que você escolher.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Como a cena deve se mover e soar; o prompt é interpretado e expandido antes da geração. Deve conter pelo menos um caractere. | STRING | Sim | Texto multilinha (padrão: vazio) |
| `keyframes` | De 1 a 10 imagens, em ordem de reprodução. Mínimo de 256x256 pixels cada. Entrada expansível: conecte imagens como `image_1`, `image_2` e assim por diante. | IMAGE | Sim | 1 a 10 imagens |
| `placement` | `"spread across the clip"` permite que o FLUX 3 posicione as imagens (uma abre o clipe, duas se tornam seu início e fim); `"at times"` fixa cada imagem a um segundo que você escolher. | DYNAMIC_COMBO | Sim | `"spread across the clip"` (padrão)<br>`"at times"` |
| `times` | Um tempo em segundos por imagem, separados por vírgula e crescentes, ex.: "0, 2.5, 5". Só aparece quando `placement` é "at times"; um tempo é necessário para cada imagem-chave. | STRING | Não | Segundos separados por vírgula (padrão: "0") |
| `aspect_ratio` | Proporção de aspecto da saída. "auto" seleciona uma a partir do prompt e das entradas. | COMBO | Sim | `"auto"` (padrão)<br>outras proporções de aspecto disponíveis |
| `duration` | Duração do clipe em segundos. "auto" ajusta a duração ao conteúdo. | COMBO | Sim | `"auto"` (padrão)<br>outras durações disponíveis |
| `resolution` | Resolução da saída. | COMBO | Sim | `"720p"` (padrão)<br>`"1080p"` |
| `generate_audio` | Gerar áudio sincronizado (ambiente, fala, efeitos). Desativado produz um vídeo sem trilha de áudio. | BOOLEAN | Sim | true / false (padrão: true) |
| `safety_tolerance` | Tolerância de moderação, 0 é a mais estrita. Solicitações que enviam imagens ou vídeo são limitadas a 2 independentemente do valor definido aqui. | INT | Sim | 0 a 4 (padrão: 2, configuração avançada) |
| `seed` | Semente para determinar se o nó deve ser executado novamente; o FLUX 3 escolhe sua própria semente, portanto, os resultados reais são não determinísticos independentemente desse valor. | INT | Sim | 0 a 4294967295 (padrão: 42, controle após a geração) |

Observação: `keyframes` deve conter pelo menos uma imagem; o nó gera um erro se nenhuma estiver conectada. Cada imagem-chave deve ter pelo menos 256x256 pixels e sua proporção de aspecto não pode ser mais extrema que 64:1.

Quando `placement` é "spread across the clip" e 3 ou mais keyframes estão conectados, `duration` deve ser definido para um valor explícito, não "auto"; caso contrário, o nó gera um erro.

Quando `placement` é "at times", `times` deve fornecer um tempo em segundos por imagem. Os tempos devem aumentar, não podem ser negativos e o último tempo não pode ultrapassar o final do clipe (até 20 segundos quando `duration` é "auto").

Como este nó envia imagens, `safety_tolerance` é limitado a 2 independentemente do valor definido.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `video` | O clipe de vídeo gerado a partir das imagens-chave com a proporção de aspecto, duração, resolução e configuração de áudio escolhidas. | VIDEO |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Flux3ImageToVideoNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `1c49838dfa13adc2ed70a51094f0dd860df7207970b8dceab6bb273653d7161c`
