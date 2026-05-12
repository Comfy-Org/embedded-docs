> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HappyHorseTextToVideoApi/pt-BR.md)

Esta documentação foi gerada por IA. Se você encontrar algum erro ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HappyHorseTextToVideoApi/en.md)

## Visão Geral

Gera um vídeo com base em um prompt de texto usando o modelo HappyHorse. Este nó envia seu prompt e configurações para a API HappyHorse, aguarda a geração do vídeo e, em seguida, baixa o resultado.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Faixa | Descrição |
|-----------|--------------|-------------|-------|-----------|
| `model` | DICT | Sim | Ver Descrição | Um dicionário contendo a seleção do modelo e seus parâmetros associados. O modelo deve ser `"happyhorse-1.0-t2v"`. Este dicionário inclui os seguintes subparâmetros:<br><br>**`prompt`** (STRING): A descrição textual do vídeo que você deseja gerar. Suporta inglês e chinês. (padrão: "").<br>**`resolution`** (COMBO): A resolução do vídeo de saída. Opções: `"720P"`, `"1080P"`.<br>**`ratio`** (COMBO): A proporção de aspecto do vídeo de saída. Opções: `"16:9"`, `"9:16"`, `"1:1"`, `"4:3"`, `"3:4"`.<br>**`duration`** (INT): A duração do vídeo em segundos. (padrão: 5, mínimo: 3, máximo: 15, passo: 1). |
| `seed` | INT | Sim | 0 a 2147483647 | Semente a ser usada para geração. Usar a mesma semente com as mesmas entradas produzirá o mesmo resultado. (padrão: 0). |
| `watermark` | BOOLEAN | Não | Verdadeiro / Falso | Se deve adicionar uma marca d'água gerada por IA ao resultado. (padrão: Falso). |

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|---------------|--------------|-----------|
| `VIDEO` | VIDEO | O arquivo de vídeo gerado. |