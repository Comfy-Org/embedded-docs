# SenseNova Conditioning

Prepare o condicionamento do SenseNova para geração de imagem ou para saída intercalada de texto e imagem. O seletor `task` define o template de prompt e o comportamento de parada, e o nó informa se o modelo deseja uma imagem, para que um loop saiba quando executar o sampler.

## Entradas

| Parâmetro | Descrição | Tipo de dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `clip` | Modelo CLIP do SenseNova. Conecte o carregador CLIP que também alimenta o CLIP Text Encode; a saída do codificador vai para `conditioning`. Obrigatório para todas as tarefas, exceto quando o condicionamento de entrada estiver vazio ou já finalizado. | CLIP | Não | - |
| `condicionamento` | Condicionamento de texto do SenseNova proveniente do CLIP Text Encode. | CONDITIONING | Sim | - |
| `negativo` | Condicionamento negativo opcional. Ele é atualizado e retornado para as tarefas `interleave` e `self-correction`. | CONDITIONING | Não | - |
| `tarefa` | Tarefa a ser executada. `"image"` codifica o prompt para um sampler padrão, `"image thinking"` permite que o modelo pense antes de responder, `"interleave"` produz texto e imagens em uma única passagem, e `"self-correction"` permite que o modelo corrija sua própria saída anterior. | DYNAMIC_COMBO | Sim | `"image"`<br>`"image thinking"`<br>`"interleave"`<br>`"self-correction"` |
| `max_tokens` | Máximo de tokens gerados durante esta chamada. Padrão: 1024. | INT | Sim | 1 a 8192 |

### Entradas de `interleave`

Estas entradas aparecem quando `task` está definido como `"interleave"`.

| Parâmetro | Descrição | Tipo de dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `thinking` | Permite que o modelo pense antes de responder. Padrão: True. | BOOLEAN | Sim | True<br>False |
| `samples` | Saída anterior do sampler, conectada ao continuar após uma solicitação de imagem. | LATENT | Não | - |

### Entradas de `self-correction`

Estas entradas aparecem quando `task` está definido como `"self-correction"`.

| Parâmetro | Descrição | Tipo de dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `samples` | Saída anterior do sampler, conectada ao continuar após uma solicitação de imagem. | LATENT | Não | - |

**Restrições e comportamento:**

* A entrada `clip` recebe o modelo CLIP do SenseNova, não a saída do CLIP Text Encode (que é `CONDITIONING`). Quando o condicionamento de entrada está vazio ou já finalizado, o nó retorna o resultado sem usar `clip`; caso contrário, um `clip` ausente ou que não seja um CLIP do SenseNova é um erro.
* `"image thinking"` precisa de exatamente uma entrada de condicionamento positivo; `"interleave"` e `"self-correction"` precisam de uma entrada positiva e uma negativa.
* Quando o modelo estiver aguardando uma imagem, conecte a saída LATENT do sampler anterior a `samples`. Passar samples antes de uma imagem ter sido solicitada é um erro.
* Quando o condicionamento de entrada já estiver finalizado, o nó o retorna inalterado com um `generated_text` vazio e `image_requested` definido como False.

## Saídas

| Nome da saída | Descrição | Tipo de dados |
|-------------|-------------|-----------|
| `conditioning` | Condicionamento para o sampler, estendido com o texto gerado por esta chamada. | CONDITIONING |
| `generated_text` | Texto gerado por esta chamada. Use SenseNova Interleave Decode para obter o resultado completo. | STRING |
| `negative` | Condicionamento negativo atualizado para as tarefas `interleave` e `self-correction`. | CONDITIONING |
| `image_requested` | True quando o modelo solicitou uma imagem: execute o sampler e, em seguida, realimente o loop de volta neste nó. | BOOLEAN |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SenseNovaConditioning/pt-BR.md)

---
**Source fingerprint (SHA-256):** `97fcdc26ccf80f48c5628f695a4ae8231b065b67414c93dec9bced6bb8d4c77c`
