# Hunyuan3D: Parte 3D

Este nó usa a API Tencent Hunyuan3D para analisar automaticamente um modelo 3D e identificar ou gerar seus componentes com base na estrutura do modelo. Ele processa o modelo e retorna um novo arquivo FBX.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Faixa |
|-----------|-------------|---------------|-------------|-------|
| `model_3d` | Modelo 3D no formato FBX. O modelo deve ter menos de 30.000 faces. | FILE3D | Sim | FBX, Any |
| `seed` | A semente controla se o nó deve ser executado novamente; os resultados são não determinísticos independentemente da semente. (padrão: 0) | INT | Não | 0 a 2147483647 |

**Nota:** A entrada `model_3d` suporta apenas arquivos no formato FBX. Se um formato de arquivo 3D diferente for fornecido, o nó gerará um erro.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|---------------|-------------|--------------|
| `FBX` | O modelo 3D processado, retornado como um arquivo FBX. | FILE3DFBX |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Tencent3DPartNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `827b42559f4b2c341f08c58f53778d27c1c6afce607c36c8d1eae7c208c6a738`
