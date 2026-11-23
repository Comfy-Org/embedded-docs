# Meshy: Image to Relief

Este nó transforma uma foto em um modelo de baixo-relevo e um mapa de profundidade de 16 bits para impressão 3D, gravação a laser e usinagem CNC. Arte escura sobre um fundo claro é elevada, e áreas claras permanecem baixas. Somente as saídas que você conectar são geradas e baixadas; portanto, sem uma saída de modelo conectada, a tarefa retorna apenas o mapa de profundidade.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `image` | Foto a ser convertida em um relevo. Arte escura sobre fundo claro é elevada. A transparência é descartada antes do envio, então achate um logotipo transparente sobre um fundo branco primeiro. | IMAGE | Sim | Imagem única |
| `relief_type` | Predefinição de entalhe. `"low"` é um entalhe raso para gravação a laser, usinagem CNC e placas; `"high"` é mais profundo para peças impressas em 3D. A predefinição seleciona o valor de `carving_depth_mm`. | DYNAMIC_COMBO | Sim | `"low"`<br>`"high"` |
| `carving_depth_mm` | Profundidade do entalhe em milímetros. Disponível quando `relief_type` está definido (padrão: 3.0 para `"low"`, 6.0 para `"high"`). | FLOAT | Sim | 0.1 a 60.0 (passo 0.1) |
| `size_mm` | Comprimento do lado maior da foto no modelo, em milímetros, medido na posição plana antes de qualquer curvatura (padrão: 60.0). | FLOAT | Sim | 20.0 a 250.0 (passo 1.0) |
| `carving_mode` | `"emboss"` eleva as partes mais próximas da foto; `"engrave"` as entalha para dentro. | COMBO | Sim | `"emboss"`<br>`"engrave"` |
| `base` | `"plate"` mantém uma placa de base sob o relevo; `"none"` recorta o fundo e não constrói placa. Selecionar uma opção revela seu parâmetro. | DYNAMIC_COMBO | Sim | `"plate"`<br>`"none"` |
| `base_thickness_mm` | Espessura da placa de base em milímetros. Disponível quando `base` é `"plate"` (padrão: 1.0). | FLOAT | Sim | 0.1 a 10.0 (passo 0.1) |
| `removal_threshold` | Profundidade abaixo da qual o fundo é recortado, no mapa de profundidade de 0 a 1. 0.3 mantém um busto inteiro; 0.8 o fragmenta. Disponível quando `base` é `"none"` (padrão: 0.01). | FLOAT | Sim | 0.01 a 1.0 (passo 0.01) |
| `bend` | `"convex"` abaula a frente para fora; `"concave"` a curva para dentro; `"off"` mantém o relevo plano. Selecionar uma curvatura revela `bend_axis` e `bend_angle`. | DYNAMIC_COMBO | Sim | `"off"`<br>`"convex"`<br>`"concave"` |
| `bend_axis` | `"xz"` curva as bordas esquerda e direita; `"yz"`, as bordas superior e inferior. Disponível quando `bend` é `"convex"` ou `"concave"`. | COMBO | Sim | `"xz"`<br>`"yz"` |
| `bend_angle` | Arco que a curvatura abrange, em graus; 360 fecha o relevo em um cilindro. Disponível quando `bend` é `"convex"` ou `"concave"` (padrão: 60.0). | FLOAT | Sim | 1.0 a 360.0 (passo 1.0) |
| `seed` | Semente que controla se o nó é executado novamente; o resultado é não determinístico independentemente da semente. Altere-a para solicitar uma saída que foi conectada após a última execução (padrão: 42). | INT | Sim | 0 a 2147483647 |
| `mesh_resolution` | Pontos da malha ao longo do lado maior da foto. Em 1024, o GLB tem cerca de 50 MB e o STL cerca de 105 MB; em 2048, cerca de 200 MB e 420 MB; uma curvatura dobra esses valores. (padrão: 1024; opção avançada) | INT | Sim | 512 a 2048 |
| `color_mapping` | Colore os arquivos GLB, OBJ, FBX e USDZ com a foto. STL e 3MF permanecem brancos. (padrão: False; opção avançada) | BOOLEAN | Sim | True / False |

**Observação:** Um formato de modelo só é gerado e baixado quando sua saída está conectada. Sem nenhuma saída de modelo conectada, a tarefa retorna apenas o mapa de profundidade; e `preview` sozinho ainda faz o modelo ser gerado para a miniatura, mas não retorna arquivo de modelo. `depth_map` mantém a faixa completa de 16 bits; Save Image (Advanced) o grava como um PNG de 16 bits.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `GLB` | O modelo do relevo baixado no formato GLB. | FILE3DGLB |
| `STL` | O modelo do relevo baixado no formato STL. | FILE3DSTL |
| `OBJ` | O modelo do relevo baixado no formato OBJ. | FILE3DOBJ |
| `FBX` | O modelo do relevo baixado no formato FBX. | FILE3DFBX |
| `USDZ` | O modelo do relevo baixado no formato USDZ. | FILE3DUSDZ |
| `3MF` | O modelo do relevo baixado no formato 3MF. | FILE3D |
| `depth_map` | Mapa de profundidade com a faixa completa de 16 bits; Save Image (Advanced) o grava como um PNG de 16 bits. | IMAGE |
| `preview` | Miniatura renderizada pelo Meshy para o relevo finalizado. | IMAGE |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MeshyImageToReliefNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `6f2f0eb49074281b99d7ee10daf3bcc5616c6596c1c4d8491c72739550395f52`
