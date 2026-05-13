> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerEulerAncestral/fr.md)

Le nœud SamplerEulerAncestral crée un échantillonneur Euler Ancestral pour la génération d'images. Cet échantillonneur utilise une approche mathématique spécifique combinant l'intégration d'Euler avec des techniques d'échantillonnage ancestrales pour produire des variations d'images. Le nœud permet de configurer le comportement d'échantillonnage en ajustant des paramètres qui contrôlent l'aléatoire et la taille des pas pendant le processus de génération.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------------|--------|-------|-------------|
| `eta` | FLOAT | Non | 0.0 - 100.0 | Contrôle la taille du pas et la stochasticité du processus d'échantillonnage (valeur par défaut : 1.0). Il s'agit d'un paramètre avancé. |
| `s_bruit` | FLOAT | Non | 0.0 - 100.0 | Contrôle la quantité de bruit ajoutée lors de l'échantillonnage (valeur par défaut : 1.0). Il s'agit d'un paramètre avancé. |

## Sorties

| Nom de sortie | Type de données | Description |
|---------------|-----------------|-------------|
| `sampler` | SAMPLER | Renvoie un échantillonneur Euler Ancestral configuré pouvant être utilisé dans le pipeline d'échantillonnage. |

---
**Source fingerprint (SHA-256):** `4d167de55f003383ccbb4a53daa14496bd931589781d56b62bf282a811669670`
