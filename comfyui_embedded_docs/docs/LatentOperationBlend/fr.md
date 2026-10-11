# Latent Operation Blend

Ce nœud crée une opération sur latent qui mélange un latent vers un latent de référence, puis renvoie cette opération afin qu’elle puisse être branchée dans des nœuds tels que Latent Apply Operation ou Latent Apply Operation CFG. Lorsque la référence a une taille spatiale différente, elle est redimensionnée vers le latent cible avec une interpolation du plus proche voisin, et une référence dont le lot est plus petit est répétée pour correspondre à la taille de lot cible. Une valeur de `strength` de 0 laisse le latent inchangé. Ce nœud est marqué comme expérimental.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `reference` | Le latent vers lequel effectuer le mélange. Ses échantillons sont convertis vers le périphérique et le dtype du latent en cours de traitement, puis redimensionnés et répétés pour correspondre à celui-ci. | LATENT | Oui | - |
| `strength` | Jusqu’où effectuer le mélange vers la référence : 0 laisse le latent inchangé, 1 correspond au latent de référence redimensionné (par défaut : 1.0). | FLOAT | Oui | 0.0 à 1.0 (pas de 0.0001) |

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `operation` | Une opération de mélange pouvant être appliquée aux échantillons latents. | LATENT_OPERATION |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LatentOperationBlend/fr.md)

---
**Source fingerprint (SHA-256):** `5890089afddf83ddd4edd992606509b118aac9ef13eb89589f73fa75e0b9dd5a`
