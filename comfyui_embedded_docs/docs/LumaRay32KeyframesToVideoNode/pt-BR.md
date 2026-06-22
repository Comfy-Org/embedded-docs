# LumaRay32KeyframesToVideoNode

Este nó gera um vídeo que interpola através de uma sequência de imagens guia, cada uma ancorada a uma posição específica na linha do tempo, usando o Luma Ray 3.2. Construa a sequência de quadros-chave usando os nós de quadro-chave do Luma Ray 3.2, conectando pelo menos 2 quadros-chave para definir a animação.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Prompt de texto para a geração do vídeo. | STRING | Sim | 1 a 6000 caracteres |
| `resolution` | A resolução de saída do vídeo gerado (padrão: "720p"). | COMBO | Sim | `"360p"`<br>`"540p"`<br>`"720p"`<br>`"1080p"` |
| `duration` | A duração do vídeo gerado (padrão: "5s"). | COMBO | Sim | `"5s"`<br>`"10s"` |
| `seed` | Semente para geração de números aleatórios para controlar a reprodutibilidade. | INT | Sim | 0 a 4294967295 |
| `keyframes` | Sequência de quadros-chave dos nós de quadro-chave do Luma Ray 3.2 (pelo menos 2). | LUMA_RAY32_KEYFRAME | Sim | 2 a 64 quadros-chave |

**Nota:** A sequência de quadros-chave deve conter pelo menos 2 quadros-chave e no máximo 64 quadros-chave. Cada quadro-chave deve ter uma posição distinta na linha do tempo. As posições dos quadros-chave são resolvidas para índices de quadros de saída com base na duração selecionada (120 quadros para 5s, 240 quadros para 10s). As posições dos quadros-chave no modo de segundos não devem exceder a duração total do vídeo.

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
|-------------|-------------|-----------|
| `video` | A saída de vídeo gerada. | VIDEO |
| `generation_id` | O identificador único para a solicitação de geração. | STRING |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LumaRay32KeyframesToVideoNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `28099e5990942860a20e23cfd5c71a36b23a6264b44097ca617f8bdd06e7857a`
