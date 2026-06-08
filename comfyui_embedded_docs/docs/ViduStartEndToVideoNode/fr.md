Voici la traduction en français de la documentation du nœud ComfyUI **Vidu Start End To Video** :

Le nœud de génération vidéo Vidu Start End To Video crée une vidéo en générant des images entre une image de début et une image de fin. Il utilise une invite textuelle pour guider le processus de génération vidéo et prend en charge divers modèles vidéo avec différents réglages de résolution et de mouvement. Le nœud valide que les images de début et de fin ont des rapports d'aspect compatibles avant le traitement.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `modèle` | Nom du modèle | COMBO | Oui | `"viduq1"` |
| `première_image` | Image de début | IMAGE | Oui | - |
| `image_fin` | Image de fin | IMAGE | Oui | - |
| `description` | Description textuelle pour la génération vidéo | STRING | Non | - |
| `durée` | Durée de la vidéo de sortie en secondes (par défaut : 5, fixée à 5 secondes) | INT | Non | 5-5 |
| `graine` | Graine pour la génération vidéo (0 pour aléatoire) (par défaut : 0) | INT | Non | 0-2147483647 |
| `résolution` | Les valeurs prises en charge peuvent varier selon le modèle et la durée (par défaut : "1080p") | COMBO | Non | `"1080p"` |
| `amplitude_mouvement` | L'amplitude de mouvement des objets dans l'image (par défaut : "auto") | COMBO | Non | `"auto"`<br>`"small"`<br>`"medium"`<br>`"large"` |

**Remarque :** Les images de début et de fin doivent avoir des rapports d'aspect compatibles (validés avec une tolérance de ratio min_rel=0,8, max_rel=1,25).

## Sorties

| Nom de la sortie | Description | Type de données |
| --- | --- | --- |
| `output` | Le fichier vidéo généré | VIDEO |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ViduStartEndToVideoNode/fr.md)

---
**Source fingerprint (SHA-256):** `d859d67b3ff73977b95e3903b461509f933f9652fedc016e1cd362f6bef1b8dc`
