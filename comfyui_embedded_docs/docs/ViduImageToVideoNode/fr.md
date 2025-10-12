> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ViduImageToVideoNode/fr.md)

Le nœud Vidu Image To Video Generation crée des vidéos à partir d'une image de départ et d'une description textuelle optionnelle. Il utilise des modèles d'IA pour générer un contenu vidéo qui prolonge l'image fournie. Le nœud envoie l'image et les paramètres à un service externe et retourne la vidéo générée.

## Entrées

| Paramètre | Type de donnée | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `model` | COMBO | Oui | `vidu_q1`<br>*Autres options VideoModelName* | Nom du modèle (par défaut : vidu_q1) |
| `image` | IMAGE | Oui | - | Image à utiliser comme image de départ pour la vidéo générée |
| `prompt` | STRING | Non | - | Description textuelle pour la génération de vidéo (par défaut : vide) |
| `duration` | INT | Non | 5-5 | Durée de la vidéo de sortie en secondes (par défaut : 5, fixée à 5 secondes) |
| `seed` | INT | Non | 0-2147483647 | Graine pour la génération de vidéo (0 pour aléatoire) (par défaut : 0) |
| `resolution` | COMBO | Non | `r_1080p`<br>*Autres options Resolution* | Les valeurs prises en charge peuvent varier selon le modèle et la durée (par défaut : r_1080p) |
| `movement_amplitude` | COMBO | Non | `auto`<br>*Autres options MovementAmplitude* | L'amplitude de mouvement des objets dans le cadre (par défaut : auto) |

**Contraintes :**
- Une seule image d'entrée est autorisée (ne peut pas traiter plusieurs images)
- L'image d'entrée doit avoir un rapport d'aspect compris entre 1:4 et 4:1

## Sorties

| Sortie | Type de donnée | Description |
|-------------|-----------|-------------|
| `output` | VIDEO | La vidéo générée en sortie |