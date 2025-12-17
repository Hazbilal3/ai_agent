"""
Agent definitions and coordination logic for the Financial Advisor System.
Author: Danish (Dan-445)
"""
import logging
from datetime import datetime
from typing import Dict, Any, Optional
import json
import pandas as pd
from bytez import Bytez

from models import (
    BudgetAnalysis, SavingsStrategy, DebtReduction
)
from utils import parse_json_safely
from config import APP_NAME, USER_ID, MODEL_ID, BYTEZ_API_KEY

logger = logging.getLogger(__name__)

class FinanceAdvisorSystem:
    """
    Coordinator system for the Financial Advisor agents using Bytez.
    """
    def __init__(self):
        if not BYTEZ_API_KEY:
             raise ValueError("BYTEZ_API_KEY is not set.")
        self.client = Bytez(BYTEZ_API_KEY)
        self.model_id = MODEL_ID

    async def analyze_finances(self, financial_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Runs the agent pipeline to analyze financial data.
        
        Args:
            financial_data: A dictionary containing income, expenses, transactions, and debts.
            
        Returns:
            A dictionary containing the analysis results (budget, savings, debt).
        """
        logger.info(f"Starting analysis with Bytez model: {self.model_id}")
        
        try:
            # Preprocess data
            self._preprocess_data(financial_data)
            
            # Step 1: Budget Analysis
            budget_analysis = self._run_budget_analysis_agent(financial_data)
            
            # Step 2: Savings Strategy
            savings_strategy = self._run_savings_strategy_agent(financial_data, budget_analysis)
            
            # Step 3: Debt Reduction
            debt_reduction = self._run_debt_reduction_agent(financial_data, budget_analysis, savings_strategy)
            
            return {
                "budget_analysis": budget_analysis,
                "savings_strategy": savings_strategy,
                "debt_reduction": debt_reduction
            }
            
        except Exception as e:
            logger.exception(f"Error during finance analysis: {str(e)}")
            default_results = self._create_default_results(financial_data)
            # Return partial results if possible, or full default
            return default_results

    def _preprocess_data(self, data: Dict[str, Any]):
        """Adds derived data like specific category sums to the input."""
        transactions = data.get("transactions", [])
        if transactions:
            try:
                df = pd.DataFrame(transactions)
                if 'Date' in df.columns:
                     df['Date'] = pd.to_datetime(df['Date'], errors='coerce').dt.strftime('%Y-%m-%d')
                
                if 'Category' in df.columns and 'Amount' in df.columns:
                    category_spending = df.groupby('Category')['Amount'].sum().to_dict()
                    data["category_spending"] = category_spending
                    data["total_spending"] = float(df['Amount'].sum())
            except Exception as e:
                logger.error(f"Error preprocessing transactions: {e}")

        manual_expenses = data.get("manual_expenses", {})
        if manual_expenses:
             try:
                total = sum(manual_expenses.values())
                data["total_manual_spending"] = total
             except Exception as e:
                 logger.error(f"Error preprocessing manual expenses: {e}")

    def _call_llm(self, system_prompt: str, user_content: str, output_schema_class=None) -> Dict[str, Any]:
        """Helper to call Bytez API."""
        try:
            # Bytez Python client usage based on general knowledge and assumptions.
            # Usually: client.models.run(model_id, input_data)
            # Input data typically needs 'prompt' or 'messages'. 
            # Given document mentions 'client.models.run(model_id, input)', let's try that.
            
            # Construct a prompt that includes system instructions if separate 'system' role isn't explicitly clear in simple run.
            # Ideally we use a chat format if supported.
            # Let's assume a standard chat formatting since we are using an Instruct model.
            
            full_prompt = (
                f"<|begin_of_text|><|start_header_id|>system<|end_header_id|>\n\n{system_prompt}<|eot_id|>"
                f"<|start_header_id|>user<|end_header_id|>\n\n{user_content}<|eot_id|>"
                f"<|start_header_id|>assistant<|end_header_id|>\n\n"
            )

            response = self.client.models.run(
                self.model_id,
                full_prompt
            )
            
            # The response is likely a string or a dict containing 'output' or 'text'.
            # Let's inspect what we get. Assuming it returns the generation text directly or in a specific field.
            output_text = response
            if isinstance(response, dict):
                 # Common keys might be 'output', 'text', 'generated_text'
                 output_text = response.get('output') or response.get('text') or response.get('generated_text') or str(response)
            
            # Parse JSON
            # We expect the model to return JSON because we will ask it to.
            return parse_json_safely(output_text, {})

        except Exception as e:
            logger.error(f"LLM call failed: {e}")
            raise

    def _run_budget_analysis_agent(self, data: Dict[str, Any]) -> Dict[str, Any]:
        logger.info("Running Budget Analysis Agent...")
        system_instruction = """You are a Budget Analysis Agent specialized in reviewing financial transactions and expenses.
You must output ONLY valid JSON matching the exact schema provided below. Do not include markdown formatting like ```json ... ```.

Your tasks:
1. Analyze income, transactions, and expenses.
2. Categorize spending into logical groups.
3. Identify spending patterns.
4. Suggest specific areas where spending could be reduced.
5. Provide actionable recommendations.

Output Schema (JSON):
{
    "total_expenses": float,
    "monthly_income": float,
    "spending_categories": [
        {"category": str, "amount": float, "percentage": float}
    ],
    "recommendations": [
        {"category": str, "recommendation": str, "potential_savings": float}
    ]
}"""
        
        user_msg = f"Analyze this financial data: {json.dumps(data)}"
        return self._call_llm(system_instruction, user_msg, BudgetAnalysis)

    def _run_savings_strategy_agent(self, data: Dict[str, Any], budget_analysis: Dict[str, Any]) -> Dict[str, Any]:
        logger.info("Running Savings Strategy Agent...")
        system_instruction = """You are a Savings Strategy Agent specialized in creating personalized savings plans.
You are the second agent. Use the provided budget analysis output to inform your strategy.
You must output ONLY valid JSON matching the exact schema provided below. Do not include markdown formatting.

Your tasks:
1. Review the budget analysis results.
2. Recommend comprehensive savings strategies.
3. Calculate optimal emergency fund size.
4. Suggest appropriate savings allocation.
5. Recommend automation techniques.

Output Schema (JSON):
{
    "emergency_fund": {
        "recommended_amount": float,
        "current_amount": float,
        "current_status": str
    },
    "recommendations": [
        {"category": str, "amount": float, "rationale": str}
    ],
    "automation_techniques": [
        {"name": str, "description": str}
    ]
}"""
        
        user_msg = f"Financial Data: {json.dumps(data)}\n\nBudget Analysis Results: {json.dumps(budget_analysis)}"
        return self._call_llm(system_instruction, user_msg, SavingsStrategy)

    def _run_debt_reduction_agent(self, data: Dict[str, Any], budget_analysis: Dict[str, Any], savings_strategy: Dict[str, Any]) -> Dict[str, Any]:
        logger.info("Running Debt Reduction Agent...")
        system_instruction = """You are a Debt Reduction Agent specialized in creating debt payoff strategies.
You are the final agent. Use the budget analysis and savings strategy to inform your plan.
You must output ONLY valid JSON matching the exact schema provided below. Do not include markdown formatting.

Your tasks:
1. Review budget analysis and savings strategy.
2. Analyze debts.
3. Create prioritized debt payoff plans (avalanche and snowball).
4. Calculate total interest and time to debt freedom.
5. Provide specific recommendations.

Output Schema (JSON):
{
    "total_debt": float,
    "debts": [
        {"name": str, "amount": float, "interest_rate": float, "min_payment": float}
    ],
    "payoff_plans": {
        "avalanche": {"total_interest": float, "months_to_payoff": int, "monthly_payment": float},
        "snowball": {"total_interest": float, "months_to_payoff": int, "monthly_payment": float}
    },
    "recommendations": [
        {"title": str, "description": str, "impact": str}
    ]
}"""
        
        user_msg = f"Financial Data: {json.dumps(data)}\n\nBudget Analysis: {json.dumps(budget_analysis)}\n\nSavings Strategy: {json.dumps(savings_strategy)}"
        return self._call_llm(system_instruction, user_msg, DebtReduction)

    def _create_default_results(self, financial_data: Dict[str, Any]) -> Dict[str, Any]:
        """Provides fallback results in case of agent failure."""
        monthly_income = financial_data.get("monthly_income", 0)
        expenses = financial_data.get("manual_expenses", {})
        
        if expenses is None:
            expenses = {}
        
        # Merge manual and transaction expenses
        if financial_data.get("transactions"):
             for transaction in financial_data["transactions"]:
                 category = transaction.get("Category", "Uncategorized")
                 amount = transaction.get("Amount", 0)
                 expenses[category] = expenses.get(category, 0) + float(amount)
        
        total_expenses = sum(expenses.values())
        
        return {
            "budget_analysis": {
                "total_expenses": total_expenses,
                "monthly_income": monthly_income,
                "spending_categories": [
                    {"category": cat, "amount": amt, "percentage": (amt / total_expenses * 100) if total_expenses > 0 else 0}
                    for cat, amt in expenses.items()
                ],
                "recommendations": [
                    {"category": "General", "recommendation": "Review expenses manually (AI Analysis Failed)", "potential_savings": 0}
                ]
            },
            "savings_strategy": {
                "emergency_fund": {
                    "recommended_amount": total_expenses * 6,
                    "current_amount": 0,
                    "current_status": "Unknown"
                },
                "recommendations": [
                    {"category": "General", "amount": 0, "rationale": "AI Analysis Failed"}
                ],
                "automation_techniques": []
            },
            "debt_reduction": {
                "total_debt": 0,
                "debts": [],
                "payoff_plans": {
                    "avalanche": {"total_interest": 0, "months_to_payoff": 0, "monthly_payment": 0},
                    "snowball": {"total_interest": 0, "months_to_payoff": 0, "monthly_payment": 0}
                },
                "recommendations": []
            }
        }
