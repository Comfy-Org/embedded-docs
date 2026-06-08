O nó de Referência de Imagem ByteDance gera vídeos usando um prompt de texto e de uma a quatro imagens de referência. Ele envia as imagens e o prompt para um serviço de API externo que cria um vídeo correspondente à sua descrição, incorporando o estilo visual e o conteúdo das suas imagens de referência. O nó oferece vários controles para resolução de vídeo, proporção de tela, duração e outros parâmetros de geração.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `modelo` | O modelo de IA a ser usado para geração de vídeo (padrão: `"seedance-1-0-lite-i2v-250428"`). | STRING | Sim | `"seedance-1-0-pro-250528"`<br>`"seedance-1-0-lite-i2v-250428"` |
| `prompt` | O prompt de texto usado para gerar o vídeo. | STRING | Sim | - |
| `imagens` | De uma a quatro imagens. Cada imagem deve ter entre 300x300 e 6000x6000 pixels, com uma proporção de tela entre 0,4 e 2,5. | IMAGE | Sim | - |
| `resolução` | A resolução do vídeo de saída. | STRING | Sim | `"480p"`<br>`"720p"` |
| `proporção` | A proporção de tela do vídeo de saída (padrão: `"adaptive"`). | STRING | Sim | `"adaptive"`<br>`"16:9"`<br>`"4:3"`<br>`"1:1"`<br>`"3:4"`<br>`"9:16"`<br>`"21:9"` |
| `duração` | A duração do vídeo de saída em segundos (padrão: 5). | INT | Sim | 3 - 12 |
| `semente` | Semente a ser usada para geração (padrão: 0). | INT | Não | 0 - 2147483647 |
| `marca d'água` | Se deve adicionar uma marca d'água "gerado por IA" ao vídeo (padrão: False). | BOOLEAN | Não | - |

**Nota:** O texto do prompt não deve conter as seguintes strings de parâmetros: `--resolution`, `--ratio`, `--duration`, `--seed` ou `--watermark`. Esses valores são controlados exclusivamente através de seus widgets de entrada dedicados.

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `output` | O arquivo de vídeo gerado com base no prompt de entrada e nas imagens de referência. | VIDEO |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDanceImageReferenceNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `d5d1292d6af2fe24dc5c8a10174204546a5a6054ea1f43db44a45ce1017957d6`
