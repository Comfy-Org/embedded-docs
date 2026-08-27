# SamplerCustomAdvanced

O nó SamplerCustomAdvanced realiza amostragem avançada no espaço latente usando configurações personalizadas de ruído, orientação e amostragem. Ele processa uma imagem latente por meio de um processo de amostragem guiado com geração de ruído personalizável e agendamentos de sigma, produzindo tanto a saída amostrada final quanto uma versão com ruído removido (denoised) quando disponível.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `ruído` | O gerador de ruído que fornece o padrão de ruído inicial e a semente para o processo de amostragem | NOISE | Sim | - |
| `guia` | O modelo de orientação que direciona o processo de amostragem para as saídas desejadas | GUIDER | Sim | - |
| `amostrador` | O algoritmo de amostragem que define como o espaço latente é percorrido durante a geração | SAMPLER | Sim | - |
| `sigmas` | O agendamento de sigma que controla os níveis de ruído ao longo das etapas de amostragem | SIGMAS | Sim | - |
| `imagem_latente` | A representação latente inicial que serve como ponto de partida para a amostragem. Suporta `noise_mask` opcional para remoção seletiva de ruído e chaves opcionais `downscale_ratio_spacial` e `downscale_ratio_temporal` para manipulação avançada de latentes | LATENT | Sim | - |

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `saída` | A representação latente amostrada final após concluir o processo de amostragem. Quaisquer chaves `downscale_ratio_spacial` ou `downscale_ratio_temporal` do latente de entrada são removidas desta saída | LATENT |
| `saída_denoisada` | Uma versão com ruído removido da saída quando o processo de amostragem produz uma predição limpa intermediária (x0); caso contrário, retorna o mesmo que a saída. Quando disponível, representa a melhor estimativa do modelo do latente limpo em cada etapa | LATENT |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerCustomAdvanced/pt-BR.md)

---
**Source fingerprint (SHA-256):** `23cffad0f7cf74dcd494c2828b2116bb4d00a1e55e42ded074b587ac20183290`
