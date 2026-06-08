Esta documentação foi gerada por IA. Se você encontrar algum erro ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MoonvalleyVideo2VideoNode/en.md)

O nó Moonvalley Marey Video to Video transforma um vídeo de entrada em um novo vídeo com base em uma descrição textual. Ele utiliza a API Moonvalley para gerar vídeos que correspondam ao seu prompt, preservando características de movimento ou pose do vídeo original. Você pode controlar o estilo e o conteúdo do vídeo de saída por meio de prompts de texto e vários parâmetros de geração.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `prompt` | Descreve o vídeo a ser gerado (entrada multilinha) | STRING | Sim | - |
| `negative_prompt` | Texto do prompt negativo (padrão: lista extensa de descritores negativos) | STRING | Não | - |
| `seed` | Valor da semente aleatória (padrão: 9) | INT | Sim | 0 a 4294967295 |
| `video` | O vídeo de referência usado para gerar o vídeo de saída. Deve ter pelo menos 5 segundos de duração. Vídeos com mais de 5s serão automaticamente cortados. Apenas o formato MP4 é suportado. | VIDEO | Sim | - |
| `control_type` | Seleção do tipo de controle (padrão: "Motion Transfer") | COMBO | Não | "Motion Transfer"<br>"Pose Transfer" |
| `motion_intensity` | Usado apenas se `control_type` for "Motion Transfer" (padrão: 100) | INT | Não | 0 a 100 |
| `steps` | Número de etapas de inferência (padrão: 33) | INT | Sim | 1 a 100 |

**Nota:** O parâmetro `motion_intensity` é aplicado apenas quando `control_type` está definido como "Motion Transfer". Ao usar "Pose Transfer", este parâmetro é ignorado.

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `output` | O vídeo gerado como saída | VIDEO |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MoonvalleyVideo2VideoNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `8202a4be469afa16d77b9e0287c290b9c3f390347fc60f23878f50fd95a758e0`
