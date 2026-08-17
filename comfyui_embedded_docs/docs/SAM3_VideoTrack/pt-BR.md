# SAM3 Video Track

Rastreie objetos entre quadros de vídeo usando o rastreador baseado em memória do SAM3. Este nó processa uma sequência de quadros de vídeo e mantém as identidades dos objetos entre os quadros, usando máscaras iniciais ou prompts de texto para definir o que rastrear.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `images` | Quadros de vídeo como imagens em lote | IMAGE | Sim | Quadros de vídeo em lote |
| `model` | O modelo SAM3 a ser usado para rastreamento | MODEL | Sim | Modelo SAM3 |
| `initial_mask` | Máscara(s) para o primeiro quadro a rastrear (uma por objeto). Necessária se `conditioning` não for fornecida. | MASK | Não | Uma máscara por objeto |
| `conditioning` | Condicionamento de texto para detectar novos objetos durante o rastreamento. Necessário se `initial_mask` não for fornecida. | CONDITIONING | Não | Condicionamento de texto |
| `detection_threshold` | Limiar de pontuação para detecção por prompt de texto (padrão: 0,5). | FLOAT | Sim | 0,0 a 1,0 |
| `max_objects` | Máximo de objetos rastreados. As máscaras iniciais contam para este limite. 0 usa o limite interno de 64 (padrão: 4). | INT | Sim | 0 a 64 |
| `detect_interval` | Executar detecção a cada N quadros (1 = todos os quadros). Valores maiores economizam processamento (padrão: 1). | INT | Sim | 1 ou mais |

**Nota:** É necessário fornecer `initial_mask` ou `conditioning`. Se ambos forem omitidos, o nó gerará um erro. Quando ambos forem fornecidos, as máscaras iniciais definem os objetos a rastrear a partir do primeiro quadro e os prompts de texto detectam objetos adicionais durante o rastreamento.

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `track_data` | Dados de rastreamento contendo máscaras de objetos e metadados em todos os quadros de vídeo, incluindo as dimensões originais do quadro. | SAM3_TRACK_DATA |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SAM3_VideoTrack/pt-BR.md)

---
**Source fingerprint (SHA-256):** `ef584628b334997a001a857a7deffb7eda34db8fa50e3d734a07b5e92566d48d`
