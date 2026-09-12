# TripoImageToModelNodeV2

O nó Tripo: Image to Model transforma uma única imagem de referência em um modelo 3D usando o serviço de imagem para modelo da Tripo. Ele faz upload da imagem, envia uma tarefa de geração, aguarda a conclusão da tarefa e retorna o arquivo 3D resultante junto com o ID da tarefa. Este é um nó de API, portanto exige uma chave válida da API do Comfy.

## Entradas

| Parâmetro | Descrição | Tipo de dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `image` | A imagem de referência usada para gerar o modelo 3D. | IMAGE | Sim | — |
| `model_version` | A versão do modelo a ser usada para geração. Se não for definida, o nó recorre à versão v3.1 (20260211) da Tripo. | COMBO | Não | Lista de versões de modelo da Tripo |
| `texture` | Gera mapas de textura. Desativado retorna geometria sem textura e ignora `pbr` (padrão: true). | BOOLEAN | Não | true<br>false |
| `pbr` | Mapas de material PBR (cor base, metálico, rugosidade, normal). Requer `texture` (padrão: true). | BOOLEAN | Não | true<br>false |
| `model_seed` | Semente usada para a etapa de geração da geometria (padrão: 42). | INT | Não | 0 a 2147483647 |
| `orientation` | Configuração de orientação aplicada ao modelo gerado (padrão: DEFAULT). | COMBO | Não | Opções de orientação da Tripo, padrão `DEFAULT` |
| `texture_seed` | Semente usada para a etapa de geração de textura (padrão: 42). | INT | Não | 0 a 2147483647 |
| `texture_quality` | detailed = texturas HD, extreme = texturas Ultra 8K (padrão: "standard"). | COMBO | Não | "standard"<br>"detailed"<br>"extreme" |
| `texture_alignment` | Como as texturas são alinhadas na geometria gerada (padrão: "original_image"). | COMBO | Não | "original_image"<br>"geometry" |
| `face_limit` | Número máximo de faces. -1 permite que a Tripo escolha de forma adaptativa (cerca de 1,4M de faces no v3.x standard, 2M em detailed). A Tripo aplica limites silenciosamente: v2.5 em 500.000, malhas quad em 150.000 (padrão: -1). | INT | Não | -1 a 2000000 |
| `quad` | Saída de malha quad. A Tripo entrega malhas quad como FBX, então o resultado chega na saída FBX e a saída GLB permanece vazia (padrão: false). | BOOLEAN | Não | true<br>false |
| `geometry_quality` | O nível de qualidade da geometria gerada (padrão: "standard"). | COMBO | Não | "standard"<br>"detailed" |
| `smart_low_poly` | Malha low-poly com topologia limpa e de estilo artesanal (500-20.000 faces, quad 500-10.000). Melhor para objetos simples; objetos complexos podem falhar (padrão: false). | BOOLEAN | Não | true<br>false |
| `auto_size` | Dimensiona modelos com textura para seu tamanho real em metros. A Tripo armazena o tamanho como a transformação de cena do modelo e o incorpora quando o modelo é convertido, recebe rig ou passa por retargeting; ignorado sem textura (padrão: true). | BOOLEAN | Não | true<br>false |

**Observações:**

- `image` é obrigatório; o nó gera um erro se nenhuma imagem for fornecida.
- Quando `smart_low_poly` está habilitado e `face_limit` está definido com um valor diferente de -1, o limite deve estar entre 500 e 20.000 para malhas triangulares, ou entre 500 e 10.000 quando `quad` está habilitado. Outros valores geram um erro.
- Quando `texture` está desabilitado, `pbr` é forçado a ficar desativado, independentemente de sua configuração, e `auto_size` não tem efeito.
- Um `face_limit` de -1 é enviado à Tripo como "sem limite", permitindo que o serviço escolha de forma adaptativa.
- Um novo formato de arquivo 3D que o nó não consegue retornar (qualquer coisa que não seja GLB ou FBX) causa um erro.

## Saídas

| Nome da saída | Descrição | Tipo de dados |
|-------------|-------------|-----------|
| `task_id do modelo` | O ID da tarefa Tripo do trabalho de geração. | MODEL_TASK_ID |
| `GLB` | O modelo gerado como um arquivo GLB. Vazio quando `quad` está habilitado. | FILE3DGLB |
| `FBX` | O modelo gerado como um arquivo FBX. Preenchido apenas quando `quad` está habilitado. | FILE3DFBX |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoImageToModelNodeV2/pt-BR.md)

---
**Source fingerprint (SHA-256):** `c8c069432f67a019995b9f4dedbf5ca3f7594ae4004104277068106821189c11`
