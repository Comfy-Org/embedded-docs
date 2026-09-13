# Luma Ray 3.2 Keyframes para Vídeo

Este nó gera um vídeo que interpola através de uma sequência de imagens-guia, cada uma ancorada a uma posição específica na linha do tempo, usando Luma Ray 3.2. Construa a sequência de keyframes usando nós Luma Ray 3.2 Keyframe, conectando pelo menos 2 keyframes para definir a animação.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Texto de prompt para a geração do vídeo (padrão: string vazia). | STRING | Sim | 1 a 6000 caracteres |
| `resolution` | A resolução de saída do vídeo gerado (padrão: "720p"). | STRING | Sim | `"360p"`<br>`"540p"`<br>`"720p"`<br>`"1080p"` |
| `duration` | A duração do vídeo gerado (padrão: "5s"). | STRING | Sim | `"5s"`<br>`"10s"` |
| `seed` | Semente para geração de números aleatórios para controlar a reprodutibilidade. | INT | Sim | 0 a 4294967295 |
| `keyframes` | Sequência de keyframes dos nós Luma Ray 3.2 Keyframe (pelo menos 2). | LUMA_RAY32_KEYFRAME | Sim | 2 a 64 keyframes |

**Nota:** A sequência de keyframes deve conter pelo menos 2 keyframes e no máximo 64 keyframes. Cada keyframe deve ter uma posição distinta na linha do tempo. As posições dos keyframes são resolvidas para índices de quadros de saída com base na duração selecionada (120 quadros para 5s, 240 quadros para 10s). As posições dos keyframes no modo segundos não devem exceder a duração total do vídeo.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `video` | A saída de vídeo gerada. | VIDEO |
| `generation_id` | O identificador único para a solicitação de geração. | STRING |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LumaRay32KeyframesToVideoNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `28099e5990942860a20e23cfd5c71a36b23a6264b44097ca617f8bdd06e7857a`
