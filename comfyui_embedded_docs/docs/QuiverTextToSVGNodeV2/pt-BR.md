# Quiver Text to SVG

Gere um gráfico vetorial escalável (SVG) a partir de um prompt de texto com o Quiver AI. Imagens de referência e instruções de estilo opcionais podem orientar a geração.

Selecionar um `model` revela os parâmetros específicos do modelo listados abaixo, e o número máximo de imagens de referência também depende do modelo selecionado.

## Entradas

### Entradas comuns

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `model` | Modelo a ser usado para a geração de SVG. | DYNAMIC_COMBO | Sim | `"arrow-2"`<br>`"arrow-2-telos"`<br>`"arrow-1.1"`<br>`"arrow-1.1-max"`<br>`"arrow-preview"` |
| `prompt` | Descrição textual da saída SVG desejada. Deve conter pelo menos um caractere que não seja espaço em branco (padrão: vazio). | STRING | Sim | Qualquer texto |
| `instructions` | Orientação adicional de estilo ou formatação. Parâmetro avançado opcional (padrão: vazio). | STRING | Não | Qualquer texto |
| `reference_images` | Slot expansível: conecte uma ou mais imagens de referência opcionais (`ref_1`, `ref_2`, ...) que orientam a geração. O número máximo de imagens depende do modelo selecionado. | IMAGE | Não | Até 14<br>Até 4 |
| `width` | Largura do canvas SVG de saída (viewBox), em unidades de usuário. Defina `width` e `height` para controlar o tamanho e a proporção da saída; deixe qualquer um deles em 0 para permitir que o modelo escolha, o que geralmente resulta em um canvas quadrado. Parâmetro avançado (padrão: 0). | INT | Sim | 0 a 8192 |
| `height` | Altura do canvas SVG de saída (viewBox), em unidades de usuário. Defina `width` e `height` para controlar o tamanho e a proporção da saída; deixe qualquer um deles em 0 para permitir que o modelo escolha, o que geralmente resulta em um canvas quadrado. Parâmetro avançado (padrão: 0). | INT | Sim | 0 a 8192 |
| `seed` | Semente para determinar se o nó deve ser executado novamente; os resultados reais são não determinísticos independentemente do valor da semente. Este parâmetro tem a funcionalidade "control after generate" (padrão: 42). | INT | Sim | 0 a 2147483647 |

### Entradas específicas do modelo

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `reasoning_effort` | Quanto raciocínio o modelo gasta antes de desenhar. Níveis mais altos melhoram o detalhe e consomem mais tokens. Usado apenas pelos modelos `"arrow-2"` e `"arrow-2-telos"` (padrão: `"high"`). | COMBO | Sim | `"low"`<br>`"medium"`<br>`"high"`<br>`"xhigh"` |
| `temperature` | Controle de aleatoriedade. Valores mais altos aumentam a aleatoriedade. Não usado pelo modelo `"arrow-2-telos"`. Parâmetro avançado (padrão: 1.0). | FLOAT | Sim | 0.0 a 2.0 (passo 0.1) |
| `top_p` | Parâmetro de amostragem de núcleo. Não usado pelo modelo `"arrow-2-telos"`. Parâmetro avançado (padrão: 1.0). | FLOAT | Sim | 0.05 a 1.0 (passo 0.05) |
| `presence_penalty` | Penalidade de presença de tokens. Não usado pelo modelo `"arrow-2-telos"`. Parâmetro avançado (padrão: 0.0). | FLOAT | Sim | -2.0 a 2.0 (passo 0.1) |

**Nota:** O número máximo de `reference_images` é 14 para `"arrow-2"`, `"arrow-2-telos"` e `"arrow-1.1-max"`, e 4 para `"arrow-1.1"` e `"arrow-preview"`. Deixe `width` ou `height` em 0 para permitir que o modelo escolha o tamanho do canvas.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `SVG` | A saída SVG gerada. | SVG |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/QuiverTextToSVGNodeV2/pt-BR.md)

---
**Source fingerprint (SHA-256):** `809d2e5bd62386723e36b7649af2f8dda40b437dc39bac9236529db5b52d32e9`
