> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerCustomAdvanced/pt-BR.md)

O nó SamplerCustomAdvanced realiza amostragem avançada no espaço latente utilizando configurações personalizadas de ruído, orientação e amostragem. Ele processa uma imagem latente por meio de um processo de amostragem guiada com geração de ruído e cronogramas de sigma personalizáveis, produzindo tanto a saída amostrada final quanto uma versão com ruído removido, quando disponível.

## Entradas

| Parâmetro | Tipo de Dados | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `noise` | NOISE | Sim | - | O gerador de ruído que fornece o padrão de ruído inicial e a semente para o processo de amostragem |
| `guider` | GUIDER | Sim | - | O modelo de orientação que direciona o processo de amostragem para as saídas desejadas |
| `sampler` | SAMPLER | Sim | - | O algoritmo de amostragem que define como o espaço latente é percorrido durante a geração |
| `sigmas` | SIGMAS | Sim | - | O cronograma de sigma que controla os níveis de ruído ao longo das etapas de amostragem |
| `latent_image` | LATENT | Sim | - | A representação latente inicial que serve como ponto de partida para a amostragem |

## Saídas

| Nome da Saída | Tipo de Dados | Descrição |
|-------------|-----------|-------------|
| `output` | LATENT | A representação latente final amostrada após a conclusão do processo de amostragem |
| `denoised_output` | LATENT | Uma versão com ruído removido da saída, quando disponível; caso contrário, retorna o mesmo que a saída |
