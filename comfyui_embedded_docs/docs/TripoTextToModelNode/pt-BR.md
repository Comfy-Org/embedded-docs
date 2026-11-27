# Tripo: Texto para Modelo

Este nó legado gera modelos 3D finalizados a partir de uma descrição textual usando a API da Tripo. Ele aguarda a conclusão da geração e então retorna o arquivo do modelo, opcionalmente com texturas e materiais PBR. Está marcado como obsoleto e é mantido para fluxos de trabalho mais antigos.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Descrição textual do modelo 3D a ser gerado (multilinha). Este parâmetro é obrigatório e não pode ficar vazio. | STRING | Sim | - |
| `prompt_negativo` | Descrição textual do que evitar no modelo gerado (multilinha). Até 255 caracteres. Enviado para a API somente quando não vazio. | STRING | Não | Até 255 caracteres |
| `versão_do_modelo` | Versão do modelo Tripo a ser usada para geração (padrão: v3_1_20260211). | COMBO | Não | Várias opções disponíveis |
| `estilo` | Não é mais suportado pela Tripo e é ignorado. Mantido para fluxos de trabalho mais antigos (padrão: "None"). | COMBO | Não | Várias opções disponíveis |
| `textura` | Gera mapas de textura. Desativado retorna geometria sem textura e ignora `pbr` (padrão: True). | BOOLEAN | Não | true / false |
| `pbr` | Mapas de material PBR (cor base, metálico, rugosidade, normal). Requer `texture`; forçado para desativado quando `texture` está desativado (padrão: True). | BOOLEAN | Não | true / false |
| `semente_da_imagem` | Semente usada para o estágio de geração de imagem (padrão: 42). | INT | Não | 0 a 2147483647 |
| `semente_do_modelo` | Semente usada para o estágio de geração do modelo (padrão: 42). | INT | Não | 0 a 2147483647 |
| `semente_da_textura` | Semente usada para o estágio de geração de textura (padrão: 42). | INT | Não | 0 a 2147483647 |
| `qualidade_da_textura` | Qualidade das texturas geradas. detailed = texturas HD, extreme = texturas 8K Ultra (padrão: standard). | COMBO | Não | "standard"<br>"detailed"<br>"extreme" |
| `limite_de_faces` | Contagem máxima de faces. -1 permite que a Tripo escolha de forma adaptativa (cerca de 1,4M de faces em v3.x standard, 2M em detailed). A Tripo limita silenciosamente: malhas quad em 150.000. (padrão: -1) | INT | Não | -1 a 2000000 |
| `quad` | Saída de malha quad. A Tripo entrega malhas quad como FBX, então o resultado chega na saída FBX e a saída GLB permanece vazia. (padrão: False) | BOOLEAN | Não | true / false |
| `qualidade_da_geometria` | Qualidade da geometria gerada (padrão: standard). | COMBO | Não | "standard"<br>"detailed" |
| `smart_low_poly` | Malha low-poly com topologia limpa, no estilo feito à mão (500-20.000 faces, quad 500-10.000). Melhor para objetos simples; objetos complexos podem falhar. (padrão: False) | BOOLEAN | Não | true / false |
| `auto_size` | Escala modelos texturizados para seu tamanho real em metros. A Tripo armazena o tamanho como a transformação de cena do modelo e o incorpora quando o modelo é convertido, rigado ou retargetado; ignorado sem textura. (padrão: True) | BOOLEAN | Não | true / false |

**Notas:**
- Este nó está obsoleto e marcado como nó legado. Ele é mantido para compatibilidade retroativa com fluxos de trabalho mais antigos.
- O parâmetro `prompt` é obrigatório: um prompt vazio faz o nó lançar um erro.
- `pbr` exige `texture`. Quando `texture` está desativado, o nó força `pbr` para desativado e ignora seu valor. `auto_size` também não tem efeito sem `texture`.
- Quando `smart_low_poly` está ativado e `face_limit` está definido com um valor diferente de -1, o limite de faces deve estar entre 500 e 20.000 para saída de triângulos, ou entre 500 e 10.000 quando `quad` está ativado; caso contrário, o nó lança um erro.
- Quando `quad` está ativado, a malha quad gerada é entregue como FBX, então a saída FBX é preenchida e a saída GLB permanece vazia.
- O parâmetro `style` é aceito, mas ignorado.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `arquivo_do_modelo` | O nome do arquivo do modelo 3D gerado no formato `<task_id>.<format>`, mantido apenas para compatibilidade retroativa. | STRING |
| `task_id_do_modelo` | O identificador único de tarefa para o processo de geração do modelo. | MODEL_TASK_ID |
| `GLB` | O modelo 3D gerado no formato GLB. Vazio quando `quad` está ativado. | FILE3DGLB |
| `FBX` | O modelo 3D gerado no formato FBX. Preenchido somente quando `quad` está ativado. | FILE3DFBX |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoTextToModelNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `c26c8437ea66d08f7f39865fedeaaf4cf8583ca64b368f3b767ea18918dd6c08`
