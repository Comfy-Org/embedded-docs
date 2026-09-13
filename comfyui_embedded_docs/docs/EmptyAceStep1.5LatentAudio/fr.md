# EmptyAceStep1.5LatentAudio

Le nœud Empty Ace Step 1.5 Latent Audio crée un tenseur latent audio vide (silencieux) pour les flux de travail de génération audio. Il construit un latent à 64 canaux dont la longueur temporelle est calculée à partir de la durée demandée, et le marque comme données audio pour utilisation par les nœuds audio en aval.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `seconds` | La durée de l'audio à générer, en secondes (par défaut : 120.0). La longueur du latent est calculée comme `seconds * 48000 / 1920`, arrondie à l'entier le plus proche. | FLOAT | Oui | 1.0 - 1000.0 (pas : 0.01) |
| `batch_size` | Le nombre d'images latentes dans le lot (par défaut : 1). | INT | Oui | 1 - 4096 |

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `LATENT` | Un tenseur latent vide représentant un audio silencieux. Le tenseur a pour forme [batch_size, 64, length], où length est dérivé de `seconds`. La sortie inclut également un identifiant de type `"audio"` et une valeur `downscale_ratio_temporal` de 1764, qui est utilisée pour le sous-échantillonnage temporel dans le traitement audio. | LATENT |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyAceStep1.5LatentAudio/fr.md)

---
**Source fingerprint (SHA-256):** `bb7120c91ce5d779147cb8553d6f96fa160d87468d4d87550fb6dd4ec89b1557`
