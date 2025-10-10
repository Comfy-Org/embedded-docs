> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingLipSyncTextToVideoNode/fr.md)

Kling Lip Sync Text to Video Node synchronise les mouvements de bouche dans un fichier vidéo pour correspondre à un texte. Il prend une vidéo en entrée et génère une nouvelle vidéo où les mouvements labiaux du personnage sont alignés avec le texte fourni. Le nœud utilise la synthèse vocale pour créer une synchronisation de parole naturelle.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `video` | VIDEO | Oui | - | Fichier vidéo d'entrée pour la synchronisation labiale |
| `text` | STRING | Oui | - | Contenu textuel pour la génération de vidéo avec synchronisation labiale. Requis lorsque le mode est text2video. Longueur maximale de 120 caractères. |
| `voice` | COMBO | Non | "Melody"<br>"Bella"<br>"Aria"<br>"Ethan"<br>"Ryan"<br>"Dorothy"<br>"Nathan"<br>"Lily"<br>"Aaron"<br>"Emma"<br>"Grace"<br>"Henry"<br>"Isabella"<br>"James"<br>"Katherine"<br>"Liam"<br>"Mia"<br>"Noah"<br>"Olivia"<br>"Sophia" | Sélection de la voix pour l'audio de synchronisation labiale (par défaut : "Melody") |
| `voice_speed` | FLOAT | Non | 0.8-2.0 | Vitesse d'élocution. Plage valide : 0.8~2.0, précise à une décimale. (par défaut : 1) |

**Exigences pour la vidéo :**
- Le fichier vidéo ne doit pas dépasser 100 Mo
- La hauteur/largeur doit être comprise entre 720px et 1920px
- La durée doit être comprise entre 2s et 10s

## Sorties

| Nom de sortie | Type de données | Description |
|-------------|-----------|-------------|
| `output` | VIDEO | Vidéo générée avec audio synchronisé labialement |
| `video_id` | STRING | Identifiant unique pour la vidéo générée |
| `duration` | STRING | Informations de durée pour la vidéo générée |