# AddNoise

Este nó adiciona ruído controlado a uma imagem latente usando um gerador de ruído especificado e valores de sigma. Ele processa a entrada por meio do sistema de amostragem do modelo para aplicar uma escala de ruído adequada ao intervalo de sigma fornecido, retornando uma nova representação latente com o ruído aplicado. Este nó está atualmente marcado como experimental.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `model` | O modelo que contém os parâmetros de amostragem e as funções de processamento | MODEL | Sim | - |
| `ruído` | O gerador de ruído que produz o padrão de ruído base | NOISE | Sim | - |
| `sigmas` | Valores de sigma que controlam a intensidade da escala de ruído. Se vazio, o nó retorna a imagem latente original inalterada. Quando vários sigmas são fornecidos, a escala de ruído é calculada como a diferença absoluta entre o primeiro e o último valor de sigma. Quando apenas um sigma é fornecido, esse valor é usado diretamente como escala. | SIGMAS | Sim | - |
| `imagem_latente` | A representação latente de entrada à qual o ruído será adicionado. Imagens latentes vazias (contendo apenas zeros) não são deslocadas durante o processamento. | LATENT | Sim | - |

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `LATENT` | A representação latente modificada com ruído adicionado. Quaisquer valores NaN ou infinitos na saída são convertidos em zeros para estabilidade. | LATENT |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/AddNoise/pt-BR.md)

---
**Source fingerprint (SHA-256):** `6b11db10af9a2b8ea24dbf3b40c08d7e37de39df746e3966e5bfc94b84dee068`
