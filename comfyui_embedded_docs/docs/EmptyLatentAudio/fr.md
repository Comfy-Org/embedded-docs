Le nœud EmptyLatentAudio crée un tenseur latent vide pour le traitement audio. Il génère une représentation audio latente vierge avec une durée et une taille de lot spécifiées, pouvant servir de point de départ pour des workflows de génération ou de traitement audio. Le nœud calcule automatiquement les dimensions latentes appropriées en fonction de la durée audio et du taux d'échantillonnage.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `secondes` | La durée de l'audio en secondes (par défaut : 47,6) | FLOAT | Oui | 1,0 - 1000,0 |
| `taille_du_lot` | Le nombre d'images latentes dans le lot (par défaut : 1) | INT | Oui | 1 - 4096 |

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `LATENT` | Renvoie un tenseur latent vide pour le traitement audio avec la durée et la taille de lot spécifiées. Le tenseur a une forme de [batch_size, 64, length], où length est calculé à partir de la durée audio et du taux d'échantillonnage. | LATENT |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyLatentAudio/fr.md)

---
**Source fingerprint (SHA-256):** `004f730131b179fe5ac072afe81b2e01a3937fceca5a260b4ae66f92774e96d9`
