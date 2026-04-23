> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SUPIRApply/pt-BR.md)

O nó SUPIRApply aplica um patch do modelo SUPIR a um modelo de difusão. Ele utiliza o patch para modificar o comportamento do modelo, permitindo incorporar orientação de uma imagem de entrada durante o processo de amostragem. O nó também fornece controles para ajustar a intensidade dessa orientação ao longo do tempo e inclui um recurso opcional para ajudar a manter a fidelidade à imagem original.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Faixa | Descrição |
|-----------|--------------|-------------|-------|-----------|
| `model` | MODEL | Sim | - | O modelo de difusão base ao qual o patch SUPIR será aplicado. |
| `model_patch` | MODELPATCH | Sim | - | O patch do modelo SUPIR contendo os pesos e a configuração para modificar o modelo. |
| `vae` | VAE | Sim | - | O VAE (Autoencoder Variacional) usado para codificar a imagem de entrada em uma representação latente. |
| `image` | IMAGE | Sim | - | A imagem de entrada usada para guiar o processo de geração. Apenas os três primeiros canais de cor (RGB) são utilizados. |
| `strength_start` | FLOAT | Não | 0.0 - 10.0 | Intensidade do controle no início da amostragem (sigma alto). A influência da orientação da imagem começa neste valor. (padrão: 1.0) |
| `strength_end` | FLOAT | Não | 0.0 - 10.0 | Intensidade do controle no final da amostragem (sigma baixo). Interpolado linearmente a partir do início. A influência da orientação da imagem termina neste valor. (padrão: 1.0) |
| `restore_cfg` | FLOAT | Não | 0.0 - 20.0 | Atrai a saída removida do ruído em direção ao latente de entrada. Quanto maior, mais forte é a fidelidade à entrada. Use 0 para desativar. (padrão: 4.0) |
| `restore_cfg_s_tmin` | FLOAT | Não | 0.0 - 1.0 | Limite de sigma abaixo do qual o `restore_cfg` é desativado. (padrão: 0.05) |

*Nota:* A entrada `image` é processada para extrair apenas os canais RGB. Se uma imagem com canal alfa for fornecida, o canal alfa é ignorado.

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|---------------|--------------|-----------|
| `model` | MODEL | O modelo de difusão com o patch SUPIR aplicado e quaisquer funções adicionais pós-CFG configuradas. |