> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LumaImageModifyNode/fr.md)

Modifie les images de manière synchrone en fonction de l'invite et du rapport d'aspect. Ce nœud prend une image d'entrée et la transforme selon l'invite textuelle fournie tout en conservant le rapport d'aspect de l'image originale.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `image` | IMAGE | Oui | - | L'image d'entrée à modifier |
| `prompt` | STRING | Oui | - | Invite pour la génération d'image (par défaut : "") |
| `poids de l'image` | FLOAT | Non | 0.0-0.98 | Poids de l'image ; plus proche de 1.0, moins l'image sera modifiée (par défaut : 0.1) |
| `modèle` | MODEL | Oui | Plusieurs options disponibles | Le modèle Luma à utiliser pour la modification d'image |
| `graine` | INT | Non | 0-18446744073709551615 | Graine pour déterminer si le nœud doit être réexécuté ; les résultats réels sont non déterministes quelle que soit la graine (par défaut : 0) |

## Sorties

| Nom de sortie | Type de données | Description |
|-------------|-----------|-------------|
| `image` | IMAGE | L'image modifiée générée par le modèle Luma |