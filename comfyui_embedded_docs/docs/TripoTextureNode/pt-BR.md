> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoTextureNode/pt-BR.md)

O TripoTextureNode gera modelos 3D texturizados usando a API Tripo. Ele recebe um ID de tarefa de modelo e aplica geração de textura com várias opções, incluindo materiais PBR, configurações de qualidade de textura e métodos de alinhamento. O nó se comunica com a API Tripo para processar a solicitação de geração de textura e retorna o arquivo de modelo resultante e o ID da tarefa.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Faixa | Descrição |
|-----------|-----------|----------|-------|-------------|
| `model_task_id` | MODEL_TASK_ID | Sim | - | O ID da tarefa do modelo ao qual aplicar as texturas |
| `texture` | BOOLEAN | Não | - | Se deve gerar texturas (padrão: True) |
| `pbr` | BOOLEAN | Não | - | Se deve gerar materiais PBR (Renderização Baseada em Física) (padrão: True) |
| `texture_seed` | INT | Não | - | Semente aleatória para geração de textura (padrão: 42) |
| `texture_quality` | COMBO | Não | "standard"<br>"detailed" | Nível de qualidade para geração de textura (padrão: "standard"). A opção "detailed" custa US$ 0,20, enquanto "standard" custa US$ 0,10. |
| `texture_alignment` | COMBO | Não | "original_image"<br>"geometry" | Método para alinhar texturas (padrão: "original_image"). "original_image" alinha texturas à imagem de entrada original, enquanto "geometry" as alinha à geometria 3D. |

*Nota: Este nó requer tokens de autenticação e chaves de API que são tratados automaticamente pelo sistema.*

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|-------------|-----------|-------------|
| `model_file` | STRING | O arquivo de modelo gerado com texturas aplicadas (apenas para compatibilidade reversa) |
| `model task_id` | MODEL_TASK_ID | O ID da tarefa para rastrear o processo de geração de textura |
| `GLB` | FILE3DGLB | O modelo 3D gerado no formato GLB com texturas aplicadas |

---
**Source fingerprint (SHA-256):** `6d2a6ff7bbbe9fa91f63c6c7d237799044d2f9aa5afe7b90b99cf9e5a21afc32`
