# ChargerLatent

Le nœud LoadLatent charge des représentations latentes qui ont été précédemment sauvegardées sous forme de fichiers .latent dans le répertoire d’entrée. Il lit les données du tenseur latent à partir du fichier sélectionné et applique les ajustements d’échelle nécessaires avant de renvoyer les résultats pour utilisation dans d’autres nœuds.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `latent` | Sélectionne le fichier .latent à charger parmi les fichiers disponibles dans le répertoire d’entrée. | COMBO | Oui | Tous les fichiers .latent dans le répertoire d’entrée |

Remarque : Pour les fichiers .latent qui ne contiennent pas le marqueur `latent_format_version_0`, le tenseur latent chargé est multiplié par 1/0.18215 afin que son échelle corresponde au format attendu par les autres nœuds.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `LATENT` | Renvoie les données de représentation latente chargées à partir du fichier sélectionné. | LATENT |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoadLatent/fr.md)

---
**Source fingerprint (SHA-256):** `0938214361687a3a98e03878b8cbc0240100cbeacc0b157c4a299e59e7728a13`
