> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VAEDecodeHunyuan3D/pt-BR.md)

O nó VAEDecodeHunyuan3D converte representações latentes em dados de voxel 3D usando um decodificador VAE. Ele processa as amostras latentes através do modelo VAE com configurações de fragmentação e resolução ajustáveis para gerar dados volumétricos adequados para aplicações 3D.

## Entradas

| Parâmetro | Tipo de Dados | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `samples` | LATENT | Sim | - | A representação latente a ser decodificada em dados de voxel 3D |
| `vae` | VAE | Sim | - | O modelo VAE usado para decodificar as amostras latentes |
| `num_chunks` | INT | Sim | 1000-500000 | O número de fragmentos para dividir o processamento, visando o gerenciamento de memória (padrão: 8000) |
| `octree_resolution` | INT | Sim | 16-512 | A resolução da estrutura de octree usada para a geração de voxel 3D (padrão: 256) |

## Saídas

| Nome da Saída | Tipo de Dados | Descrição |
|-------------|-----------|-------------|
| `voxels` | VOXEL | Os dados de voxel 3D gerados a partir da representação latente decodificada |
