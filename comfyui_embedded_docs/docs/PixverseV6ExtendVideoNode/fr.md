# PixVerse V6 Prolonger la vidéo

Ce nœud prolonge une vidéo existante à l'aide du modèle PixVerse V6, en générant éventuellement une piste audio native en plus du prolongement. La vidéo source doit être plus courte que 40 secondes et ne pas dépasser 1920 pixels en largeur ni en hauteur. La sortie conserve la résolution de la vidéo source ; ainsi, le paramètre de qualité contrôle la qualité de rendu du prolongement plutôt que la taille de l'image.

## Entrées

### Entrées communes

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `video` | Vidéo à prolonger. | VIDEO | Oui | Moins de 40 secondes ; 1920 pixels maximum en largeur et en hauteur |
| `model` | Modèle et paramètres de génération. | DYNAMIC_COMBO | Oui | « PixVerse V6 » |

### Entrées PixVerse V6

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `prompt` | Prompt décrivant la manière dont la vidéo doit se poursuivre. (défaut : vide) | STRING | Oui | 1–5000 caractères |
| `quality` | Qualité de rendu du prolongement généré : la 1080p est nettement meilleure que la 540p ou la 360p. Elle ne redimensionne jamais la vidéo : la sortie conserve la résolution de la vidéo source. (défaut : « 720p ») | COMBO | Oui | « 360p »<br>« 540p »<br>« 720p »<br>« 1080p » |
| `duration_seconds` | Durée de la vidéo générée en secondes. (défaut : 5) | INT | Oui | 1–15 |
| `generate_audio` | Générer une piste audio native en même temps que la vidéo. (défaut : true) | BOOLEAN | Oui | true / false |
| `seed` | Seed pour la génération vidéo. PixVerse l'enregistre mais ne peut pas reproduire une génération à partir de celle-ci. (défaut : 42) | INT | Oui | 0–2147483647 |
| `negative_prompt` | Une description textuelle facultative des éléments indésirables dans la vidéo. (défaut : vide) | STRING | Non | Jusqu'à 2048 caractères |
| `style` | Un style visuel facultatif appliqué à l'ensemble de la vidéo. (défaut : « none ») | COMBO | Non | Plusieurs options disponibles ; « none » est l'option par défaut |

**Remarque :** La `video` source doit être plus courte que 40 secondes et ne pas dépasser 1920 pixels en largeur comme en hauteur ; les vidéos plus longues ou plus grandes sont rejetées. La sortie générée conserve la résolution de la vidéo source, donc `quality` modifie la fidélité de rendu, et non la taille de l'image de sortie. Le `prompt` est obligatoire et doit contenir entre 1 et 5000 caractères après suppression des espaces en début et fin. Le `negative_prompt`, lorsqu'il est fourni, est limité à 2048 caractères. La `seed` est enregistrée par PixVerse mais ne peut pas être utilisée pour reproduire la même génération.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `video` | La vidéo de prolongement générée, à la même résolution que la vidéo source. | VIDEO |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PixverseV6ExtendVideoNode/fr.md)

---
**Source fingerprint (SHA-256):** `8bd2a04a5da95b39fb963922e2e54a7aa4efb670260fa38313d21db3af295029`
