O TripoTextureNode gera modelos 3D texturizados usando a API Tripo. Ele recebe um ID de tarefa de modelo e aplica geração de textura com várias opções, incluindo materiais PBR, configurações de qualidade de textura e métodos de alinhamento. O nó se comunica com a API Tripo para processar a solicitação de geração de textura e retorna o arquivo de modelo resultante e o ID da tarefa.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `model_task_id` | O ID da tarefa do modelo ao qual aplicar as texturas | MODEL_TASK_ID | Sim | - |
| `textura` | Se deve gerar texturas (padrão: True) | BOOLEAN | Não | - |
| `pbr` | Se deve gerar materiais PBR (Renderização Baseada em Física) (padrão: True) | BOOLEAN | Não | - |
| `semente_textura` | Semente aleatória para geração de textura (padrão: 42) | INT | Não | - |
| `qualidade_textura` | Nível de qualidade para geração de textura (padrão: "standard"). A opção "detailed" custa US$ 0,20, enquanto "standard" custa US$ 0,10. | COMBO | Não | "standard"<br>"detailed" |
| `alinhamento_textura` | Método para alinhar texturas (padrão: "original_image"). "original_image" alinha texturas à imagem de entrada original, enquanto "geometry" as alinha à geometria 3D. | COMBO | Não | "original_image"<br>"geometry" |

*Nota: Este nó requer tokens de autenticação e chaves de API que são tratados automaticamente pelo sistema.*

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `model_file` | O arquivo de modelo gerado com texturas aplicadas (apenas para compatibilidade reversa) | STRING |
| `model task_id` | O ID da tarefa para rastrear o processo de geração de textura | MODEL_TASK_ID |
| `GLB` | O modelo 3D gerado no formato GLB com texturas aplicadas | FILE3DGLB |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoTextureNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `6d2a6ff7bbbe9fa91f63c6c7d237799044d2f9aa5afe7b90b99cf9e5a21afc32`
