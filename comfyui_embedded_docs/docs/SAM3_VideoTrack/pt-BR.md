> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SAM3_VideoTrack/pt-BR.md)

# Visão Geral

Rastreie objetos entre quadros de vídeo usando o rastreador baseado em memória do SAM3. Este nó processa uma sequência de quadros de vídeo e mantém as identidades dos objetos entre os quadros, usando máscaras iniciais ou prompts de texto para definir o que rastrear.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Intervalo | Descrição |
|-----------|--------------|-------------|-----------|-----------|
| `imagens` | IMAGE | Sim | Quadros de vídeo em lote | Quadros de vídeo como imagens em lote |
| `model` | MODEL | Sim | Modelo SAM3 | O modelo SAM3 a ser usado para rastreamento |
| `máscara_inicial` | MASK | Não | Uma máscara por objeto | Máscara(s) para o primeiro quadro a ser rastreado (uma por objeto). Obrigatório se `condicionamento` não for fornecido. |
| `condicionamento` | CONDITIONING | Não | Condicionamento de texto | Condicionamento de texto para detectar novos objetos durante o rastreamento. Obrigatório se `máscara_inicial` não for fornecido. |
| `limiar_de_deteccao` | FLOAT | Não | 0,0 a 1,0 (padrão: 0,5) | Limiar de pontuação para detecção baseada em prompt de texto |
| `máximo_de_objetos` | INT | Não | 0 a 64 (padrão: 0) | Máximo de objetos rastreados. Máscaras iniciais contam para este limite. 0 usa o limite interno de 64. |
| `intervalo_de_deteccao` | INT | Não | 1 a ilimitado (padrão: 1) | Executar detecção a cada N quadros (1 = a cada quadro). Valores maiores economizam processamento. |

**Observação:** É necessário fornecer `initial_mask` ou `conditioning`. Se ambos forem omitidos, o nó gerará um erro.

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|---------------|--------------|-----------|
| `track_data` | SAM3TrackData | Dados de rastreamento contendo máscaras de objetos e metadados em todos os quadros de vídeo |

---
**Source fingerprint (SHA-256):** `30768bdf5839c1d7b984675e68a127a27f21b17724a2dc885e27f00c272db3cb`
