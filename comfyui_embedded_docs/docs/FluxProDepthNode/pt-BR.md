Este nó gera imagens usando uma imagem de controle de profundidade como guia. Ele recebe uma imagem de controle e um prompt de texto, e então cria uma nova imagem que segue tanto as informações de profundidade da imagem de controle quanto a descrição no prompt. O nó se conecta a uma API externa para realizar o processo de geração de imagem.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `control_image` | A imagem de controle de profundidade usada para guiar a geração da imagem | IMAGE | Sim | - |
| `prompt` | Prompt para a geração da imagem (padrão: string vazia) | STRING | Não | - |
| `prompt_upsampling` | Se deve realizar upsampling no prompt. Se ativo, modifica automaticamente o prompt para uma geração mais criativa, mas os resultados são não determinísticos (a mesma semente não produzirá exatamente o mesmo resultado). (padrão: Falso) | BOOLEAN | Não | - |
| `skip_preprocessing` | Se deve pular o pré-processamento; defina como Verdadeiro se `control_image` já estiver com profundidade aplicada, Falso se for uma imagem bruta. (padrão: Falso) | BOOLEAN | Não | - |
| `guidance` | Força de orientação para o processo de geração da imagem (padrão: 15) | FLOAT | Não | 1-100 |
| `steps` | Número de etapas para o processo de geração da imagem (padrão: 50) | INT | Não | 15-50 |
| `seed` | A semente aleatória usada para criar o ruído. (padrão: 0) | INT | Não | 0-18446744073709551615 |

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `output_image` | A imagem gerada com base na imagem de controle de profundidade e no prompt | IMAGE |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FluxProDepthNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `34b80d7d63158b7dc4ad02da6b3a573b713d77efd0955d3477409f776f964462`
