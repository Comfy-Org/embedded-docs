# SamplerEulerAncestral

Le nœud SamplerEulerAncestral crée un échantillonneur Euler Ancestral pour générer des images. Cet échantillonneur utilise une approche mathématique spécifique qui combine l'intégration d'Euler avec des techniques d'échantillonnage ancestral pour produire des variations d'images. Le nœud vous permet de configurer le comportement d'échantillonnage en ajustant des paramètres qui contrôlent le caractère aléatoire et la taille de pas pendant le processus de génération.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `eta` | Contrôle la taille de pas et la stochasticité du processus d'échantillonnage (défaut : 1.0). Ceci est un paramètre avancé. | FLOAT | Oui | 0.0 - 100.0 |
| `s_bruit` | Contrôle la quantité de bruit ajoutée lors de l'échantillonnage (défaut : 1.0). Ceci est un paramètre avancé. | FLOAT | Oui | 0.0 - 100.0 |

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `sampler` | Renvoie un échantillonneur Euler Ancestral configuré qui peut être utilisé dans le pipeline d'échantillonnage. | SAMPLER |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerEulerAncestral/fr.md)

---
**Source fingerprint (SHA-256):** `0d3c1f0ffe01eb6cc17fd53e743713f659218ec19001c670440472ae7d0d3887`
