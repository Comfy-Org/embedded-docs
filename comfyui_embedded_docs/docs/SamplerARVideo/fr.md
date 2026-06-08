Voici la traduction de la documentation du nœud Sampler AR Video :

Le nœud Sampler AR Video fournit une méthode d'échantillonnage spécialisée pour les modèles vidéo autorégressifs, tels que ceux utilisant les techniques de Forçage Causal ou d'Auto-Forçage. Il gère tous les paramètres liés à la boucle autorégressive (AR) directement dans le workflow, ce qui facilite la configuration de la génération d'images vidéo par le modèle, une étape à la fois.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `nombre_d’images_par_bloc` | Images par bloc autorégressif. Une valeur de 1 signifie que le modèle génère une image à la fois (image par image), tandis qu'une valeur de 3 signifie qu'il génère trois images ensemble (par bloc). Ce paramètre doit correspondre au mode d'entraînement du point de contrôle. Valeur par défaut : 1. | INT | Oui | 1 à 64 |

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `SAMPLER` | Un objet échantillonneur configuré qui utilise la fonction d'échantillonnage "ar_video" avec les paramètres autorégressifs spécifiés. | SAMPLER |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerARVideo/fr.md)

---
**Source fingerprint (SHA-256):** `5b735f98fdde074ee9483503fee0e2322d510aed846336b382a8ea89a363c9e4`
