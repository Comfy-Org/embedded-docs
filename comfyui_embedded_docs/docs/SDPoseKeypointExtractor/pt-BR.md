O nó SDPoseKeypointExtractor detecta pontos-chave de pose humana a partir de imagens de entrada usando o modelo SDPose. Ele pode processar imagens completas ou regiões específicas definidas por caixas delimitadoras e gera os pontos-chave detectados no formato OpenPose, que inclui as coordenadas para cada pessoa e uma pontuação de confiança para cada ponto-chave.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `modelo` | O modelo SDPose usado para detecção de pontos-chave. Deve ser um modelo com o atributo `heatmap_head`, especificamente do repositório SDPose. | MODEL | Sim | - |
| `vae` | O modelo VAE usado para codificar as imagens de entrada no espaço latente para processamento. | VAE | Sim | - |
| `imagem` | A imagem de entrada ou lote de imagens do qual extrair os pontos-chave de pose. | IMAGE | Sim | - |
| `tamanho_do_lote` | O número de imagens a serem processadas de uma vez ao executar no modo de imagem completa (ou seja, quando `caixas_delimitadoras` não é fornecido). Isso pode acelerar o processamento. (padrão: 16) | INT | Não | 1 a 10000 |
| `caixas_delimitadoras` | Caixas delimitadoras opcionais para detecções mais precisas. Necessário para detecção de múltiplas pessoas. Se fornecido, o nó extrairá pontos-chave de cada região especificada. | BOUNDINGBOX | Não | - |

**Restrições dos Parâmetros:**
*   A entrada `model` deve ser um modelo SDPose específico. Se o modelo fornecido não tiver o atributo `heatmap_head`, o nó gerará um erro.
*   O nó opera em dois modos distintos com base na entrada `bboxes`:
    1.  **Modo Caixa Delimitadora:** Quando `bboxes` é fornecido, ele processa cada região especificada individualmente. Isso é necessário para detectar várias pessoas em uma única imagem.
    2.  **Modo Imagem Completa:** Quando `bboxes` não é fornecido, ele processa a imagem inteira como um lote. O parâmetro `batch_size` se aplica apenas neste modo.

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `keypoints` | Pontos-chave no formato de quadro OpenPose (largura_do_canvas, altura_do_canvas, pessoas). A saída contém as pessoas detectadas, cada uma com uma matriz de coordenadas de pontos-chave (x, y) e suas respectivas pontuações de confiança. | POSE_KEYPOINT |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SDPoseKeypointExtractor/pt-BR.md)

---
**Source fingerprint (SHA-256):** `7903b51c9137aa08bb8843362740fcf93cea9c09d142bd1db3b5eee945c853e4`
