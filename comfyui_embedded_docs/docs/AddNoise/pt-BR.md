> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/AddNoise/pt-BR.md)

Este nó adiciona ruído controlado a uma imagem latente usando um gerador de ruído específico e valores sigma. Ele processa a entrada através do sistema de amostragem do modelo para aplicar a escala de ruído apropriada para o intervalo sigma fornecido, retornando uma nova representação latente com o ruído aplicado.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Faixa | Descrição |
|-----------|--------------|-------------|-------|-----------|
| `model` | MODEL | Sim | - | O modelo contendo parâmetros de amostragem e funções de processamento |
| `noise` | NOISE | Sim | - | O gerador de ruído que produz o padrão de ruído base |
| `sigmas` | SIGMAS | Sim | - | Valores sigma que controlam a intensidade da escala de ruído. Se vazio, o nó retorna a imagem latente original inalterada. Quando múltiplos sigmas são fornecidos, a escala de ruído é calculada como a diferença absoluta entre o primeiro e o último valor sigma. Quando apenas um sigma é fornecido, esse valor é usado diretamente como escala. |
| `latent_image` | LATENT | Sim | - | A representação latente de entrada à qual o ruído será adicionado. Imagens latentes vazias (contendo apenas zeros) não são deslocadas durante o processamento. |

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|---------------|--------------|-----------|
| `LATENT` | LATENT | A representação latente modificada com ruído adicionado. Quaisquer valores NaN ou infinitos na saída são convertidos para zeros para estabilidade. |

---
**Source fingerprint (SHA-256):** `8f387f95aeec2780d27bee5b954ad2c6cd6daa9242a1ea15697455b157bc80d5`
