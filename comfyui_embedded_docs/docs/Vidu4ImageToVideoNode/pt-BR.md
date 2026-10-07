# Vidu Q4 Image-to-Video Generation

Gere um vídeo a partir de um quadro inicial e um prompt opcional com um modelo Vidu Q4. A saída mantém a proporção de aspecto da imagem de entrada.

Selecionar um `model` revela os parâmetros específicos desse modelo.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `image` | Quadro inicial do vídeo gerado. A proporção de aspecto deve estar entre 1:5 e 5:1. | IMAGE | Sim | N/A |
| `model` | Modelo a ser usado para geração de vídeo. Selecionar um modelo revela os parâmetros específicos dele: `prompt`, `resolution`, `duration`, `audio` e `seed`. | DYNAMIC_COMBO | Sim | `"Vidu Q4 Preview"` |
| `prompt` | Um prompt de texto opcional para geração de vídeo, com até 5000 caracteres (padrão: vazio). | STRING | Sim | Qualquer texto |
| `resolution` | Resolução do vídeo de saída (padrão: `"720p"`). | COMBO | Sim | `"540p"`<br>`"720p"`<br>`"1080p"`<br>`"2K"`<br>`"4K"` |
| `duration` | Duração do vídeo de saída em segundos (padrão: 5). | INT | Sim | 3 a 16 |
| `audio` | Quando habilitado, gera vídeo com som, incluindo diálogos e efeitos sonoros (padrão: True). | BOOLEAN | Sim | `True`<br>`False` |
| `seed` | A seed controla se o nó deve ser executado novamente; os resultados não são determinísticos independentemente da seed. Este parâmetro tem a funcionalidade "controle após gerar" (padrão: 42). | INT | Sim | 1 a 2147483647 |

**Nota:** A proporção de aspecto de `image` deve permanecer entre 1:5 e 5:1, e o `prompt` não pode exceder 5000 caracteres. O resultado mantém a proporção de aspecto da imagem de entrada, portanto o tamanho de saída segue a configuração `resolution` apenas dentro dessa proporção.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `VIDEO` | O arquivo de vídeo gerado. | VIDEO |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Vidu4ImageToVideoNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `8778696edbdfb821afaa99dcba09cbebff57fd4cd2378273e82ad9fb18600b62`
