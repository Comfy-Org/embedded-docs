# SeedVR2ProgressiveSampler

Amostrador sequencial de fragmentação temporal para fluxos de trabalho nativos do SeedVR2. Este nó processa latentes de vídeo longos dividindo-os em fragmentos temporais menores, amostrando cada fragmento sequencialmente e mesclando os resultados. Ele serve como um substituto direto para o KSampler padrão ao trabalhar com modelos SeedVR2 em sequências que, de outra forma, causariam erros de memória insuficiente.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
|-----------|-----------|--------------|-------------|-------|
| `model` | O modelo usado para remover ruído do latent de entrada | MODEL | Sim | |
| `seed` | A semente aleatória usada para criar o ruído (padrão: 0) | INT | Sim | 0 a 0xffffffffffffffff |
| `steps` | O número de etapas usadas no processo de remoção de ruído (padrão: 20) | INT | Sim | 1 a 10000 |
| `cfg` | A escala de Orientação Livre de Classificador equilibra criatividade e aderência ao prompt. Valores mais altos resultam em imagens que correspondem mais ao prompt, porém valores muito altos impactarão negativamente a qualidade (padrão: 1.0) | FLOAT | Sim | 0.0 a 100.0 |
| `sampler_name` | O algoritmo usado na amostragem, que pode afetar a qualidade, velocidade e estilo da saída gerada | COMBO | Sim | Múltiplas opções disponíveis |
| `scheduler` | O agendador controla como o ruído é gradualmente removido para formar a imagem | COMBO | Sim | Múltiplas opções disponíveis |
| `positive` | O condicionamento descrevendo os atributos que você deseja incluir na imagem | CONDITIONING | Sim | |
| `negative` | O condicionamento descrevendo os atributos que você deseja excluir da imagem | CONDITIONING | Sim | |
| `latent` | A imagem latent para remover ruído | LATENT | Sim | |
| `denoise` | A quantidade de remoção de ruído aplicada; valores mais baixos manterão a estrutura da imagem inicial, permitindo amostragem imagem para imagem (padrão: 1.0) | FLOAT | Sim | 0.0 a 1.0 |
| `frames_per_chunk` | Quadros de pixel por fragmento temporal. Deve ser um valor 4n+1 (1, 5, 9, 13, 17, 21, ...) para corresponder às restrições do SeedVR2 (padrão: 21) | INT | Sim | 1 a 16384 (passo de 4) |
| `temporal_overlap` | Quadros latentes mesclados entre fragmentos adjacentes para ocultar a emenda; 0 significa sem mesclagem (padrão: 0) | INT | Sim | 0 a 16384 |
| `chunking_mode` | manual = usa frames_per_chunk exatamente; auto = reduz o fragmento até caber na VRAM (padrão: "manual") | COMBO | Sim | "manual"<br>"auto" |

**Nota sobre `frames_per_chunk`:** Este parâmetro deve ser uma contagem de quadros de pixel 4n+1 (1, 5, 9, 13, 17, 21, ...). O nó gerará um erro se um valor inválido for fornecido.

**Nota sobre `temporal_overlap`:** O valor de sobreposição é automaticamente limitado a no máximo um a menos que o tamanho do fragmento latent para garantir o processamento válido do fragmento.

**Nota sobre `chunking_mode`:** Quando definido como "auto", o nó tentará automaticamente tamanhos de fragmento menores se o fragmento atual causar um erro de memória insuficiente. Se todas as tentativas falharem, o nó gera um erro.

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
|---------------|-----------|--------------|
| `latent` | A saída latent com ruído removido, concatenada de todos os fragmentos temporais de volta em um único tensor latent SeedVR2 colapsado | LATENT |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SeedVR2ProgressiveSampler/pt-BR.md)

---
**Source fingerprint (SHA-256):** `a4574c3e619954b5569551b5b2ba112ecbff918dcebb5ba718a14e77701144a9`
