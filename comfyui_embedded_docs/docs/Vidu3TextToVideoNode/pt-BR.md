# Geração de Vídeo de Texto para Vídeo Vidu Q3

O nó Vidu Q3 Text-to-Video Generation cria um vídeo a partir de uma descrição textual. Ele usa o modelo Vidu Q3 Pro ou Q3 Turbo para gerar conteúdo de vídeo com base no seu prompt, permitindo controlar a duração, a resolução, a proporção de aspecto e se o vídeo inclui áudio.

## Entradas

### Entradas comuns

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `model` | Modelo a ser usado para geração de vídeo. Selecionar um modelo revela parâmetros adicionais de configuração para proporção de aspecto, resolução, duração e áudio. | COMBO | Sim | `"viduq3-pro"`<br>`"viduq3-turbo"` |
| `prompt` | Descrição textual para geração de vídeo, com comprimento máximo de 2000 caracteres. | STRING | Sim | N/A |
| `seed` | Valor de semente para controlar a aleatoriedade da geração (padrão: 1). | INT | Sim | 0 a 2147483647 |

### Entradas do viduq3-pro e viduq3-turbo

Os seguintes parâmetros de configuração são compartilhados pelos modelos `viduq3-pro` e `viduq3-turbo`.

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `model.aspect_ratio` | A proporção de aspecto do vídeo de saída. | COMBO | Sim | `"16:9"`<br>`"9:16"`<br>`"3:4"`<br>`"4:3"`<br>`"1:1"` |
| `model.resolution` | Resolução do vídeo de saída. | COMBO | Sim | `"720p"`<br>`"1080p"` |
| `model.duration` | Duração do vídeo de saída em segundos (padrão: 5). | INT | Sim | 1 a 16 |
| `model.audio` | Quando habilitado, gera vídeo com som (incluindo diálogo e efeitos sonoros) (padrão: False). | BOOLEAN | Sim | True/False |

**Observação:** Os parâmetros `aspect_ratio`, `resolution`, `duration` e `audio` são obrigatórios quando um `model` é selecionado, pois fazem parte da sua configuração. O `prompt` não deve estar vazio e não pode exceder 2000 caracteres.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `video` | O arquivo de vídeo gerado. | VIDEO |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Vidu3TextToVideoNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `89c23454375a43cdfaf46c9e0e55a8a8166d02ada47ca2e237bd9f73fa4d78db`
