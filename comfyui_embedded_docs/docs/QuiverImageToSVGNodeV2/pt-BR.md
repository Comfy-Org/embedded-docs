# Quiver Image to SVG

Vetorize uma imagem raster em um gráfico vetorial escalável (SVG) com o Quiver AI. A imagem é enviada à API do Quiver AI, que retorna o resultado vetorizado.

Selecionar um `model` revela os parâmetros específicos do modelo listados abaixo.

## Entradas

### Entradas comuns

| Parâmetro | Descrição | Tipo de dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `model` | Modelo a ser usado para vetorização SVG. | DYNAMIC_COMBO | Sim | `"arrow-2"`<br>`"arrow-2-telos"`<br>`"arrow-1.1"`<br>`"arrow-1.1-max"`<br>`"arrow-preview"` |
| `image` | Imagem de entrada a ser vetorizada. | IMAGE | Sim | N/A |
| `auto_crop` | Recorta automaticamente para o assunto dominante. Parâmetro avançado (padrão: False). | BOOLEAN | Sim | `True`<br>`False` |
| `target_size` | Redimensionamento quadrado aplicado à imagem de entrada antes da vetorização, em pixels. 0 mantém o tamanho da origem, o que vetoriza de forma mais limpa do que forçar um redimensionamento; qualquer outro valor abaixo de 128 é limitado a 128. Isso não define a tela de saída; use `width` e `height` para isso. Parâmetro avançado (padrão: 0). | INT | Sim | 0 a 4096 |
| `width` | Largura da tela SVG de saída (viewBox), em unidades de usuário. Defina `width` e `height` para controlar o tamanho e a proporção da saída; deixe qualquer um deles em 0 para permitir que o modelo escolha, o que geralmente resulta em uma tela quadrada. Parâmetro avançado (padrão: 0). | INT | Sim | 0 a 8192 |
| `height` | Altura da tela SVG de saída (viewBox), em unidades de usuário. Defina `width` e `height` para controlar o tamanho e a proporção da saída; deixe qualquer um deles em 0 para permitir que o modelo escolha, o que geralmente resulta em uma tela quadrada. Parâmetro avançado (padrão: 0). | INT | Sim | 0 a 8192 |
| `seed` | Semente para determinar se o nó deve ser executado novamente; os resultados reais são não determinísticos independentemente do valor da semente. Este parâmetro tem a funcionalidade "controle após gerar" (padrão: 42). | INT | Sim | 0 a 2147483647 |

### Entradas específicas do modelo

| Parâmetro | Descrição | Tipo de dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `reasoning_effort` | Quanto raciocínio o modelo gasta antes de desenhar. Níveis mais altos melhoram o detalhe e custam mais tokens. Usado apenas pelos modelos `"arrow-2"` e `"arrow-2-telos"` (padrão: `"high"`). | COMBO | Sim | `"low"`<br>`"medium"`<br>`"high"`<br>`"xhigh"` |
| `temperature` | Controle de aleatoriedade. Valores mais altos aumentam a aleatoriedade. Não usado pelo modelo `"arrow-2-telos"`. Parâmetro avançado (padrão: 1.0). | FLOAT | Sim | 0.0 a 2.0 (passo 0.1) |
| `top_p` | Parâmetro de amostragem de núcleo. Não usado pelo modelo `"arrow-2-telos"`. Parâmetro avançado (padrão: 1.0). | FLOAT | Sim | 0.05 a 1.0 (passo 0.05) |
| `presence_penalty` | Penalidade de presença de token. Não usado pelo modelo `"arrow-2-telos"`. Parâmetro avançado (padrão: 0.0). | FLOAT | Sim | -2.0 a 2.0 (passo 0.1) |

**Nota:** `target_size` é aplicado antes da vetorização e não altera a tela de saída. Deixe `width` ou `height` em 0 para permitir que o modelo escolha o tamanho da tela.

## Saídas

| Nome da saída | Descrição | Tipo de dados |
|-------------|-------------|-----------|
| `SVG` | A saída SVG vetorizada. | SVG |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/QuiverImageToSVGNodeV2/pt-BR.md)

---
**Source fingerprint (SHA-256):** `186769b09bef2d2dbbfc26102f375ff80f8b324a24cd593da20afcea9cc2095b`
