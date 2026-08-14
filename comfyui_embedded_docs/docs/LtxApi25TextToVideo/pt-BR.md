# LtxApi25TextToVideo

LTX 2.5 Text To Video é um nó de API que gera vídeos de qualidade profissional a partir de uma descrição textual usando o modelo LTX 2.5. Você fornece um prompt e escolhe configurações de geração, como o nível do modelo, duração, resolução, taxa de quadros e se deseja incluir áudio; o nó envia a tarefa para a API LTX e retorna o vídeo resultante.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Intervalo |
|-----------|-------------|--------------|-------------|-----------|
| `model` | O nível do modelo LTX 2.5 a ser usado para a geração de vídeo. | STRING | Sim | "LTX-2.5 (Fast)"<br>"LTX-2.5 (Pro)" |
| `model.duration` | A duração do vídeo gerado. | INT | Sim | Inteiro |
| `model.resolution` | A resolução de saída do vídeo. As opções disponíveis dependem do `model` selecionado. | STRING | Sim | Com "LTX-2.5 (Fast)":<br>"1280x720"<br>"720x1280"<br>"1920x1080"<br>"1080x1920"<br>"2560x1440"<br>"1440x2560"<br>"3840x2160"<br>"2160x3840"<br>Com "LTX-2.5 (Pro)":<br>"1280x720"<br>"720x1280"<br>"1920x1080"<br>"1080x1920" |
| `model.fps` | Taxa de quadros do vídeo gerado (padrão: 25). | INT | Não | Inteiro |
| `model.generate_audio` | Se deve gerar áudio junto com o vídeo (padrão: True). | BOOLEAN | Não | True<br>False |
| `prompt` | A descrição textual do vídeo a ser gerado. É necessário um prompt não vazio de até 10.000 caracteres (padrão: ""). | STRING | Sim | 1 a 10.000 caracteres |
| `seed` | Valor da semente usado para geração reproduzível (padrão: 42). | INT | Não | Inteiro |

Nota: As opções disponíveis de `model.resolution` dependem do `model` selecionado. "LTX-2.5 (Fast)" suporta resoluções de até 2160x3840, enquanto "LTX-2.5 (Pro)" suporta resoluções de até 1920x1080.

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
|---------------|-------------|--------------|
| `video` | O vídeo gerado retornado pela API LTX, pronto para uso posterior no fluxo de trabalho. Se a geração de áudio estiver habilitada, o vídeo inclui áudio sincronizado. | VIDEO |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LtxApi25TextToVideo/pt-BR.md)

---
**Source fingerprint (SHA-256):** `02e131116fb0760cce2cea1e9bc49fa16dd7e4e296903fef5e44b7942b6e84c9`
