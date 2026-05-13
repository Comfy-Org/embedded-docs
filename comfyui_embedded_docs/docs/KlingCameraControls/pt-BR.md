> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingCameraControls/pt-BR.md)

O nó Kling Camera Controls permite configurar vários parâmetros de movimento e rotação de câmera para criar efeitos de controle de movimento na geração de vídeos. Ele fornece controles para posicionamento, rotação e zoom da câmera, simulando diferentes movimentos cinematográficos.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Faixa | Descrição |
|-----------|--------------|-------------|-------|-----------|
| `camera_control_type` | COMBO | Sim | `"simple"`<br>`"advanced"` | Especifica o tipo de configuração de controle de câmera a ser utilizado |
| `horizontal_movement` | FLOAT | Não | -10.0 a 10.0 | Controla o movimento da câmera ao longo do eixo horizontal (eixo x). Valores negativos indicam movimento para a esquerda, positivos para a direita (padrão: 0.0) |
| `vertical_movement` | FLOAT | Não | -10.0 a 10.0 | Controla o movimento da câmera ao longo do eixo vertical (eixo y). Valores negativos indicam movimento para baixo, positivos para cima (padrão: 0.0) |
| `pan` | FLOAT | Não | -10.0 a 10.0 | Controla a rotação da câmera no plano vertical (eixo x). Valores negativos indicam rotação para baixo, positivos para cima (padrão: 0.5) |
| `tilt` | FLOAT | Não | -10.0 a 10.0 | Controla a rotação da câmera no plano horizontal (eixo y). Valores negativos indicam rotação para a esquerda, positivos para a direita (padrão: 0.0) |
| `roll` | FLOAT | Não | -10.0 a 10.0 | Controla o ângulo de rotação da câmera (eixo z). Valores negativos indicam rotação anti-horária, positivos horária (padrão: 0.0) |
| `zoom` | FLOAT | Não | -10.0 a 10.0 | Controla a alteração na distância focal da câmera. Valores negativos indicam campo de visão mais estreito, positivos campo mais amplo (padrão: 0.0) |

**Observação:** Pelo menos um dos parâmetros de controle de câmera (`horizontal_movement`, `vertical_movement`, `pan`, `tilt`, `roll` ou `zoom`) deve ter um valor diferente de zero para que a configuração seja válida.

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|---------------|--------------|-----------|
| `camera_control` | CAMERA_CONTROL | Retorna as configurações de controle de câmera configuradas para uso na geração de vídeos |

---
**Source fingerprint (SHA-256):** `4e1d826518ae17afd2c0aa22ebf6cce67b3ef33bb1730f0ce5ead5b9431cd548`
