"""
Core logic for the Deep Research Agent.
Author: Danish (Dan-445)
"""
import logging
from typing import List, Tuple, Any

from agno.agent import Agent
from agno.run.agent import RunOutput
from agno.models.together import Together
from composio_agno import ComposioToolSet, Action

from config import MODEL_ID

logger = logging.getLogger(__name__)

class DeepResearchSystem:
    """
    A system for conducting deep research using LLMs and external tools.
    """
    
    def __init__(self, together_key: str, composio_key: str):
        self.together_key = together_key
        self.composio_key = composio_key
        self.llm = None
        self.composio_tools = None
        
        # Initialize immediately
        self._initialize_agents()

    def _initialize_agents(self):
        """Initialize Together AI LLM and Composio toolset."""
        logger.info("Initializing DeepResearch agents...")
        try:
            self.llm = Together(id=MODEL_ID, api_key=self.together_key)
            
            toolset = ComposioToolSet(api_key=self.composio_key)
            self.composio_tools = toolset.get_tools(actions=[
                Action.COMPOSIO_SEARCH_TAVILY_SEARCH, 
                Action.PERPLEXITYAI_PERPLEXITY_AI_SEARCH, 
                Action.GOOGLEDOCS_CREATE_DOCUMENT_MARKDOWN
            ])
            logger.info("Initialization successful.")
        except Exception as e:
            logger.error(f"Failed to initialize agents: {e}")
            raise

    def generate_questions(self, topic: str, domain: str) -> List[str]:
        """Generate specific research questions."""
        logger.info(f"Generating questions for topic: {topic}")
        
        question_generator = Agent(
            name="Question Generator",
            model=self.llm,
            instructions="""
            You are an expert at breaking down research topics into specific questions.
            Generate exactly 5 specific yes/no research questions about the given topic in the specified domain.
            Respond ONLY with the text of the 5 questions formatted as a numbered list, and NOTHING ELSE.
            """
        )
        
        try:
            result: RunOutput = question_generator.run(
                f"Generate exactly 5 specific yes/no research questions about the topic '{topic}' in the domain '{domain}'."
            )
            raw_text = result.content
            # Clean up <think> tags if present (common in reasoning models)
            if "</think>" in raw_text:
                raw_text = raw_text.split("</think>", 1)[1].strip()
            
            # Simple list parsing
            questions = [q.strip() for q in raw_text.split('\n') if q.strip()]
            return questions
        except Exception as e:
            logger.error(f"Error generating questions: {e}")
            raise

    def research_question(self, topic: str, domain: str, question: str) -> str:
        """Conduct deep research on a single question."""
        logger.info(f"Researching question: {question}")
        
        research_agent = Agent(
            model=self.llm,
            tools=[self.composio_tools],
            instructions=f"""
            You are a sophisticated research assistant. 
            Answer the following research question about the topic '{topic}' in the domain '{domain}':
            
            {question}
            
            Use the PERPLEXITYAI_PERPLEXITY_AI_SEARCH and COMPOSIO_SEARCH_TAVILY_SEARCH tools to provide a concise, well-sourced answer.
            """
        )
        
        try:
            result: RunOutput = research_agent.run()
            return result.content
        except Exception as e:
            logger.error(f"Error researching question: {e}")
            return f"Failed to research question. Error: {str(e)}"

    def compile_report(self, topic: str, domain: str, qa_pairs: List[dict]) -> str:
        """Compile findings into a report and create a Google Doc."""
        logger.info("Compiling final report...")
        
        qa_sections = "\n".join(
            f"<h2>{idx+1}. {qa['question']}</h2>\n<p>{qa['answer']}</p>" 
            for idx, qa in enumerate(qa_pairs)
        )
        
        compiler_agent = Agent(
            name="Report Compiler",
            model=self.llm,
            tools=[self.composio_tools],
            instructions=f"""
            You are a sophisticated research assistant. Compile the findings into a professional, McKinsey-style report.
            
            Structure:
            1. Executive Summary
            2. Research Analysis (Narrative style, not Q&A)
            3. Conclusion/Implications
            
            Topic: {topic}
            Domain: {domain}
            
            Findings:
            {qa_sections}
            
            Action: Use GOOGLEDOCS_CREATE_DOCUMENT_MARKDOWN to create a Google Doc with the HTML report.
            """
        )
        
        try:
            result: RunOutput = compiler_agent.run()
            return result.content
        except Exception as e:
            logger.error(f"Error compiling report: {e}")
            raise
