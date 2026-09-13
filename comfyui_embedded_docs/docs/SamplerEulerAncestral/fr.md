# SamplerEulerAncestral

Le nœud SamplerEulerAncestral crée un échantillonneur Euler Ancestral qui peut être utilisé lors de la génération d'images. Cet échantillonneur combine l'intégration d'Euler avec l'échantillonnage ancestral, ce qui ajoute un certain degré d'aléatoire à chaque étape afin de produire des résultats variés. Le nœud vous permet d'ajuster la quantité d'aléatoire appliquée via ses paramètres.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `eta` | Contrôle la taille du pas et le caractère stochastique du processus d'échantillonnage (par défaut : 1.0). Il s'agit d'un paramètre avancé. | FLOAT | Oui | 0.0 - 100.0 |
| `s_noise` | Contrôle la quantité de bruit ajoutée pendant l'échantillonnage (par défaut : 1.0). Il s'agit d'un paramètre avancé. | FLOAT | Oui | 0.0 - 100.0 |

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `sampler` | Retourne un échantillonneur Euler Ancestral configuré pouvant être utilisé dans le pipeline d'échantillonnage. | SAMPLER |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerEulerAncestral/fr.md)

---
**Source fingerprint (SHA-256):** `0d3c1f0ffe01eb6cc17fd53e743713f659218ec19001c670440472ae7d0d3887`
