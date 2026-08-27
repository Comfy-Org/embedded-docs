# ChargerLatent

Le nœud LoadLatent charge des représentations latentes précédemment enregistrées à partir de fichiers .latent situés dans le répertoire d’entrée. Il lit les données du tenseur latent depuis le fichier sélectionné et applique les ajustements d’échelle nécessaires avant de renvoyer les données latentes pour une utilisation dans d’autres nœuds.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `latent` | Sélectionne le fichier .latent à charger parmi les fichiers disponibles dans le répertoire d’entrée | COMBO | Oui | Tous les fichiers .latent du répertoire d’entrée (liste dynamique, triés par ordre alphabétique) |

Remarque : La liste des fichiers disponibles est générée dynamiquement et ne comprend que les fichiers se terminant par .latent présents dans le répertoire d’entrée. Si le fichier sélectionné n’existe plus, le nœud le signale comme un fichier latent invalide.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `LATENT` | Renvoie les données de représentation latente chargées à partir du fichier sélectionné sous forme de tenseur flottant. Si le fichier ne contient pas le marqueur `latent_format_version_0`, le tenseur est mis à l’échelle par 1/0.18215 avant d’être renvoyé ; les fichiers contenant ce marqueur sont renvoyés à leur échelle stockée. | LATENT |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoadLatent/fr.md)

---
**Source fingerprint (SHA-256):** `0938214361687a3a98e03878b8cbc0240100cbeacc0b157c4a299e59e7728a13`
