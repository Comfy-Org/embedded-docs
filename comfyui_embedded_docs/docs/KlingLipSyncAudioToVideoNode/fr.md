# Synchronisation labiale Kling : Vidéo avec audio

Le nœud Kling Lip Sync Audio to Video synchronise les mouvements de la bouche dans un fichier vidéo avec le contenu audio d'un fichier audio. Ce nœud analyse les schémas vocaux de l'audio et ajuste les mouvements faciaux de la vidéo afin de créer une synchronisation labiale réaliste. Le processus nécessite à la fois une vidéo contenant un visage distinct et un fichier audio avec des voix clairement identifiables.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `video` | Le fichier vidéo contenant un visage à synchroniser labialement | VIDEO | Oui | - |
| `audio` | Le fichier audio contenant les voix à synchroniser avec la vidéo | AUDIO | Oui | - |
| `voice_language` | La langue de la voix dans le fichier audio (par défaut : "en") | COMBO | Oui | `"en"`<br>`"zh"`<br>`"es"`<br>`"fr"`<br>`"de"`<br>`"it"`<br>`"pt"`<br>`"pl"`<br>`"tr"`<br>`"ru"`<br>`"nl"`<br>`"cs"`<br>`"ar"`<br>`"ja"`<br>`"hu"`<br>`"ko"` |

**Contraintes importantes :**

- Le fichier audio ne doit pas dépasser 5 Mo
- Le fichier vidéo ne doit pas dépasser 100 Mo
- Les dimensions de la vidéo doivent être comprises entre 720 px et 1920 px en hauteur/largeur
- La durée de la vidéo doit être comprise entre 2 secondes et 10 secondes
- L'audio doit contenir des voix clairement identifiables
- La vidéo doit contenir un visage distinct

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `output` | La vidéo traitée avec les mouvements de bouche synchronisés | VIDEO |
| `video_id` | L'identifiant unique de la vidéo traitée | STRING |
| `duration` | La durée de la vidéo traitée | STRING |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingLipSyncAudioToVideoNode/fr.md)

---
**Source fingerprint (SHA-256):** `2f88af3191ac4f9c5c9fa1aaa5b744a12620b66e55a1fe0ab16b8b3b61110128`
