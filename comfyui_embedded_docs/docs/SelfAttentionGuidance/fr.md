> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SelfAttentionGuidance/fr.md)

Voici la traduction en français de la documentation du nœud Self-Attention Guidance :

Le nœud Self-Attention Guidance applique un guidage aux modèles de diffusion en modifiant le mécanisme d'attention pendant le processus d'échantillonnage. Il capture les scores d'attention des étapes de débruitage non conditionnées et les utilise pour créer des cartes de guidage floues qui influencent la sortie finale. Cette technique aide à guider le processus de génération en exploitant les propres schémas d'attention du modèle.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------------|--------|-------|-------------|
| `model` | MODEL | Oui | - | Le modèle de diffusion auquel appliquer le guidage par auto-attention |
| `scale` | FLOAT | Non | -2.0 à 5.0 | La force de l'effet de guidage par auto-attention (par défaut : 0.5) |
| `blur_sigma` | FLOAT | Non | 0.0 à 10.0 | La quantité de flou appliquée pour créer la carte de guidage (par défaut : 2.0) |

## Sorties

| Nom de la sortie | Type de données | Description |
|------------------|-----------------|-------------|
| `model` | MODEL | Le modèle modifié avec le guidage par auto-attention appliqué |

**Remarque :** Ce nœud est actuellement expérimental et présente des limitations avec les lots fragmentés. Il ne peut sauvegarder les scores d'attention que d'un seul appel UNet et peut ne pas fonctionner correctement avec des tailles de lots plus importantes.

---
**Source fingerprint (SHA-256):** `5f16ecd8f74bfd71073c6e3a65be08e54e4f5b9c56fe08deb48f35df381e82fa`
