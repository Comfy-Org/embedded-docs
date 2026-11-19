# Kling 4.0 Image

Gere ou edite imagens com o Kling 4.0 a partir de um prompt de texto e até 10 imagens de referência. Solicite uma única imagem ou deixe o nó retornar uma série de imagens relacionadas que mantêm os mesmos personagens e estilo.

## Entradas

| Parâmetro | Descrição | Tipo de dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `reference_images` | Espaços expansíveis para imagens de referência (`image_1` ... `image_10`). Refira-se a eles no prompt como `@Image1`, `@Image2` e assim por diante. | AUTOGROW | Não | 0 a 10 imagens |
| `prompt` | Descrição da imagem. Refira-se às imagens conectadas como `@Image1`, `@Image2`, ... Padrão: string vazia. | STRING | Sim | Texto multilinha |
| `resolution` | Resolução da imagem de saída. Padrão: `"2K"`. | COMBO | Sim | `"2K"`<br>`"4K"`<br>`"8K"` |
| `aspect_ratio` | Proporção da imagem de saída. `"auto"` segue as imagens de referência; caso contrário, o prompt. Padrão: `"auto"`. | COMBO | Sim | `"auto"`<br>`"9:16"`<br>`"2:3"`<br>`"3:4"`<br>`"1:1"`<br>`"4:3"`<br>`"3:2"`<br>`"16:9"`<br>`"21:9"` |
| `series_amount` | Gera uma série de imagens relacionadas que mantêm os mesmos personagens e estilo. `"auto"` permite que o modelo escolha de 2 a 10 imagens. Padrão: `"disabled"`. | COMBO | Sim | `"disabled"`<br>`"auto"`<br>`"2"`<br>`"3"`<br>`"4"`<br>`"5"`<br>`"6"`<br>`"7"`<br>`"8"`<br>`"9"`<br>`"10"` |
| `seed` | A seed controla se o nó deve ser executado novamente; os resultados são não determinísticos independentemente da seed. Padrão: 42. | INT | Sim | 0 a 2147483647 |

**Restrições e comportamento:**

* No máximo 10 imagens de referência podem ser conectadas.
* Cada imagem deve ter pelo menos 300x300 pixels, com uma proporção entre 2:5 e 5:2.
* Um prompt que menciona `@ImageN` gera um erro quando menos de N imagens estão conectadas.
* Com `series_amount` definido como `"disabled"`, o nó retorna uma imagem; qualquer outro valor retorna um lote com essa quantidade de imagens.
* O preço de uma chamada varia conforme a resolução, o número de imagens de referência e o número de imagens da série.

## Saídas

| Nome da saída | Descrição | Tipo de dados |
|-------------|-------------|-----------|
| `image` | A imagem gerada, ou um lote de imagens quando `series_amount` estiver habilitado. | IMAGE |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Kling4ImageNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `7840b108419e759942aed332456cab73e748d9f018462011da3b1293646a4ffe`
