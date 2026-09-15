# Fish Audio Texto para Fala

## Entradas

### Entradas comuns

| Parâmetro | Descrição | Tipo de dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `text` | O texto a ser convertido em fala. Com duas ou mais vozes conectadas, marque mudanças de falante com @Voice1, @Voice2, etc. (padrão: vazio) | STRING | Sim | Qualquer texto não vazio |
| `model` | Modelo a ser usado para conversão de texto em fala. | DYNAMIC_COMBO | Sim | "s2.1-pro"<br>"s1" |
| `seed` | A seed controla se o nó deve ser executado novamente; os resultados não são determinísticos independentemente da seed. (padrão: 42) | INT | Sim | 0 a 2147483647 |

### Entradas do s2.1-pro

Estas entradas aparecem quando o modelo s2.1-pro é selecionado.

| Parâmetro | Descrição | Tipo de dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `voices` | Slot expansível: conecte de 0 a 5 itens de voz (`voice_1`, `voice_2`, ...). Vozes para síntese. Deixe vazio para usar a voz padrão. Com duas ou mais vozes, marque mudanças de falante no texto com @Voice1, @Voice2, etc. | FISHAUDIO_VOICE | Não | 0 a 5 vozes |
| `temperature` | Expressividade. Valores mais altos são mais variados, valores mais baixos são mais consistentes. (padrão: 0.7) | FLOAT | Sim | 0.0 a 1.0 |
| `top_p` | Diversidade via amostragem de núcleo. (padrão: 0.7) | FLOAT | Sim | 0.01 a 1.0 |
| `speed` | Velocidade da fala. 1.0 é normal, <1.0 mais lento, >1.0 mais rápido. (padrão: 1.0) | FLOAT | Sim | 0.5 a 2.0 |
| `volume` | Ajuste de volume em decibéis. 0 significa sem alteração. (padrão: 0.0) | FLOAT | Sim | -10.0 a 10.0 |
| `normalize` | Normaliza números e texto para inglês e chinês, melhorando a estabilidade para números e datas. (padrão: true) | BOOLEAN | Sim | true / false |

### Entradas do s1

Estas entradas aparecem quando o modelo s1 é selecionado.

| Parâmetro | Descrição | Tipo de dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `voice` | Voz para síntese. Deixe desconectado para usar a voz padrão. | FISHAUDIO_VOICE | Não | Voz única opcional |
| `temperature` | Expressividade. Valores mais altos são mais variados, valores mais baixos são mais consistentes. (padrão: 0.7) | FLOAT | Sim | 0.0 a 1.0 |
| `top_p` | Diversidade via amostragem de núcleo. (padrão: 0.7) | FLOAT | Sim | 0.01 a 1.0 |
| `speed` | Velocidade da fala. 1.0 é normal, <1.0 mais lento, >1.0 mais rápido. (padrão: 1.0) | FLOAT | Sim | 0.5 a 2.0 |
| `volume` | Ajuste de volume em decibéis. 0 significa sem alteração. (padrão: 0.0) | FLOAT | Sim | -10.0 a 10.0 |
| `normalize` | Normaliza números e texto para inglês e chinês, melhorando a estabilidade para números e datas. (padrão: true) | BOOLEAN | Sim | true / false |

**Nota:** A entrada `text` não pode estar vazia. As tags de falante (@Voice1, @Voice2, etc.) não diferenciam maiúsculas de minúsculas e devem se referir a uma voz conectada; marcar uma voz que não está conectada gera um erro. Quando duas ou mais vozes estão conectadas, o texto deve referenciar cada voz conectada pelo menos uma vez, ou o nó reporta as tags ausentes. No s2.1-pro, conectar 0 vozes usa a voz padrão, 1 voz usa apenas essa voz, e 2 ou mais vozes habilitam o diálogo com vários falantes. No s1, uma única voz opcional é usada e deixá-la desconectada usa a voz padrão. Indicadores de emoção podem ser colocados no texto: [happy] e [whispering] no s2.1-pro, e (happy) no s1.

## Saídas

| Nome da saída | Descrição | Tipo de dados |
|-------------|-------------|-----------|
| `audio` | A fala gerada como um arquivo de áudio. | AUDIO |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FishAudioTextToSpeech/pt-BR.md)

---
**Source fingerprint (SHA-256):** `6cc005ae76fc7b60d9399b1b0a3c5de40a6eff47cd6f0f0b73b4212c0270ae29`
