# PixVerse Texte en Vidéo

Génère des vidéos à partir d'un prompt textuel et de divers paramètres de génération. Ce nœud crée du contenu vidéo via l'API PixVerse, permettant de contrôler le format d'image, la qualité, la durée, le style de mouvement, etc.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `prompt` | Invite pour la génération vidéo (par défaut : "") | STRING | Oui | - |
| `rapport d'aspect` | Format d'image pour la vidéo générée | COMBO | Oui | `"16:9"`<br>`"9:16"`<br>`"1:1"` |
| `qualité` | Paramètre de qualité vidéo (par défaut : « 540p ») | COMBO | Oui | `"540p"`<br>`"1080p"` |
| `durée (secondes)` | Durée de la vidéo générée en secondes | COMBO | Oui | `"5"`<br>`"10"` |
| `mode de mouvement` | Style de mouvement pour la génération vidéo | COMBO | Oui | `"normal"`<br>`"fast"` |
| `graine` | Graine pour la génération vidéo (par défaut : 0) | INT | Oui | 0 à 2147483647 |
| `prompt négatif` | Invite négative facultative décrivant les éléments indésirables de l'image (par défaut : "") | STRING | Non | - |
| `modèle PixVerse` | Modèle facultatif pour influencer le style de génération, créé par le nœud PixVerse Template | CUSTOM | Non | - |

**Remarque :** Le `prompt` doit contenir au moins 1 caractère. Lors de l'utilisation d'une qualité 1080p, le mode de mouvement est automatiquement défini sur `normal` et la durée est limitée à 5 secondes. Pour les durées autres que 5 secondes, le mode de mouvement est également défini automatiquement sur `normal`.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `output` | Le fichier vidéo généré | VIDEO |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PixverseTextToVideoNode/fr.md)

---
**Source fingerprint (SHA-256):** `cb95579dc6c9afa17455b0216ec46571ad2c0455606cf3b9c725ca512c45f938`
