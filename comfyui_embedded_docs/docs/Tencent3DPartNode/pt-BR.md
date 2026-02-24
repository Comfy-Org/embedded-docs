> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Tencent3DPartNode/pt-BR.md)

Este nó utiliza a API Tencent Hunyuan3D para analisar automaticamente um modelo 3D e gerar ou identificar seus componentes com base em sua estrutura. Ele processa o modelo e retorna um novo arquivo FBX.

## Entradas

| Parâmetro | Tipo de Dados | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `model_3d` | FILE3D | Sim | FBX, Qualquer | O modelo 3D a ser processado. O modelo deve estar no formato FBX e ter menos de 30000 faces. |
| `seed` | INT | Não | 0 a 2147483647 | Um valor de semente para controlar se o nó deve ser executado novamente. Os resultados são não determinísticos, independentemente do valor da semente. (padrão: 0) |

**Observação:** A entrada `model_3d` suporta apenas arquivos no formato FBX. Se um formato de arquivo 3D diferente for fornecido, o nó gerará um erro.

## Saídas

| Nome da Saída | Tipo de Dados | Descrição |
|-------------|-----------|-------------|
| `FBX` | FILE3DFBX | O modelo 3D processado, retornado como um arquivo FBX. |
