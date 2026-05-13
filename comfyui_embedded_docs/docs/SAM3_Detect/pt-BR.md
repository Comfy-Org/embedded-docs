> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SAM3_Detect/pt-BR.md)

# Nó SAM3 Detect

## Visão Geral

O nó SAM3 Detect realiza detecção e segmentação de vocabulário aberto usando descrições de texto, caixas delimitadoras ou prompts de pontos. Ele pode identificar e segmentar objetos em uma imagem com base no que você descreve em texto, onde você desenha caixas ou onde você clica em pontos.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Faixa | Descrição |
|-----------|-----------|----------|-------|-------------|
| `model` | MODEL | Sim | - | O modelo SAM3 a ser usado para detecção e segmentação |
| `image` | IMAGE | Sim | - | A imagem de entrada a ser processada |
| `conditioning` | CONDITIONING | Não | - | Condicionamento de texto do CLIPTextEncode. Necessário ao usar prompts de texto para detecção |
| `bboxes` | BOUNDING_BOX | Não | - | Caixas delimitadoras para segmentar. Pode ser uma única caixa (aplicada a todos os quadros), uma lista de caixas (aplicada a todos os quadros) ou uma lista de listas (caixas por quadro). Quando fornecido sem condicionamento de texto, o nó segmenta dentro de cada caixa |
| `positive_coords` | STRING | Não | - | Prompts de pontos positivos no formato JSON `[{"x": int, "y": int}, ...]` usando coordenadas de pixels. São pontos que você deseja incluir na segmentação |
| `negative_coords` | STRING | Não | - | Prompts de pontos negativos no formato JSON `[{"x": int, "y": int}, ...]` usando coordenadas de pixels. São pontos que você deseja excluir da segmentação |
| `threshold` | FLOAT | Não | 0.0 a 1.0 | Limiar de confiança para detecções baseadas em texto. Apenas detecções com pontuações acima deste valor são mantidas (padrão: 0.5) |
| `refine_iterations` | INT | Não | 0 a 5 | Número de passagens de refinamento do decodificador SAM. Valores maiores podem melhorar a qualidade das máscaras. Defina como 0 para usar máscaras brutas do detector sem refinamento (padrão: 2) |
| `individual_masks` | BOOLEAN | Não | Verdadeiro/Falso | Quando ativado, gera máscaras separadas para cada objeto detectado em vez de combiná-las em uma única máscara (padrão: Falso) |

### Restrições e Notas dos Parâmetros

- **Prompts de texto**: Para usar detecção baseada em texto, você deve fornecer a entrada `conditioning`. Quando o condicionamento de texto é fornecido, o nó executa detecção guiada por texto na imagem.
- **Prompts de caixa**: Quando `bboxes` são fornecidos sem condicionamento de texto, o nó segmenta a área dentro de cada caixa delimitadora.
- **Prompts de ponto**: Quando `positive_coords` ou `negative_coords` são fornecidos, o nó usa segmentação baseada em pontos. Os pontos são escalados automaticamente para a resolução interna do modelo.
- **Múltiplos tipos de prompt**: Você pode combinar diferentes tipos de prompt. Por exemplo, você pode fornecer tanto condicionamento de texto quanto caixas delimitadoras para restringir a detecção de texto a áreas específicas.
- **Processamento em lote**: O nó suporta imagens em lote. Ao processar múltiplos quadros, as caixas delimitadoras podem ser fornecidas por quadro usando um formato de lista de listas.
- **Formato JSON para pontos**: As coordenadas dos pontos devem ser fornecidas como strings JSON válidas no formato `[{"x": 100, "y": 200}, {"x": 150, "y": 250}]`.

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|-------------|-----------|-------------|
| `masks` | MASK | Máscaras de segmentação. Quando `individual_masks` é Falso (padrão), retorna uma única máscara combinada por quadro. Quando Verdadeiro, retorna máscaras individuais para cada objeto detectado |
| `bboxes` | BOUNDING_BOX | Caixas delimitadoras detectadas com coordenadas e pontuações de confiança. Cada caixa inclui valores `x`, `y`, `largura`, `altura` e `pontuação` |

---
**Source fingerprint (SHA-256):** `d073bda7eca934f3c64e1be740f5fb5249d27046a8be5902ea5d2245d5f679ea`
