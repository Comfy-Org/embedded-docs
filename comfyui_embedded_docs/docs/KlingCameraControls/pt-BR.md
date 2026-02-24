> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingCameraControls/pt-BR.md)

O nó Kling Camera Controls permite configurar vários parâmetros de movimento e rotação da câmera para criar efeitos de controle de movimento na geração de vídeo. Ele fornece controles para posicionamento, rotação e zoom da câmera para simular diferentes movimentos de câmera.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `camera_control_type` | COMBO | Sim | Múltiplas opções disponíveis | Especifica o tipo de configuração de controle de câmera a ser usado |
| `horizontal_movement` | FLOAT | Não | -10.0 a 10.0 | Controla o movimento da câmera ao longo do eixo horizontal (eixo x). Negativo indica esquerda, positivo indica direita (padrão: 0.0) |
| `vertical_movement` | FLOAT | Não | -10.0 a 10.0 | Controla o movimento da câmera ao longo do eixo vertical (eixo y). Negativo indica para baixo, positivo indica para cima (padrão: 0.0) |
| `pan` | FLOAT | Não | -10.0 a 10.0 | Controla a rotação da câmera no plano vertical (eixo x). Negativo indica rotação para baixo, positivo indica rotação para cima (padrão: 0.5) |
| `tilt` | FLOAT | Não | -10.0 a 10.0 | Controla a rotação da câmera no plano horizontal (eixo y). Negativo indica rotação para a esquerda, positivo indica rotação para a direita (padrão: 0.0) |
| `roll` | FLOAT | Não | -10.0 a 10.0 | Controla a quantidade de rotação lateral (rolagem) da câmera (eixo z). Negativo indica anti-horário, positivo indica horário (padrão: 0.0) |
| `zoom` | FLOAT | Não | -10.0 a 10.0 | Controla a mudança na distância focal da câmera. Negativo indica campo de visão mais estreito (zoom in), positivo indica campo de visão mais amplo (zoom out) (padrão: 0.0) |

**Observação:** Pelo menos um dos parâmetros de controle de câmera (`horizontal_movement`, `vertical_movement`, `pan`, `tilt`, `roll` ou `zoom`) deve ter um valor diferente de zero para que a configuração seja válida.

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|-------------|-----------|-------------|
| `camera_control` | CAMERA_CONTROL | Retorna as configurações de controle de câmera configuradas para uso na geração de vídeo |
