# TripoTextToModelNodeV2

Gera um modelo 3D a partir de uma descrição textual usando o serviço Tripo. O nó envia o prompt e as configurações para o Tripo, aguarda a conclusão da tarefa de geração e retorna o arquivo 3D finalizado junto com o identificador da tarefa.

## Entradas

| Parâmetro | Descrição | Tipo de dados | Obrigatório | Valores |
|-----------|-------------|-----------|----------|-------|
| `prompt` | A descrição textual do modelo a ser gerado. Não pode estar vazio. | STRING | Sim | Texto multilinha |
| `negative_prompt` | Texto que descreve o que não deve aparecer no modelo gerado. Até 255 caracteres. | STRING | Não | Texto multilinha, máximo de 255 caracteres |
| `model_version` | A versão do modelo Tripo usada para geração (padrão: `v3.1_20260211`). | COMBO | Não | Lista de versões de modelo Tripo compatíveis |
| `texture` | Gera mapas de textura. Desativado retorna apenas a geometria e ignora `pbr` (padrão: True). | BOOLEAN | Não | True<br>False |
| `pbr` | Mapas de material PBR (cor base, metálico, rugosidade, normal). Requer `texture` (padrão: True). | BOOLEAN | Não | True<br>False |
| `image_seed` | Valor de seed para geração de imagem (padrão: 42). | INT | Não | 0 a 2147483647 |
| `model_seed` | Valor de seed para geração de modelo (padrão: 42). | INT | Não | 0 a 2147483647 |
| `texture_seed` | Valor de seed para geração de textura (padrão: 42). | INT | Não | 0 a 2147483647 |
| `texture_quality` | Nível de detalhe da textura (padrão: "standard"). "detailed" = texturas HD, "extreme" = texturas 8K Ultra. | COMBO | Não | `"standard"`<br>`"detailed"`<br>`"extreme"` |
| `face_limit` | Número máximo de faces. -1 permite que o Tripo escolha de forma adaptativa (cerca de 1,4 milhão de faces no v3.x standard, 2 milhões no detailed). O Tripo limita silenciosamente: v2.5 em 500.000, malhas quad em 150.000 (padrão: -1). | INT | Não | -1 a 2000000 |
| `quad` | Saída de malha quad. O Tripo entrega malhas quad como FBX, então o resultado chega na saída FBX e a saída GLB permanece vazia (padrão: False). | BOOLEAN | Não | True<br>False |
| `geometry_quality` | Nível de detalhe da geometria (padrão: "standard"). | COMBO | Não | `"standard"`<br>`"detailed"` |
| `smart_low_poly` | Malha low-poly com topologia limpa e de estilo artesanal (500 a 20.000 faces; quad 500 a 10.000). Melhor para temas simples; os complexos podem falhar (padrão: False). | BOOLEAN | Não | True<br>False |
| `auto_size` | Escala modelos com textura para seu tamanho real em metros. O Tripo armazena o tamanho como a transformação de cena do modelo e o incorpora quando o modelo é convertido, recebe rig ou passa por retarget; ignorado sem textura (padrão: True). | BOOLEAN | Não | True<br>False |

### Notas

- `prompt` é obrigatório e não pode estar vazio ou conter apenas espaços em branco.
- Quando `texture` é definido como False, `pbr` é forçado a ser desativado e `auto_size` não tem efeito.
- Quando `smart_low_poly` está ativado e `face_limit` não é -1, `face_limit` deve estar entre 500 e 20.000 para malhas triangulares, ou entre 500 e 10.000 quando `quad` está ativado.
- Com `quad` ativado, o Tripo retorna um arquivo FBX, então a saída `GLB` permanece vazia e a saída `FBX` é preenchida.

## Saídas

| Nome da saída | Descrição | Tipo de dados |
|-------------|-------------|-----------|
| `model task_id` | Identificador da tarefa de geração do Tripo que produziu o modelo. | MODEL_TASK_ID |
| `GLB` | O modelo gerado em formato GLB. Vazio quando `quad` está ativado. | FILE3D_GLB |
| `FBX` | O modelo gerado em formato FBX. Preenchido apenas quando `quad` está ativado. | FILE3D_FBX |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoTextToModelNodeV2/pt-BR.md)

---
**Source fingerprint (SHA-256):** `8af7044188c6dbb87d23298bf7b99fe826bdc7bd7ba0948db2066887274faa00`
