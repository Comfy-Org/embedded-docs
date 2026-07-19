# Synchronisation labiale Kling vidéo avec texte

Voici la traduction en français de la documentation du nœud Kling Lip Sync Text to Video :

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingLipSyncTextToVideoNode/en.md)

Le nœud Kling Lip Sync Text to Video synchronise les mouvements des lèvres dans un fichier vidéo pour les faire correspondre à un texte donné. Il prend une vidéo en entrée et génère une nouvelle vidéo où les mouvements des lèvres du personnage sont alignés sur le texte fourni. Le nœud utilise la synthèse vocale pour créer une synchronisation de la parole d'apparence naturelle.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `vidéo` | Fichier vidéo d'entrée pour la synchronisation labiale | VIDEO | Oui | - |
| `texte` | Contenu textuel pour la génération vidéo labiale synchronisée. Requis lorsque le mode est text2video. Longueur maximale de 120 caractères. | STRING | Oui | - |
| `voix` | Sélection de la voix pour l'audio de synchronisation labiale (par défaut : "Melody") | COMBO | Non | "Melody"<br>"Bella"<br>"Aria"<br>"Ethan"<br>"Ryan"<br>"Dorothy"<br>"Nathan"<br>"Lily"<br>"Aaron"<br>"Emma"<br>"Grace"<br>"Henry"<br>"Isabella"<br>"James"<br>"Katherine"<br>"Liam"<br>"Mia"<br>"Noah"<br>"Olivia"<br>"Sophia" |
| `vitesse de la voix` | Débit de parole. Plage valide : 0,8~2,0, précis à une décimale près. (par défaut : 1) | FLOAT | Non | 0.8-2.0 |

**Exigences vidéo :**

- Le fichier vidéo ne doit pas dépasser 100 Mo
- La hauteur/largeur doit être comprise entre 720 px et 1920 px
- La durée doit être comprise entre 2 s et 10 s

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `id_vidéo` | Vidéo générée avec audio synchronisé sur les lèvres | VIDEO |
| `id_vidéo` | Identifiant unique de la vidéo générée | STRING |
| `durée` | Informations sur la durée de la vidéo générée | STRING |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingLipSyncTextToVideoNode/fr.md)

---
**Source fingerprint (SHA-256):** `f16200d52ba05acfedebc027dde91e2c91bdbb80086888d947c9f56a4e92856d`
