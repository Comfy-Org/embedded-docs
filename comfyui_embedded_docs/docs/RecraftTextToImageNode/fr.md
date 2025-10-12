> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RecraftTextToImageNode/fr.md)

Génère des images de manière synchrone en fonction de l'invite et de la résolution. Ce nœud se connecte à l'API Recraft pour créer des images à partir de descriptions textuelles avec des dimensions et des options de style spécifiées.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `prompt` | STRING | Oui | - | Invite pour la génération d'image. (défaut : "") |
| `taille` | COMBO | Oui | "1024x1024"<br>"1152x896"<br>"896x1152"<br>"1216x832"<br>"832x1216"<br>"1344x768"<br>"768x1344"<br>"1536x640"<br>"640x1536" | La taille de l'image générée. (défaut : "1024x1024") |
| `n` | INT | Oui | 1-6 | Le nombre d'images à générer. (défaut : 1) |
| `seed` | INT | Oui | 0-18446744073709551615 | Graine pour déterminer si le nœud doit se réexécuter ; les résultats réels sont non déterministes quelle que soit la graine. (défaut : 0) |
| `recraft_style` | COMBO | Non | Options multiples disponibles | Sélection de style optionnelle pour la génération d'image. |
| `negative_prompt` | STRING | Non | - | Une description textuelle optionnelle des éléments indésirables sur une image. (défaut : "") |
| `recraft_controls` | COMBO | Non | Options multiples disponibles | Contrôles additionnels optionnels sur la génération via le nœud Recraft Controls. |

**Note :** Le paramètre `seed` contrôle uniquement quand le nœud se réexécute mais ne rend pas la génération d'image déterministe. Les images de sortie réelles varieront même avec la même valeur de graine.

## Sorties

| Nom de sortie | Type de données | Description |
|-------------|-----------|-------------|
| `IMAGE` | IMAGE | L'image(s) générée(s) sous forme de tenseur de sortie. |
