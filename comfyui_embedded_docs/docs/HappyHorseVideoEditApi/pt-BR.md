# HappyHorse Edição de Vídeo

Esta documentação foi gerada por IA. Se encontrar algum erro ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HappyHorseVideoEditApi/en.md)

## Visão Geral

Edite um vídeo usando instruções de texto ou imagens de referência com o modelo HappyHorse. A duração da saída é de 3 a 15 segundos e corresponde ao vídeo de entrada; entradas com mais de 15 segundos são truncadas.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `model` | Configuração do modelo contendo a seleção do modelo, prompt, resolução, proporção de aspecto e imagens de referência opcionais. | DICT | Sim | Veja abaixo |
| `video` | O vídeo a ser editado. | VIDEO | Sim | - |
| `seed` | Semente a ser usada para geração (padrão: 0). | INT | Sim | 0 a 2147483647 |
| `watermark` | Se deve adicionar uma marca d'água gerada por IA ao resultado (padrão: Falso). | BOOLEAN | Não | Verdadeiro / Falso |

### Detalhes do Parâmetro `model`

O parâmetro `model` é um dicionário com os seguintes campos:

| Campo | Descrição | Tipo de Dado | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `model` | O modelo de edição de vídeo HappyHorse a ser usado. | STRING | Sim | `"happyhorse-1.0-video-edit"` |
| `prompt` | Instruções de edição ou requisitos de transferência de estilo. Deve ter pelo menos 1 caractere. | STRING | Sim | - |
| `resolution` | A resolução de saída. | STRING | Sim | `"720P"`<br>`"1080P"` |
| `ratio` | Proporção de aspecto. Se não for alterada, aproxima-se da proporção do vídeo de entrada. | STRING | Sim | `"16:9"`<br>`"9:16"`<br>`"1:1"`<br>`"4:3"`<br>`"3:4"` |
| `reference_images` | Imagens de referência opcionais (image1, image2, image3, image4, image5) para guiar a edição. | DICT | Não | 0 a 5 imagens |

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `video` | A saída do vídeo editado. | VIDEO |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HappyHorseVideoEditApi/pt-BR.md)

---
**Source fingerprint (SHA-256):** `af6747efbea1c65e4909d35dad009cbc2ffaad787d0f2031581c227deb9bf53c`
