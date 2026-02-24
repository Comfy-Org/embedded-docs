> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyLatentHunyuan3Dv2/pt-BR.md)

O nó EmptyLatentHunyuan3Dv2 cria tensores latentes vazios especificamente formatados para os modelos de geração 3D Hunyuan3Dv2. Ele gera espaços latentes vazios com as dimensões e a estrutura corretas exigidas pela arquitetura Hunyuan3Dv2, permitindo que você inicie fluxos de trabalho de geração 3D do zero. O nó produz tensores latentes preenchidos com zeros que servem como base para os processos subsequentes de geração 3D.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `resolution` | INT | Sim | 1 - 8192 | A dimensão de resolução para o espaço latente (padrão: 3072) |
| `batch_size` | INT | Sim | 1 - 4096 | O número de imagens latentes no lote (padrão: 1) |

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|-------------|-----------|-------------|
| `LATENT` | LATENT | Retorna um tensor latente contendo amostras vazias formatadas para a geração 3D Hunyuan3Dv2 |
