> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingLipSyncAudioToVideoNode/fr.md)

Le nœud Kling Lip Sync Audio to Video synchronise les mouvements de la bouche dans un fichier vidéo pour qu'ils correspondent au contenu audio d'un fichier sonore. Ce nœud analyse les modèles vocaux dans l'audio et ajuste les mouvements faciaux dans la vidéo pour créer un lip-sync réaliste. Le processus nécessite à la fois une vidéo contenant un visage distinct et un fichier audio avec des vocaux clairement discernables.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `video` | VIDEO | Oui | - | Le fichier vidéo contenant un visage à synchroniser |
| `audio` | AUDIO | Oui | - | Le fichier audio contenant les vocaux à synchroniser avec la vidéo |
| `voice_language` | COMBO | Non | `"en"`<br>`"zh"`<br>`"es"`<br>`"fr"`<br>`"de"`<br>`"it"`<br>`"pt"`<br>`"pl"`<br>`"tr"`<br>`"ru"`<br>`"nl"`<br>`"cs"`<br>`"ar"`<br>`"ja"`<br>`"hu"`<br>`"ko"` | La langue de la voix dans le fichier audio (par défaut : "en") |

**Contraintes importantes :**
- Le fichier audio ne doit pas dépasser 5 Mo
- Le fichier vidéo ne doit pas dépasser 100 Mo
- Les dimensions de la vidéo doivent être comprises entre 720px et 1920px en hauteur/largeur
- La durée de la vidéo doit être comprise entre 2 secondes et 10 secondes
- L'audio doit contenir des vocaux clairement discernables
- La vidéo doit contenir un visage distinct

## Sorties

| Nom de sortie | Type de données | Description |
|-------------|-----------|-------------|
| `output` | VIDEO | La vidéo traitée avec les mouvements de bouche synchronisés |
| `video_id` | STRING | L'identifiant unique de la vidéo traitée |
| `duration` | STRING | La durée de la vidéo traitée |