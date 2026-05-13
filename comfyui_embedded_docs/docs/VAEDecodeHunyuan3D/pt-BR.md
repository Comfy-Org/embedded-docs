> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VAEDecodeHunyuan3D/pt-BR.md)

O nó VAEDecodeHunyuan3D converte representações latentes em dados de voxel 3D usando um decodificador VAE. Ele processa as amostras latentes através do modelo VAE com configurações ajustáveis de divisão em partes e resolução para gerar dados volumétricos adequados para aplicações 3D.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Faixa | Descrição |
|-----------|--------------|-------------|-------|-----------|
| `samples` | LATENT | Sim | - | A representação latente a ser decodificada em dados de voxel 3D |
| `vae` | VAE | Sim | - | O modelo VAE usado para decodificar as amostras latentes |
| `num_chunks` | INT | Sim | 1000-500000 | O número de partes em que o processamento será dividido para gerenciamento de memória (padrão: 8000) |
| `octree_resolution` | INT | Sim | 16-512 | A resolução da estrutura octree usada para geração de voxel 3D (padrão: 256) |

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|---------------|--------------|-----------|
| `voxels` | VOXEL | Os dados de voxel 3D gerados a partir da representação latente decodificada |

---
**Source fingerprint (SHA-256):** `a53ad8e14a2ffca6278866753046d5959f057a4c3fdba5623b37545cee27d557`
