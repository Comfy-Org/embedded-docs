Voici la traduction en français de la documentation du nœud LumaImageToVideoNode :

Génère des vidéos de manière synchrone à partir d'une invite textuelle et d'images de début/fin optionnelles. Ce nœud utilise l'API Luma pour créer des vidéos, vous permettant de définir le contenu de la vidéo via une invite et de spécifier éventuellement la première et/ou la dernière image pour contrôler la structure de la vidéo.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `prompt` | Invite pour la génération vidéo (par défaut : "") | STRING | Oui | - |
| `modèle` | Sélectionne le modèle de génération vidéo parmi les modèles Luma disponibles | COMBO | Oui | Plusieurs options disponibles |
| `résolution` | Résolution de sortie pour la vidéo générée (par défaut : "540p"). Ce paramètre est ignoré lors de l'utilisation du modèle `ray-1-6`. | COMBO | Oui | `"540p"`<br>`"720p"`<br>`"1080p"`<br>`"4k"` |
| `durée` | Durée de la vidéo générée. Ce paramètre est ignoré lors de l'utilisation du modèle `ray-1-6`. | COMBO | Oui | `"5s"`<br>`"9s"` |
| `boucle` | Indique si la vidéo générée doit boucler (par défaut : False) | BOOLEAN | Oui | - |
| `seed` | Graine pour déterminer si le nœud doit se réexécuter ; les résultats réels sont non déterministes quelle que soit la graine. (par défaut : 0) | INT | Oui | 0 à 18446744073709551615 |
| `première_image` | Première image de la vidéo générée. (optionnel) | IMAGE | Non | - |
| `dernière_image` | Dernière image de la vidéo générée. (optionnel) | IMAGE | Non | - |
| `luma_concepts` | Concepts de caméra optionnels pour dicter le mouvement de la caméra via le nœud Luma Concepts. (optionnel) | CUSTOM | Non | - |

**Remarque :** Au moins l'une des images `first_image` ou `last_image` doit être fournie. Le nœud lèvera une exception si les deux sont absentes. Les paramètres `resolution` et `duration` sont ignorés lorsque le `model` est défini sur `ray-1-6`.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `output` | Le fichier vidéo généré | VIDEO |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LumaImageToVideoNode/fr.md)

---
**Source fingerprint (SHA-256):** `210286ad38cecc5b3b0689f470ff473e996abfd251f88a45bcac936751ae2674`
