# SAM3 Video Track

Rastreie objetos entre quadros de vídeo usando o rastreador baseado em memória do SAM3. Este nó processa uma sequência de quadros de vídeo e mantém as identidades dos objetos entre os quadros, usando máscaras iniciais ou prompts de texto para definir o que rastrear.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `imagens` | Quadros de vídeo como imagens em lote | IMAGE | Sim | Quadros de vídeo em lote |
| `model` | O modelo SAM3 a ser usado para rastreamento | MODEL | Sim | Modelo SAM3 |
| `máscara_inicial` | Máscara(s) para o primeiro quadro a ser rastreado (uma por objeto). Obrigatório se `condicionamento` não for fornecido. | MASK | Não | Uma máscara por objeto |
| `condicionamento` | Condicionamento de texto para detectar novos objetos durante o rastreamento. Obrigatório se `máscara_inicial` não for fornecido. | CONDITIONING | Não | Condicionamento de texto |
| `limiar_de_deteccao` | Limiar de pontuação para detecção baseada em prompt de texto | FLOAT | Não | 0,0 a 1,0 (padrão: 0,5) |
| `máximo_de_objetos` | Máximo de objetos rastreados. Máscaras iniciais contam para este limite. 0 usa o limite interno de 64. | INT | Não | 0 a 64 (padrão: 0) |
| `intervalo_de_deteccao` | Executar detecção a cada N quadros (1 = a cada quadro). Valores maiores economizam processamento. | INT | Não | 1 a ilimitado (padrão: 1) |

**Observação:** É necessário fornecer `initial_mask` ou `conditioning`. Se ambos forem omitidos, o nó gerará um erro.

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `track_data` | Dados de rastreamento contendo máscaras de objetos e metadados em todos os quadros de vídeo | SAM3TrackData |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SAM3_VideoTrack/pt-BR.md)

---
**Source fingerprint (SHA-256):** `30768bdf5839c1d7b984675e68a127a27f21b17724a2dc885e27f00c272db3cb`
