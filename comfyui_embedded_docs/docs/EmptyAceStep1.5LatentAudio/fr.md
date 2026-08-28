# EmptyAceStep1.5LatentAudio

Le nœud Empty Ace Step 1.5 Latent Audio crée un tenseur latent vide conçu pour le traitement audio. Il génère un latent audio silencieux d'une durée et d'une taille de lot spécifiées, pouvant servir de point de départ pour des flux de travail de génération audio dans ComfyUI. Le nœud calcule la longueur du latent en fonction des secondes saisies et d'un taux d'échantillonnage fixe.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `seconds` | La durée de l'audio à générer, en secondes (défaut : 120.0). | FLOAT | Oui | 1.0 - 1000.0 |
| `batch_size` | Le nombre d'images latentes dans le lot (défaut : 1). | INT | Oui | 1 - 4096 |

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `LATENT` | Un tenseur latent vide représentant un audio silencieux, avec un identifiant de type « audio ». La sortie inclut également une valeur `downscale_ratio_temporal` de 1764, utilisée pour la réduction d'échelle temporelle dans le traitement audio. | LATENT |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyAceStep1.5LatentAudio/fr.md)

---
**Source fingerprint (SHA-256):** `bb7120c91ce5d779147cb8553d6f96fa160d87468d4d87550fb6dd4ec89b1557`
