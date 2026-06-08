O nó Kling Omni Image (Pro) cria ou edita imagens usando o modelo de IA Kling mais recente. Ele gera imagens com base em uma descrição textual e pode opcionalmente usar imagens de referência para orientar o estilo ou conteúdo. O nó envia uma solicitação para uma API externa, que processa a tarefa e retorna a(s) imagem(ns) final(is).

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `model_name` | O modelo Kling AI específico a ser usado para geração de imagens. | COMBO | Sim | `"kling-v3-omni"`<br>`"kling-image-o1"` |
| `prompt` | Um prompt textual descrevendo o conteúdo da imagem. Pode incluir descrições positivas e negativas. O texto deve ter entre 1 e 2500 caracteres. | STRING | Sim | - |
| `resolution` | A resolução alvo para a imagem gerada. Observação: a resolução 4K não é suportada para o modelo `kling-image-o1`. | COMBO | Sim | `"1K"`<br>`"2K"`<br>`"4K"` |
| `aspect_ratio` | A proporção de aspecto desejada (largura para altura) para a imagem gerada. | COMBO | Sim | `"16:9"`<br>`"9:16"`<br>`"1:1"`<br>`"4:3"`<br>`"3:4"`<br>`"3:2"`<br>`"2:3"`<br>`"21:9"` |
| `quantidade_de_séries` | Gera uma série de imagens. Este recurso não é suportado para o modelo `kling-image-o1`. (padrão: "disabled") | COMBO | Sim | `"disabled"`<br>`"2"`<br>`"3"`<br>`"4"`<br>`"5"`<br>`"6"`<br>`"7"`<br>`"8"`<br>`"9"` |
| `reference_images` | Até 10 imagens de referência adicionais. Cada imagem deve ter pelo menos 300 pixels de largura e altura, e sua proporção de aspecto deve estar entre 1:2,5 e 2,5:1. | IMAGE | Não | - |
| `semente` | A semente controla se o nó deve ser executado novamente; os resultados são não determinísticos independentemente da semente. (padrão: 0) | INT | Não | 0 a 2147483647 |

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `image` | A(s) imagem(ns) final(is) gerada(s) ou editada(s) pelo modelo Kling AI. Se uma série foi solicitada, múltiplas imagens são retornadas como um lote. | IMAGE |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingOmniProImageNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `7bbed260436bc60e284c99e091cd28b2b0cf50e98e876f94278f1ac2834e61f8`
