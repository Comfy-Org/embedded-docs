# Mesclar Splats

O nó Merge Splats combina múltiplos modelos de splat gaussiano em um único splat através da concatenação de seus dados. Isso é útil para mesclar várias decodificações do mesmo latente geradas com sementes diferentes, o que pode densificar a superfície e melhorar a qualidade ao criar malhas 3D.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
|-----------|-------------|-----------|----------|-------|
| `splat0` | Primeiro splat gaussiano a mesclar | SPLAT | Sim | Pelo menos 1 splat obrigatório |
| `splat1` | Segundo splat gaussiano a mesclar | SPLAT | Sim | Pelo menos 1 splat obrigatório |
| `splat2` | Splat gaussiano adicional a mesclar (opcional) | SPLAT | Não | Até 32 splats no total |
| `splat3` | Splat gaussiano adicional a mesclar (opcional) | SPLAT | Não | Até 32 splats no total |
| ... | Splats adicionais (até splat31) | SPLAT | Não | Até 32 splats no total |

**Nota:** A lista de entradas automaticamente cria novos campos à medida que você conecta splats. Você deve conectar pelo menos um splat. O nó aceita um mínimo de 2 e máximo de 32 splats.

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
|-------------|-------------|-----------|
| `splat` | O splat gaussiano mesclado contendo todos os splats de entrada concatenados | SPLAT |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MergeSplat/pt-BR.md)

---
**Source fingerprint (SHA-256):** `597671a3c37d1a4fb7b5a772396e08b7041b3fe8f04120891b1382d42e409d26`
