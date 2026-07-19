# Carregar Modelo de Interpolação de Quadros

Esta documentação foi gerada por IA. Se você encontrar algum erro ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FrameInterpolationModelLoader/en.md)

## Visão Geral

Este nó carrega um modelo de interpolação de quadros a partir de um arquivo e o prepara para uso no fluxo de trabalho. Ele detecta automaticamente o tipo de modelo (FILM ou RIFE) e configura o modelo para desempenho ideal no seu hardware.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `model_name` | Selecione um modelo de interpolação de quadros para carregar. Os modelos devem ser colocados na pasta 'frame_interpolation'. | STRING | Sim | Lista de arquivos de modelo na pasta `frame_interpolation` |

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `FRAME_INTERPOLATION_MODEL` | O modelo de interpolação de quadros carregado e configurado, pronto para uso em outros nós. | MODEL |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FrameInterpolationModelLoader/pt-BR.md)

---
**Source fingerprint (SHA-256):** `497c20d5123bcbfd321dc4a659250ce3e0903e55c3a0274d3ed45710d75573d9`
