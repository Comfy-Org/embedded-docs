> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageBlur/pt-BR.md)

O nó `ImageBlur` aplica um desfoque Gaussiano a uma imagem, permitindo o suavização de bordas e a redução de detalhes e ruído. Ele oferece controle sobre a intensidade e a dispersão do desfoque por meio de parâmetros.

## Entradas

| Campo          | Tipo de Dados | Descrição                                                                   |
|----------------|---------------|-----------------------------------------------------------------------------|
| `image`        | `IMAGE`       | A imagem de entrada a ser desfocada. Este é o alvo principal para o efeito de desfoque. |
| `blur_radius`  | `INT`         | Determina o raio do efeito de desfoque. Um raio maior resulta em um desfoque mais pronunciado. |
| `sigma`        | `FLOAT`       | Controla a dispersão do desfoque. Um valor de sigma mais alto significa que o desfoque afetará uma área mais ampla ao redor de cada pixel. |

## Saídas

| Campo  | Tipo de Dados | Descrição                                                              |
|--------|---------------|------------------------------------------------------------------------|
| `image`| `IMAGE`       | A saída é a versão desfocada da imagem de entrada, com o grau de desfoque determinado pelos parâmetros de entrada. |
