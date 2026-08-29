# PixVerse V6 Fusion (références vers vidéo)

PixVerse V6 Fusion (Référence vers vidéo) compose une vidéo à partir de sujets, d’arrière-plans et de vidéos de référence avec PixVerse. Placez une référence dans la scène en la nommant dans le prompt, par exemple « @Subject1 marche dans @Background1 ». Le fait de connecter une vidéo de référence bascule le modèle en mode Omni, où la durée de sortie correspond à la vidéo de référence la plus longue.

## Entrées

### Entrées communes

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `model` | Paramètres du modèle et de génération. Sélectionne le modèle et expose ses paramètres de génération ci-dessous. La seule option disponible est « PixVerse V6 ». | DYNAMIC_COMBO | Oui | « PixVerse V6 » |

### Entrées PixVerse V6

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `prompt` | Prompt pour la génération de la vidéo. Référez-vous aux références connectées comme @Subject1, @Background1, @Video1. Par défaut : vide. | STRING | Oui | 1 à 5000 caractères |
| `aspect_ratio` | Format d’image de sortie. L’option « auto » n’est autorisée que lorsqu’au moins une vidéo de référence est connectée. | COMBO | Oui | « auto »<br>plus les formats d’image PixVerse V6 prédéfinis |
| `quality` | Résolution de sortie. Définit le bord long : 360p correspond à 640px, 540p à 1024px, 720p à 1280px, 1080p à 1920px. Par défaut : « 720p ». | COMBO | Oui | « 360p »<br>« 540p »<br>« 720p »<br>« 1080p » |
| `duration_seconds` | Durée de la vidéo générée en secondes. Lorsque des vidéos de référence sont connectées, la durée de sortie suit plutôt la vidéo de référence la plus longue et ce paramètre est ignoré. Par défaut : 5. | INT | Oui | 1 à 15 |
| `generate_audio` | Générer une piste audio native avec la vidéo. Par défaut : True. | BOOLEAN | Oui | True<br>False |
| `seed` | Graine (seed) pour la génération de la vidéo. PixVerse l’enregistre mais ne reproduit pas une exécution à partir de celle-ci. Par défaut : 42. | INT | Oui | 0 à 2147483647 |
| `negative_prompt` | Une description textuelle facultative des éléments indésirables dans la vidéo. Par défaut : vide. | STRING | Non | Jusqu’à 2048 caractères |
| `style` | Un style visuel facultatif appliqué à l’ensemble de la vidéo. Par défaut : « none ». | COMBO | Non | « none »<br>plus les styles PixVerse V6 prédéfinis |

### Entrées de référence

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `subjects` | Emplacement extensible : connectez des images de référence des sujets à placer dans la scène. Les emplacements sont nommés subject1 à subject8 ; référez-vous-y dans le prompt comme @Subject1, @Subject2, etc. | IMAGE | Non | 0 à 8 images |
| `backgrounds` | Emplacement extensible : connectez des images de référence de la scène dans laquelle les sujets sont placés. Les emplacements sont nommés background1 à background2 ; référez-vous-y dans le prompt comme @Background1, @Background2. | IMAGE | Non | 0 à 2 images |
| `videos` | Emplacement extensible : connectez des vidéos de référence pour emprunter des sujets, des mouvements, des cadrages ou des styles. Les emplacements sont nommés video1 à video2 ; référez-vous-y dans le prompt comme @Video1, @Video2. Chaque vidéo doit durer au plus 15 secondes, et la durée totale ne doit pas dépasser 15 secondes. Connecter au moins une vidéo fait basculer le nœud en mode Omni. | VIDEO | Non | 0 à 2 vidéos<br>15 secondes max chacune<br>15 secondes au total |

Note : Connectez au moins un sujet, un arrière-plan ou une vidéo de référence. Les balises de référence dans le prompt (par exemple @Subject1, @Background1, @Video1) doivent correspondre aux emplacements connectés, sinon la requête est rejetée. Lorsqu’au moins une vidéo de référence est connectée (mode Omni), la durée de sortie correspond à la vidéo de référence la plus longue, `duration_seconds` est ignoré, `aspect_ratio` peut être défini sur « auto », et jusqu’à 10 images de référence sont acceptées. Sans vidéo de référence, au plus 7 images de référence (sujets et arrière-plans combinés) sont acceptées, et le format d’image « auto » n’est pas autorisé.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `video` | La vidéo de fusion générée, téléchargée depuis PixVerse. | VIDEO |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PixverseV6FusionVideoNode/fr.md)

---
**Source fingerprint (SHA-256):** `a83ef07f6f1918921e93fa67c2eca351754794f629aa216ccff21ce80901aebd`
