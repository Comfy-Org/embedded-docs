# VAEDecodeHunyuan3D

O nó VAEDecodeHunyuan3D converte representações latentes em dados de voxels 3D usando um decodificador VAE. Ele processa as amostras latentes através do modelo VAE com configurações ajustáveis de divisão em blocos (chunking) e resolução para gerar dados volumétricos adequados para aplicações 3D.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `amostras` | A representação latente a ser decodificada em dados de voxels 3D | LATENT | Sim | - |
| `vae` | O modelo VAE usado para decodificar as amostras latentes | VAE | Sim | - |
| `num_chunks` | O número de blocos em que o processamento é dividido para gerenciamento de memória. Parâmetro avançado (padrão: 8000) | INT | Sim | 1000-500000 |
| `octree_resolution` | A resolução da estrutura octree usada para geração de voxels 3D. Parâmetro avançado (padrão: 256) | INT | Sim | 16-512 |

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `voxels` | Os dados de voxels 3D gerados a partir da representação latente decodificada | VOXEL |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VAEDecodeHunyuan3D/pt-BR.md)

---
**Source fingerprint (SHA-256):** `740e328e9e7817aa1a029c5fadddf5457c91bbb5ac12c7e8af2cd81bee6184a7`
