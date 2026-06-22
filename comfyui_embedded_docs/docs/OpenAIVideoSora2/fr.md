# OpenAI Sora - Vidéo

Voici la traduction de la documentation du nœud OpenAIVideoSora2, conforme à vos règles :

Le nœud OpenAIVideoSora2 génère des vidéos à l'aide des modèles Sora d'OpenAI. Il crée un contenu vidéo basé sur des invites textuelles et des images d'entrée optionnelles, puis renvoie la vidéo générée en sortie. Le nœud prend en charge différentes durées et résolutions vidéo selon le modèle sélectionné.

**AVIS D'OBSOLESCENCE :** OpenAI cessera de fournir l'API Sora v2 en septembre 2026. Ce nœud sera supprimé de ComfyUI à ce moment-là.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `modèle` | Le modèle OpenAI Sora à utiliser pour la génération vidéo (par défaut : "sora-2") | COMBO | Oui | "sora-2"<br>"sora-2-pro" |
| `invite` | Texte d'orientation ; peut être vide si une image d'entrée est présente (par défaut : vide) | STRING | Oui | - |
| `taille` | La résolution de la vidéo générée (par défaut : "1280x720") | COMBO | Oui | "720x1280"<br>"1280x720"<br>"1024x1792"<br>"1792x1024" |
| `durée` | La durée de la vidéo générée en secondes (par défaut : 8) | COMBO | Oui | 4<br>8<br>12 |
| `image` | Image d'entrée optionnelle pour la génération vidéo | IMAGE | Non | - |
| `graine` | Graine pour déterminer si le nœud doit être réexécuté ; les résultats réels sont non déterministes quelle que soit la graine (par défaut : 0) | INT | Non | 0 à 2147483647 |

**Contraintes et limitations :**

- Le modèle "sora-2" ne prend en charge que les résolutions "720x1280" et "1280x720"
- Une seule image d'entrée est prise en charge lors de l'utilisation du paramètre `image`
- Les résultats sont non déterministes quelle que soit la valeur de la graine

## Sorties

| Nom de la sortie | Description | Type de données |
| --- | --- | --- |
| `output` | La vidéo générée en sortie | VIDEO |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/OpenAIVideoSora2/fr.md)

---
**Source fingerprint (SHA-256):** `c87b696dd92c6a6a929f49d189a375b1ebed80bf47f24667ee17c0b210330e55`
