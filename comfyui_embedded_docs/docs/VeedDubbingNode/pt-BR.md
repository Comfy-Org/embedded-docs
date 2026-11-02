# VEED Dubbing

O VEED Dubbing traduz a fala de um vídeo para outro idioma com o VEED, clonando a voz de cada falante e sincronizando os lábios com a tradução. O clipe é enviado, o trabalho do VEED é consultado periodicamente e o vídeo dublado retorna a 25 fps, com a mesma duração da nova faixa de áudio. Use-o para localizar um clipe finalizado sem refilmar nem regravar a voz.

## Entradas

| Parâmetro | Descrição | Tipo de dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `model` | Modelo de dublagem. `"standard"` é mais barato e retorna áudio mono, com espanhol latino-americano e português brasileiro; `"pro"` adiciona sotaques regionais e áudio estéreo. Selecionar um modelo revela `video`, `target_language`, `source_language` e `seed`. | DYNAMIC_COMBO | Sim | `"standard"`<br>`"pro"` |

### Entradas do standard

Estas entradas aparecem quando `model` está definido como `"standard"`.

| Parâmetro | Descrição | Tipo de dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `video` | Vídeo com um rosto visível e fala, de até 599 segundos. A saída tem a mesma duração da faixa de áudio e é reproduzida a 25 fps. | VIDEO | Sim | Até 599 segundos |
| `target_language` | Idioma para dublar, um dos 85 idiomas. (padrão: `"English"`) | COMBO | Sim | 85 idiomas |
| `source_language` | Idioma falado no vídeo, ou `"auto"` para detectá-lo. (padrão: `"auto"`) | COMBO | Sim | `"auto"`<br>85 idiomas |
| `seed` | A seed controla se o nó deve ser executado novamente; os resultados são não determinísticos independentemente da seed. (padrão: 42) | INT | Sim | 0 a 2147483647 |

### Entradas do pro

Estas entradas aparecem quando `model` está definido como `"pro"`.

| Parâmetro | Descrição | Tipo de dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `video` | Vídeo com um rosto visível e fala, de até 599 segundos. A saída tem a mesma duração da faixa de áudio e é reproduzida a 25 fps. | VIDEO | Sim | Até 599 segundos |
| `target_language` | Idioma ou sotaque regional para dublar: 87 idiomas mais 14 sotaques, como `"English (UK)"`, `"Spanish (Mexico)"` e `"Portuguese (Brazil)"`. (padrão: `"English (US)"`) | COMBO | Sim | 101 opções |
| `source_language` | Idioma falado no vídeo, ou `"auto"` para detectá-lo. (padrão: `"auto"`) | COMBO | Sim | `"auto"`<br>91 idiomas |
| `seed` | A seed controla se o nó deve ser executado novamente; os resultados são não determinísticos independentemente da seed. (padrão: 42) | INT | Sim | 0 a 2147483647 |

O nó para com um erro quando o vídeo não tem faixa de áudio, quando o clipe tem mais de 599 segundos ou quando o trabalho do VEED falha.

## Saídas

| Nome da saída | Descrição | Tipo de dados |
|-------------|-------------|-----------|
| `VIDEO` | O vídeo dublado: a filmagem original com a fala traduzida e o movimento labial correspondente. | VIDEO |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VeedDubbingNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `fb818ca510e20bccffde61dca98c457984b8a110976e56f2a513f6c7f4d80c80`
