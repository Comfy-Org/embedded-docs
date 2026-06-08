Esta documentação foi gerada por IA. Caso encontre erros ou tenha sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingOmniProEditVideoNode/en.md)

O nó Kling Omni Edit Video (Pro) utiliza um modelo de IA para editar um vídeo existente com base em uma descrição textual. Você fornece um vídeo de origem e um prompt, e o nó gera um novo vídeo com a mesma duração, aplicando as alterações solicitadas. Opcionalmente, é possível usar imagens de referência para guiar o estilo e manter o áudio original do vídeo de origem.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `nome_do_modelo` | O modelo de IA a ser usado para edição de vídeo (padrão: `"kling-v3-omni"`). | COMBO | Sim | `"kling-v3-omni"`<br>`"kling-video-o1"` |
| `prompt` | Um prompt textual descrevendo o conteúdo do vídeo. Pode incluir descrições positivas e negativas. | STRING | Sim |  |
| `vídeo` | Vídeo para edição. A duração do vídeo de saída será a mesma. | VIDEO | Sim |  |
| `manter_som_original` | Determina se o áudio original do vídeo de entrada será mantido na saída (padrão: True). | BOOLEAN | Sim |  |
| `imagens_de_referência` | Até 4 imagens de referência adicionais. | IMAGE | Não |  |
| `resolução` | A resolução do vídeo de saída (padrão: `"1080p"`). | COMBO | Não | `"1080p"`<br>`"720p"` |
| `semente` | A semente controla se o nó deve ser executado novamente; os resultados são não determinísticos independentemente da semente (padrão: 0). | INT | Não | 0 a 2147483647 |

**Restrições e Limitações:**

* O `prompt` deve ter entre 1 e 2500 caracteres.
* O `video` de entrada deve ter duração entre 3,0 e 10,05 segundos.
* As dimensões do `video` de entrada devem estar entre 720x720 e 2160x2160 pixels.
* No máximo 4 `reference_images` podem ser fornecidas quando um vídeo é usado.
* Cada `reference_image` deve ter pelo menos 300x300 pixels.
* Cada `reference_image` deve ter uma proporção de aspecto entre 1:2,5 e 2,5:1.

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `vídeo` | O vídeo editado gerado pelo modelo de IA. | VIDEO |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingOmniProEditVideoNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `ddc3fdc8c97cdcdd34f16a0916b13ffe6adeb46e58e2933516c9a6aef7c36730`
