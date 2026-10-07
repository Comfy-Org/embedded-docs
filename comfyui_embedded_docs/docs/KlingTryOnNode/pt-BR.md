# Kling Virtual Try-On

Vista uma pessoa com uma peça de roupa usando o provador virtual da Kling. Conecte uma foto de uma pessoa e uma foto da peça de vestuário, e o nó retorna uma nova imagem dessa pessoa vestindo a peça.

## Entradas

| Parâmetro | Descrição | Tipo de dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `person_image` | Foto de uma pessoa, idealmente de frente ou em visão de três quartos. Imagens com um lado superior a 2048 pixels são reduzidas primeiro. | IMAGE | Sim | N/A |
| `garment_image` | A peça de roupa a ser colocada: foto de produto, foto planificada (flat lay), manequim ou foto em modelo. Uma foto em modelo pode trazer o restante desse look. Somente roupas; sapatos, bolsas e acessórios não são suportados. | IMAGE | Sim | N/A |
| `keep_pose` | Desative para permitir que a pose mude para uma melhor apresentação do look. Parâmetro avançado (padrão: True). | BOOLEAN | Sim | `True`<br>`False` |
| `seed` | A seed controla se o nó deve ser executado novamente; os resultados são não determinísticos independentemente da seed. Este parâmetro tem a funcionalidade de controle após a geração (padrão: 42). | INT | Sim | 0 a 2147483647 |

**Observação:** O resultado tem o mesmo tamanho que a `person_image`, limitado a 2048 pixels no lado mais longo. Ambas as entradas são enviadas para a API da Kling, o que pode levar um momento.

## Saídas

| Nome da saída | Descrição | Tipo de dados |
|-------------|-------------|-----------|
| `IMAGE` | A pessoa vestindo a peça de roupa. | IMAGE |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingTryOnNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `03c2f9f1169ec2de3dd58162f9a7718a9c1f9af584aa63f280a0c4feefb70478`
