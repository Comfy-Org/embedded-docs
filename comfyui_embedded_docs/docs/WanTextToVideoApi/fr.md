> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanTextToVideoApi/fr.md)

Voici la traduction en français de la documentation du nœud WanTextToVideoApi :

Le nœud Wan Texte vers Vidéo génère un contenu vidéo à partir de descriptions textuelles. Il utilise des modèles d'IA pour créer des vidéos à partir de prompts et prend en charge diverses tailles de vidéo, durées et entrées audio facultatives. Le nœud peut générer automatiquement l'audio si nécessaire et propose des options d'amélioration du prompt et de filigrane.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------------|--------|-------|-------------|
| `modèle` | COMBO | Oui | "wan2.5-t2v-preview"<br>"wan2.6-t2v" | Modèle à utiliser (par défaut : "wan2.6-t2v") |
| `invite` | STRING | Oui | - | Prompt décrivant les éléments et les caractéristiques visuelles. Prend en charge l'anglais et le chinois (par défaut : "") |
| `negative_prompt` | STRING | Non | - | Prompt négatif décrivant ce qu'il faut éviter (par défaut : "") |
| `taille` | COMBO | Non | "480p: 1:1 (624x624)"<br>"480p: 16:9 (832x480)"<br>"480p: 9:16 (480x832)"<br>"720p: 1:1 (960x960)"<br>"720p: 16:9 (1280x720)"<br>"720p: 9:16 (720x1280)"<br>"720p: 4:3 (1088x832)"<br>"720p: 3:4 (832x1088)"<br>"1080p: 1:1 (1440x1440)"<br>"1080p: 16:9 (1920x1080)"<br>"1080p: 9:16 (1080x1920)"<br>"1080p: 4:3 (1632x1248)"<br>"1080p: 3:4 (1248x1632)" | Résolution et rapport hauteur/largeur de la vidéo (par défaut : "720p: 1:1 (960x960)") |
| `durée` | INT | Non | 5-15 (par pas de 5) | Durée de la vidéo en secondes. Une durée de 15 secondes est disponible uniquement pour le modèle Wan 2.6 (par défaut : 5) |
| `audio` | AUDIO | Non | - | L'audio doit contenir une voix claire et forte, sans bruit parasite ni musique de fond |
| `seed` | INT | Non | 0-2147483647 | Graine à utiliser pour la génération (par défaut : 0) |
| `generate_audio` | BOOLEAN | Non | - | Si aucune entrée audio n'est fournie, générer l'audio automatiquement (par défaut : False) |
| `prompt_extend` | BOOLEAN | Non | - | Indique s'il faut améliorer le prompt avec l'aide de l'IA (par défaut : True) |
| `watermark` | BOOLEAN | Non | - | Indique s'il faut ajouter un filigrane généré par l'IA au résultat (par défaut : False) |
| `type_de_plan` | COMBO | Non | "single"<br>"multi" | Spécifie le type de plan pour la vidéo générée, c'est-à-dire si la vidéo est un plan continu unique ou plusieurs plans avec des coupures. Ce paramètre n'est effectif que lorsque prompt_extend est True (par défaut : "single") |

**Remarque :** Le modèle Wan 2.6 ne prend pas en charge les résolutions 480p. Une durée de 15 secondes n'est prise en charge que par le modèle Wan 2.6. Lors de la fourniture d'une entrée audio, celle-ci doit avoir une durée comprise entre 3,0 et 29,0 secondes et contenir une voix claire sans bruit de fond ni musique.

## Sorties

| Nom de la sortie | Type de données | Description |
|------------------|-----------------|-------------|
| `output` | VIDEO | La vidéo générée en fonction des paramètres d'entrée |

---
**Source fingerprint (SHA-256):** `e978f384365060a6d71899e4e2e22b2c6f4268fb0da988c8902e4876d8597a96`
