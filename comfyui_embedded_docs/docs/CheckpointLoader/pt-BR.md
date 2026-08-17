# Carregar Checkpoint com Configuração (OBSOLETO)

O nó CheckpointLoader carrega um checkpoint de modelo pré-treinado juntamente com seu arquivo de configuração. Ele recebe um arquivo de configuração e um arquivo de checkpoint como entradas e retorna os componentes do modelo carregado, incluindo o modelo principal, o modelo CLIP e o modelo VAE para uso no fluxo de trabalho.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `config_name` | O arquivo de configuração que define a arquitetura e as configurações do modelo | STRING | Sim | Arquivos de configuração disponíveis |
| `ckpt_name` | O arquivo de checkpoint que contém os pesos e parâmetros do modelo treinado | STRING | Sim | Arquivos de checkpoint disponíveis |

**Nota:** Este nó requer a seleção de um arquivo de configuração e de um arquivo de checkpoint. O arquivo de configuração deve corresponder à arquitetura do arquivo de checkpoint que está sendo carregado.

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `MODEL` | O componente principal do modelo carregado, pronto para inferência | MODEL |
| `CLIP` | O componente do modelo CLIP carregado, para codificação de texto | CLIP |
| `VAE` | O componente do modelo VAE carregado, para codificação e decodificação de imagens | VAE |

**Nota importante:** Este nó foi marcado como obsoleto e pode ser removido em versões futuras. Considere usar nós de carregamento alternativos para novos fluxos de trabalho.

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CheckpointLoader/pt-BR.md)

---
**Source fingerprint (SHA-256):** `820cd9f7a5ccd5a70d2b29906c8deca3632d2ccba84ca51022717e061afb72b3`
