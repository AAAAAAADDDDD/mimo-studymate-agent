# Xiaomi MiMo 100T Token Plan Application Draft

## Project Name
MiMo StudyMate Agent: AI-powered bilingual learning and assessment assistant for international students

## Core Pain Point
International students often need to process long lecture transcripts, PPT screenshots, case materials, and assessment briefs in a second language. Existing tools can translate or summarise, but they often fail to preserve course concepts, explain difficult terms, connect cases to lecture theory, and generate structured revision materials.

## Project Description
MiMo StudyMate Agent is a study workflow Agent built with Xiaomi MiMo API. It transforms messy academic materials into bilingual lecture notes, concept tables, case-to-theory mappings, quiz questions, and simple academic English revision notes. The system is designed for high-frequency, long-context learning tasks and will use MiMo models for reasoning, summarisation, translation, and structured content generation.

## Agent Workflow
1. Input ingestion: user pastes transcript, PPT OCR text, case material, or assessment brief.
2. Cleaning agent: removes noise, identifies topic boundaries, and keeps original meaning.
3. Concept extraction agent: extracts key academic concepts and definitions.
4. Explanation agent: explains difficult concepts in Chinese-supported simple English.
5. Application agent: maps case evidence to lecture concepts.
6. Quiz agent: generates practice questions and model answers.
7. Token tracking: logs model, usage, task type, and input size.

## Why Token Support Is Needed
This project relies on long-context AI workflows. A single lecture transcript or PPT export can easily exceed tens of thousands of tokens. A normal study cycle may include translation, explanation, concept mapping, quiz generation, and assessment preparation. Therefore, the project has a high and continuous token demand.

## Current MVP
The current MVP includes:
- Streamlit web interface
- MiMo API call through LiteLLM
- Modular Agent pipeline
- Multiple task modes
- Local JSON run logs
- Token usage metadata tracking

## Future Plan
- Add PDF and PPTX parser
- Add OCR and multimodal MiMo support for screenshots
- Add RAG knowledge base for course materials
- Add export to Word/PDF
- Add student progress memory and quiz review mode
- Deploy online demo
