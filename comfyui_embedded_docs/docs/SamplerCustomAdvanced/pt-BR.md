O nó SamplerCustomAdvanced realiza amostragem avançada no espaço latente usando configurações personalizadas de ruído, orientação e amostragem. Ele processa uma imagem latente por meio de um processo de amostragem guiada com geração de ruído personalizável e agendamentos sigma, produzindo tanto a saída final amostrada quanto uma versão com redução de ruído, quando disponível.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `ruído` | O gerador de ruído que fornece o padrão de ruído inicial e a semente para o processo de amostragem | NOISE | Sim | - |
| `guia` | O modelo de orientação que direciona o processo de amostragem para as saídas desejadas | GUIDER | Sim | - |
| `amostrador` | O algoritmo de amostragem que define como o espaço latente é percorrido durante a geração | SAMPLER | Sim | - |
| `sigmas` | O agendamento sigma que controla os níveis de ruído ao longo das etapas de amostragem | SIGMAS | Sim | - |
| `imagem_latente` | A representação latente inicial que serve como ponto de partida para a amostragem | LATENT | Sim | - |

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `output` | A representação latente final amostrada após concluir o processo de amostragem | LATENT |
| `denoised_output` | Uma versão com redução de ruído da saída, quando disponível; caso contrário, retorna o mesmo que a saída | LATENT |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerCustomAdvanced/pt-BR.md)

---
**Source fingerprint (SHA-256):** `bf711ecc0684ad04babe5c63a246195f358204d203e836587a90feff742929a3`
