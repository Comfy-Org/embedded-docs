# PerturbedAttentionGuidance

Le nœud PerturbedAttentionGuidance applique un guidage d'attention perturbé à un modèle de diffusion afin d'améliorer la qualité de génération. Pendant l'échantillonnage, il effectue une prédiction supplémentaire dans laquelle l'auto-attention du bloc intermédiaire est remplacée par une version simplifiée qui transmet directement les projections de valeur, puis ajoute la différence mise à l'échelle entre la prédiction conditionnelle normale et cette prédiction perturbée au résultat débruité. Définir `scale` sur 0 désactive entièrement l'effet.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `model` | Le modèle de diffusion auquel appliquer le guidage d'attention perturbé | MODEL | Oui | - |
| `scale` | La force de l'effet de guidage d'attention perturbé (par défaut : 3.0). Lorsque cette valeur est définie sur 0, le nœud n'a aucun effet et renvoie le résultat débruité d'origine inchangé. | FLOAT | Oui | 0.0 - 100.0 (pas : 0.01) |

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `model` | Le modèle modifié avec le patch de guidage d'attention perturbé attaché à son processus d'échantillonnage | MODEL |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PerturbedAttentionGuidance/fr.md)

---
**Source fingerprint (SHA-256):** `1cf824486ae695a9e563c70a4798aaf4c9c067ae3b53172c9767e3c5093d0096`
