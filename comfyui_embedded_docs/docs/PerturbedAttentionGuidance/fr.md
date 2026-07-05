# PerturbedAttentionGuidance

Le nœud PerturbedAttentionGuidance applique un guidage par attention perturbée à un modèle de diffusion afin d'améliorer la qualité de génération. Il modifie le mécanisme d'auto-attention du modèle pendant l'échantillonnage en le remplaçant par une version simplifiée qui se concentre sur les projections de valeurs. Cette technique contribue à améliorer la cohérence et la qualité des images générées en ajustant le processus de débruitage conditionnel.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `modèle` | Le modèle de diffusion auquel appliquer le guidage par attention perturbée | MODEL | Oui | - |
| `échelle` | L'intensité de l'effet de guidage par attention perturbée (par défaut : 3,0). Lorsqu'elle est définie sur 0, le nœud n'a aucun effet et renvoie le résultat de débruitage d'origine. | FLOAT | Non | 0,0 - 100,0 |


| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `model` | Le modèle modifié avec le guidage par attention perturbée appliqué | MODEL |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PerturbedAttentionGuidance/fr.md)

---
**Source fingerprint (SHA-256):** `8808aa3a3f7cfe306e17f8f4424779cb8e4565647bbcc9d4907da2215affe191`
