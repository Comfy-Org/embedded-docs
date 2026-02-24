> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CheckpointLoader/pt-BR.md)

O nó CheckpointLoader carrega um checkpoint de modelo pré-treinado juntamente com seu arquivo de configuração. Ele recebe um arquivo de configuração e um arquivo de checkpoint como entradas e retorna os componentes do modelo carregados, incluindo o modelo principal, o modelo CLIP e o modelo VAE, para uso no fluxo de trabalho.

## Entradas

| Parâmetro | Tipo de Dados | Tipo de Entrada | Padrão | Intervalo | Descrição |
|-----------|-----------|------------|---------|-------|-------------|
| `config_name` | STRING | COMBO | - | Arquivos de configuração disponíveis | O arquivo de configuração que define a arquitetura e as configurações do modelo |
| `ckpt_name` | STRING | COMBO | - | Arquivos de checkpoint disponíveis | O arquivo de checkpoint contendo os pesos e parâmetros treinados do modelo |

**Observação:** Este nó requer que tanto um arquivo de configuração quanto um arquivo de checkpoint sejam selecionados. O arquivo de configuração deve corresponder à arquitetura do arquivo de checkpoint que está sendo carregado.

## Saídas

| Nome da Saída | Tipo de Dados | Descrição |
|-------------|-----------|-------------|
| `MODEL` | MODEL | O componente do modelo principal carregado, pronto para inferência |
| `CLIP` | CLIP | O componente do modelo CLIP carregado para codificação de texto |
| `VAE` | VAE | O componente do modelo VAE carregado para codificação e decodificação de imagem |

**Nota Importante:** Este nó foi marcado como obsoleto e pode ser removido em versões futuras. Considere usar nós de carregamento alternativos para novos fluxos de trabalho.
