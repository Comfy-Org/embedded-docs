# Atenção Esparsa em Blocos do Modelo

O nó **Block Sparse Attention** modifica um modelo para que suas camadas de atenção se concentrem apenas nas partes mais relevantes da entrada, em vez de considerarem tudo de uma vez, o que reduz o trabalho computacional necessário para sequências longas. A economia cresce com o comprimento da sequência, já que sequências curtas geralmente são mais rápidas com atenção normal (densa).

## Entradas

### Entradas comuns

| Parâmetro | Descrição | Tipo de dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `model` | O modelo a ser patchado. | MODEL | Sim | N/A |
| `selection` | Método usado para escolher blocos de chave para atenção completa em nível de token (exibido como `method`). <br>`sol-attn`: O Sparsifying Online Attention usa um limiar adaptativo sem treinamento para cada cabeça de atenção e bloco de consulta.<br>`sla`: O Sparse-Linear Attention mantém uma porcentagem fixa dos blocos de chave com maior pontuação; use apenas com pesos de modelo treinados para este padrão.<br>`vsa`: O Video Sparse Attention (FastVideo) usa divisão em cubos de vídeo 3D e um ramo de atenção grosseira aprendido; requer pesos do modelo FastH3. | DYNAMIC_COMBO | Sim | `"sol-attn"`<br>`"sla"`<br>`"vsa"` |
| `start_percent` | Ponto percentual em que a atenção esparsa começa. Antes deste ponto, a atenção permanece densa. Padrão: 0.2. | FLOAT | Não | mín: 0.0, máx: 1.0, passo: 0.01 |
| `end_percent` | Ponto percentual em que a atenção esparsa termina. Após este ponto, a atenção retorna a densa. Padrão: 1.0. | FLOAT | Não | mín: 0.0, máx: 1.0, passo: 0.01 |
| `dense_blocks` | Blocos do Transformer que sempre são executados de forma densa, por exemplo '0, 1, 47-49'. Padrão: "" (vazio). Entrada avançada. | STRING | Não | Padrão: "" |
| `min_tokens` | Sequências mais curtas que isto permanecem densas. Padrão: 12288. Entrada avançada. | INT | Não | mín: 0, máx: 1048576, passo: 512 |
| `extra_tokens` | Tokens extras com maior pontuação que cada bloco de consulta atende além dos blocos selecionados. Quanto mais próximo de denso, maior o tempo de atenção; 256 recomendado, 0 desativa. Ignorado para VSA. Padrão: 256. Entrada avançada. | INT | Não | mín: 0, máx: 256, passo: 64 |
| `sink_conditioning` | Somente MiniMax-H3. `exact_kv`: cada consulta atende exatamente às linhas empacotadas de texto/áudio/referência (cerca de 3% de custo). `exact_kv_and_rows`: além disso, executa as linhas de consulta do áudio de destino de forma densa (mantém o áudio gerado intacto). `off` desabilita este comportamento. Padrão: "exact_kv_and_rows". Entrada avançada. | COMBO | Não | `"exact_kv"`<br>`"exact_kv_and_rows"`<br>`"off"` |
| `verbose` | Registra se cada formato de atenção usou atenção esparsa ou por que permaneceu densa. Padrão: False. Entrada avançada. | BOOLEAN | Não | Padrão: False |

### Entradas do sol-attn

| Parâmetro | Descrição | Tipo de dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `tau` | Limiar em sigmas da distribuição de pontuação. Um valor mais alto é mais esparso: 1.0 mantém exatos cerca de 16% dos blocos de chave, 1.5 cerca de 7%, 2.0 cerca de 2.7%. Padrão: 1.3. | FLOAT | Não | mín: 0.0, máx: 4.0, passo: 0.05 |

### Entradas do sla

| Parâmetro | Descrição | Tipo de dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `keep_percent` | Porcentagem de blocos de chave que cada bloco de consulta mantém exatos (sinks e a diagonal são incluídos adicionalmente). As LoRAs no estilo SLA de seleção são destiladas considerando esse valor; sem uma LoRA desse tipo, um valor mais alto fica mais próximo do denso. Padrão: 10.0. | FLOAT | Não | mín: 0.5, máx: 95.0, passo: 0.5 |

### Entradas do vsa

| Parâmetro | Descrição | Tipo de dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `keep_percent` | Porcentagem de cubos de vídeo que cada cubo de consulta mantém; checkpoints FastH3-VSA são treinados em 10. Usa as camadas `to_gate_compress` do modelo para o ramo grosseiro quando presentes. Padrão: 10.0. | FLOAT | Não | mín: 0.5, máx: 95.0, passo: 0.5 |

**Nota:** Apenas os parâmetros pertencentes ao método atualmente selecionado são exibidos na interface.

## Saídas

| Nome da saída | Descrição | Tipo de dados |
|-------------|-------------|-----------|
| `model` | O modelo com atenção esparsa em blocos aplicada. | MODEL |

## Restrições e limitações

- Sequências mais curtas que `min_tokens`, blocos listados em `dense_blocks` e etapas de amostragem fora da janela de `start_percent` a `end_percent` recorrem ao backend de atenção densa do modelo selecionado pelo nó Model Attention Backend.
- `extra_tokens` é ignorado quando o método `vsa` está selecionado. Uma mensagem é registrada porque os pesos VSA foram treinados com seu padrão esparso.
- O método `vsa` requer um modelo MiniMax-H3; qualquer outro modelo gera um erro. Se o modelo não tiver camadas `to_gate_compress`, o estágio fino é executado sem o ramo grosseiro e um aviso é registrado.
- `dense_blocks` é ignorado para modelos que não relatam índices de bloco, o que é anotado no log quando `verbose` está habilitado.
- `sink_conditioning` aplica-se apenas a modelos MiniMax-H3 que relatam um layout compatível com o comprimento de sequência atual.

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BlockSparseAttention/pt-BR.md)

---
**Source fingerprint (SHA-256):** `0c34876b49a04db0ab265526e2bb5f784e150591aab631713ad2ab420a3327c4`
