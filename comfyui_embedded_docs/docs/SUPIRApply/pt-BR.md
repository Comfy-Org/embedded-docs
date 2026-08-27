# SUPIRApply

O nó SUPIRApply aplica um patch do modelo SUPIR a um modelo de difusão. Ele usa o patch para modificar o comportamento do modelo, permitindo incorporar orientação de uma imagem de entrada durante o processo de amostragem. O nó também fornece controles para ajustar a força dessa orientação ao longo do tempo e inclui um recurso opcional para ajudar a manter a fidelidade à imagem original.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `model` | O modelo de difusão base ao qual o patch do SUPIR será aplicado. | MODEL | Sim | - |
| `model_patch` | O patch do modelo SUPIR contendo os pesos e a configuração para modificar o modelo. | MODELPATCH | Sim | - |
| `vae` | O VAE (Autoencoder Variacional) usado para codificar a imagem de entrada em uma representação latente. | VAE | Sim | - |
| `image` | A imagem de entrada usada para guiar o processo de geração. Apenas os três primeiros canais de cor (RGB) são utilizados. | IMAGE | Sim | - |
| `strength_start` | Força de controle no início da amostragem (sigma alto). A influência da orientação da imagem começa nesse valor. (padrão: 1.0) | FLOAT | Sim | 0.0 - 10.0 |
| `strength_end` | Força de controle no final da amostragem (sigma baixo). É interpolada linearmente a partir do valor inicial. A influência da orientação da imagem termina nesse valor. (padrão: 1.0) | FLOAT | Sim | 0.0 - 10.0 |
| `restore_cfg` | Atrai a saída com ruído removido em direção ao latente de entrada. Quanto maior o valor, maior a fidelidade à entrada. Use 0 para desativar. (padrão: 4.0) | FLOAT | Sim | 0.0 - 20.0 |
| `restore_cfg_s_tmin` | Limiar de sigma abaixo do qual o `restore_cfg` é desativado. (padrão: 0.05) | FLOAT | Sim | 0.0 - 1.0 |

*Observação:* A entrada `image` é processada para extrair apenas os canais RGB. Se uma imagem com canal alfa for fornecida, o canal alfa será ignorado.

*Observação:* O `restore_cfg` só tem efeito quando definido com um valor maior que 0. Definir como 0 desativa completamente o pós-processamento de restauração. Quando ativo, a correção é aplicada somente enquanto o valor atual de sigma estiver acima de `restore_cfg_s_tmin`.

*Observação:* Este nó é marcado como experimental no ComfyUI.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `model` | O modelo de difusão com o patch do SUPIR aplicado e quaisquer funções adicionais de pós-CFG configuradas. | MODEL |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SUPIRApply/pt-BR.md)

---
**Source fingerprint (SHA-256):** `fa9f67f63777160863c44c620d8de11e92f79245c3f5b60e138975dfd0cc65c7`
