Este nó utiliza a API Tencent Hunyuan3D para analisar automaticamente um modelo 3D e gerar ou identificar seus componentes com base em sua estrutura. Ele processa o modelo e retorna um novo arquivo FBX.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `modelo_3d` | O modelo 3D a ser processado. O modelo deve estar no formato FBX e ter menos de 30.000 faces. | FILE3D | Sim | FBX, Qualquer |
| `semente` | Um valor de semente para controlar se o nó deve ser executado novamente. Os resultados são não determinísticos, independentemente do valor da semente. (padrão: 0) | INT | Não | 0 a 2147483647 |

**Observação:** A entrada `model_3d` suporta apenas arquivos no formato FBX. Se um formato de arquivo 3D diferente for fornecido, o nó gerará um erro.

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `FBX` | O modelo 3D processado, retornado como um arquivo FBX. | FILE3DFBX |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Tencent3DPartNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `eae7d0197d4391af1f5f24f120c64f1045649182108affad10b9a00f329310fe`
