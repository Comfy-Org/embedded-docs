> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ViduMultiFrameVideoNode/pt-BR.md)

Esta documentação foi gerada por IA. Se você encontrar algum erro ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ViduMultiFrameVideoNode/en.md)

Este nó gera um vídeo criando transições entre múltiplos quadros-chave. Ele começa a partir de uma imagem inicial e anima através de uma sequência de imagens finais e prompts definidos pelo usuário, produzindo um único arquivo de vídeo como saída.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Faixa | Descrição |
| :--- | :--- | :--- | :--- | :--- |
| `modelo` | COMBO | Sim | `"viduq2-pro"`<br>`"viduq2-turbo"` | O modelo Vidu a ser usado para geração de vídeo. |
| `imagem_inicial` | IMAGE | Sim | - | A imagem do quadro inicial. A proporção deve estar entre 1:4 e 4:1. |
| `semente` | INT | Não | 0 a 2147483647 | Um valor de semente para geração de números aleatórios, garantindo resultados reproduzíveis (padrão: 1). |
| `resolução` | COMBO | Sim | `"720p"`<br>`"1080p"` | A resolução do vídeo de saída. |
| `quadros` | DYNAMICCOMBO | Sim | `"2"`<br>`"3"`<br>`"4"`<br>`"5"`<br>`"6"`<br>`"7"`<br>`"8"`<br>`"9"` | Número de transições de quadros-chave (2-9). Selecionar um valor revela dinamicamente as entradas necessárias para cada quadro. |

**Entradas dos Quadros (Reveladas Dinamicamente):**
Quando você seleciona um valor para `frames` (por exemplo, "3"), o nó exibirá um conjunto correspondente de entradas obrigatórias para cada transição. Para cada quadro `i` de 1 até o número selecionado, você deve fornecer:

* `end_image{i}` (IMAGE): A imagem alvo para esta transição. A proporção deve estar entre 1:4 e 4:1.
* `prompt{i}` (STRING): Uma descrição textual que orienta a transição para este quadro (máximo de 2000 caracteres).
* `duration{i}` (INT): A duração em segundos para este segmento específico de transição.

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
| :--- | :--- | :--- |
| `output` | VIDEO | O arquivo de vídeo gerado contendo todas as transições animadas. |

---
**Source fingerprint (SHA-256):** `02ddbb1e041b6d9e6654ab6c3cc25f4c2e5bc1545d84a30624608edc85e51f96`
