# Génération de vidéo à partir de références Vidu2

Voici la traduction en français de la documentation du nœud Vidu2 Reference-to-Video Generation :

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Vidu2ReferenceVideoNode/en.md)

Le nœud Vidu2 de génération vidéo à partir de références crée une vidéo à partir d'une invite textuelle et de plusieurs images de référence. Vous pouvez définir jusqu'à sept sujets, chacun avec son propre ensemble d'images de référence, et les référencer dans l'invite en utilisant `@subject{subject_id}`. Le nœud génère une vidéo avec une durée, un rapport hauteur/largeur et un mouvement configurables.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `modèle` | Le modèle d'IA à utiliser pour la génération vidéo. | COMBO | Oui | `"viduq2"` |
| `sujets` | Pour chaque sujet, fournissez jusqu'à 3 images de référence (7 images au total pour tous les sujets). Référencez-les dans les invites via `@subject{subject_id}`. | AUTOGROW | Oui | N/A |
| `invite` | La description textuelle utilisée pour guider la génération vidéo. Lorsque le paramètre `audio` est activé, la vidéo inclura une voix générée et une musique de fond basées sur cette invite. | STRING | Oui | N/A |
| `audio` | Lorsqu'il est activé, la vidéo contiendra une voix générée et une musique de fond basées sur l'invite (par défaut : `False`). | BOOLEAN | Non | N/A |
| `durée` | La durée de la vidéo générée en secondes (par défaut : `5`). | INT | Non | 1 à 10 |
| `graine` | Un nombre utilisé pour contrôler l'aléatoire de la génération afin d'obtenir des résultats reproductibles (par défaut : `1`). | INT | Non | 0 à 2147483647 |
| `rapport d’aspect` | La forme du cadre vidéo. | COMBO | Non | `"16:9"`<br>`"9:16"`<br>`"4:3"`<br>`"3:4"`<br>`"1:1"` |
| `résolution` | La résolution en pixels de la vidéo de sortie. | COMBO | Non | `"720p"`<br>`"1080p"` |
| `amplitude du mouvement` | Contrôle l'amplitude du mouvement des objets dans le cadre. | COMBO | Non | `"auto"`<br>`"small"`<br>`"medium"`<br>`"large"` |

**Contraintes :**

* L'`prompt` doit contenir entre 1 et 2000 caractères.
* Vous pouvez définir plusieurs sujets, mais le nombre total d'images de référence pour tous les sujets ne doit pas dépasser 7.
* Chaque sujet individuel peut avoir un maximum de 3 images de référence.
* Chaque image de référence doit avoir un rapport largeur/hauteur compris entre 1:4 et 4:1.
* Chaque image de référence doit avoir une largeur et une hauteur d'au moins 128 pixels.

## Sorties

| Nom de la sortie | Description | Type de données |
| --- | --- | --- |
| `output` | Le fichier vidéo généré. | VIDEO |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Vidu2ReferenceVideoNode/fr.md)

---
**Source fingerprint (SHA-256):** `3e02b05a0e374442a6ca4ce6a3dbc182b4059e19b5ed7dfc2794e036de7beffd`
