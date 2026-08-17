# Carregar Modelo de Interpolação de Quadros

## Visão Geral

Este nó carrega um modelo de interpolação de quadros a partir de um arquivo e o prepara para uso no fluxo de trabalho. Ele detecta automaticamente o tipo de modelo (FILM ou RIFE) e o configura para desempenho ideal no seu hardware.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `model_name` | Selecione um modelo de interpolação de quadros para carregar. Os modelos devem ser colocados na pasta `frame_interpolation`. | COMBO | Sim | Lista de arquivos de modelo na pasta `frame_interpolation` |

Observação: Se o arquivo selecionado não for um modelo de interpolação de quadros FILM ou RIFE reconhecido, o nó gera um erro.

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `FRAME_INTERPOLATION_MODEL` | O modelo de interpolação de quadros carregado e configurado, pronto para uso em outros nós. | INTERP_MODEL |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FrameInterpolationModelLoader/pt-BR.md)

---
**Source fingerprint (SHA-256):** `21f470ee2852dbd1b332ac4a506eaa20dc8578c04b63c4fe1a072878b57beaba`
