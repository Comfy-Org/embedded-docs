Le nœud LoadLatent charge des représentations latentes préalablement sauvegardées à partir de fichiers .latent dans le répertoire d’entrée. Il lit les données du tenseur latent depuis le fichier et applique les ajustements d’échelle nécessaires avant de renvoyer les données latentes pour une utilisation dans d’autres nœuds.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `latent` | Sélectionne le fichier .latent à charger parmi les fichiers disponibles dans le répertoire d’entrée | STRING | Oui | Tous les fichiers .latent dans le répertoire d’entrée |

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `LATENT` | Renvoie les données de représentation latente chargées depuis le fichier sélectionné | LATENT |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoadLatent/fr.md)

---
**Source fingerprint (SHA-256):** `020185a6066263b75b2417411f07af54d31a2a3a056d650eacfff188dc2cb87e`
