Este nó utiliza a API Tencent Hunyuan3D para editar as texturas de um modelo 3D. Você fornece um modelo 3D e uma descrição textual das alterações desejadas, e o nó retorna uma nova versão do modelo com suas texturas redesenhadas de acordo com sua instrução.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `model_3d` | Modelo 3D no formato FBX. O modelo deve ter menos de 100.000 faces. | FILE3D | Sim | FBX, Qualquer |
| `prompt` | Descreve a edição da textura. Suporta até 1024 caracteres UTF-8. | STRING | Sim |  |
| `seed` | A semente controla se o nó deve ser executado novamente; os resultados são não determinísticos independentemente da semente. (padrão: 0) | INT | Não | 0 a 2147483647 |

**Observação:** A entrada `model_3d` deve ser um arquivo no formato FBX. Outros formatos de arquivo 3D não são suportados por este nó.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `GLB` | O modelo 3D processado no formato GLB. | FILE3D |
| `OBJ` | O modelo 3D processado no formato OBJ. | FILE3D |
| `texture_image` | A imagem de textura recém-gerada para o modelo 3D. | IMAGE |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Tencent3DTextureEditNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `c8e81fcfc24707746b8d1291d31aff325523cd93a627b896402ce1b5a96c7e87`
