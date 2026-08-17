# AudioLatentVide

Le nœud EmptyLatentAudio crée un tenseur latent vide pour le traitement audio. Il génère une représentation latente audio vierge avec une durée et une taille de lot spécifiées, qui peut être utilisée comme point de départ pour des flux de travail de génération ou de traitement audio. Le nœud calcule automatiquement les dimensions latentes appropriées en fonction de la durée audio et du taux d'échantillonnage.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `seconds` | La durée de l'audio en secondes (défaut : 47.6) | FLOAT | Oui | 1.0 - 1000.0 (pas de 0.1) |
| `batch_size` | Le nombre d'images latentes dans le lot (défaut : 1) | INT | Oui | 1 - 4096 |

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `LATENT` | Renvoie un tenseur latent vide pour le traitement audio avec la durée et la taille de lot spécifiées. Le tenseur a une forme de [batch_size, 64, length], où length est calculé à partir de la durée audio et du taux d'échantillonnage. La sortie inclut également des métadonnées indiquant que le type est « audio » et un rapport de sous-échantillonnage temporel de 2048. | LATENT |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyLatentAudio/fr.md)

---
**Source fingerprint (SHA-256):** `6ca63d26febe2d87ff751a57044eb81b553b19756f4b3f9478ecb5a733ec0041`
