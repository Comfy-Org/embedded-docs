# PerturbedAttentionGuidance

Le nœud PerturbedAttentionGuidance applique un guidage par attention perturbée à un modèle de diffusion afin d'améliorer la qualité de génération. Il ajuste le processus de débruitage du modèle pendant l'échantillonnage en comparant la prédiction conditionnelle normale avec une prédiction effectuée à l'aide d'un mécanisme d'attention simplifié qui n'utilise que les projections de valeurs, puis ajoute la différence mise à l'échelle au résultat. Lorsque l'échelle est définie sur 0, le nœud n'a aucun effet.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `modèle` | Le modèle de diffusion auquel appliquer le guidage par attention perturbée | MODEL | Oui | - |
| `échelle` | La force de l'effet de guidage par attention perturbée (par défaut : 3.0). Lorsqu'elle est définie sur 0, le nœud n'a aucun effet et renvoie le résultat débruité d'origine. | FLOAT | Oui | 0.0 - 100.0 (step: 0.01) |

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `model` | Le modèle modifié auquel le guidage par attention perturbée a été appliqué | MODEL |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PerturbedAttentionGuidance/fr.md)

---
**Source fingerprint (SHA-256):** `1cf824486ae695a9e563c70a4798aaf4c9c067ae3b53172c9767e3c5093d0096`
