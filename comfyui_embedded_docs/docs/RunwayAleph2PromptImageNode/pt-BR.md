# Runway Aleph2 Imagem de Prompt

Este nó ancora uma imagem de orientação a um momento específico no vídeo de saída, controlando a aparência do vídeo editado naquele ponto. Conecte este nó à entrada `prompt_images` do nó Runway Aleph2 Vídeo para Vídeo e encadeie vários deles (até 5) usando a entrada opcional `prompt_images`.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
|-----------|-----------|--------------|-------------|-------|
| `imagem` | A imagem de orientação para posicionar no momento escolhido do vídeo de saída. | IMAGE | Sim | - |
| `posição` | Como posicionar esta imagem na linha do tempo do vídeo de saída. Escolha entre tempo absoluto (segundos a partir do início) ou tempo fracionário (percentual da duração do vídeo). | COMBO | Sim | `Absolute (seconds)`<br>`Fraction (0.0 to 1.0)` |
| `imagens_de_prompt` | Imagens de prompt anteriores opcionais para encadear com esta. Conecte a saída de outro nó Runway Aleph2 Imagem de Prompt aqui para construir uma cadeia de até 5 imagens de orientação. | PROMPT_IMAGE_CHAIN | Não | - |

**Detalhes do Modo de Posição:**

Quando `position` está definido como `Absolute (seconds)`, você deve fornecer um valor `seconds` (padrão: 0.0, faixa: 0.0 a 30.0, incremento: 0.1). Isso especifica o tempo exato em segundos a partir do início do vídeo de saída onde esta imagem se aplica.

Quando `position` está definido como `Fraction (0.0 to 1.0)`, você deve fornecer um valor `fraction` (padrão: 0.0, faixa: 0.0 a 1.0, incremento: 0.01). Isso especifica onde no vídeo de saída esta imagem se aplica como uma fração de sua duração total (0.0 = início, 1.0 = fim).

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
|---------------|-----------|--------------|
| `imagens_de_prompt` | Uma cadeia de imagens de prompt que pode ser conectada à entrada `prompt_images` do nó Runway Aleph2 Vídeo para Vídeo. | PROMPT_IMAGE_CHAIN |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RunwayAleph2PromptImageNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `a8b86fb5d73d27cc58aa59c195ca058eec8a5c9433ea09522ff3e905f6b88193`
