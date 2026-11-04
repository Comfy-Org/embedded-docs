# ByteDance Texto para Vídeo

O nó ByteDance Text to Video gera um vídeo usando modelos ByteDance por meio de uma API com base em um prompt de texto. Você fornece um prompt e escolhe configurações como modelo, resolução, proporção de aspecto e duração; o nó envia a solicitação de geração e retorna o vídeo gerado.

**Nota:** A BytePlus descontinua o modelo Seedance 1.5 Pro em 11 de novembro de 2026, então este nó não o oferece mais e os fluxos salvos com ele param de funcionar. Use `seedance-1-0-pro-250528`, `seedance-1-0-pro-fast-251015` ou o [nó parceiro Seedance 2.5](https://docs.comfy.org/pt-BR/tutorials/partner-nodes/bytedance/seedance-2-5).

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `model` | O modelo ByteDance usado para gerar o vídeo (padrão: `"seedance-1-0-pro-fast-251015"`). | COMBO | Sim | `"seedance-1-0-pro-250528"`<br>`"seedance-1-0-pro-fast-251015"` |
| `prompt` | O prompt de texto usado para gerar o vídeo. | STRING | Sim | - |
| `resolution` | A resolução do vídeo de saída. | COMBO | Sim | `"480p"`<br>`"720p"`<br>`"1080p"` |
| `aspect_ratio` | A proporção de aspecto do vídeo de saída. | COMBO | Sim | `"16:9"`<br>`"4:3"`<br>`"1:1"`<br>`"3:4"`<br>`"9:16"`<br>`"21:9"` |
| `duration` | A duração do vídeo de saída em segundos (padrão: 5). | INT | Sim | 3 a 12 |
| `seed` | Semente a ser usada para a geração (padrão: 0). | INT | Não | 0 a 2147483647 |
| `camera_fixed` | Especifica se a câmera deve ser fixada. A plataforma acrescenta uma instrução para fixar a câmera ao seu prompt, mas não garante o efeito real (padrão: False). | BOOLEAN | Não | - |
| `watermark` | Se deve adicionar uma marca d'água "gerado por IA" ao vídeo (padrão: False). | BOOLEAN | Não | - |
| `generate_audio` | Adiciona uma faixa de áudio gerada por IA. Os modelos restantes ignoram esta entrada (padrão: False). | BOOLEAN | Não | - |

**Restrições dos Parâmetros:**

- O parâmetro `prompt` deve conter pelo menos 1 caractere após a remoção de espaços em branco.
- O parâmetro `prompt` não pode conter os seguintes parâmetros de texto: "resolution", "ratio", "duration", "seed", "camerafixed", "watermark".
- O nó constrói o prompt final acrescentando as configurações selecionadas de `resolution`, `aspect_ratio`, `duration`, `seed`, `camera_fixed` e `watermark` ao texto do prompt.
- O parâmetro `duration` é limitado a valores entre 3 e 12 segundos.
- O parâmetro `seed` aceita valores de 0 a 2.147.483.647.
- O parâmetro `generate_audio` é aceito por compatibilidade, mas os modelos restantes o ignoram.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `output` | O arquivo de vídeo gerado | VIDEO |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDanceTextToVideoNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `83b805b63e59a76cae378b0407b409e1bfe900677ef1e01fc836fede47283eee`
