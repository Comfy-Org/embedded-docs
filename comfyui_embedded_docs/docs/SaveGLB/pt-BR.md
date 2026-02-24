> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveGLB/pt-BR.md)

O nó SaveGLB salva dados de malha 3D como arquivos GLB, que é um formato comum para modelos 3D. Ele recebe dados de malha como entrada e os exporta para o diretório de saída com o prefixo de nome de arquivo especificado. O nó pode salvar várias malhas se a entrada contiver múltiplos objetos de malha, e adiciona automaticamente metadados aos arquivos quando os metadados estão habilitados.

## Entradas

| Parâmetro | Tipo de Dados | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `mesh` | MESH | Sim | - | Os dados da malha 3D a serem salvos como um arquivo GLB |
| `filename_prefix` | STRING | Não | - | O prefixo para o nome do arquivo de saída (padrão: "mesh/ComfyUI") |

## Saídas

| Nome da Saída | Tipo de Dados | Descrição |
|-------------|-----------|-------------|
| `ui` | UI | Exibe os arquivos GLB salvos na interface do usuário com informações de nome de arquivo e subpasta |
