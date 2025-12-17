"""
Utility functions for the Financial Advisor Agent.
Author: Danish (Dan-445)
"""
import json
import csv
from io import StringIO
from typing import Any, List, Dict, Tuple, Optional, Union
import logging
import pandas as pd

logger = logging.getLogger(__name__)

def parse_json_safely(data: Union[str, Dict[str, Any], List[Any]], default_value: Any = None) -> Any:
    """
    Safely parse JSON data with error handling.

    Args:
        data: The input data, potentially a JSON string or already parsed object.
        default_value: The value to return if parsing fails.

    Returns:
        parsed data or default_value.
    """
    try:
        if isinstance(data, str):
            return json.loads(data)
        return data
    except json.JSONDecodeError:
        logger.error("Failed to parse JSON data")
        return default_value
    except Exception as e:
        logger.exception(f"Unexpected error parsing JSON: {e}")
        return default_value

def parse_csv_transactions(file_content: bytes) -> Dict[str, Any]:
    """
    Parse CSV file content into a list of transactions.

    Args:
        file_content: The raw bytes content of the CSV file.

    Returns:
        A dictionary containing the list of transactions and category totals.

    Raises:
        ValueError: If parsing fails or required columns are missing.
    """
    try:
        # Read CSV content
        df = pd.read_csv(StringIO(file_content.decode('utf-8')))
        
        # Validate required columns
        required_columns = ['Date', 'Category', 'Amount']
        missing_columns = [col for col in required_columns if col not in df.columns]
        
        if missing_columns:
            raise ValueError(f"Missing required columns: {', '.join(missing_columns)}")
        
        # Convert date strings to datetime and then to string format YYYY-MM-DD
        if 'Date' in df.columns:
            df['Date'] = pd.to_datetime(df['Date'], errors='coerce').dt.strftime('%Y-%m-%d')
            if df['Date'].isnull().any():
                 logger.warning("Some dates could not be parsed and were set to NaT/None")
        
        # Convert amount strings to float, handling currency symbols and commas
        if 'Amount' in df.columns:
            if df['Amount'].dtype == object:
                # Remove currency symbols and commas, then convert
                df['Amount'] = df['Amount'].replace(r'[$,]', '', regex=True)
                df['Amount'] = pd.to_numeric(df['Amount'], errors='coerce').fillna(0.0)
            else:
                df['Amount'] = pd.to_numeric(df['Amount'], errors='coerce').fillna(0.0)
        
        # Group by category and calculate totals
        category_totals = df.groupby('Category')['Amount'].sum().reset_index()
        
        # Convert to list of dictionaries
        transactions = df.to_dict('records')
        
        return {
            'transactions': transactions,
            'category_totals': category_totals.to_dict('records')
        }
    except Exception as e:
        logger.exception(f"Error parsing CSV file: {e}")
        raise ValueError(f"Error parsing CSV file: {str(e)}")

def validate_csv_format(file) -> Tuple[bool, str]:
    """
    Validate CSV file format and content.

    Args:
        file: The file object (Streamlit UploadedFile).

    Returns:
        A tuple (is_valid, message).
    """
    try:
        content = file.read().decode('utf-8')
        try:
            csv.Sniffer().sniff(content) # Check if it's a valid CSV format
            has_header = csv.Sniffer().has_header(content)
        except csv.Error:
             # Sniffer can fail on some valid CSVs or very small files, fallback to pandas try
             has_header = True # Assume true and let pandas fail if structure is wrong

        file.seek(0)  # Reset file pointer
        
        # If sniffer explicitly said no header, we can flag it, but usually pandas read_csv handles headers well.
        # We will check columns.

        df = pd.read_csv(StringIO(content))
        required_columns = ['Date', 'Category', 'Amount']
        missing_columns = [col for col in required_columns if col not in df.columns]
        
        if missing_columns:
             # If columns are missing, maybe it has no header?
             # But we require specific column names, so headers are mandatory.
            return False, f"Missing required columns: {', '.join(missing_columns)}"
            
        # Validate date format
        try:
            pd.to_datetime(df['Date'], errors='raise')
        except Exception:
            return False, "Invalid date format in Date column. Expected YYYY-MM-DD or similar."
            
        # Validate amount format (should be numeric after removing currency symbols)
        try:
            if df['Amount'].dtype == object:
                clean_amounts = df['Amount'].replace(r'[$,]', '', regex=True)
                pd.to_numeric(clean_amounts, errors='raise')
            else:
                pd.to_numeric(df['Amount'], errors='raise')
        except Exception:
            return False, "Invalid amount format in Amount column. Must be numeric."
            
        return True, "CSV format is valid"
    except Exception as e:
        logger.error(f"Invalid CSV format: {e}")
        return False, f"Invalid CSV format: {str(e)}"
