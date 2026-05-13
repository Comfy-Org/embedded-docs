> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LumaVideoNode/fr.md)

Voici la traduction en français de la documentation du nœud LumaVideoNode :

Génère des vidéos de manière synchrone à partir d'une invite textuelle et de paramètres de sortie. Ce nœud crée du contenu vidéo en utilisant des descriptions textuelles et divers paramètres de génération, produisant la vidéo finale une fois le processus de génération terminé.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------------|--------|-------|-------------|
| `prompt` | STRING | Oui | - | Invite pour la génération vidéo (par défaut : chaîne vide). Doit comporter au moins 3 caractères. |
| `modèle` | COMBO | Oui | `"ray_1_6"`<br>`"ray_2"` | Le modèle de génération vidéo à utiliser. |
| `rapport d'aspect` | COMBO | Oui | `"16:9"`<br>`"9:16"`<br>`"1:1"`<br>`"4:3"`<br>`"3:4"`<br>`"21:9"`<br>`"9:21"` | Le rapport hauteur/largeur de la vidéo générée (par défaut : "16:9"). |
| `résolution` | COMBO | Oui | `"540p"`<br>`"720p"`<br>`"1080p"` | La résolution de sortie de la vidéo (par défaut : "540p"). Ce paramètre est ignoré lors de l'utilisation du modèle `ray_1_6`. |
| `durée` | COMBO | Oui | `"5s"`<br>`"9s"` | La durée de la vidéo générée. Ce paramètre est ignoré lors de l'utilisation du modèle `ray_1_6`. |
| `boucle` | BOOLEAN | Oui | - | Indique si la vidéo doit boucler (par défaut : False). |
| `graine` | INT | Oui | 0 à 18446744073709551615 | Graine pour déterminer si le nœud doit être réexécuté ; les résultats réels sont non déterministes quelle que soit la graine (par défaut : 0). |
| `luma_concepts` | CUSTOM | Non | - | Concepts de caméra optionnels pour dicter le mouvement de la caméra via le nœud Luma Concepts. |

**Remarque :** Lors de l'utilisation du modèle `ray_1_6`, les paramètres `duration` et `resolution` sont automatiquement ignorés et n'affectent pas la génération.

## Sorties

| Nom de sortie | Type de données | Description |
|---------------|-----------------|-------------|
| `output` | VIDEO | Le fichier vidéo généré. |

---
**Source fingerprint (SHA-256):** `44482bc91c3df2cc9ac22d06197668af45849e8bfde8bd435905f11f2593342c`
