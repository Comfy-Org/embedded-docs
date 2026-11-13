# LumaRay32VideoReframeNode

Ce nœud modifie le ratio d'affichage d'une vidéo existante en utilisant Luma Ray 3.2, qui remplit les zones de toile nouvellement exposées avec du contenu généré. La vidéo source peut durer jusqu'à 10 secondes, et la facturation est effectuée par seconde de sortie.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `vidéo` | Vidéo source à recadrer. Jusqu'à 10 secondes. | VIDEO | Oui | - |
| `invite` | Décrit comment les zones de toile nouvellement exposées doivent être remplies. | STRING | Oui | - |
| `rapport d'aspect` | Le ratio d'affichage cible pour la vidéo recadrée (par défaut : "16:9"). | STRING | Oui | "16:9"<br>"9:16"<br>"1:1"<br>"4:3"<br>"3:4"<br>"21:9" |
| `résolution` | La résolution de sortie de la vidéo recadrée (par défaut : "720p"). | STRING | Oui | "360p"<br>"540p"<br>"720p"<br>"1080p" |
| `graine` | Graine pour une génération reproductible. | INT | Oui | - |

**Remarque :** La résolution `1080p` n'est pas disponible pour les ratios d'affichage verticaux (`9:16` et `3:4`) lors du recadrage.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `identifiant_génération` | La vidéo recadrée avec le nouveau ratio d'affichage et les zones de toile remplies. | VIDEO |
| `identifiant_génération` | L'identifiant unique de la demande de génération. | STRING |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LumaRay32VideoReframeNode/fr.md)

---
**Source fingerprint (SHA-256):** `e265f3d5245fb3d56778e4e0e72be7bd05f9a1b5dcb37b71cefe6386b4ba934b`
