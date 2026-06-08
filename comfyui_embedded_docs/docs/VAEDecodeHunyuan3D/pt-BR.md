O nó VAEDecodeHunyuan3D converte representações latentes em dados de voxel 3D usando um decodificador VAE. Ele processa as amostras latentes através do modelo VAE com configurações ajustáveis de divisão em partes e resolução para gerar dados volumétricos adequados para aplicações 3D.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `amostras` | A representação latente a ser decodificada em dados de voxel 3D | LATENT | Sim | - |
| `vae` | O modelo VAE usado para decodificar as amostras latentes | VAE | Sim | - |
| `num_chunks` | O número de partes em que o processamento será dividido para gerenciamento de memória (padrão: 8000) | INT | Sim | 1000-500000 |
| `octree_resolution` | A resolução da estrutura octree usada para geração de voxel 3D (padrão: 256) | INT | Sim | 16-512 |

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `voxels` | Os dados de voxel 3D gerados a partir da representação latente decodificada | VOXEL |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VAEDecodeHunyuan3D/pt-BR.md)

---
**Source fingerprint (SHA-256):** `a53ad8e14a2ffca6278866753046d5959f057a4c3fdba5623b37545cee27d557`
