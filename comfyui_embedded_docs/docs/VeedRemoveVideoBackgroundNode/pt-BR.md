# VEED Remove Video Background

Recorte o sujeito de um vídeo com o VEED e retorne os quadros junto com uma máscara alfa. Use as duas saídas para composição, ou envie-as por Join Image with Alpha e Save WEBM para gravar um vídeo transparente. Escolha `"standard"` para as melhores bordas em qualquer fundo, `"fast"` quando a velocidade for importante, ou `"green screen"` para filmagens gravadas contra um fundo verde.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `model` | Modelo de segmentação a usar: `"standard"` para qualquer fundo com as melhores bordas e saída de até 3840x2160, `"fast"` para um resultado mais rápido de até 1920x1080, ou `"green screen"` para remover um fundo verde de até 3840x2160. Vídeos maiores são reduzidos. Selecionar uma opção revela seus parâmetros. | DYNAMIC_COMBO | Sim | `"standard"`<br>`"fast"`<br>`"green screen"` |
| `video` | O vídeo do qual recortar o sujeito. Até 60 segundos. | VIDEO | Sim | Até 60 segundos |
| `refine_foreground_edges` | Bordas mais limpas em cabelo, pelo e detalhes finos. Desativá-lo reduz o custo. Disponível para `"standard"` e `"fast"` (padrão: True). | BOOLEAN | Sim | false<br>true |
| `subject_is_person` | Desative quando o sujeito for um objeto ou animal. Disponível para `"standard"` e `"fast"` (padrão: True). | BOOLEAN | Sim | false<br>true |
| `spill_suppression_strength` | Com que intensidade o tom verde é removido do sujeito. Aumente quando restarem manchas verdes; diminua quando as cores do sujeito mudarem. Disponível para `"green screen"` (padrão: 0.8). | FLOAT | Sim | 0.0 a 1.0 (passo 0.01) |

O clipe é limitado a 60 segundos; vídeos mais longos são rejeitados com um erro. A máscara é 1 onde o fundo foi removido, então use Invert Mask antes de Image Composite Masked quando quiser manter o sujeito.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `images` | Os quadros do vídeo com o fundo removido. | IMAGE |
| `mask` | 1 onde o fundo foi removido, por quadro. | MASK |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VeedRemoveVideoBackgroundNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `1bf52a380ab09437a5a57f70215856d4ea0055f78ce8b42fe2a2b87d686e8d26`
