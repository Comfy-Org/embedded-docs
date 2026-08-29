# Suavizar dados de pose corporal SAM3D

O Smooth SAM3D Body Pose Data reduz o tremor entre quadros em sequências de pose corporal 3D ao calcular a média do movimento ao longo do tempo. Ele aplica suavização total aos dados de câmera e aparência, enquanto reduz a suavização da geometria da malha quando o sujeito gira rapidamente, de modo que giros rápidos não sejam achatados.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Faixa |
|-----------|-------------|---------------|-------------|-------|
| `mhr_pose_data` | A sequência de dados de pose MHR a ser suavizada, contendo parâmetros de modelo, parâmetros de forma, parâmetros de expressão, layout de keypoints MHR70 e dados de malha relacionados. | MHR_POSE_DATA | Sim | — |
| `intensidade` | Intensidade da suavização. 0 = bruto, 1 = suavizado. (padrão: 1.0) | FLOAT | Sim | 0.0 a 1.0 (passo 0.05) |
| `método` | gaussian: média ponderada simétrica, melhor suavizador de uso geral.<br>savgol: ajuste polinomial deslizante, preserva picos agudos. (padrão: "savgol") | COMBO | Sim | "gaussian"<br>"savgol" |
| `janela` | Janela temporal em quadros (valores ímpares). (padrão: 7) | INT | Sim | 1 a 51 (valores ímpares, passo 2) |
| `rotation_threshold_degrees` | Desativa a suavização para esta taxa de rotação da raiz (graus/quadro) para preservar giros rápidos. 30° é adequado para a maioria dos conteúdos; valores baixos podem desativar a suavização em tremores comuns e impactar silenciosamente a qualidade. 0 = desativa. (padrão: 30.0) | FLOAT | Sim | 0.0 a 90.0 (passo 1.0) |

Nota: Quando `strength` é 0.0 ou menor, ou `window` é 1 ou menor, o nó retorna os dados de entrada inalterados. A entrada deve conter pelo menos 2 quadros e dados de keypoints; caso contrário, o nó retorna os dados de entrada inalterados. Quando `rotation_threshold_degrees` é 0.0, a redução da suavização baseada em rotação é desativada.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|---------------|
| `mhr_pose_data` | A sequência de dados de pose MHR suavizada, com redução do tremor entre quadros. | MHR_POSE_DATA |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SAM3DBody_Smooth/pt-BR.md)

---
**Source fingerprint (SHA-256):** `a80a1c121f1d2bc49e9112576775588d5deab4690c4cd6ec9c1f98de78457b30`
