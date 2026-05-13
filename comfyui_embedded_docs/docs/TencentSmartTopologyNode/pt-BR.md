> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TencentSmartTopologyNode/pt-BR.md)

Este nó realiza retopologia inteligente em um modelo 3D, criando automaticamente uma nova malha mais limpa com contagem de polígonos otimizada. Ele se conecta a uma API Tencent Hunyuan 3D para processar o modelo, suportando formatos de arquivo GLB e OBJ de até 200MB. O nó retorna o modelo processado como um arquivo OBJ.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Faixa | Descrição |
|-----------|--------------|-------------|-------|-----------|
| `modelo_3d` | FILE3D | Sim | - | Modelo 3D de entrada (GLB ou OBJ). O arquivo deve estar nos formatos GLB ou OBJ e não pode exceder 200MB. |
| `tipo_de_polígono` | STRING | Sim | `"triangle"`<br>`"quadrilateral"` | Tipo de composição da superfície. |
| `nível_de_faces` | STRING | Sim | `"medium"`<br>`"high"`<br>`"low"` | Nível de redução de polígonos. |
| `semente` | INT | Não | 0 a 2147483647 | A semente controla se o nó deve ser executado novamente; os resultados são não determinísticos independentemente da semente. (padrão: 0) |

**Observação:** O parâmetro `seed` é usado para acionar uma nova execução do nó, mas a saída final não é garantida de ser a mesma para o mesmo valor de semente.

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|---------------|--------------|-----------|
| `OBJ` | FILE3D | O modelo 3D processado com topologia otimizada, retornado no formato OBJ. |

---
**Source fingerprint (SHA-256):** `13c2dce5f5fbc46a505d0366d8da1c4e762d3a64d11fae1bcceebd510b273f62`
