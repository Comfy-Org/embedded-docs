# PixVerse Texte en Vidéo

Génère des vidéos à partir d'un prompt textuel en utilisant l'API PixVerse. Le nœud vous permet de contrôler la forme, la qualité, la durée et le style de mouvement de la vidéo, et peut éventuellement appliquer un modèle de style enregistré. Il envoie la requête, attend la fin de la génération et renvoie la vidéo terminée.

## Entrées

| Paramètre | Description | Type de données | Obligatoire | Plage |
|-----------|-------------|-----------------|-------------|-------|
| `prompt` | Prompt pour la génération de la vidéo (par défaut : "") | STRING | Oui | Doit contenir au moins 1 caractère |
| `rapport d'aspect` | Rapport d'aspect de la vidéo générée | COMBO | Oui | `"16:9"`<br>`"9:16"`<br>`"1:1"` |
| `qualité` | Réglage de la qualité vidéo (par défaut : "540p") | COMBO | Oui | `"540p"`<br>`"1080p"` |
| `durée (secondes)` | Durée de la vidéo générée en secondes | COMBO | Oui | `"5"`<br>`"10"` |
| `mode de mouvement` | Style de mouvement pour la génération vidéo | COMBO | Oui | `"normal"`<br>`"fast"` |
| `graine` | Graine pour la génération vidéo (par défaut : 0) | INT | Oui | 0 à 2147483647 |
| `prompt négatif` | Description textuelle facultative des éléments non souhaités sur une image (par défaut : "") | STRING | Non | - |
| `modèle PixVerse` | Modèle facultatif pour influencer le style de génération, créé par le nœud PixVerse Template | CUSTOM | Non | - |

**Remarque :** Le `prompt` doit contenir au moins 1 caractère. Lorsque la qualité 1080p est sélectionnée, le mode de mouvement est automatiquement défini sur `normal` et la durée est limitée à 5 secondes. Pour toute durée autre que 5 secondes, le mode de mouvement est également automatiquement défini sur `normal`.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `output` | Le fichier vidéo généré | VIDEO |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PixverseTextToVideoNode/fr.md)

---
**Source fingerprint (SHA-256):** `cb95579dc6c9afa17455b0216ec46571ad2c0455606cf3b9c725ca512c45f938`
