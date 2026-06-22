# Geração de Vídeo de Texto para Vídeo Vidu Q3

O nó de Geração de Texto para Vídeo Vidu Q3 cria um vídeo a partir de uma descrição textual. Ele utiliza o modelo Vidu Q3 Pro ou Q3 Turbo para gerar conteúdo de vídeo com base no seu prompt, permitindo controlar a duração, resolução, proporção de aspecto e se o vídeo inclui áudio.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `modelo` | Modelo a ser usado para geração de vídeo. A seleção de um modelo revela parâmetros de configuração adicionais para proporção de aspecto, resolução, duração e áudio. | COMBO | Sim | `"viduq3-pro"`<br>`"viduq3-turbo"` |
| `model.aspect_ratio` | A proporção de aspecto do vídeo de saída. Este parâmetro é revelado quando um `modelo` é selecionado. | COMBO | Sim* | `"16:9"`<br>`"9:16"`<br>`"3:4"`<br>`"4:3"`<br>`"1:1"` |
| `model.resolution` | Resolução do vídeo de saída. Este parâmetro é revelado quando um `modelo` é selecionado. | COMBO | Sim* | `"720p"`<br>`"1080p"` |
| `model.duration` | Duração do vídeo de saída em segundos (padrão: 5). Este parâmetro é revelado quando um `modelo` é selecionado. | INTEIRO | Sim* | 1 a 16 |
| `model.audio` | Quando ativado, gera vídeo com som (incluindo diálogo e efeitos sonoros) (padrão: Falso). Este parâmetro é revelado quando um `modelo` é selecionado. | BOOLEANO | Sim* | Verdadeiro/Falso |
| `prompt` | Uma descrição textual para geração de vídeo, com comprimento máximo de 2000 caracteres. | STRING | Sim | N/A |
| `semente` | Um valor de semente para controlar a aleatoriedade da geração (padrão: 1). | INTEIRO | Não | 0 a 2147483647 |

*Nota: Os parâmetros `aspect_ratio`, `resolution`, `duration` e `audio` são obrigatórios assim que um `model` é selecionado, pois fazem parte de sua configuração.

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `video` | O arquivo de vídeo gerado. | VIDEO |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Vidu3TextToVideoNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `a98b6c3093d659a5a4344c2c495063acf47a7922bf7d1fc851c3b8d8c0c87c5e`
