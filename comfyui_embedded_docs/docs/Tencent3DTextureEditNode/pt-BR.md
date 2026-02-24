> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Tencent3DTextureEditNode/pt-BR.md)

Este nó utiliza a API Tencent Hunyuan3D para editar as texturas de um modelo 3D. Você fornece um modelo 3D e uma descrição textual das alterações desejadas, e o nó retorna uma nova versão do modelo com suas texturas redesenhadas de acordo com seu prompt.

## Entradas

| Parâmetro | Tipo de Dados | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `model_3d` | FILE3D | Sim | FBX, Qualquer | Modelo 3D no formato FBX. O modelo deve ter menos de 100.000 faces. |
| `prompt` | STRING | Sim | | Descreve a edição de textura. Suporta até 1024 caracteres UTF-8. |
| `seed` | INT | Não | 0 a 2147483647 | O *seed* controla se o nó deve ser executado novamente; os resultados são não determinísticos independentemente do *seed*. (padrão: 0) |

**Observação:** A entrada `model_3d` deve ser um arquivo no formato FBX. Outros formatos de arquivo 3D não são suportados por este nó.

## Saídas

| Nome da Saída | Tipo de Dados | Descrição |
|-------------|-----------|-------------|
| `GLB` | FILE3D | O modelo 3D processado no formato GLB. |
| `FBX` | FILE3D | O modelo 3D processado no formato FBX. |