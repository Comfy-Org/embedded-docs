# Controles de Câmera Kling

O nó Kling Camera Controls permite configurar vários parâmetros de movimento e rotação de câmera para criar efeitos de controle de movimento na geração de vídeos. Ele fornece controles para posicionamento, rotação e zoom da câmera, simulando diferentes movimentos cinematográficos.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `camera_control_type` | Especifica o tipo de configuração de controle de câmera a ser utilizado | COMBO | Sim | `"simple"`<br>`"advanced"` |
| `horizontal_movement` | Controla o movimento da câmera ao longo do eixo horizontal (eixo x). Valores negativos indicam movimento para a esquerda, positivos para a direita (padrão: 0.0) | FLOAT | Não | -10.0 a 10.0 |
| `vertical_movement` | Controla o movimento da câmera ao longo do eixo vertical (eixo y). Valores negativos indicam movimento para baixo, positivos para cima (padrão: 0.0) | FLOAT | Não | -10.0 a 10.0 |
| `pan` | Controla a rotação da câmera no plano vertical (eixo x). Valores negativos indicam rotação para baixo, positivos para cima (padrão: 0.5) | FLOAT | Não | -10.0 a 10.0 |
| `tilt` | Controla a rotação da câmera no plano horizontal (eixo y). Valores negativos indicam rotação para a esquerda, positivos para a direita (padrão: 0.0) | FLOAT | Não | -10.0 a 10.0 |
| `roll` | Controla o ângulo de rotação da câmera (eixo z). Valores negativos indicam rotação anti-horária, positivos horária (padrão: 0.0) | FLOAT | Não | -10.0 a 10.0 |
| `zoom` | Controla a alteração na distância focal da câmera. Valores negativos indicam campo de visão mais estreito, positivos campo mais amplo (padrão: 0.0) | FLOAT | Não | -10.0 a 10.0 |

**Observação:** Pelo menos um dos parâmetros de controle de câmera (`horizontal_movement`, `vertical_movement`, `pan`, `tilt`, `roll` ou `zoom`) deve ter um valor diferente de zero para que a configuração seja válida.

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `camera_control` | Retorna as configurações de controle de câmera configuradas para uso na geração de vídeos | CAMERA_CONTROL |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingCameraControls/pt-BR.md)

---
**Source fingerprint (SHA-256):** `4e1d826518ae17afd2c0aa22ebf6cce67b3ef33bb1730f0ce5ead5b9431cd548`
