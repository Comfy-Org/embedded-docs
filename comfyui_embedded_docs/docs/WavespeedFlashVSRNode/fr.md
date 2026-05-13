> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WavespeedFlashVSRNode/fr.md)

Le nœud WavespeedFlashVSRNode est un upscaler vidéo rapide et de haute qualité qui améliore la résolution et restaure la netteté des séquences vidéo de faible résolution ou floues. Il traite une entrée vidéo et produit une nouvelle vidéo à une résolution supérieure choisie par l'utilisateur.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------------|--------|-------|-------------|
| `video` | VIDEO | Oui | N/A | Le fichier vidéo d'entrée à upscaler. Doit être au format conteneur MP4 avec une durée comprise entre 5 secondes et 10 minutes. |
| `target_resolution` | STRING | Oui | `"720p"`<br>`"1080p"`<br>`"2K"`<br>`"4K"` | La résolution souhaitée pour la vidéo de sortie upscalée. |

**Contraintes d'entrée :**

* Le fichier `video` d'entrée doit être au format conteneur MP4.
* La durée de la `video` d'entrée doit être comprise entre 5 secondes et 10 minutes (600 secondes).

## Sorties

| Nom de sortie | Type de données | Description |
|---------------|-----------------|-------------|
| `output` | VIDEO | Le fichier vidéo upscalé à la résolution cible sélectionnée. |

---
**Source fingerprint (SHA-256):** `9a495889753ac866177921727228846d8ef9516c54ccd9aa425350b87237c397`
