# Grok Video

O nó Grok Video gera um vídeo curto a partir de uma descrição textual. Ele pode criar um vídeo do zero usando um prompt ou animar uma única imagem de entrada com base em um prompt. O nó envia uma requisição para uma API externa e retorna o vídeo gerado.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `model` | O modelo a ser usado para geração de vídeo. | COMBO | Sim | `"grok-imagine-video"`<br>`"grok-imagine-video-beta"` |
| `prompt` | Descrição textual do vídeo desejado. | STRING | Sim | - |
| `resolution` | A resolução do vídeo de saída. | COMBO | Sim | `"480p"`<br>`"720p"` |
| `aspect_ratio` | A proporção de aspecto do vídeo de saída (padrão: "auto"). | COMBO | Sim | `"auto"`<br>`"16:9"`<br>`"4:3"`<br>`"3:2"`<br>`"1:1"`<br>`"2:3"`<br>`"3:4"`<br>`"9:16"` |
| `duration` | A duração do vídeo de saída em segundos (padrão: 6). | INT | Sim | 1 a 15 |
| `seed` | Semente para determinar se o nó deve ser executado novamente; os resultados reais são não determinísticos independentemente da semente (padrão: 0). | INT | Sim | 0 a 2147483647 |
| `image` | Uma imagem de entrada opcional para animar. | IMAGE | Não | - |

**Nota:** Se uma `image` for fornecida, apenas uma imagem é suportada. Fornecer múltiplas imagens causará um erro. O `prompt` deve ter pelo menos 1 caractere após a remoção de espaços em branco.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `output` | O vídeo gerado. | VIDEO |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GrokVideoNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `d48049fafbe4dbf50eb5a42495d445fa4c7fc590a1d70267e220ccedc2f5328a`
