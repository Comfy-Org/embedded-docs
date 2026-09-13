# Suavizar dados de pose corporal SAM3D

Smooth SAM3D Body Pose Data reduz a trepidação entre quadros em uma sequência de poses corporais 3D ao calcular a média do movimento ao longo do tempo. Dados de câmera e aparência são suavizados totalmente, enquanto a geometria da malha é suavizada menos quando o sujeito gira rapidamente, para que giros rápidos não sejam achatados.

## Entradas

| Parâmetro | Descrição | Tipo de dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `mhr_pose_data` | A sequência de dados de pose MHR a ser suavizada, contendo parâmetros de modelo, parâmetros de forma, parâmetros de expressão, layout de keypoints MHR70 e dados de malha relacionados. | MHR_POSE_DATA | Sim | — |
| `strength` | Intensidade da suavização. 0 = bruto, 1 = suavizado. (padrão: 1.0) | FLOAT | Sim | 0.0 a 1.0 (passo 0.05) |
| `method` | gaussian: média ponderada simétrica, melhor suavizador de uso geral.<br>savgol: ajuste polinomial deslizante, preserva picos acentuados. (padrão: "savgol") | COMBO | Sim | "gaussian"<br>"savgol" |
| `window` | Janela temporal em quadros (valores ímpares). (padrão: 7) | INT | Sim | 1 a 51 (valores ímpares, passo 2) |
| `rotation_threshold_degrees` | Desativa a suavização para esta taxa de rotação da raiz (grau/quadro) a fim de preservar giros rápidos. 30° é adequado para a maioria do conteúdo; valores baixos podem desativar a suavização em trepidações comuns e impactar silenciosamente a qualidade. 0 = desativar. (padrão: 30.0) | FLOAT | Sim | 0.0 a 90.0 (passo 1.0) |

Observação: quando `strength` é 0.0 ou menor, ou `window` é 1 ou menor, o nó retorna os dados de entrada inalterados. A entrada deve conter pelo menos 2 quadros e dados de keypoints; caso contrário, o nó retorna os dados de entrada inalterados. Quando `rotation_threshold_degrees` é 0.0, o recuo da suavização baseado em rotação é desativado.

## Saídas

| Nome da saída | Descrição | Tipo de dados |
|-------------|-------------|-----------|
| `mhr_pose_data` | A sequência de dados de pose MHR suavizada com trepidação entre quadros reduzida. | MHR_POSE_DATA |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SAM3DBody_Smooth/pt-BR.md)

---
**Source fingerprint (SHA-256):** `a80a1c121f1d2bc49e9112576775588d5deab4690c4cd6ec9c1f98de78457b30`
