# Agentic AI for Google Sheets

## Resumen

## Funcionalidades

    - Transformar prompts en fórmulas
    - Interactuar con el documento a través de prompts
    - Rellenar las celdas con datos obtenidos desde la web
    - Rellener las celdas con datos propios de nuestra empresa
    - Usar ese documento como Knowledge Base para RAG propio

## Diseño de la solución

    - Agente que pueda consultar la web, el documento o interactuar con la API de Sheets

    - Google Apps Script (GAS)
    - ChromaDB
    - Embeddings Model
    - LLMs

## Restricciones (Reto)

    - Podrá ejecutarse en local en cualquier PC
        - 8GB RAM sin gráfica dedicada
    - Si no se consigue, podrá ejecutarse en Google Collab o HuggingFace Spaces en la capa gratuita