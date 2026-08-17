# Sampler AR Video

Le nœud Sampler AR Video fournit une méthode d'échantillonnage spécialisée pour les modèles vidéo autorégressifs, tels que ceux utilisant les techniques de forçage causal ou d'auto-forçage. Il gère tous les paramètres liés à la boucle autorégressive (AR) directement dans le flux de travail, ce qui facilite la configuration de la façon dont le modèle génère les images vidéo une étape à la fois.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `num_frame_per_block` | Images par bloc autorégressif. Une valeur de 1 signifie que le modèle génère une image à la fois (image par image), tandis qu'une valeur de 3 signifie qu'il génère trois images ensemble (par blocs). Ce paramètre doit correspondre au mode d'entraînement du point de contrôle. Défaut : 1. | INT | Oui | 1 to 64 |

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `SAMPLER` | Un objet échantillonneur configuré qui utilise la fonction d'échantillonnage « ar_video » avec les paramètres autorégressifs spécifiés. | SAMPLER |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerARVideo/fr.md)

---
**Source fingerprint (SHA-256):** `9ec72f52f5b77746f1587e64966bfa6cfd80ce8bb40a4fcb267f5197d09189fc`
