> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanTextToVideoApi/fr.md)

Le nœud Wan Text to Video génère du contenu vidéo basé sur des descriptions textuelles. Il utilise des modèles d'IA pour créer des vidéos à partir de prompts et prend en charge différentes tailles de vidéo, durées et entrées audio optionnelles. Le nœud peut générer automatiquement de l'audio lorsque nécessaire et offre des options pour l'amélioration des prompts et le filigrane.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `model` | COMBO | Oui | "wan2.5-t2v-preview" | Modèle à utiliser (par défaut : "wan2.5-t2v-preview") |
| `prompt` | STRING | Oui | - | Prompt utilisé pour décrire les éléments et les caractéristiques visuelles, prend en charge l'anglais/le chinois (par défaut : "") |
| `negative_prompt` | STRING | Non | - | Prompt textuel négatif pour guider ce qu'il faut éviter (par défaut : "") |
| `size` | COMBO | Non | "480p: 1:1 (624x624)"<br>"480p: 16:9 (832x480)"<br>"480p: 9:16 (480x832)"<br>"720p: 1:1 (960x960)"<br>"720p: 16:9 (1280x720)"<br>"720p: 9:16 (720x1280)"<br>"720p: 4:3 (1088x832)"<br>"720p: 3:4 (832x1088)"<br>"1080p: 1:1 (1440x1440)"<br>"1080p: 16:9 (1920x1080)"<br>"1080p: 9:16 (1080x1920)"<br>"1080p: 4:3 (1632x1248)"<br>"1080p: 3:4 (1248x1632)" | Résolution et format de la vidéo (par défaut : "480p: 1:1 (624x624)") |
| `duration` | INT | Non | 5-10 | Durées disponibles : 5 et 10 secondes (par défaut : 5) |
| `audio` | AUDIO | Non | - | L'audio doit contenir une voix claire et forte, sans bruit parasite ni musique de fond |
| `seed` | INT | Non | 0-2147483647 | Graine à utiliser pour la génération (par défaut : 0) |
| `generate_audio` | BOOLEAN | Non | - | S'il n'y a pas d'entrée audio, générer l'audio automatiquement (par défaut : False) |
| `prompt_extend` | BOOLEAN | Non | - | Indique s'il faut améliorer le prompt avec l'assistance de l'IA (par défaut : True) |
| `watermark` | BOOLEAN | Non | - | Indique s'il faut ajouter un filigrane "Généré par IA" au résultat (par défaut : True) |

**Note :** Le paramètre `duration` n'accepte que les valeurs de 5 ou 10 secondes, car ce sont les durées disponibles. Lorsqu'une entrée audio est fournie, elle doit avoir une durée comprise entre 3,0 et 29,0 secondes et contenir une voix claire sans bruit de fond ni musique.

## Sorties

| Nom de sortie | Type de données | Description |
|-------------|-----------|-------------|
| `output` | VIDEO | La vidéo générée basée sur les paramètres d'entrée |