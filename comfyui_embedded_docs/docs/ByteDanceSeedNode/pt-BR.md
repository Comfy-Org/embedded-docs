# ByteDance Seed

O ByteDance Seed gera respostas de texto usando os modelos Seed 2.0 da ByteDance. Forneça um prompt de texto e, opcionalmente, inclua uma ou mais imagens ou vídeos para contexto multimodal.

## Entradas

### Entradas comuns

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Faixa |
|-----------|-------------|-----------|----------|-------|
| `model` | O modelo Seed usado para gerar a resposta. | DYNAMIC_COMBO | Sim | `"Seed 2.0 Pro"`<br>`"Seed 2.0 Lite"`<br>`"Seed 2.0 Mini"` |
| `prompt` | Entrada de texto para o modelo. (padrão: "") | STRING | Sim | N/A |
| `seed` | A semente (seed) controla se o nó deve ser executado novamente; os resultados são não determinísticos, independentemente da semente. (padrão: 0) | INT | Sim | 0 to 2147483647 |
| `system_prompt` | Instruções fundamentais que ditam o comportamento do modelo. (padrão: "") | STRING | Não | N/A |

### Seed 2.0 Pro, Seed 2.0 Lite e Seed 2.0 Mini Entradas

Esta configuração é compartilhada por todas as três opções de modelo.

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Faixa |
|-----------|-------------|-----------|----------|-------|
| `temperature` | Controla a aleatoriedade. 0.0 é determinístico, valores mais altos são mais aleatórios. (padrão: 1.0) | FLOAT | Sim | 0.0 to 2.0 |

### Entradas de referência

O seletor `model` fornece estes espaços expansíveis, que conectam imagens e vídeos para dar contexto multimodal ao modelo.

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Faixa |
|-----------|-------------|-----------|----------|-------|
| `images` | Imagem(ns) opcional(is) para usar como contexto para o modelo. Até 20 imagens. Slot expansível: conecte de 1 a 20 itens (ex.: `image_1`...`image_20`). | IMAGE | Não | `image_1` to `image_20` |
| `videos` | Vídeo(s) opcional(is) para usar como contexto para o modelo. Até 4 vídeos. Slot expansível: conecte de 1 a 4 itens (ex.: `video_1`...`video_4`). | VIDEO | Não | `video_1` to `video_4` |

**Nota:** O seletor `model` determina qual modelo Seed é usado para gerar a resposta. Cada opção corresponde a um ID de modelo específico: `"Seed 2.0 Pro"` → `seed-2-0-pro-260328`, `"Seed 2.0 Lite"` → `seed-2-0-lite-260228` e `"Seed 2.0 Mini"` → `seed-2-0-mini-260215`.

**Nota sobre restrições:** No máximo 20 imagens e 4 vídeos são suportados por solicitação. O `prompt` deve ser uma string não vazia.

**Nota sobre preços:** O preço é baseado em tokens e exibido na interface do nó como uma faixa aproximada por 1 mil tokens: Seed 2.0 Mini: $0.00025-$0.0009; Seed 2.0 Lite: $0.0003-$0.002; Seed 2.0 Pro: $0.0005-$0.003.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `output` | A resposta de texto gerada pelo modelo Seed. | STRING |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDanceSeedNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `23c9b0e9983a65ce859e2e92acfe71604297f16d711fa094a6617a9915a46020`
