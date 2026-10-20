# FLUX 3 Max Image to Video

FLUX 3 Max Image to Video anima de 1 a 10 imagens com o FLUX 3 Max. Cada imagem se torna um quadro do clipe: uma imagem o abre, duas se tornam seu primeiro e último quadro, e mais imagens são distribuídas ao longo do clipe ou fixadas nos tempos que você escolher.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Como a cena deve se mover e soar (padrão: vazio). | STRING | Sim | Texto multilinha |
| `keyframes` | Slot expansível: conecte de 1 a 10 imagens de quadro-chave na ordem de reprodução, por exemplo, `image_1`, `image_2` e assim por diante. Cada imagem se torna um quadro do clipe. | IMAGE | Sim | 1 a 10 imagens |
| `placement` | `"spread across the clip"` coloca a primeira imagem no início, a última no fim e as demais uniformemente entre elas; `"at times"` fixa cada imagem em um segundo que você escolher (padrão: `"spread across the clip"`). | DYNAMIC_COMBO | Sim | `"spread across the clip"`<br>`"at times"` |
| `aspect_ratio` | Proporção da saída. `"auto"` segue a primeira imagem de quadro-chave (padrão: `"auto"`). | COMBO | Sim | `"auto"`<br>`"21:9"`<br>`"2:1"`<br>`"16:9"`<br>`"4:3"`<br>`"1:1"`<br>`"3:4"`<br>`"9:16"` |
| `duration` | Duração do clipe em segundos (padrão: `"5"`). | COMBO | Sim | `"5"`<br>`"6"`<br>`"7"`<br>`"8"`<br>`"9"`<br>`"10"`<br>`"11"`<br>`"12"`<br>`"13"`<br>`"14"`<br>`"15"`<br>`"16"`<br>`"17"`<br>`"18"`<br>`"19"`<br>`"20"` |
| `resolution` | Resolução da saída (padrão: `"720p"`). | COMBO | Sim | `"720p"`<br>`"1080p"` |
| `reasoning_level` | Quanto o modelo raciocina sobre o prompt e o expande antes de gerar. `"high"` demora mais; o preço é o mesmo (padrão: `"high"`). | COMBO | Sim | `"low"`<br>`"high"` |
| `generate_audio` | Gera áudio sincronizado. Desativado, produz um vídeo sem faixa de áudio (padrão: true). | BOOLEAN | Sim | `true`<br>`false` |
| `seed` | Semente que controla se o nó é executado novamente. Os resultados são não determinísticos independentemente deste valor (padrão: 42). | INT | Sim | 0 a 2147483646 |

### Entradas «at times»

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `times` | Um tempo em segundos por imagem, separados por vírgula e em ordem crescente, por exemplo, "0, 2.5, 5". Aparece apenas quando `placement` é `"at times"`. | STRING | Não | Segundos separados por vírgula (padrão: "0") |

Observação: `prompt` deve conter pelo menos um caractere. `keyframes` deve conter pelo menos uma imagem e não pode conter mais de 10; uma entrada em lote conta uma vez por imagem.

Com `placement` definido como `"spread across the clip"`, uma ou duas imagens são enviadas como imagem inicial e uma imagem final opcional, enquanto três ou mais são posicionadas em quadros-chave distribuídos uniformemente ao longo do clipe a 24 fps.

Com `placement` definido como `"at times"`, `times` deve fornecer um valor por imagem, esses valores devem ser crescentes, não podem ser negativos, e o último tempo não pode ultrapassar o fim do clipe.

O preço exibido é baseado em `resolution` e `duration`: 720p é cobrado a $0.060775 por segundo e 1080p a $0.103675 por segundo até 7 de novembro de 2026, e a $0.2431 e $0.4147 por segundo após essa data. O custo total estimado do clipe é mostrado na interface.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `video` | O clipe de vídeo gerado a partir das imagens de quadro-chave, com a proporção, duração, resolução e configuração de áudio escolhidas. | VIDEO |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Flux3MaxImageToVideoNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `fd8bbd627022f86d3ecb3482530a6c8c37d4225e32db36c35185eac318ed4c75`
