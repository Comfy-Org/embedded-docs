# Aplicar Wan Uni3C ControlNet

## Visão Geral

Este nó aplica um ControlNet Uni3C a um modelo de difusão de vídeo Wan, utilizando um vídeo de orientação renderizado (por exemplo, renderizações de nuvem de pontos deformados) para influenciar a saída do modelo. Ele injeta sinais de controle em camadas de blocos específicas, permitindo orientação baseada em trajetória de câmera durante a geração de vídeo.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Faixa |
|-----------|-------------|-----------|----------|-------|
| `modelo` | O modelo de difusão Wan a ser modificado. | MODEL | Sim | – |
| `model_patch` | Um patch ControlNet Uni3C (deve ser uma instância de `comfy.ldm.wan.uni3c.WanUni3CControlnet`). | MODEL_PATCH | Sim | – |
| `vae` | O VAE usado para codificar o vídeo de orientação em latentes. | VAE | Sim | – |
| `renderizar_vídeo` | O vídeo de orientação renderizado a partir da trajetória da câmera, mais comumente renderizações de nuvem de pontos deformados da imagem de entrada. | IMAGE | Sim | – |
| `força` | A intensidade do sinal de controle aplicado. | FLOAT | Sim | -10.0 a 10.0 (padrão: 1.0) |
| `percentual_inicial` | A porcentagem do processo de remoção de ruído na qual o controle é iniciado. | FLOAT | Sim | 0.0 a 1.0 (padrão: 0.0) |
| `percentual_final` | A porcentagem do processo de remoção de ruído na qual o controle é encerrado. | FLOAT | Sim | 0.0 a 1.0 (padrão: 1.0) |

**Observações:**
- O `model_patch` deve ser um ControlNet Uni3C; caso contrário, o nó gerará um erro.
- A dimensão interna do controlnet deve corresponder à dimensão do modelo Wan – um erro será gerado se forem diferentes.
- Espera-se que a imagem de entrada `render_video` esteja no formato RGB (apenas os 3 primeiros canais são utilizados).

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `MODEL` | O modelo Wan modificado com o ControlNet Uni3C aplicado. | MODEL |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanUni3CControlnetApply/pt-BR.md)

---
**Source fingerprint (SHA-256):** `f69253f06aba9208778f713ad36e9995f53a15d2e61243b853b9ac9131637371`
