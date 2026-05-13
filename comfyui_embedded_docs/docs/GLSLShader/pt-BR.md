> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GLSLShader/pt-BR.md)

O nó GLSL Shader aplica código de shader de fragmento GLSL ES personalizado a imagens de entrada. Ele permite escrever programas de shader que podem processar múltiplas imagens e aceitar parâmetros uniformes (floats, inteiros, booleanos e curvas) para criar efeitos visuais complexos. O tamanho da saída pode ser determinado pela primeira imagem de entrada ou definido manualmente.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Intervalo | Descrição |
|-----------|--------------|-------------|-----------|-----------|
| `fragment_shader` | STRING | Sim | N/A | Código-fonte do shader de fragmento GLSL (compatível com GLSL ES 3.00 / WebGL 2.0). Padrão: Um shader básico que gera a primeira imagem de entrada. |
| `modo_tamanho` | COMBO | Sim | `"from_input"`<br>`"custom"` | Tamanho da saída: 'from_input' usa as dimensões da primeira imagem de entrada, 'custom' permite tamanho manual. |
| `width` | INT | Não | 1 a 16384 | A largura da imagem de saída quando `modo_tamanho` está definido como `"custom"`. Padrão: 512. |
| `height` | INT | Não | 1 a 16384 | A altura da imagem de saída quando `modo_tamanho` está definido como `"custom"`. Padrão: 512. |
| `imagens` | IMAGE | Sim | 1 a 8 imagens | Imagens de entrada a serem processadas pelo shader. As imagens estão disponíveis como `u_image0` a `u_image7` (sampler2D) no código do shader. |
| `floats` | FLOAT | Não | 0 a 8 floats | Valores uniformes de ponto flutuante para o shader. Os floats estão disponíveis como `u_float0` a `u_float7` no código do shader. Padrão: 0.0. |
| `ints` | INT | Não | 0 a 8 inteiros | Valores uniformes inteiros para o shader. Os inteiros estão disponíveis como `u_int0` a `u_int7` no código do shader. Padrão: 0. |
| `booleanos` | BOOLEAN | Não | 0 a 8 booleanos | Valores uniformes booleanos para o shader. Os booleanos estão disponíveis como `u_bool0` a `u_bool7` (bool) no código do shader. Padrão: Falso. |
| `curvas` | CURVE | Não | 0 a 8 curvas | Valores uniformes de curva para o shader. As curvas estão disponíveis como `u_curve0` a `u_curve7` (sampler2D, LUT 1D) no código do shader. Amostre com `texture(u_curve0, vec2(x, 0.5)).r`. |

**Observações:**

* Os parâmetros `width` e `height` são obrigatórios e visíveis apenas quando `size_mode` está definido como `"custom"`.
* Pelo menos uma imagem de entrada é necessária.
* O código do shader sempre tem acesso a um uniforme `u_resolution` (vec2) contendo as dimensões da saída.
* No máximo 8 imagens de entrada, 8 uniformes float, 8 uniformes inteiros, 8 uniformes booleanos e 8 uniformes de curva podem ser fornecidos.

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|---------------|--------------|-----------|
| `IMAGE0` | IMAGE | A primeira imagem de saída do shader. Disponível via `layout(location = 0) out vec4 fragColor0` no código do shader. |
| `IMAGE1` | IMAGE | A segunda imagem de saída do shader. Disponível via `layout(location = 1) out vec4 fragColor1` no código do shader. |
| `IMAGE2` | IMAGE | A terceira imagem de saída do shader. Disponível via `layout(location = 2) out vec4 fragColor2` no código do shader. |
| `IMAGE3` | IMAGE | A quarta imagem de saída do shader. Disponível via `layout(location = 3) out vec4 fragColor3` no código do shader. |

---
**Source fingerprint (SHA-256):** `7830977409a5efab205b7c927eb83499a9e1e8299959b34643c9c3f1f586c058`
