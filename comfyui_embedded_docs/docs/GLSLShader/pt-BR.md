> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GLSLShader/pt-BR.md)

O nó GLSL Shader aplica código personalizado de fragment shader GLSL ES a imagens de entrada. Ele permite que você escreva programas de shader que podem processar múltiplas imagens e aceitar parâmetros uniformes (floats e inteiros) para criar efeitos visuais complexos. O tamanho da saída pode ser determinado pela primeira imagem de entrada ou definido manualmente.

## Entradas

| Parâmetro | Tipo de Dados | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `fragment_shader` | STRING | Sim | N/A | Código-fonte do fragment shader GLSL (compatível com GLSL ES 3.00 / WebGL 2.0). Padrão: Um shader básico que emite a primeira imagem de entrada. |
| `size_mode` | COMBO | Sim | `"from_input"`<br>`"custom"` | Tamanho da saída: 'from_input' usa as dimensões da primeira imagem de entrada, 'custom' permite definir o tamanho manualmente. |
| `width` | INT | Não | 1 a 16384 | A largura da imagem de saída quando `size_mode` está definido como `"custom"`. Padrão: 512. |
| `height` | INT | Não | 1 a 16384 | A altura da imagem de saída quando `size_mode` está definido como `"custom"`. Padrão: 512. |
| `images` | IMAGE | Sim | 1 a 8 imagens | Imagens de entrada a serem processadas pelo shader. As imagens estão disponíveis como `u_image0` a `u_image7` (sampler2D) no código do shader. |
| `floats` | FLOAT | Não | 0 a 8 floats | Valores uniformes de ponto flutuante para o shader. Os floats estão disponíveis como `u_float0` a `u_float7` no código do shader. Padrão: 0.0. |
| `ints` | INT | Não | 0 a 8 inteiros | Valores uniformes inteiros para o shader. Os inteiros estão disponíveis como `u_int0` a `u_int7` no código do shader. Padrão: 0. |

**Observações:**
*   Os parâmetros `width` e `height` são obrigatórios e visíveis apenas quando `size_mode` está definido como `"custom"`.
*   Pelo menos uma imagem de entrada é necessária.
*   O código do shader sempre tem acesso a um uniforme `u_resolution` (vec2) contendo as dimensões da saída.
*   Um máximo de 8 imagens de entrada, 8 uniformes float e 8 uniformes inteiros pode ser fornecido.

## Saídas

| Nome da Saída | Tipo de Dados | Descrição |
|-------------|-----------|-------------|
| `IMAGE0` | IMAGE | A primeira imagem de saída do shader. Disponível via `layout(location = 0) out vec4 fragColor0` no código do shader. |
| `IMAGE1` | IMAGE | A segunda imagem de saída do shader. Disponível via `layout(location = 1) out vec4 fragColor1` no código do shader. |
| `IMAGE2` | IMAGE | A terceira imagem de saída do shader. Disponível via `layout(location = 2) out vec4 fragColor2` no código do shader. |
| `IMAGE3` | IMAGE | A quarta imagem de saída do shader. Disponível via `layout(location = 3) out vec4 fragColor3` no código do shader. |