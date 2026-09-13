# SAM3 Video Track

Rastreie objetos em frames de vídeo usando o rastreador baseado em memória do SAM3. O nó processa uma sequência de frames de vídeo e mantém as identidades dos objetos entre os frames, usando máscaras iniciais ou prompts de texto para definir o que rastrear, e pode detectar novos objetos ao longo do caminho usando condicionamento de texto.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `images` | Frames de vídeo como imagens em lote | IMAGE | Sim | Frames de vídeo em lote |
| `model` | O modelo SAM3 a ser usado para rastreamento | MODEL | Sim | Modelo SAM3 |
| `initial_mask` | Máscara(s) para o primeiro frame a ser rastreado (uma por objeto) | MASK | Não | Uma máscara por objeto |
| `conditioning` | Condicionamento de texto para detectar novos objetos durante o rastreamento | CONDITIONING | Não | Condicionamento de texto |
| `detection_threshold` | Limite de pontuação para detecção com prompt de texto (padrão: 0.5) | FLOAT | Não | 0.0 a 1.0 (passo 0.01) |
| `max_objects` | Máximo de objetos rastreados. Máscaras iniciais contam para este limite. 0 usa o limite interno de 64. (padrão: 4) | INT | Não | 0 a 64 |
| `detect_interval` | Executa a detecção a cada N frames (1=a cada frame). Valores mais altos economizam processamento. (padrão: 1) | INT | Não | 1 ou maior |

**Observação:** É necessário fornecer `initial_mask` ou `conditioning`. Se ambos forem omitidos, o nó gera um erro.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `track_data` | Dados de rastreamento contendo máscaras de objetos e metadados em todos os frames de vídeo | SAM3_TRACK_DATA |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SAM3_VideoTrack/pt-BR.md)

---
**Source fingerprint (SHA-256):** `ef584628b334997a001a857a7deffb7eda34db8fa50e3d734a07b5e92566d48d`
