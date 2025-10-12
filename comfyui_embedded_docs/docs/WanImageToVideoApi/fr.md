> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanImageToVideoApi/fr.md)

Le nœud Wan Image to Video génère du contenu vidéo à partir d'une seule image d'entrée et d'une invite textuelle. Il crée des séquences vidéo en étendant l'image initiale selon la description fournie, avec des options pour contrôler la qualité vidéo, la durée et l'intégration audio.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `model` | COMBO | Oui | "wan2.5-i2v-preview"<br>"wan2.5-i2v-preview" | Modèle à utiliser (par défaut : "wan2.5-i2v-preview") |
| `image` | IMAGE | Oui | - | Image d'entrée qui sert de première frame pour la génération vidéo |
| `prompt` | STRING | Oui | - | Invite utilisée pour décrire les éléments et caractéristiques visuelles, supporte l'anglais/chinois (par défaut : vide) |
| `negative_prompt` | STRING | Non | - | Invite textuelle négative pour guider ce qu'il faut éviter (par défaut : vide) |
| `resolution` | COMBO | Non | "480P"<br>"720P"<br>"1080P" | Qualité de résolution vidéo (par défaut : "480P") |
| `duration` | INT | Non | 5-10 | Durées disponibles : 5 et 10 secondes (par défaut : 5) |
| `audio` | AUDIO | Non | - | L'audio doit contenir une voix claire et forte, sans bruit parasite ni musique de fond |
| `seed` | INT | Non | 0-2147483647 | Graine à utiliser pour la génération (par défaut : 0) |
| `generate_audio` | BOOLEAN | Non | - | S'il n'y a pas d'audio en entrée, générer automatiquement l'audio (par défaut : Faux) |
| `prompt_extend` | BOOLEAN | Non | - | Indique s'il faut améliorer l'invite avec l'assistance de l'IA (par défaut : Vrai) |
| `watermark` | BOOLEAN | Non | - | Indique s'il faut ajouter un filigrane "Généré par IA" au résultat (par défaut : Vrai) |

**Contraintes :**

- Exactement une image d'entrée est requise pour la génération vidéo
- Le paramètre de durée n'accepte que les valeurs de 5 ou 10 secondes
- Lorsqu'un audio est fourni, il doit avoir une durée comprise entre 3,0 et 29,0 secondes

## Sorties

| Nom de sortie | Type de données | Description |
|-------------|-----------|-------------|
| `output` | VIDEO | Vidéo générée basée sur l'image d'entrée et l'invite |
