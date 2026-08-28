# SAM3 Video Track

Trackeia objetos entre os quadros de vídeo usando o rastreador baseado em memória do SAM3. Este nó processa uma sequência de quadros de vídeo e mantém as identidades dos objetos entre os quadros, usando máscaras iniciais ou prompts de texto para definir o que rastrear.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `imagens` | Quadros de vídeo como imagens em lote | IMAGE | Sim | Quadros de vídeo em lote |
| `model` | O modelo SAM3 a ser usado para rastreamento | MODEL | Sim | Modelo SAM3 |
| `máscara_inicial` | Máscara(s) para o primeiro quadro a rastrear (uma por objeto) | MASK | Não | Uma máscara por objeto |
| `condicionamento` | Condicionamento de texto para detectar novos objetos durante o rastreamento | CONDITIONING | Não | Condicionamento de texto |
| `limiar_de_deteccao` | Limiar de pontuação para detecção por prompt de texto (padrão: 0.5) | FLOAT | Não | 0.0 a 1.0 |
| `máximo_de_objetos` | Máximo de objetos rastreados. Máscaras iniciais contam para esse limite. 0 usa o limite interno de 64. (padrão: 4) | INT | Não | 0 a 64 |
| `intervalo_de_deteccao` | Executar detecção a cada N quadros (1=todo quadro). Valores maiores economizam computação. (padrão: 1) | INT | Não | 1 ou mais |

**Nota:** É necessário fornecer `initial_mask` ou `conditioning`. Se ambos forem omitidos, o nó gera um erro.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `dados_de_rastreamento` | Dados de rastreamento contendo máscaras de objetos e metadados em todos os quadros de vídeo | SAM3TrackData |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SAM3_VideoTrack/pt-BR.md)

---
**Source fingerprint (SHA-256):** `ef584628b334997a001a857a7deffb7eda34db8fa50e3d734a07b5e92566d48d`
