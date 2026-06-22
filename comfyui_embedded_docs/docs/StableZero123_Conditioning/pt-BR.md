# StableZero123_Conditioning

O nó **StableZero123_Conditioning** processa uma imagem de entrada e ângulos de câmera para gerar dados de condicionamento e representações latentes para geração de modelos 3D. Ele utiliza um modelo de visão CLIP para codificar as características da imagem, combina essas características com informações de incorporação da câmera baseadas nos ângulos de elevação e azimute, e produz condicionamentos positivo e negativo, juntamente com uma representação latente para tarefas de geração 3D subsequentes.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `clip_vision` | O modelo de visão CLIP usado para codificar as características da imagem | CLIP_VISION | Sim | - |
| `imagem_inicial` | A imagem de entrada a ser processada e codificada | IMAGE | Sim | - |
| `vae` | O modelo VAE usado para codificar pixels no espaço latente | VAE | Sim | - |
| `largura` | Largura de saída para a representação latente (padrão: 256, deve ser divisível por 8) | INT | Sim | 16 a MAX_RESOLUTION |
| `altura` | Altura de saída para a representação latente (padrão: 256, deve ser divisível por 8) | INT | Sim | 16 a MAX_RESOLUTION |
| `tamanho_do_lote` | Número de amostras a serem geradas no lote (padrão: 1) | INT | Sim | 1 a 4096 |
| `elevação` | Ângulo de elevação da câmera em graus (padrão: 0.0) | FLOAT | Sim | -180.0 a 180.0 |
| `azimute` | Ângulo de azimute da câmera em graus (padrão: 0.0) | FLOAT | Sim | -180.0 a 180.0 |

**Observação:** Os parâmetros `width` e `height` devem ser divisíveis por 8, pois o nó os divide automaticamente por 8 para criar as dimensões da representação latente.

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `positive` | Dados de condicionamento positivo combinando características da imagem e incorporações da câmera | CONDITIONING |
| `negative` | Dados de condicionamento negativo com características inicializadas como zero | CONDITIONING |
| `latent` | Representação latente com dimensões [batch_size, 4, height//8, width//8] | LATENT |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StableZero123_Conditioning/pt-BR.md)

---
**Source fingerprint (SHA-256):** `a9d6619c800119c9a619665f322d49ded1478ceb40df56ca5707b31242cb0e47`
