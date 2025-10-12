> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LumaVideoNode/fr.md)

Génère des vidéos de manière synchrone en fonction des paramètres d'invite et de sortie. Ce nœud crée du contenu vidéo à l'aide de descriptions textuelles et de divers paramètres de génération, produisant la vidéo finale une fois le processus de génération terminé.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `prompt` | STRING | Oui | - | Invite pour la génération de vidéo (par défaut : chaîne vide) |
| `modèle` | COMBO | Oui | Plusieurs options disponibles | Le modèle de génération vidéo à utiliser |
| `rapport d'aspect` | COMBO | Oui | Plusieurs options disponibles | Le format d'image pour la vidéo générée (par défaut : 16:9) |
| `résolution` | COMBO | Oui | Plusieurs options disponibles | La résolution de sortie pour la vidéo (par défaut : 540p) |
| `durée` | COMBO | Oui | Plusieurs options disponibles | La durée de la vidéo générée |
| `boucle` | BOOLEAN | Oui | - | Indique si la vidéo doit être en boucle (par défaut : Faux) |
| `graine` | INT | Oui | 0 à 18446744073709551615 | Graine pour déterminer si le nœud doit être réexécuté ; les résultats réels sont non déterministes quelle que soit la graine (par défaut : 0) |
| `luma_concepts` | CUSTOM | Non | - | Concepts de caméra optionnels pour dicter le mouvement de la caméra via le nœud Luma Concepts |

**Note :** Lors de l'utilisation du modèle `ray_1_6`, les paramètres `duration` et `resolution` sont automatiquement définis sur Aucun et n'affectent pas la génération.

## Sorties

| Nom de sortie | Type de données | Description |
|-------------|-----------|-------------|
| `output` | VIDEO | Le fichier vidéo généré |
