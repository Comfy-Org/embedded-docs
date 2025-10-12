> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ViduStartEndToVideoNode/fr.md)

Le nœud Vidu Start End To Video Generation crée une vidéo en générant des images intermédiaires entre une image de départ et une image de fin. Il utilise une description textuelle pour guider le processus de génération vidéo et prend en charge divers modèles vidéo avec différents paramètres de résolution et de mouvement. Le nœud vérifie que les images de début et de fin ont des rapports d'aspect compatibles avant le traitement.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `model` | COMBO | Oui | `"vidu_q1"`<br>[Autres valeurs de modèles de l'énumération VideoModelName] | Nom du modèle (par défaut : "vidu_q1") |
| `first_frame` | IMAGE | Oui | - | Image de départ |
| `end_frame` | IMAGE | Oui | - | Image de fin |
| `prompt` | STRING | Non | - | Une description textuelle pour la génération vidéo |
| `duration` | INT | Non | 5-5 | Durée de la vidéo de sortie en secondes (par défaut : 5, fixée à 5 secondes) |
| `seed` | INT | Non | 0-2147483647 | Graine pour la génération vidéo (0 pour aléatoire) (par défaut : 0) |
| `resolution` | COMBO | Non | `"1080p"`<br>[Autres valeurs de résolution de l'énumération Resolution] | Les valeurs prises en charge peuvent varier selon le modèle et la durée (par défaut : "1080p") |
| `movement_amplitude` | COMBO | Non | `"auto"`<br>[Autres valeurs d'amplitude de mouvement de l'énumération MovementAmplitude] | L'amplitude du mouvement des objets dans le cadre (par défaut : "auto") |

**Note :** Les images de début et de fin doivent avoir des rapports d'aspect compatibles (vérifiés avec une tolérance de rapport min_rel=0.8, max_rel=1.25).

## Sorties

| Nom de sortie | Type de données | Description |
|-------------|-----------|-------------|
| `output` | VIDEO | Le fichier vidéo généré |
