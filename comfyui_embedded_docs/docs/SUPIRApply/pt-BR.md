# SUPIRApply

O nó SUPIRApply aplica um patch de modelo SUPIR a um modelo de difusão. Ele usa o patch para modificar o comportamento do modelo, permitindo incorporar orientação de uma imagem de entrada durante o processo de amostragem. O nó também fornece controles para ajustar a força dessa orientação ao longo do tempo e inclui um recurso opcional para ajudar a manter a fidelidade à entrada original.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `model` | O modelo de difusão base ao qual o patch SUPIR será aplicado. | MODEL | Sim | - |
| `model_patch` | O patch de modelo SUPIR contendo os pesos e a configuração para modificar o modelo. | MODEL_PATCH | Sim | - |
| `vae` | O VAE (Variational Autoencoder) usado para codificar a imagem de entrada em uma representação latente. | VAE | Sim | - |
| `image` | A imagem de entrada usada para orientar o processo de geração. Apenas os três primeiros canais de cor (RGB) são usados. | IMAGE | Sim | - |
| `strength_start` | Força de controle no início da amostragem (sigma alto). A influência da orientação da imagem começa neste valor. (padrão: 1.0) | FLOAT | Sim | 0.0 - 10.0 |
| `strength_end` | Força de controle no final da amostragem (sigma baixo). Interpolada linearmente a partir do início. A influência da orientação da imagem termina neste valor. (padrão: 1.0) | FLOAT | Sim | 0.0 - 10.0 |
| `restore_cfg` | Puxa a saída desruidificada em direção ao latente de entrada. Valores mais altos = maior fidelidade à entrada. 0 para desabilitar. (padrão: 4.0, configuração avançada) | FLOAT | Sim | 0.0 - 20.0 |
| `restore_cfg_s_tmin` | Limite de sigma abaixo do qual `restore_cfg` é desabilitado. (padrão: 0.05, configuração avançada) | FLOAT | Sim | 0.0 - 1.0 |

*Nota:* A entrada `image` é processada para extrair apenas os canais RGB. Se uma imagem com canal alfa for fornecida, o canal alfa será ignorado.

*Nota:* Se o patch de modelo SUPIR fornecer pesos do codificador de denoise, a imagem de entrada será codificada com esses pesos em vez do codificador VAE regular.

*Nota:* `restore_cfg` só tem efeito quando definido como um valor maior que 0. Definí-lo como 0 desabilita completamente o pós-processamento de restauração. Quando ativo, a correção é aplicada apenas enquanto o valor de sigma atual estiver acima de `restore_cfg_s_tmin`.

*Nota:* Este nó está marcado como experimental no ComfyUI.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `model` | Uma cópia clonada do modelo de entrada com o patch SUPIR aplicado e quaisquer funções pós-CFG adicionais configuradas. | MODEL |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SUPIRApply/pt-BR.md)

---
**Source fingerprint (SHA-256):** `fa9f67f63777160863c44c620d8de11e92f79245c3f5b60e138975dfd0cc65c7`
