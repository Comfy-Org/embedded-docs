# Wan 3.0 Référence vers vidéo

Ce nœud génère une vidéo à partir d’un prompt textuel et d’images, de vidéos et de fichiers audio de référence optionnels en utilisant le modèle Wan 3.0. Les médias de référence peuvent être combinés librement et mentionnés dans le prompt sous la forme @Image1, @Video1 et @Audio1. Le nœud soumet la demande de génération à l’API Wan et renvoie la vidéo finale.

## Entrées

### Entrées communes

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `model` | Sélectionne la variante du modèle Wan 3.0 utilisée pour la génération. | DYNAMIC_COMBO | Oui | `wan3.0-video`<br>`wan3.0-video-prime` |
| `seed` | Graine (seed) à utiliser pour la génération. Par défaut : 42. | INT | Oui | 0 à 2147483647 |
| `watermark` | Indique s’il faut ajouter un filigrane généré par IA au résultat. Par défaut : false. | BOOLEAN | Oui | true<br>false |

### Entrées wan3.0-video et wan3.0-video-prime

Les deux options de modèle partagent le même ensemble de paramètres.

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `prompt` | Prompt décrivant les éléments et les caractéristiques visuelles. Prend en charge l’anglais et le chinois. Référez-vous aux médias de référence connectés comme @Image1, @Video1, @Audio1, numérotés par type dans l’ordre d’entrée. Par défaut : vide. | STRING | Oui | Jusqu’à 20 000 caractères |
| `resolution` | Résolution de la vidéo de sortie. | COMBO | Oui | "1080P"<br>"720P"<br>"480P" |
| `ratio` | Format d’image de la vidéo de sortie. Avec 'adaptive', les dimensions de sortie sont dérivées des médias d’entrée. | COMBO | Oui | "adaptive"<br>"16:9"<br>"9:16"<br>"1:1"<br>"4:3"<br>"3:4" |
| `duration` | Durée de sortie en secondes. Avec 'auto', le modèle choisit une durée adaptée au prompt et aux médias de référence. La durée combinée des vidéos de référence et de la sortie ne doit pas dépasser 30 secondes. | COMBO | Oui | "auto"<br>"2" à "30" (secondes entières) |
| `audio` | Indique si la vidéo de sortie contient une piste audio. Par défaut : true. | BOOLEAN | Oui | true<br>false |
| `prompt_extend` | Indique si le prompt doit être amélioré à l’aide de l’IA. Par défaut : true. | BOOLEAN | Oui | true<br>false |

### Entrées de référence

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `reference_images` | Emplacement extensible : connectez 1 à 10 images de référence. Les références sont numérotées de image1 à image10 dans l’ordre d’entrée. | IMAGE | Non | 0 à 10 images |
| `reference_videos` | Emplacement extensible : connectez 1 à 5 vidéos de référence. Les références sont numérotées de video1 à video5 dans l’ordre d’entrée. | VIDEO | Non | 0 à 5 vidéos |
| `reference_audios` | Emplacement extensible : connectez 1 à 5 extraits audio de référence. Les références sont numérotées de audio1 à audio5 dans l’ordre d’entrée. | AUDIO | Non | 0 à 5 extraits audio |

**Contraintes :**

- Le prompt doit contenir au moins un caractère non vide, ou au moins une image, une vidéo ou un extrait audio de référence doit être connecté.
- Les balises de référence dans le prompt doivent correspondre aux entrées connectées. Par exemple, @Image1 fait référence à la première image de référence connectée, @Video2 à la deuxième vidéo de référence connectée et @Audio1 au premier extrait audio de référence connecté. Les balises sont numérotées séparément par type dans l’ordre d’entrée.
- Chaque image de référence connectée doit contenir exactement une image, pas un lot.
- Chaque vidéo de référence doit faire 15 secondes ou moins. La durée totale de toutes les vidéos de référence ne doit pas dépasser 15 secondes.
- Chaque extrait audio de référence doit faire 15 secondes ou moins. La durée totale de tous les extraits audio de référence ne doit pas dépasser 15 secondes.
- Lorsque `duration` n’est pas 'auto', la durée totale de toutes les vidéos de référence plus la durée de sortie sélectionnée ne doit pas dépasser 30 secondes.

## Sorties

| Nom de la sortie | Description | Type de données |
|------------------|-------------|-----------------|
| `video` | Le fichier vidéo généré. Inclut une piste audio lorsque le paramètre `audio` est activé. | VIDEO |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Wan3ReferenceToVideoApi/fr.md)

---
**Source fingerprint (SHA-256):** `09caa8142d71235417a3dfc5676c5f6accc2af1287fad3b7050844dd9453cc64`
