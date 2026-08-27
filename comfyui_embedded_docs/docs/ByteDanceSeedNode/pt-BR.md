# ByteDance Seed

Gere respostas de texto usando os modelos Seed 2.0 da ByteDance. Forneça um prompt de texto e, opcionalmente, inclua imagens ou vídeos para contexto multimodal.

## Entradas

### Entradas comuns

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `modelo` | O modelo Seed usado para gerar a resposta. | DYNAMIC_COMBO | Sim | `"Seed 2.0 Pro"`<br>`"Seed 2.0 Lite"`<br>`"Seed 2.0 Mini"` |
| `prompt` | Texto de entrada para o modelo. (padrão: "") | STRING | Sim | N/A |
| `seed` | A semente (seed) controla se o nó deve ser executado novamente; os resultados são não determinísticos independentemente da semente. (padrão: 0) | INT | Sim | 0 a 2147483647 |
| `prompt do sistema` | Instruções fundamentais que determinam o comportamento do modelo. (padrão: "") | STRING | Não | N/A |

### Entradas do modelo (compartilhadas por Seed 2.0 Pro, Seed 2.0 Lite e Seed 2.0 Mini)

Todos os três modelos Seed expõem os mesmos subparâmetros quando selecionados.

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `temperature` | Controla a aleatoriedade. 0.0 é determinístico, valores maiores são mais aleatórios. (padrão: 1.0) | FLOAT | Sim | 0.0 a 2.0 (passo: 0.01) |

### Entradas de referência

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `images` | Imagem(ns) opcional(is) para usar como contexto para o modelo. Até 20 imagens. Slot expansível: conecte de 1 a 20 itens, ex.: `image_1` a `image_20`. | IMAGE | Não | 0 a 20 imagens |
| `videos` | Vídeo(s) opcional(is) para usar como contexto para o modelo. Até 4 vídeos. Slot expansível: conecte de 1 a 4 itens, ex.: `video_1` a `video_4`. | VIDEO | Não | 0 a 4 vídeos |

**Nota:** O parâmetro `model` é uma combinação dinâmica que expõe os subparâmetros de referência e temperatura quando um modelo é selecionado. Você pode conectar entradas de imagem e vídeo a este parâmetro para fornecer contexto multimodal. Há suporte para no máximo 20 imagens e 4 vídeos por solicitação, e `prompt` é obrigatório e deve conter pelo menos um caractere sem espaço em branco.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `output` | A resposta de texto gerada pelo modelo Seed. | STRING |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDanceSeedNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `23c9b0e9983a65ce859e2e92acfe71604297f16d711fa094a6617a9915a46020`
