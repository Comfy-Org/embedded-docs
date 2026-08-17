# PerturbedAttentionGuidance

Le nœud PerturbedAttentionGuidance applique une guidance par attention perturbée à un modèle de diffusion pour améliorer la qualité de génération. Il modifie le mécanisme d'auto-attention du modèle pendant l'échantillonnage en le remplaçant par une version simplifiée qui se concentre sur les projections de valeurs. Cette technique contribue à améliorer la cohérence et la qualité des images générées en ajustant le processus de débruitage conditionnel.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `model` | Le modèle de diffusion auquel appliquer la guidance par attention perturbée | MODEL | Oui | - |
| `scale` | La force de l'effet de guidance par attention perturbée (défaut : 3,0). Lorsqu'elle est définie sur 0, le nœud n'a aucun effet et renvoie le résultat débruité d'origine. | FLOAT | Oui | 0,0 - 100,0 |

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `model` | Le modèle modifié avec la guidance par attention perturbée appliquée | MODEL |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PerturbedAttentionGuidance/fr.md)

---
**Source fingerprint (SHA-256):** `1cf824486ae695a9e563c70a4798aaf4c9c067ae3b53172c9767e3c5093d0096`
