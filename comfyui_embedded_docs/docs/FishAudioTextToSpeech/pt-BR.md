# Fish Audio Texto para Fala

Este nó converte texto escrito em áudio falado usando modelos de texto para fala da Fish Audio. Ele oferece suporte a indicações incorporadas no texto: `[happy]` e `[whispering]` no s2.1-pro, `(happy)` no s1, e `[directions]` em linguagem natural, além de tags de palavra `<whisper>...</whisper>`, no drama-3. O diálogo com vários locutores usa tags @Voice1/@Voice2 quando várias vozes estão conectadas. Três modelos estão disponíveis: drama-3 e s2.1-pro, que ambos oferecem suporte a até cinco vozes e diálogo com vários locutores, e s1, que usa uma única voz opcional.

## Entradas

### Entradas comuns

| Parâmetro | Descrição | Tipo de dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `text` | O texto a ser convertido em fala. Com duas ou mais vozes conectadas, marque as mudanças de locutor com @Voice1, @Voice2, etc. (padrão: vazio) | STRING | Sim | Qualquer texto não vazio |
| `model` | Modelo a ser usado para texto para fala. | DYNAMIC_COMBO | Sim | "drama-3"<br>"s2.1-pro"<br>"s1" |
| `seed` | A seed controla se o nó deve ser executado novamente; os resultados são não determinísticos independentemente da seed. (padrão: 42) | INT | Sim | 0 a 2147483647 |

### Entradas do drama-3 e do s2.1-pro

Estas entradas aparecem quando o modelo `drama-3` ou `s2.1-pro` é selecionado. Os conjuntos de parâmetros são idênticos.

| Parâmetro | Descrição | Tipo de dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `voices` | Slot expansível: conecte de 0 a 5 itens de voz (`voice_1`, `voice_2`, ...). Vozes para síntese. Deixe vazio para uma voz aleatória. Com duas ou mais vozes, marque as mudanças de locutor no texto com @Voice1, @Voice2, etc. | FISHAUDIO_VOICE | Não | 0 a 5 vozes |
| `temperature` | Expressividade. Valores mais altos são mais variados; valores mais baixos são mais consistentes. (padrão: 0.7) | FLOAT | Sim | 0.0 a 1.0 |
| `top_p` | Diversidade via amostragem nucleus. (padrão: 0.7) | FLOAT | Sim | 0.01 a 1.0 |
| `speed` | Velocidade da fala. 1.0 é normal, <1.0 mais lento, >1.0 mais rápido. (padrão: 1.0) | FLOAT | Sim | 0.5 a 2.0 |
| `volume` | Ajuste de volume em decibéis. 0 significa sem alteração. (padrão: 0.0) | FLOAT | Sim | -10.0 a 10.0 |
| `normalize` | Normaliza números e texto para inglês e chinês, melhorando a estabilidade para números e datas. (padrão: true) | BOOLEAN | Sim | true / false |

### Entradas do s1

Estas entradas aparecem quando o modelo s1 é selecionado.

| Parâmetro | Descrição | Tipo de dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `voice` | Voz para síntese. Deixe desconectado para uma voz aleatória. | FISHAUDIO_VOICE | Não | Voz única opcional |
| `temperature` | Expressividade. Valores mais altos são mais variados; valores mais baixos são mais consistentes. (padrão: 0.7) | FLOAT | Sim | 0.0 a 1.0 |
| `top_p` | Diversidade via amostragem nucleus. (padrão: 0.7) | FLOAT | Sim | 0.01 a 1.0 |
| `speed` | Velocidade da fala. 1.0 é normal, <1.0 mais lento, >1.0 mais rápido. (padrão: 1.0) | FLOAT | Sim | 0.5 a 2.0 |
| `volume` | Ajuste de volume em decibéis. 0 significa sem alteração. (padrão: 0.0) | FLOAT | Sim | -10.0 a 10.0 |
| `normalize` | Normaliza números e texto para inglês e chinês, melhorando a estabilidade para números e datas. (padrão: true) | BOOLEAN | Sim | true / false |

**Observação:** A entrada `text` não pode estar vazia. As tags de locutor (@Voice1, @Voice2, etc.) não diferenciam maiúsculas de minúsculas e devem se referir a uma voz conectada; marcar uma voz que não está conectada gera um erro. Quando duas ou mais vozes estão conectadas, o texto deve referenciar cada voz conectada pelo menos uma vez, ou o nó reporta as tags ausentes. No drama-3 e no s2.1-pro, conectar 0 vozes usa uma voz aleatória, 1 voz usa apenas essa voz, e 2 ou mais vozes habilitam o diálogo com vários locutores. No s1, uma única voz opcional é usada e deixá-la desconectada usa uma voz aleatória. As indicações podem ser colocadas no texto: `[happy]` e `[whispering]` no s2.1-pro, `(happy)` no s1, e `[directions]` em linguagem natural e tags de palavra `<whisper>...</whisper>` no drama-3.

## Saídas

| Nome da saída | Descrição | Tipo de dados |
|-------------|-------------|-----------|
| `audio` | A fala gerada como um arquivo de áudio. | AUDIO |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FishAudioTextToSpeech/pt-BR.md)

---
**Source fingerprint (SHA-256):** `adcfe8f994b8fbe07efb3dd3f86c8955ea3cec62cc3f0321efd2b63c0470b7a3`
