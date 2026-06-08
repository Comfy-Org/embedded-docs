Este nó utiliza o modelo mais recente da Kling AI para gerar um vídeo a partir de um quadro inicial, um quadro final opcional ou imagens de referência. Ele pode criar um único vídeo ou um storyboard multi-cena com prompts e durações individuais para cada segmento. O nó processa essas entradas para produzir um vídeo com duração e resolução especificadas, com geração opcional de áudio.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `model_name` | O modelo específico da Kling AI a ser usado para geração de vídeo. | COMBO | Sim | `"kling-v3-omni"`<br>`"kling-video-o1"` |
| `prompt` | Um prompt de texto descrevendo o conteúdo do vídeo. Pode incluir descrições positivas e negativas. Ignorado quando storyboards estão ativados. | STRING | Sim | - |
| `duration` | A duração desejada do vídeo gerado em segundos (padrão: 5). | INT | Sim | 3 a 15 |
| `first_frame` | A imagem inicial para a sequência de vídeo. | IMAGE | Sim | - |
| `end_frame` | Um quadro final opcional para o vídeo. Não pode ser usado simultaneamente com `reference_images`. Não funciona com storyboards. | IMAGE | Não | - |
| `reference_images` | Até 6 imagens de referência adicionais. | IMAGE | Não | - |
| `resolution` | A resolução de saída para o vídeo gerado (padrão: "1080p"). | COMBO | Não | `"4k"`<br>`"1080p"`<br>`"720p"` |
| `storyboards` | Gera uma série de segmentos de vídeo com prompts e durações individuais. Suportado apenas para `kling-v3-omni`. Quando ativado, cada storyboard requer um prompt e uma duração. | DYNAMIC_COMBO | Não | `"desativado"`<br>`"1 storyboard"`<br>`"2 storyboards"`<br>`"3 storyboards"`<br>`"4 storyboards"`<br>`"5 storyboards"`<br>`"6 storyboards"` |
| `gerar_áudio` | Gera áudio para o vídeo (padrão: Falso). Suportado apenas para `kling-v3-omni`. | BOOLEAN | Não | Verdadeiro / Falso |
| `semente` | A semente controla se o nó deve ser executado novamente; os resultados são não determinísticos independentemente da semente (padrão: 0). | INT | Não | 0 a 2147483647 |

**Restrições Importantes:**

* A entrada `end_frame` não pode ser usada ao mesmo tempo que a entrada `reference_images`.
* A entrada `end_frame` não pode ser usada simultaneamente com storyboards.
* O modelo `kling-video-o1` não suporta durações maiores que 10 segundos, geração de áudio, resolução 4k ou storyboards.
* Se você não fornecer um `end_frame` ou nenhuma `reference_images` com o modelo `kling-video-o1`, a `duration` só pode ser definida como 5 ou 10 segundos.
* Todas as imagens de entrada (`first_frame`, `end_frame` e quaisquer `reference_images`) devem ter uma dimensão mínima de 300 pixels tanto em largura quanto em altura.
* A proporção de aspecto de todas as imagens de entrada deve estar entre 1:2,5 e 2,5:1.
* No máximo 6 imagens podem ser fornecidas através da entrada `reference_images`.
* O texto do `prompt` deve ter entre 1 e 2500 caracteres de comprimento (0 caracteres permitidos quando storyboards estão ativados).
* Quando storyboards estão ativados, a duração total de todos os segmentos do storyboard deve ser igual ao valor global de `duration`.
* Cada prompt de storyboard deve ter entre 1 e 512 caracteres de comprimento.

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `output` | O arquivo de vídeo gerado. | VIDEO |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingOmniProFirstLastFrameNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `bd0fb11242b7f79062079b1aa48c3524abf59ecf06a90f013e57b6910cd8e224`
