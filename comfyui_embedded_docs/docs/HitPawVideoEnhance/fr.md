> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HitPawVideoEnhance/fr.md)

Voici la traduction en français de la documentation du nœud HitPaw Video Enhance, en respectant vos règles :

Le nœud HitPaw Video Enhance utilise une API externe pour améliorer la qualité des vidéos. Il agrandit les vidéos basse résolution vers une résolution plus élevée, supprime les artefacts visuels et réduit le bruit. Le coût de traitement est calculé par seconde de la vidéo d'entrée.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------------|--------|-------|-------------|
| `modèle` | DYNAMIC COMBO | Oui | Plusieurs options disponibles | Le modèle d'IA à utiliser pour l'amélioration vidéo. La sélection d'un modèle révèle un paramètre `resolution` imbriqué. Les modèles disponibles et leurs résolutions prises en charge varient. |
| `model.resolution` | COMBO | Oui | `"original"`<br>`"720p"`<br>`"1080p"`<br>`"2k/qhd"`<br>`"4k/uhd"`<br>`"8k"` | La résolution cible pour la vidéo améliorée. Certaines options peuvent être indisponibles selon le `modèle` sélectionné. |
| `vidéo` | VIDEO | Oui | N/A | Le fichier vidéo d'entrée à améliorer. |

**Contraintes :**

* La `video` d'entrée doit avoir une durée comprise entre 0,5 seconde et 60 minutes (3600 secondes).
* La `resolution` sélectionnée doit être supérieure aux dimensions de la vidéo d'entrée. Si la vidéo est carrée, la résolution sélectionnée doit être supérieure à sa largeur/hauteur. Pour les vidéos non carrées, la résolution sélectionnée doit être supérieure à la dimension la plus courte de la vidéo. Si la résolution cible est inférieure, une erreur sera générée. Choisissez `"original"` pour conserver la résolution de la vidéo d'entrée.

## Sorties

| Nom de la sortie | Type de données | Description |
|------------------|-----------------|-------------|
| `vidéo` | VIDEO | Le fichier vidéo amélioré. |

---
**Source fingerprint (SHA-256):** `0f329cbf61784474ee5b97a92d28a3e2383dc40e208f8a8317f3c4f60b43e5b2`
