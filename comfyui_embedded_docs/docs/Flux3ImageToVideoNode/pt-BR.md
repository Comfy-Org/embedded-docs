# Flux 3 Imagem para Vídeo

Flux 3 Image to Video anima de 1 a 10 imagens com o FLUX 3. Cada imagem se torna um quadro do clipe: uma imagem o abre, duas fazem a transição da primeira para a segunda, e mais imagens são distribuídas ao longo dele ou fixadas nos tempos que você escolher.

## Entradas

### Entradas comuns

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `placement` | `"spread across the clip"` permite que o FLUX 3 posicione as imagens (uma abre o clipe, duas se tornam seu início e fim); `"at times"` fixa cada imagem em um segundo que você escolher. | DYNAMIC_COMBO | Sim | `"spread across the clip"` (padrão)<br>`"at times"` |
| `prompt` | Como a cena deve se mover e soar; o prompt é interpretado e expandido antes da geração. Deve conter pelo menos um caractere. | STRING | Sim | Texto multilinha (padrão: vazio) |
| `aspect_ratio` | Proporção da saída. `"auto"` escolhe uma com base no prompt e nas entradas. | COMBO | Sim | `"auto"` (padrão)<br>outras proporções disponíveis |
| `duration` | Duração do clipe em segundos. `"auto"` ajusta a duração ao conteúdo. | COMBO | Sim | `"auto"` (padrão)<br>outras durações disponíveis |
| `resolution` | Resolução da saída. | COMBO | Sim | `"720p"` (padrão)<br>`"1080p"` |
| `generate_audio` | Gera áudio sincronizado (ambiente, fala, efeitos). Desativado produz um vídeo sem faixa de áudio. | BOOLEAN | Sim | true / false (padrão: true) |
| `safety_tolerance` | Tolerância de moderação; 0 é a mais restritiva. Solicitações que enviam imagens ou vídeo são limitadas a 2, independentemente do valor definido aqui. | INT | Sim | 0 a 4 (padrão: 2, configuração avançada) |
| `seed` | Semente para determinar se o nó deve ser reexecutado; o FLUX 3 escolhe sua própria semente, então os resultados reais são não determinísticos independentemente deste valor. | INT | Sim | 0 a 4294967295 (padrão: 42, controle após geração) |

### Entradas de "spread across the clip"

Esta opção de posicionamento não tem parâmetros adicionais.

### Entradas de "at times"

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `times` | Um tempo em segundos por imagem, separado por vírgulas e crescente, por exemplo, `"0, 2.5, 5"`. Só aparece quando `placement` é `"at times"`; é necessário um tempo para cada imagem de quadro-chave. | STRING | Não | Segundos separados por vírgulas (padrão: "0") |

### Entradas de referência

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `keyframes` | Slot expansível: conecte de 1 a 10 imagens de quadro-chave na ordem de reprodução, por exemplo, `image_1`, `image_2` e assim por diante. Cada imagem se torna um quadro do clipe. Mínimo de 256x256 pixels cada; a proporção não pode ser mais extrema que 64:1. | IMAGE | Sim | 1 a 10 imagens |

Observação: `keyframes` deve conter pelo menos uma imagem; o nó gera um erro se nenhuma estiver conectada. Cada imagem de quadro-chave deve ter pelo menos 256x256 pixels e sua proporção não pode ser mais extrema que 64:1.

Quando `placement` for `"spread across the clip"` e 3 ou mais imagens de quadro-chave estiverem conectadas, `duration` deve ser definido com um valor explícito, não `"auto"`; caso contrário, o nó gera um erro.

Quando `placement` for `"at times"`, `times` deve fornecer um tempo em segundos por imagem. Os tempos devem ser crescentes, não podem ser negativos, e o último tempo não pode ultrapassar o fim do clipe (até 20 segundos quando `duration` for `"auto"`).

Como este nó envia imagens, `safety_tolerance` é limitado a 2, independentemente do valor definido.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `video` | O clipe de vídeo gerado, construído a partir das imagens de quadro-chave com a proporção, duração, resolução e configuração de áudio escolhidas. | VIDEO |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Flux3ImageToVideoNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `1c49838dfa13adc2ed70a51094f0dd860df7207970b8dceab6bb273653d7161c`
