## Visão Geral

Desenha pontos de referência faciais e linhas de conexão (uma malha facial) sobre uma imagem de entrada. Este nó utiliza os dados de pontos de referência produzidos por um nó de detecção facial para visualizar as características faciais detectadas, como olhos, nariz, boca e contorno do rosto.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `face_landmarks` | Os dados de pontos de referência facial de um nó de detecção. | FACE_LANDMARKS | Sim |  |
| `image` | A imagem onde a malha será desenhada. Se não estiver conectada, será usado um canvas preto do mesmo tamanho do resultado da detecção. | IMAGE | Não |  |
| `connections` | Determina quais partes da malha facial serão desenhadas. `"all"` desenha a malha completa (oval, olhos, sobrancelhas, lábios, íris, nariz). `"fill"` desenha um polígono sólido do oval facial (máscara de silhueta). `"custom"` permite ativar ou desativar cada característica individualmente. (padrão: `"all"`) | COMBO | Sim | `"all"`<br>`"fill"`<br>`"custom"` |
| `color` | A cor das linhas e pontos da malha. (padrão: `#00ff00`) | COLOR | Sim |  |
| `thickness` | A espessura das linhas da malha em pixels. Definir como 0 desativa o desenho de linhas. (padrão: 1) | INT | Sim | 0 a 8 |
| `point_size` | O raio dos pontos de referência em pixels. Definir como 0 desativa o desenho de pontos. (padrão: 2) | INT | Sim | 0 a 16 |

**Nota sobre o parâmetro `connections`:** Quando `"custom"` é selecionado, entradas booleanas adicionais aparecem para cada característica facial (ex.: `face_oval`, `lips`, `left_eye`, `right_eye`, `left_eyebrow`, `right_eyebrow`, `left_iris`, `right_iris`, `nose`, `tesselation`). Apenas as características que você ativar serão desenhadas.

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `IMAGE` | A imagem de entrada com a malha de pontos de referência facial desenhada sobre ela. | IMAGE |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MediaPipeFaceMeshVisualize/pt-BR.md)

---
**Source fingerprint (SHA-256):** `fb5437d73378b0c8daa68669c2e19058ccb7133ed68fc51c8d4c5bab8662f243`
