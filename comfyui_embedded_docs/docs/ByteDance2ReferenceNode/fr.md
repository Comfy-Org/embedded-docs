> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDance2ReferenceNode/fr.md)

Le nœud ByteDance Seedance 2.0 Reference to Video utilise le modèle d'IA Seedance 2.0 pour créer, éditer ou étendre des vidéos en fonction de votre prompt texte et des éléments de référence fournis. Il peut utiliser des images, des vidéos et de l'audio comme références pour guider le processus de génération, prenant en charge des tâches comme l'édition et l'extension vidéo.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `model` | COMBO | Oui | `"Seedance 2.0"`<br>`"Seedance 2.0 Fast"` | Le modèle d'IA à utiliser. Seedance 2.0 est pour une qualité maximale, tandis que Seedance 2.0 Fast est optimisé pour la vitesse. La sélection d'un modèle révèle des entrées supplémentaires requises pour `prompt`, `resolution`, `duration`, `ratio`, `generate_audio`, et des entrées optionnelles pour `reference_images`, `reference_videos`, `reference_audios`, `reference_assets`, et `auto_downscale`. |
| `seed` | INT | Non | 0 à 2147483647 | Un nombre utilisé pour contrôler si le nœud doit se ré-exécuter. Les résultats sont non déterministes quelle que soit la valeur de la graine (par défaut : 0). |
| `watermark` | BOOLEAN | Non | `True` / `False` | Indique s'il faut ajouter un filigrane à la vidéo générée (par défaut : False). |

**Contraintes importantes :**
*   Au moins une image ou vidéo de référence (fournie via les entrées `reference_images`, `reference_videos` ou `reference_assets`) est requise pour que le nœud fonctionne.
*   Chaque vidéo de référence doit durer au moins 1,8 seconde. La durée combinée de toutes les vidéos de référence ne peut pas dépasser 15,1 secondes.
*   Chaque extrait audio de référence doit durer au moins 1,8 seconde. La durée combinée de tous les fichiers audio de référence ne peut pas dépasser 15,1 secondes.

## Sorties

| Nom de la sortie | Type de données | Description |
|-------------|-----------|-------------|
| `video` | VIDEO | Le fichier vidéo généré. |